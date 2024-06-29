-- Part 1
CREATE TABLE customer(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(100),
	last_name VARCHAR(100) NOT NULL
)

CREATE TABLE customer_profile(
	id SERIAL PRIMARY KEY,
	isLoggedIn BOOLEAN default false,
	customer_id INTEGER,
	CONSTRAINT customer_id_fk FOREIGN KEY(customer_id) REFERENCES customer(id)
)

INSERT INTO customer(first_name, last_name)
VALUES ('John', 'Doe'),
	   ('Jerome' ,'Lalu'),
	   ('Lea', 'Rive')
	   
INSERT INTO customer_profile(isLoggedIn, customer_id)
SELECT false, id
FROM customer
WHERE id = 1
INSERT INTO customer_profile(isLoggedIn, customer_id)
SELECT true, id
FROM customer
WHERE id = 2

-- SELECT * FROM customer_profile
The number of customers that are not LoggedIn

SELECT C.first_name
FROM customer_profile CP
JOIN customer C
	ON CP.customer_id = C.id
WHERE CP.isLoggedIn = true

SELECT C.first_name, CP.isLoggedIn
FROM customer C
LEFT JOIN customer_profile CP
	ON CP.customer_id = C.id
	
SELECT customer_id, MAX(id) id
INTO TEMP TABLE aux
FROM customer_profile
GROUP BY customer_id
SELECT COUNT(*)
FROM customer C
LEFT JOIN aux A
	ON A.customer_id = C.id
LEFT JOIN customer_profile CP
	ON A.id = CP.id
WHERE CP.isLoggedIn <> true


-- Part 2
CREATE TABLE book(
	book_id SERIAL PRIMARY KEY, 
	title VARCHAR(100) NOT NULL, 
	author VARCHAR(100) NOT NULL
)

INSERT INTO book(title, author)
VALUES ('Alice In Wonderland', 'Lewis Carroll'),
	   ('Harry Potter', 'J.K Rowling'),
	   ('To kill a mockingbird', 'Harper Lee')

CREATE TABLE student(
	student_id SERIAL PRIMARY KEY, 
	name VARCHAR(100) NOT NULL UNIQUE, 
	age SMALLINT CHECK (age <= 15)
)

INSERT INTO student(name, age)
VALUES ('John', 12),
	   ('Lera', 11),
	   ('Patrick', 10),
	   ('Bob', 14)

CREATE TABLE library(
	book_id INTEGER,
	student_id INTEGER,
	borrowed_date DATE,
	CONSTRAINT book_id_fk FOREIGN KEY(book_id) REFERENCES book(book_id),
	CONSTRAINT student_id_fk FOREIGN KEY(student_id) REFERENCES student(student_id),
	PRIMARY KEY (book_id, student_id)
)

INSERT INTO library(book_id, student_id, borrowed_date)
VALUES (1, 1, '02/15/2022'),
	   (3, 4, '03/03/2021'),
	   (1, 2, '05/23/2021'),
	   (2, 4, '08/12/2021')
	   
SELECT *
FROM library

SELECT S.name, B.title
FROM library L
JOIN student S
	ON L.student_id = S.student_id
JOIN book B
	ON B.book_id = L.book_id

SELECT AVG(age)
FROM library L
JOIN student S
	ON S.student_id = L.student_id
WHERE L.book_id = 1

DELETE FROM student
WHERE student_id = 1
-- ERROR:  update or delete on table "student" violates foreign key constraint "student_id_fk" on table "library"

