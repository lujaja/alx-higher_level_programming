--script list all the cities of Caifonia that can be found in the DB
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states
	WHERE name = "California" LIMIT 1)
ORDER BY id ASC;
