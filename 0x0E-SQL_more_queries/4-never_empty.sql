-- creates the table id_not_null
-- data in table: id INT with the default value 1, name VARCHAR(256)
-- script should not fail if table exists

CREATE TABLE IF NOT EXISTS id_not_null (
       id INT DEFAULT 1,
       name VARCHAR(256)
);
