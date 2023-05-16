-- List the number of recordswith the same score on second_table
SELECT score, COUNT(*)
FROM second_table
GROUP BY score;
