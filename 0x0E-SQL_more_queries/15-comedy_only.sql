-- select all the comedy shows
SELECT s.title
FROM tv_genres g, tv_show_genres n, tv_shows s
WHERE s.id = n.show_id
	AND n.genre_id = g.id
	AND g.name = "Comedy"
ORDER BY s.title;
