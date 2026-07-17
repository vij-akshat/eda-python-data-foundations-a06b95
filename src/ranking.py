from src.models import Order
from src.analytics import revenue_by_region, paid_orders

# Rank regions by revenue, biggest first — the order an executive reads.
def regions_ranked(orders: list[Order]) -> list[tuple[str, float]]:
    totals = revenue_by_region(orders)
    # sorted() returns a new list; key picks WHAT to sort by, reverse flips it.
    return sorted(totals.items(), key=lambda kv: kv[1], reverse=True)

# Top-N: the N biggest paid orders, for a "largest deals" widget.
def top_orders(orders: list[Order], n: int = 3) -> list[Order]:
    biggest = sorted(paid_orders(orders), key=lambda o: o.amount, reverse=True)
    return biggest[:n]   # slicing takes the first N after sorting
