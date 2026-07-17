import sqlite3
from src.models import Order

# A tiny data-access layer: Python in, SQL out, typed records back.
def connect(path: str = "orders.db") -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row     # rows behave like dicts: row["region"]
    return conn

def revenue_by_region(conn: sqlite3.Connection) -> dict[str, float]:
    cur = conn.execute(
        """
        SELECT region, SUM(amount) AS revenue
        FROM orders
        WHERE status = 'paid'
        GROUP BY region
        """
    )
    return {row["region"]: row["revenue"] for row in cur.fetchall()}

# NEVER build SQL with string formatting. Use a ? placeholder + a params tuple.
def orders_in_region(conn: sqlite3.Connection, region: str) -> list[Order]:
    cur = conn.execute(
        "SELECT id, region, amount, status FROM orders WHERE region = ?",
        (region,),                     # the value is bound safely, not interpolated
    )
    return [Order(r["id"], r["region"], r["amount"], r["status"]) for r in cur]
