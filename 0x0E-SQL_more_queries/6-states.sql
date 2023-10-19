-- Create or ensure the existence of the 'hbtn_0d_usa' database.
-- Switch to the 'hbtn_0d_usa' database context.
-- Create or ensure the existence of the 'states' table within the 'hbtn_0d_usa' database.
-- The 'states' table schema consists of two columns:
--   1. 'id' of type INT, which is unique, auto-generated, cannot be null, and serves as the primary key.
--   2. 'name' of type VARCHAR(256), which cannot be null.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       name VARCHAR(256) NOT NULL
);
