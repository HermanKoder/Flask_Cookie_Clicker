CREATE DATABASE cookieDB;

USE cookieDB;

CREATE TABLE cookieScore (
    id INT NOT NULL AUTO_INCREMENT,
    cookies INT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE registrer (
    id int NOT NULL AUTO_INCREMENT,
    navn INT NOT NULL,
    passord INT NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO cookieScore (cookies) VALUE (100);
INSERT INTO cookieScore (cookies) VALUE (23);
INSERT INTO cookieScore (cookies) VALUE (345);
INSERT INTO cookieScore (cookies) VALUE (456);

INSERT INTO cookieScore (id, cookies) VALUE (11, 456);
INSERT INTO cookieScore (id, cookies) VALUE (22, 456);
INSERT INTO cookieScore (id, cookies) VALUE (33, 456);
INSERT INTO cookieScore (id, cookies) VALUE (44, 456);