-- Display the top 3 of cities temperature
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
WHERE month BETWEEN 7 AND 8
ORDER BY avg_temp
LIMIT 3
