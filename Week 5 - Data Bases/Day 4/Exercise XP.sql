-- Exercise 1
SELECT *
FROM items
ORDER BY price ASC

SELECT *
FROM items
WHERE price >= 80
ORDER BY price DESC

SELECT CONCAT(name, ' ', lastname) Name
FROM customers
ORDER BY name
LIMIT 3

SELECT DISTINCT name
FROM customers
ORDER BY name DESC

-- Exercise 2
SELECT *
FROM customer

SELECT CONCAT(first_name, ' ', last_name) full_name
FROM customer


SELECT DISTINCT(create_date)
FROM customer

SELECT *
FROM customer
ORDER BY first_name DESC


SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate

SELECT c.*, a.address, a.phone
FROM customer c
JOIN address a
	ON c.address_id = a.address_id
WHERE a.district = 'Texas'
