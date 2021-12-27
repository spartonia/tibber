# Tibber

# Installation

Create a virtualenv

```bash
virtualenv -p python3 ~/.venv/tibber
```

activate env

```bash
source ~/.venv/tibber/bin/activate
```

and install requirements:

```
pip install -r requirements.txt
```

creata a file called `database.ini` and fill in the db credentials:

```ini
[postgresql]
host=
database=
user=
password=
```

# Tasks:

### Task 1

Run

```bash
python initialize.py
```

### Task 2

Create a view that shows the product ids, the product names and their normalised
prices in Norwegian Kronor (NOK) using the latest rates in the currency rates table.

```sql
CREATE VIEW normalised_prices AS
WITH latest_rates AS (
    SELECT * FROM rate WHERE date IN (SELECT MAX(date) FROM rate)
),
normalised AS(
    SELECT product_id, product_name, purchase_price / rate AS normalised_price
    FROM product p
    INNER JOIN latest_rates r
    ON p.currency = r.to_currency
)
 SELECT * FROM normalised;
```

### Task 2

Create a query returning the top-3 most expensive products that do not require
the installation service and can be bought in Norway.

```sql
SELECT *
FROM product
WHERE currency = 'NOK'
AND installation = false
ORDER BY purchase_price DESC
LIMIT 3;
```

### Task 3

Create a query returning the average product price in Sweden without taking into
account Easee products.

```sql
SELECT AVG(purchase_price) AS average_price_sweden
FROM product
WHERE currency = 'SEK'
AND product_name NOT LIKE '%Easee%';
```
