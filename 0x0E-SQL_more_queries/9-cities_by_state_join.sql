--  lists all cities contained in the database
SELECT cities.id AS id, cities.name AS name, states.name AS name
FROM cities LEFT JOIN states
ON states.id = cities.state_id
ORDER BY cities.id;
