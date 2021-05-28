-- lists all shows without the genre Comedy
SELECT DISTINCT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres on tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.id NOT IN (
	SELECT s.id
	FROM tv_shows s, tv_show_genres n, tv_genres g
	WHERE g.id = n.genre_id
		AND n.show_id = s.id
		AND g.name = "Comedy")
ORDER BY title;
