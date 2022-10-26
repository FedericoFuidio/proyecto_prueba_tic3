DROP DATABASE tic3db;

CREATE DATABASE tic3db
    WITH 
    OWNER = 'postgres'
    ENCODING =  'UTF8' 
    LC_COLLATE =  'Spanish_Uruguay.1252'
    LC_CTYPE =  'Spanish_Uruguay.1252' 
    TABLESPACE = pg_default
    CONNECTION LIMIT = 10;

\c tic3db

INSERT INTO api_user( id ,  first_name ,  last_name ,  mail ,  phone_number ,  password )
VALUES ( '1' ,  'Marco' ,  'Zunino' ,  'mzunino@correo.um.edu.uy' ,  '091919919' ,  '123' );

INSERT INTO api_user( id ,  first_name ,  last_name ,  mail ,  phone_number ,  password )
VALUES ( '101' ,  'nombre1' ,  'apellido1' ,  'usuario1@gmail.com',  '099123456' ,  '123' );

INSERT INTO api_comprador( user_id )
VALUES ( '1' );

INSERT INTO api_vendedor( user_id )
VALUES ( '101' );

INSERT INTO api_vehiculo( vendedor_id ,  tipo ,  marca ,  modelo ,  matricula ,  precio_base )
VALUES ( '101' ,  'Venta' ,  'VW' ,  'Gol' ,  'ABC 1234' ,  'USD 30,000' );

INSERT INTO api_vehiculo( vendedor_id ,  tipo ,  marca ,  modelo ,  matricula ,  precio_base )
VALUES ( '101' ,  'Alquiler' ,  'BMW' ,  'Serie 3' ,  'XYZ 6789' ,  'USD 40,000' );

INSERT INTO api_vehiculo( vendedor_id ,  tipo ,  marca ,  modelo ,  matricula ,  precio_base )
VALUES ( '1' ,  'Venta' ,  'Fiat' ,  'Uno' ,  'AAA 1111' ,  'USD 10,000' );

INSERT INTO api_like( comprador_id, vehiculo_id )
VALUES ( '101', '4');