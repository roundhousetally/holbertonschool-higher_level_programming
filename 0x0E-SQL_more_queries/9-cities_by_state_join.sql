-- lists all cities contained in database
-- on mysql server
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states ON cities.state_id = states.id;
