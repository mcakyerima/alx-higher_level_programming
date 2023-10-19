-- To import a SQL dump, use the provided link: https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql.
-- Create a database named 'hbtn_0d_tvshows' by running the following command:
--   echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
-- Import the SQL dump into the 'hbtn_0d_tvshows' database using the 'curl' command.
-- This script lists all shows contained in 'hbtn_0d_tvshows' that do not have a linked genre.
-- Each record in the result set displays: tv_shows.title - tv_show_genres.genre_id.
-- The query results are sorted in ascending order based on 'tv_shows.title' and 'tv_show_genres.genre_id'.
-- A LEFT JOIN is used to include shows without a genre, and the condition WHERE tv_show_genres.genre_id IS NULL filters such records.
-- This query utilizes a single SELECT statement, and the database name is expected to be passed as an argument to the MySQL command.

SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows
LEFT JOIN tv_show_genres
       ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
