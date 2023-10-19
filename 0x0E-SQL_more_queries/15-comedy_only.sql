-- To import a SQL dump, use the provided link: https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql.
-- Create a database named 'hbtn_0d_tvshows' by running the following command:
--   echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
-- Import the SQL dump into the 'hbtn_0d_tvshows' database using the 'curl' command.
-- This script lists all Comedy shows in the 'hbtn_0d_tvshows' database.
-- The 'tv_genres' table contains a single record where the 'name' is 'Comedy' (the 'id' may vary).
-- Each record in the result set displays: tv_shows.title.
-- The query results are sorted in ascending order by the show title.
-- The script uses a single SELECT statement, and the database name is expected to be passed as an argument to the MySQL command.

SELECT tv_shows.title
  FROM tv_shows
INNER JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
 WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title ASC;
