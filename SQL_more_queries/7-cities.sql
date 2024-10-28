-- a script that creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE If NOT EXISTS cities(
	id INT NOT NULL AUTO_INCREMENT UNIQUE,
	name VARCHAR(256),
	PRIMARY KEY (id)
);
