--This script displays top 3 of cities temp during july and august
CREATE TABLE iF NOT EXISTS j_a
	SELECT *
	FROM temperatures
	WHERE month = 7 OR month = 8;
SELECT city, AVG(value) as avg_temp
FROM a_j
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
