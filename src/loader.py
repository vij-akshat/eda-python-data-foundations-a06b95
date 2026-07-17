import csv
from src.models import Order

# Real data lives in files, not Python literals. Read a CSV into Orders.
def load_orders(path: str) -> list[Order]:
    orders: list[Order] = []
    with open(path, newline="") as f:           # context manager closes the file
        reader = csv.DictReader(f)               # each row is a dict keyed by header
        for row in reader:
            orders.append(
                Order(
                    id=row["id"],
                    region=row["region"],
                    # CSV values are ALWAYS strings — cast amount to float.
                    amount=float(row["amount"]),
                    status=row["status"],
                )
            )
    return orders
