-- creates the database hbtn_0d_usa
-- table states

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- USE THE DATABASE
USE hbtn_0d_usa;

-- CREATE THE TABLE
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,

	-- Define foreign key constraint
	FOREIGN KEY (state_id) REFERENCES states(id)
);

