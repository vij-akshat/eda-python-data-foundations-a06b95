from collections import defaultdict
from src.models import Order

# A small in-memory dataset stands in for a real warehouse for now.
ORDERS: list[Order] = [
    Order('o1', 'AMER', 120.0, 'paid'),
    Order('o2', 'EMEA', 80.0, 'pending'),
    Order('o3', 'AMER', 200.0, 'paid'),
    Order('o4', 'APAC', 50.0, 'refunded'),
    Order('o5', 'EMEA', 300.0, 'paid'),
]

# A list comprehension filters rows: keep only the revenue-generating orders.
def paid_orders(orders: list[Order]) -> list[Order]:
    return [o for o in orders if o.is_revenue()]

# Aggregate: total revenue across the paid orders.
def total_revenue(orders: list[Order]) -> float:
    return sum(o.amount for o in paid_orders(orders))

# Group-by: revenue per region, the heart of any KPI report.
def revenue_by_region(orders: list[Order]) -> dict[str, float]:
    totals: dict[str, float] = defaultdict(float)
    for o in paid_orders(orders):
        totals[o.region] += o.amount
    return dict(totals)
