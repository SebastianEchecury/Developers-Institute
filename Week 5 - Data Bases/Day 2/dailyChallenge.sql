SELECT COUNT(*)
FROM actors

INSERT INTO actors (first_name, last_name, number_oscars)
VALUES('Prueba1', 'Prueba2', 5)
-- ERROR:  null value in column "age" of relation "actors" violates not-null constraint