-- To import a SQL dump, use the provided link: https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql.
-- Create a database named 'hbtn_0d_tvshows' by running the following command:
--   echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
-- Import the SQL dump into the 'hbtn_0d_tvshows' database using the 'curl' command.
-- This script lists all genres from 'hbtn_0d_tvshows' and displays the number of shows linked to each genre.
-- Each record in the result set displays: tv_genres.name - number_shows.
-- Genres without any linked shows are not displayed.
-- The query results are sorted in descending order by the number of shows linked to each genre.
-- This script uses a single SELECT statement, and the database name is expected to be passed as an argument to the MySQL command.

SELECT tv_genres.name AS genre, COUNT(*) AS 'number_shows'
  FROM tv_genres
INNER JOIN tv_show_genres
        ON tv_genres.id = tv_show_genres.genre_id
  GROUP BY genre
  ORDER BY number_shows DESC;
