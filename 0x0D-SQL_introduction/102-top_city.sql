-- Display the top 3 of cities temperature
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
WHERE month BETWEEN 7 AND 8
ORDER BY avg_temp DESC
LIMIT 3;
