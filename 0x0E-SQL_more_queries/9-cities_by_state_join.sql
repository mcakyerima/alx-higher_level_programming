-- Retrieve a list of all cities available in the 'hbtn_0d_usa' database.
-- Each record in the result set displays: cities.id - cities.name - states.name.
-- The query results are sorted in ascending order based on the 'cities.id' column.
-- This query uses a single SELECT statement and involves an implicit JOIN operation between the 'cities' and 'states' tables.
-- The database name is expected to be passed as an argument to the MySQL command.

SELECT cities.id, cities.name, states.name
  FROM cities
  JOIN states
    ON cities.state_id = states.id
ORDER BY cities.id ASC;
