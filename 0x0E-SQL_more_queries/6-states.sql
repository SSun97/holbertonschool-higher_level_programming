-- create a database and table
CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
CREATE TABLE IF NOT EXIST hbtn_0d_usa.states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256), PRIMARY KEY(id));
