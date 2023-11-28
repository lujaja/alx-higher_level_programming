--This script list all cities contained in the DB
SELECT cities.id, cities.name, states.name
FROM cities, states
ORDER BY cities.id ASC;
