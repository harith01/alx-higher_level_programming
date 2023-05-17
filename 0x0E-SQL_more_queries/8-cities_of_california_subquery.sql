-- List all cities of California that can be founf in the database
SELECT id, name from cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
