CREATE_PRODUCT_TABLE = """
CREATE TABLE IF NOT EXISTS product (
    product_id      VARCHAR(50)     PRIMARY KEY,
    product_name    VARCHAR(100)    NOT NULL,
    purchase_price  INTEGER         NOT NULL,
    currency        VARCHAR(3)      NOT NULL,
    installation    BOOLEAN         NOT NULL
);
"""

CREATE_RATE_TABLE = """
CREATE TABLE IF NOT EXISTS rate (
    date            DATE        NOT NULL,
    from_currency   VARCHAR(3)  NOT NULL,
    to_currency     VARCHAR(3)  NOT NULL,
    rate            NUMERIC     NOT NULL,
    PRIMARY KEY(date, from_currency, to_currency)

);
"""

NORMALIZED_PRICES_VIEW = """
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
"""

TOP_3_PRODUCTS_NORWAY = """
    SELECT *
    FROM product
    WHERE currency = 'NOK'
    AND installation = false
    ORDER BY purchase_price DESC
    LIMIT 3;
"""

AVG_PRODUCT_PRICE_SWEDEN = """
    SELECT AVG(purchase_price) AS average_price_sweden
    FROM product
    WHERE currency = 'SEK'
    AND product_name NOT LIKE '%Easee%';
"""