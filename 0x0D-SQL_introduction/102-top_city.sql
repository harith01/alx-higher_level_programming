-- Display the top 3 of cities temperature
SELECT city, AVG(value) AS avg_temp
FROM temperatures
BETWEEN month 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
