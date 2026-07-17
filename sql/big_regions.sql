-- HAVING filters on the AGGREGATE, after grouping — WHERE can't see SUM yet.
SELECT region,
       SUM(amount)               AS revenue,
       COUNT(DISTINCT status)    AS distinct_statuses
FROM orders
GROUP BY region
HAVING SUM(amount) > 150          -- keep only regions above a revenue floor
ORDER BY revenue DESC;
