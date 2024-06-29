-- CREATE DATABASE public

-- CREATE TABLE items(
-- 	id SERIAL PRIMARY KEY,
-- 	description VARCHAR(100),
-- 	price DECIMAL(10, 2)
-- )


-- CREATE TABLE customers(
-- 	id SERIAL PRIMARY KEY,
-- 	name VARCHAR(100),
-- 	lastName VARCHAR(100)
-- )


INSERT INTO items(description, price)
VALUES ('Small Desk', 100),
	   ('Large desk', 300),
	   ('Fan', 30)
	   
INSERT INTO customers (name, lastName)
VALUES ('Greg', 'Jones'),
	   ('Sandra', 'Jones'),
	   ('Scott', 'Scott'),
	   ('Trevor', 'Green'),
	   ('Melanie', 'Johnson')
	   
SELECT *
FROM items
-- WHERE price > 80
WHERE price <= 300


SELECT *
FROM customers
-- WHERE lastName = 'Smith'
-- WHERE lastName = 'Jones'
WHERE name != 'Scott'