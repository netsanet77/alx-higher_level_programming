-- lists all shows contained in database hbtn_0d_tvshows without a genre linked
-- Each record should display tv_shows.title and tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Use only one SELECT statement
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres RIGHT OUTER JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
