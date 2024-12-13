CREATE DATABASE cookieDB;

USE cookieDB;

CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    navn VARCHAR(255) NOT NULL,
    mail VARCHAR(255) NOT NULL,
    passord VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE cookieScore (
    id INT NOT NULL AUTO_INCREMENT,
    cookies INT NOT NULL,
    user_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
