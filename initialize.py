import csv

from db import with_cursor
from fetch_rates import fetch_rates_and_insert
from queries import CREATE_PRODUCT_TABLE, CREATE_RATE_TABLE


COUNTRY_CODE_TO_CURRENCY = {
    'SE': 'SEK',
    'NO': 'NOK',
    'DE': 'EUR',
    'US': 'USD'
}

@with_cursor
def create_tables(cursor=None):
    """ Create tables in the PostgreSQL datbase"""
    commands = (
        CREATE_PRODUCT_TABLE,
        CREATE_RATE_TABLE
    )

    print("Creating tables..")
    for c in commands:
        try:
            cursor.execute(c)
        except Exception as e:
            print(f"Error creating table: {e}")
        else:
            print("Table created!")



def read_csv(csv_file = 'data.csv'):
    print("Reading products from csv file..")
    with open(csv_file) as f:
        lines = list(csv.reader(f, delimiter=','))
    header = lines[0]
    dict_lines = []
    for line in lines[1:]:
        dict_lines.append(
            dict(zip(header, line))
        )
    print("Done!")
    return dict_lines

@with_cursor
def insert_products(cursor=None):
    print("Populating product table..")
    items = read_csv()
    j = [dict(
        product_id = item['market'] + '-' + item['variation_sku'],
        product_name = item['product_name'],
        purchase_price = item['purchase_price'],
        installation = item['installation'],
        currency = COUNTRY_CODE_TO_CURRENCY.get(item['market'])
    ) for item in items]

    q = """
        INSERT INTO product(product_id, product_name, purchase_price, installation, currency)
        VALUES (%(product_id)s, %(product_name)s, %(purchase_price)s, %(installation)s, %(currency)s);
    """

    try:
        cursor.executemany(q, j)
    except Exception as e:
        print(f"Couldn't insert products. Error: {e} ")
    else:
        print(f"Product table filled.")
    


if __name__ == '__main__':
    create_tables()
    insert_products()
    fetch_rates_and_insert()
