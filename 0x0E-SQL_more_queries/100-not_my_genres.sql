-- To import a SQL dump, use the provided link: https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql.
-- Create a database named 'hbtn_0d_tvshows' by running the following command:
--   echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
-- Import the SQL dump into the 'hbtn_0d_tvshows' database using the 'curl' command.
-- This script uses the 'hbtn_0d_tvshows' database to list all genres not linked to the show 'Dexter.'
-- The 'tv_shows' table contains a single record where the 'title' is 'Dexter' (the 'id' may vary).
-- Each record in the result set displays: tv_genres.name.
-- The query results are sorted in ascending order by the genre name.
-- The script utilizes a maximum of two SELECT statements, and the database name is expected to be passed as an argument to the MySQL command.

SELECT tv_genres.name
  FROM tv_genres
 WHERE tv_genres.name NOT IN (
    SELECT tv_genres.name
      FROM tv_genres
INNER JOIN tv_show_genres
        ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
     WHERE tv_shows.title = "Dexter"
  )
ORDER BY tv_genres.name ASC;
