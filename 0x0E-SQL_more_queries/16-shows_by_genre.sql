-- lists all shows, and all genres linked to that show
SELECT s.title, g.name
FROM tv_shows s
LEFT JOIN tv_show_genres n ON s.id = n.show_id
lEFT JOIN tv_genres g on n.genre_id = g.id
ORDER BY s.title, g.name;
