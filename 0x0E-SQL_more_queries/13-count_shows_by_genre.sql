-- list all genres and display number of shows linked
SELECT g.name AS genre, COUNT(sg.show_id) AS number_of_shows
FROM tv_genres AS g
JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
GROUP BY g.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;

