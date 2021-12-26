import requests
import warnings
import dateparser

from datetime import datetime

from db import with_cursor

# Ignore dateparser warnings regarding pytz
warnings.filterwarnings(
    "ignore",
    message="The localize method is no longer necessary, as this time zone supports the fold attribute",
)

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
        cursor.execute(_q, _values)
    except Exception as e:
        print(f"Couldn't insert rates. Error: {e} ")
    else:
        print(f"Rates updated for date: {_date}")


def fetch_rates_and_insert(_date=None):
    if not _date:
        _date = datetime.now().date()
    
    j = fetch_rates(_date)
    

    date = dateparser.parse(j['date']).date()
    rates = j['rates']
    cols = ', '.join([k.upper() for k in rates.keys()])
    vals = [date] + [str(v) for v in rates.values()]
    vals_place_holder = ', '.join(['%s' for _ in vals]) 
    q = """
        INSERT INTO rate(date, {cols}) VALUES ({vals});
    """.format(cols = cols, vals =vals_place_holder)

    insert_rates(q, vals, date)
