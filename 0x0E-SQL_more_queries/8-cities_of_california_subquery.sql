-- Retrieve a list of all cities in California available in the 'hbtn_0d_usa' database.
-- The 'states' table in the database contains a single record where the 'name' is 'California' (the 'id' may vary).
-- The query results are sorted in ascending order based on the 'id' of the cities.
-- The query does not utilize the JOIN keyword.
-- The database name is expected to be passed as an argument to the MySQL command.

SELECT id, name
  FROM cities
 WHERE state_id = (SELECT id FROM states WHERE name = "California")
 GROUP BY id
 ORDER BY id ASC;
