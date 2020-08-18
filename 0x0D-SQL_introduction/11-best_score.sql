-- script that lists all records with a score over or equal to ten
-- on my sql server
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY score DESC;
