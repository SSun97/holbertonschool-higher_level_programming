-- show the top 3 stats' temperature
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state;
