-- Conditional aggregation: one scan, several measures, via CASE inside SUM.
SELECT
    region,
    SUM(CASE WHEN status = 'paid'     THEN amount ELSE 0 END) AS paid_revenue,
    SUM(CASE WHEN status = 'refunded' THEN amount ELSE 0 END) AS refunded_amount,
    SUM(CASE WHEN status = 'pending'  THEN 1      ELSE 0 END) AS pending_count
FROM orders
GROUP BY region;
