-- Inner Join
SELECT shows.title, show_gen.genre_id
FROM tv_shows as shows
INNER JOIN tv_show_genres as show_gen
ON shows.title = show_gen.show_id
ORDER BY shows.title, show_gen.genre_id;
