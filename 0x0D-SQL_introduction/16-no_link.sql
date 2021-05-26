-- list all records and don't show the rows without name value;
SELECT
	score,
	name
FROM
	second_table
WHERE
	name IS NOT NULL
ORDER BY
	score DESC;
