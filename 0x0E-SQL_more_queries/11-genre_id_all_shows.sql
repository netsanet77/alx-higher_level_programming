-- lists all shows contained in database hbtn_0d_tvshows
-- Each record should display tv_shows.title and tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- if a show doesn't have a genre, display NULL
-- Use only one SELECT statement
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres RIGHT OUTER JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
