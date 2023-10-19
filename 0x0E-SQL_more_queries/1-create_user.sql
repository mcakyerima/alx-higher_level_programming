-- Log in to MySql SERVER with admin privileges eg (root)

-- Create or update user user_0d_1 and set their password, but only if it doesn't exist
CREATE USER IF NOT EXIST 'user_01_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user user_0d_1 on all db's and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flush the privileges to apply changes
FLUSH PRIVILEGES;

