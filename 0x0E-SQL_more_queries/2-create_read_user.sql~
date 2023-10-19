-- Log into MySQL with admin access

-- Creating the database hbtn_0d_2 if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create or Update the user user_0d_2 and set their password but only if it doesn't exist
CREATE USER IF NOT EXIST 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privileges to the user user_0d_2 on the database hbtn_0d_2
GRANT SELECT PRIVILEGES ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
