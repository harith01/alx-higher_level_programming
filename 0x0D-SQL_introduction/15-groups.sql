-- List the number of recordswith the same score on second_table
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score;
