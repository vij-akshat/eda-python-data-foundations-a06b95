-- The same "revenue per region" report — but declarative, run by the database.
SELECT region,
       SUM(amount) AS revenue,
       COUNT(*)    AS paid_orders
FROM orders
WHERE status = 'paid'        -- filter: only revenue-generating rows
GROUP BY region              -- bucket the surviving rows by region
ORDER BY revenue DESC;       -- biggest region first
