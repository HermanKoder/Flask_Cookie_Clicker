
CREATE DATABASE cookieclicker;

USE cookieclicker;

CREATE TABLE cookieScore (
    id int NOT NULL AUTO_INCREMENT,
    cookies NOT NULL,
    PRIMARY KEY (id)
    FOREIGN KEY (id) REFERENCES (id)
);

CREATE TABLE login (
    id int NOT NULL AUTO_INCREMENT,
    navn varchar(50) NOT NULL,
    passord varchar(255) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO login (navn, passord) VALUE ("Herman", "Bolla");

SELECT login FROM cookieScore
INNER JOIN 