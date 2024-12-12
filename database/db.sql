
CREATE DATABASE cookieclicker;

USE cookieclicker;

CREATE TABLE cookieScore (
    id int NOT NULL AUTO_INCREMENT,
    cookies NOT NULL,
    PRIMARY KEY (id)
    FOREIGN KEY (id) REFERENCES (id)
);

INSERT INTO cookieScore (navn, passord) VALUE ("Herman", "Bolla");




CREATE TABLE login (
    id int NOT NULL AUTO_INCREMENT,
    navn varchar(50) NOT NULL,
    passord varchar(255) NOT NULL,
    PRIMARY KEY (id)
);