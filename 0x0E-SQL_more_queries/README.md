
# ADVANCE SQL QUERIES USING THE SHOWS DB

Author: [@mcakyerima](https://github.com/mcakyerima) 🚀

Welcome to the Shows Repository! This repository contains a collection of MySQL scripts for various tasks related to TV shows and databases. You can find queries for listing genres, creating users, and much more.

## Folder Structure

- [0-privileges.sql](0-privileges.sql) - Initial script for setting privileges.
- [1-create_user.sql](1-create_user.sql) - Create user SQL script.
- [10-genre_id_by_show.sql](10-genre_id_by_show.sql) - Query to get genre IDs by show.
- [100-not_my_genres.sql](100-not_my_genres.sql) - Query for finding shows not in a particular genre.
- [101-not_a_comedy.sql](101-not_a_comedy.sql) - Query for finding shows that are not in the "Comedy" genre.
- [102-rating_shows.sql](102-rating_shows.sql) - Query for rating shows.
- [103-rating_genres.sql](103-rating_genres.sql) - Query for rating genres.
- [11-genre_id_all_shows.sql](11-genre_id_all_shows.sql) - Query to get genre IDs for all shows.
- [12-no_genre.sql](12-no_genre.sql) - Query for shows with no genre.
- [13-count_shows_by_genre.sql](13-count_shows_by_genre.sql) - Query to count shows by genre.
- [14-my_genres.sql](14-my_genres.sql) - Query for "My Genres."
- [15-comedy_only.sql](15-comedy_only.sql) - Query to find shows in the "Comedy" genre.
- [16-shows_by_genre.sql](16-shows_by_genre.sql) - Query for shows by genre.
- [2-create_read_user.sql](2-create_read_user.sql) - Create and read user script.
- [3-force_name.sql](3-force_name.sql) - Force name script.
- [4-never_empty.sql](4-never_empty.sql) - Script for a field that should never be empty.
- [5-unique_id.sql](5-unique_id.sql) - SQL script for unique IDs.
- [6-states.sql](6-states.sql) - Script for creating states.
- [7-cities.sql](7-cities.sql) - Script for creating cities.
- [8-cities_of_california_subquery.sql](8-cities_of_california_subquery.sql) - Query for finding cities in California using a subquery.
- [9-cities_by_state_join.sql](9-cities_by_state_join.sql) - Query for finding cities by state using JOIN.

## Environment

- Language: MySQL scripts
- OS: Ubuntu 14.04 LTS
- MySQL Version: 5.7.8
- Suggested Style Guide: SQLStyle
- Usage: `cat [filename] | mysql -hlocalhost -uroot -p [database]`

📺 Happy scripting!
