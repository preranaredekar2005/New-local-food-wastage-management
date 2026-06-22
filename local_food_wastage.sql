-- Database: food_Waste

-- DROP DATABASE IF EXISTS "food_Waste";

CREATE DATABASE "food_Waste"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
---------------------------------------------------
-- 1. CREATE TABLE
---------------------------------------------------

CREATE TABLE food (
    id INTEGER PRIMARY KEY,
    city VARCHAR(100),
    provider_type VARCHAR(100),
    meal_type VARCHAR(50),
    diet_type VARCHAR(50),
    quantity INTEGER
);

---INSERT DATA
INSERT INTO food VALUES (1,'Mumbai','Restaurant','Lunch','Vegetarian',120);
INSERT INTO food VALUES (2,'Pune','Supermarket','Dinner','Vegan',95);
INSERT INTO food VALUES (3,'Nagpur','Catering Service','Breakfast','Non-Vegetarian',110);
INSERT INTO food VALUES (4,'Nashik','Grocery Store','Snacks','Vegetarian',60);
INSERT INTO food VALUES (5,'Thane','Restaurant','Lunch','Vegan',140);
INSERT INTO food VALUES (6,'Aurangabad','Supermarket','Dinner','Vegetarian',85);
INSERT INTO food VALUES (7,'Mumbai','Catering Service','Breakfast','Vegetarian',130);
INSERT INTO food VALUES (8,'Pune','Restaurant','Lunch','Non-Vegetarian',150);
INSERT INTO food VALUES (9,'Nagpur','Grocery Store','Dinner','Vegetarian',90);
INSERT INTO food VALUES (10,'Thane','Supermarket','Snacks','Vegan',75);

-------VIEW DATA
SELECT * FROM food;

----------TOTAL FOODS
SELECT SUM(quantity) AS total_food
FROM food;

-------TOTAL RECORDS
SELECT COUNT(*) AS total_records
FROM food;

---------CITY WISE ANALYSIS
SELECT city,
SUM(quantity) AS total_quantity
FROM food
GROUP BY city
ORDER BY total_quantity DESC;

-------PROVIDER TYPE ANALYSIS
SELECT provider_type,
COUNT(*) AS total_listings
FROM food
GROUP BY provider_type;

-----MEAL TYPE ANALYSIS
SELECT meal_type,
SUM(quantity) AS total_food
FROM food
GROUP BY meal_type;

---------DIET TYPE ANALYSIS
SELECT diet_type,
SUM(quantity) AS total_food
FROM food
GROUP BY diet_type;

---------------AVERAGE FOOD PER PROVIDER
SELECT provider_type,
AVG(quantity) AS avg_quantity
FROM food
GROUP BY provider_type;

----------TOP CITY
SELECT city,
SUM(quantity) AS total_food
FROM food
GROUP BY city
ORDER BY total_food DESC
LIMIT 1;

-----FILTER VEGETARIAN
SELECT *
FROM food
WHERE diet_type = 'Vegetarian';

--------FILTER DINNER
SELECT *
FROM food
WHERE meal_type = 'Dinner';

-----------HAVING CONDITION
SELECT city,
SUM(quantity) AS total_quantity
FROM food
GROUP BY city
HAVING SUM(quantity) > 100;

--------SORT BY QUANTITY
SELECT *
FROM food
ORDER BY quantity DESC;

---------DISTINCT CITY
SELECT COUNT(DISTINCT city) AS total_cities
FROM food;