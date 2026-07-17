-- The relational shape of the same orders we modeled in Python.
CREATE TABLE orders (
    id      TEXT PRIMARY KEY,
    region  TEXT NOT NULL,   -- 'AMER' | 'EMEA' | 'APAC'
    amount  REAL NOT NULL,   -- revenue in USD
    status  TEXT NOT NULL    -- 'paid' | 'pending' | 'refunded'
);

INSERT INTO orders VALUES
    ('o1', 'AMER', 120.0, 'paid'),
    ('o2', 'EMEA', 80.0,  'pending'),
    ('o3', 'AMER', 200.0, 'paid'),
    ('o4', 'APAC', 50.0,  'refunded'),
    ('o5', 'EMEA', 300.0, 'paid');
