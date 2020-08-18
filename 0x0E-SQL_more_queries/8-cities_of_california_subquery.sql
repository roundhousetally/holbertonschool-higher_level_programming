-- script lists all cities of california
-- on mysql server
SELECT id, name FROM cities WHERE state_id = (
SELECT id FROM states WHERE name = "California") ORDER BY id;
