-- script that lists num of records w the same score
-- on mysql server
SELECT `score`, COUNT(*) AS `number` FROM `second_table` GROUP BY `score` DESC;
