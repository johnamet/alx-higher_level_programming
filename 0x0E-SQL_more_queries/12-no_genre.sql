--  lists all shows contained in the database hbtn_0d_tvshows.

SELECT s.title, COALESCE(g.genre_id, 'NULL') AS genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g ON s.id = g.show_id
WHERE genre_id = 'NULL'
ORDER BY s.title ASC, g.genre_id ASC;

