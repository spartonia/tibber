from contextlib import contextmanager
from functools import wraps

from psycopg2.pool import ThreadedConnectionPool
from psycopg2.extras import NamedTupleCursor

from utils import db_config

_db = None

def _build_db_connection(**overrides):
    args =  db_config()
    global _db
    _db = ThreadedConnectionPool(1, 5, cursor_factory=NamedTupleCursor, **args)


@contextmanager
def get_cursor():
    '''
    Returns a psycopg cursor with `autocommit` enabled. I.e. writes are saved
    as soon as `cursor.execute()` is called.
    '''
    if not _db:
        _build_db_connection()
    con = None
    try:
        con = _db.getconn()
        con.autocommit = True
        yield con.cursor()
    finally:
        if con:
            _db.putconn(con)

'''
`db()` is equivalend to `get_cursor()`
'''
db = get_cursor

@contextmanager
def get_transaction_cursor():
    '''
    Returns a cursor with `autocommit` disabled. commit() will be called if the
    with block succeeds, recording all changes.
    '''
    if not _db:
        _build_db_connection()
    con = None
    try:
        con = _db.getconn()
        con.autocommit = False
        yield con.cursor()
        con.commit()
    finally:
        if con:
            _db.putconn(con)


@contextmanager
def conn():
    if not _db:
        _build_db_connection()
    con = None
    try:
        con = _db.getconn()
        con.autocommit = False
        yield con
    finally:
        if con:
            _db.putconn(con)


def with_cursor(db_operation):
    '''
    Injects a psycopg cursor into db_operation.
    If `cursor` is specified, that instance will be passed to `db_operation`,
    which is useful for testing and working with transactions.
    '''

    @wraps(db_operation)
    def db_operation_with_cursor(
        *args,
        cursor=None,
        **kwargs,
    ):
        if cursor:
            return db_operation(*args, cursor=cursor, **kwargs)
        with get_cursor() as cursor:
            return db_operation(*args, cursor=cursor, **kwargs)

    return db_operation_with_cursor