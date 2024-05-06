CREATE TABLE student(
	id SERIAL PRIMARY KEY,
	last_name VARCHAR (100),
	first_name VARCHAR (100),
	birth_date DATE
)

INSERT INTO student(first_name, last_name, birth_date)
VALUES ('Marc', 'Benichou', '11/02/1998'),
	   ('Yoan', 'Cohen', '12/03/2010'),
	   ('Lea', 'Benichou', '07/27/1987'),
	   ('Amelia', 'Dux', '04/07/1996'),
	   ('David', 'Grez', '06/14/2003'),
	   ('Omer', 'Simpson', '10/03/1980')
	   
SELECT *
FROM student
-- DROP TABLE student

SELECT first_name, last_name
FROM student
-- WHERE id = 2
-- WHERE last_name = 'Benichou' and first_name = 'Marc'
-- WHERE last_name = 'Benichou' OR first_name = 'Marc'
-- WHERE first_name LIKE '%a%'
-- WHERE first_name LIKE 'A%'
-- WHERE first_name LIKE '%a'
-- WHERE SUBSTRING(first_name, LENGTH(first_name)-1, 1) = 'a'
WHERE id IN (1, 3)

SELECT *
FROM student
WHERE birth_date >= '01/01/2000'