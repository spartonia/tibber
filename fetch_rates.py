import requests
import warnings

from datetime import datetime

from db import with_cursor


def fetch_rates(date):
    print(f"Fetching rates for {date}")
    try:
        _url = f"https://api.vatcomply.com/rates?base=NOK&date={date}"
        response = requests.get(_url)
        j = response.json()
    except Exception as e:
        print(f"Error fetching rates: {e}")
        raise Exception(e)
    else:
        return j
   
@with_cursor
def insert_rates(_q, _values, _date, cursor=None):
    print("Inserting..")
    try:
        cursor.executemany(_q, _values)
    except Exception as e:
        print(f"Couldn't insert rates. Error: {e} ")
    else:
        print(f"Rates updated for date: {_date}")


def fetch_rates_and_insert(_date=None):
    if not _date:
        _date = datetime.now().date()
    
    j = fetch_rates(_date)
    

    rates = j['rates']
   
    values = [dict(
        date = _date,
        from_currency = j['base'],
        to_currency = currency,
        rate = rate
    ) for currency, rate in rates.items()]

    q = """
        INSERT INTO rate(date, from_currency, to_currency, rate)
        VALUES (%(date)s, %(from_currency)s, %(to_currency)s, %(rate)s);
    """
    insert_rates(q, values, _date)
