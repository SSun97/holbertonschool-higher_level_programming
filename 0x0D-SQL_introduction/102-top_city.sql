-- show top 3 city temperature
SELECT
	city, AVG(value) as avg_temp
FROM
	temperatures
WHERE
	month > 6 and month <9
GROUP BY
	city
ORDER BY
	avg_temp DESC LIMIT 3;
