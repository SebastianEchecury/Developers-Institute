-- Exercise 1
-- Get a list of all the languages, from the language table.
SELECT name
FROM language

-- Get a list of all films joined with their languages – 
-- select the following details : film title, description, and language name.
SELECT F.title, F.description, L.name
FROM film F
JOIN language L
	ON F.language_id = F.language_id
	
-- Get all languages, even if there are no films in those languages – 
-- select the following details : film title, description, and language name.
SELECT * -- FALTA
FROM film F
FULL OUTER JOIN language L 
	ON F.language_id = F.language_id

-- Create a new table called new_film 
-- with the following columns : id, name. Add some new films to the table.
CREATE TABLE new_film(
	id SERIAL PRIMARY KEY,
	name VARCHAR(250)
)

INSERT INTO new_film(name) -- SELECT * FROM new_film
VALUES ('Forrest Gump'),
	   ('Harry Potter')

-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.
CREATE TABLE customer_review( -- DROP TABLE customer_review
	review_id SERIAL PRIMARY KEY,
	film_id INTEGER,
	language_id INTEGER,
	title VARCHAR(100),
	score SMALLINT,
	review_text TEXT,
	last_update DATE,
	FOREIGN KEY (film_id) REFERENCES new_film (id),
	FOREIGN KEY (language_id) REFERENCES language (language_id)
)

-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO customer_review(film_id, language_id, title, score, review_text, last_update)
VALUES(1, 1, 'title1', 7, 'text1', CURRENT_DATE),
	  (2, 2, 'title2', 5, 'text2', CURRENT_DATE)

SELECT *
FROM customer_review


-- Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film
WHERE id = 1
-- ERROR:  update or delete on table "new_film" violates foreign key constraint "customer_review_film_id_fkey" on table "customer_review"


-- Exercise 2
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film
SET language_id = 2
WHERE film_id = 133

-- Which foreign keys (references) are defined for the customer table? 
-- How does this affect the way in which we INSERT into the customer table?
customer_address_id_fkey FOREIGN KEY (address_id)
When we insert a new record, the value of customer_address_id_fkey should exist as address_id in address table

-- We created a new table called customer_review. Drop this table. 
-- Is this an easy step, or does it need extra checking?
DROP TABLE customer_review
It doesnt need an extra checking since no table has any field as foreign key in customer_review table

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT COUNT(*) -- 133
FROM rental
WHERE return_date IS NULL

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT *
FROM film F -- 1000
JOIN inventory I -- 4581
	ON F.film_id = I.film_id
JOIN rental R -- 16044
	ON R.inventory_id = I.inventory_id
JOIN payment P -- 183
	ON R.rental_id = P.rental_id
WHERE return_date IS NULL
ORDER BY P.amount DESC
LIMIT 30

-- Your friend is at the store, and decides to rent a movie. 
-- He knows he wants to see 4 movies, but he can’t remember their names. 
-- Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.

SELECT *-- F.title
FROM film F
JOIN inventory I
	ON F.film_id = I.film_id
JOIN rental R
	ON R.inventory_id = I.inventory_id
JOIN customer C
	ON C.customer_id = R.customer_id
WHERE (F.title ILIKE '%boat%' OR F.description ILIKE '%boat%')
  AND C.first_name = 'Matthew'
  AND C.last_name = 'Mahan'
ORDER BY F.replacement_cost DESC
LIMIT 1

SELECT title
FROM film F
JOIN inventory I
	ON F.film_id = I.film_id
JOIN rental R
	ON R.inventory_id = I.inventory_id
JOIN customer C
	ON C.customer_id = R.customer_id
JOIN payment P
	ON P.rental_id = R.rental_id
WHERE C.first_name = 'Matthew'
  AND C.last_name = 'Mahan'
  AND R.return_date >= '2005-07-28' AND R.return_date <= '2005-08-01'
  AND P.amount > 4

SELECT F.title
FROM film F
JOIN film_actor FA
	ON F.film_id = FA.film_id
JOIN actor A
	ON FA.actor_id = A.actor_id
WHERE description ILIKE '%sumo wrestler%'
  AND A.first_name = 'Penelope' AND A.last_name = 'Monroe'
  
SELECT F.title
FROM film F
JOIN film_category FC
	ON F.film_id = FC.film_id
JOIN category C
	ON C.category_id = FC.category_id
WHERE F.length < 60 
  AND F.rating = 'R'
  AND C.name = 'Documentary'
