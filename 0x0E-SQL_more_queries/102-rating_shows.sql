-- To import a SQL dump, use the provided link: https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql.
-- Create a database named 'hbtn_0d_tvshows_rate' by running the following command:
--   echo "CREATE DATABASE hbtn_0d_tvshows_rate;" | mysql -uroot -p
-- Import the SQL dump into the 'hbtn_0d_tvshows_rate' database using the 'curl' command.
-- This script lists all shows from 'hbtn_0d_tvshows_rate' by their rating.
-- Each record in the result set displays: tv_shows.title - rating sum.
-- The query results are sorted in descending order by the rating.
-- The script uses a single SELECT statement, and the database name is expected to be passed as an argument to the MySQL command.

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS 'rating'
  FROM tv_shows
INNER JOIN tv_show_ratings
        ON tv_shows.id = tv_show_ratings.show_id
  GROUP BY title
  ORDER BY rating DESC;
