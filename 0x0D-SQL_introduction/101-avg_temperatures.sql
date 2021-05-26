-- import a database and show the avgrage of tempreture of each city
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
