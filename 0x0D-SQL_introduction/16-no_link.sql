-- This script list all records which name is not nullof DB second_table 
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
