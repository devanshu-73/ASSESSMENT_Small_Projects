-- # Write SQL query to solve the problem given below 
-- Make sure to user right sql syntax to solve the query given below :
-- ● Write sql query to find the items whose prices are higher than or equal 250rs. 
-- Order the result by product price in descending, then product name in 
-- ascending. Return pro_name and pro_price 

-- ● Write a sql query to find the cheapest item. Return pro_name and pro_price.

-- ● Write the sql query to calculate the average price of the items for each company. Return average price and company code.

-- ● Write the sql query to find the average total for all the product mention in the table 

CREATE TABLE product (
    product_id INT PRIMARY KEY,
    pro_name VARCHAR(255),
    pro_price DECIMAL(10, 2),
    pro_code VARCHAR(10),
    company_code VARCHAR(10)
);

-- Sample data insertion for testing
INSERT INTO product (product_id, pro_name, pro_price, pro_code, company_code) VALUES
(101, 'Keyboard', 300.00, 'K123', 'C1'),
(102, 'Motherboard', 500.00, 'M456', 'C2'),
(103, 'Monitor', 350.00, 'M789', 'C1'),
(104, 'Monitor', 350.00, 'M789', 'C1'),
(105, 'Monitor', 350.00, 'M789', 'C1'),
(106, 'Speaker', 200.00, 'S012', 'C3');
(107, 'Speaker', 200.00, 'S012', 'C3');
(108, 'Speaker', 200.00, 'S012', 'C3');
(109, 'Speaker', 200.00, 'S012', 'C3');
(110, 'Speaker', 200.00, 'S012', 'C3');