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