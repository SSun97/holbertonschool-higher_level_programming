-- create database
CREATE DATABASE IF NOT EXISTS hbt_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbt_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
