-- creates the database hbtn_0d_usa
-- table states

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- USE THE DATABASE
USE hbtn_0d_usa;

-- CREATE THE TABLE
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);

