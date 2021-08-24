Python 3.7.8. Simple connection to MySQL using Flask and getting data from HTML page 

1) --------------------------------------
Python - 3.7.8
Mysql  - 8.0.26.0

2) --------------------------------------
pip3 install Flask
pip3 install Flask-MySQLdb

3) --------------------------------------
Db name ----- logtest

CREATE SCHEMA `logtest` DEFAULT CHARACTER SET utf8 ;
USE `logtest`;

CREATE TABLE IF NOT EXISTS `accounts` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`username` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8; 
