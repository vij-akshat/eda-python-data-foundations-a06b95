from dataclasses import dataclass

# A dataclass describes the SHAPE of one row of enterprise data.
# Type hints document what each field holds — the compiler-of-the-mind
# (and tools like mypy) check them.
@dataclass(frozen=True)
class Order:
    id: str
    region: str          # 'AMER' | 'EMEA' | 'APAC'
    amount: float        # revenue in USD
    status: str          # 'paid' | 'pending' | 'refunded'

    # __post_init__ runs right after construction — validate invariants here.
    def __post_init__(self) -> None:
        if self.amount < 0:
            raise ValueError(f"order {self.id}: amount cannot be negative")
        if self.region not in ('AMER', 'EMEA', 'APAC'):
            raise ValueError(f"order {self.id}: unknown region {self.region!r}")

    # A method computes a derived value from the record's own fields.
    def is_revenue(self) -> bool:
        return self.status == 'paid'

    # A derived field: net contribution counts only revenue, else zero.
    def net_revenue(self) -> float:
        return self.amount if self.is_revenue() else 0.0
