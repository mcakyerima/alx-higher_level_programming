-- Create or ensure the existence of the 'unique_id' table.
-- The 'unique_id' table contains two columns: 'id' of type INT with a default value of 1 (unique) and 'name' of type VARCHAR(256).
-- The script will not fail if the table already exists.

CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
