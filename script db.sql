DROP DATABASE tic3db;

CREATE DATABASE tic3db
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Uruguay.1252'
    LC_CTYPE = 'Spanish_Uruguay.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = 10;

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    email VARCHAR(45) UNIQUE NOT NULL,
);

CREATE TABLE compradores (
    usuario INT PRIMARY KEY,

    FOREIGN KEY (usuario)
        REFERENCES usuarios (id)
);

CREATE TABLE vendedores (
    usuario INT PRIMARY KEY,

    FOREIGN KEY (usuario)
        REFERENCES usuarios (id)
);

CREATE TABLE vehiculos (
    id SERIAL PRIMARY KEY,
    matricula VARCHAR(8) UNIQUE NOT NULL,
    vendedor INT NOT NULL,
    precio VARCHAR(20),

    FOREIGN KEY (vendedor)
        REFERENCES vendedores (usuario)
);

CREATE TABLE chats (
    id SERIAL PRIMARY KEY,
    calificacion INT,
);

CREATE TABLE likes (
    comprador INT NOT NULL,
    vehiculo INT NOT NULL,
    chat INT UNIQUE,

    PRIMARY KEY (comprador, vehiculo),
    FOREIGN KEY (comprador)
        REFERENCES compradores (usuario),
    FOREIGN KEY (vehiculo)
        REFERENCES vehiculos (id),
    FOREIGN KEY (chat)
        REFERENCES chats (id)
);

CREATE TABLE mensajes (
    id SERIAL PRIMARY KEY,
    chat INT NOT NULL,

    FOREIGN KEY (chat)
        REFERENCES chats (id)
);


