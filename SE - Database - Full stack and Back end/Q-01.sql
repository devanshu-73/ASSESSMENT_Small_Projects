-- # Write SQL query to solve the problem given below 
-- Make sure to user right sql syntax to solve the query given below :
-- ● Write sql query to find the items whose prices are higher than or equal 250rs. 
-- Order the result by product price in descending, then product name in 
-- ascending. Return pro_name and pro_price 

-- ● Write a sql query to find the cheapest item. Return pro_name and pro_price.

-- ● Write the sql query to calculate the average price of the items for each company. Return average price and company code.

-- ● Write the sql query to find the average total for all the product mention in the table 

create database assignment;

use assignment;

CREATE TABLE product (
    product_id INT PRIMARY KEY,
    pro_name VARCHAR(255),
    pro_price DECIMAL(10, 2),
    pro_code VARCHAR(10),
    company_code VARCHAR(10)
);

INSERT INTO product (product_id, pro_name, pro_price, pro_code) VALUES
(101, 'Mother Board', 3200.00, 15),
(102, 'Key Board', 450.00, 16),
(103, 'Zip Drive', 250.00, 14),
(104, 'Speaker', 550.00, 16),
(105, 'Monitor', 5000.00, 11),
(106, 'DVD Drive', 900.00, 12),
(107, 'CD Drive', 800.00, 12),
(108, 'Printer', 2600.00, 13),
(109, 'Refill Cartridge', 350.00, 13),
(110, 'Mouse', 250.00, 12);

-- Write SQL query to find the items whose prices are higher than or equal 250rs. Order the result by product price in descending, then product name in ascending. Return pro_name and pro_price.

SELECT pro_name, pro_price
FROM product
WHERE pro_price >= 250
ORDER BY pro_price DESC, pro_name ASC;

-- Write a SQL query to find the cheapest item. Return pro_name and pro_price.

SELECT pro_name, pro_price
FROM product
ORDER BY pro_price ASC
LIMIT 1;

-- Write the SQL query to calculate the average price of the items for each company. Return average price and company code.

SELECT AVG(pro_price) AS average_price, company_code
FROM product
GROUP BY company_code;

-- Write the SQL query to find the average total for all the products mentioned in the table.

SELECT AVG(pro_price) AS average_total_price
FROM product;