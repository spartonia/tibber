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
    date    DATE        PRIMARY KEY,
    eur     NUMERIC NOT NULL,
    usd     NUMERIC NOT NULL,
    jpy     NUMERIC NOT NULL,
    bgn     NUMERIC NOT NULL,
    czk     NUMERIC NOT NULL,
    dkk     NUMERIC NOT NULL,
    gbp     NUMERIC NOT NULL,
    huf     NUMERIC NOT NULL,
    pln     NUMERIC NOT NULL,
    ron     NUMERIC NOT NULL,
    sek     NUMERIC NOT NULL,
    chf     NUMERIC NOT NULL,
    isk     NUMERIC NOT NULL,
    nok     NUMERIC NOT NULL,
    hrk     NUMERIC NOT NULL,
    rub     NUMERIC NOT NULL,
    try     NUMERIC NOT NULL,
    aud     NUMERIC NOT NULL,
    brl     NUMERIC NOT NULL,
    cad     NUMERIC NOT NULL,
    cny     NUMERIC NOT NULL,
    hkd     NUMERIC NOT NULL,
    idr     NUMERIC NOT NULL,
    ils     NUMERIC NOT NULL,
    inr     NUMERIC NOT NULL,
    krw     NUMERIC NOT NULL,
    mxn     NUMERIC NOT NULL,
    myr     NUMERIC NOT NULL,
    nzd     NUMERIC NOT NULL,
    php     NUMERIC NOT NULL,
    sgd     NUMERIC NOT NULL,
    thb     NUMERIC NOT NULL,
    zar     NUMERIC NOT NULL
);
"""