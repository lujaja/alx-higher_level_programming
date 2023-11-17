-- This script list numbers of records with same score in table
SELECT score, COUNT(score) AS numbers FROM second_table GROUP BY score
ORDER BY numbers DESC;
