-- Lists all records of scond_table except rows without 'name'
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
