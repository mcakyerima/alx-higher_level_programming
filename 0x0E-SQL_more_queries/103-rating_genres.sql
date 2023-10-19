-- To import a SQL dump, use the provided link: https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql.
-- Create a database named 'hbtn_0d_tvshows_rate' by running the following command:
--   echo "CREATE DATABASE hbtn_0d_tvshows_rate;" | mysql -uroot -p
-- Import the SQL dump into the 'hbtn_0d_tvshows_rate' database using the 'curl' command.
-- This script lists all genres from 'hbtn_0d_tvshows_rate' by their rating.
-- Each record in the result set displays: tv_genres.name - rating sum.
-- The query results are sorted in descending order by the rating.
-- The script uses a single SELECT statement, and the database name is expected to be passed as an argument to the MySQL command.

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS 'rating'
  FROM tv_genres
INNER JOIN tv_show_genres
        ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_show_ratings
        ON tv_show_ratings.show_id = tv_show_genres.show_id
  GROUP BY name
  ORDER BY rating DESC;
