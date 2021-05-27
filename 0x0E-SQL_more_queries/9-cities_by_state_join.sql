--  lists all cities contained in the database
SELECT cities.id AS id, cities.name AS name, states.name AS name
FROM cities NATURAL JOIN states
ON states.id = cities.states_id;
