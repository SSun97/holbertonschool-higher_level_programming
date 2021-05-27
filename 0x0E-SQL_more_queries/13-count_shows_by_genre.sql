-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name AS 'genre', COUNT(*) AS "number_of_shows"
FROM tv_genres
RIGHT JOIN tv_show_genres
on tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY COUNT(*) DESC;

