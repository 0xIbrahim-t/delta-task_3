CREATE DATABASE IF NOT EXISTS game_db;

USE game_db;

CREATE USER IF NOT EXISTS 'username' IDENTIFIED BY 'password';

GRANT ALL ON game_db.* TO 'username'@'%';
FLUSH PRIVILEGES;

create table users (username VARCHAR(10), password VARCHAR(1024), points INT);
create table QA (question VARCHAR(1024), questionby VARCHAR(1024), answeredby VARCHAR(1024));
