-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
-- states.id INT unique, auto generated, can’t be null and is a primary key
-- states.name VARCHAR(256) can’t be null
-- if hbtn_0d_usa and/or states already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);
