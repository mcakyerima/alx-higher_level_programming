-- Create or ensure the existence of the 'hbtn_0d_usa' database.
-- Switch to the 'hbtn_0d_usa' database context.
-- Create or ensure the existence of the 'cities' table within the 'hbtn_0d_usa' database.
-- The 'cities' table schema consists of three columns:
--   1. 'id' of type INT, which is unique, auto-generated, cannot be null, and serves as the primary key.
--   2. 'state_id' of type INT, which cannot be null and must be a FOREIGN KEY that references the 'id' column in the 'states' table.
--   3. 'name' of type VARCHAR(256), which cannot be null.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       FOREIGN KEY (state_id) REFERENCES states (id)
);
