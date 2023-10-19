-- To import a SQL dump, use the provided link: https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql.
-- Create a database named 'hbtn_0d_tvshows' by running the following command:
--   echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
-- Import the SQL dump into the 'hbtn_0d_tvshows' database using the 'curl' command.
-- This script lists all shows from the 'hbtn_0d_tvshows' database and all genres linked to each show.
-- If a show doesn't have a genre, NULL is displayed in the genre column.
-- Each record in the result set displays: tv_shows.title - tv_genres.name.
-- The query results are sorted in ascending order by the show title and genre name.
-- The script uses a single SELECT statement, and the database name is expected to be passed as an argument to the MySQL command.

SELECT tv_shows.title, tv_genres.name
  FROM tv_shows
 LEFT JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
 LEFT JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
  ORDER BY tv_shows.title, tv_genres.name ASC;
