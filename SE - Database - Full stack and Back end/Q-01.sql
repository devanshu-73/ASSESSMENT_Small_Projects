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
INSERT INTO product (product_id, pro_name, pro_price, pro_code) VALUES
(101, 'Mother Board', 3200.00,15),
(102, 'Key Board', 450.00,16),
(103, 'Zip Drive', 250.00, 14),
(104, 'Speaker', 550.00,16 ),
(105, 'Monitor', 5000.00, 11),
(106, 'DVD Drive', 900.00, 12);
(107, 'CD Drive', 800.00,12 );
(108, 'Printer', 2600.00, 13);
(109, 'Refill Cartridge', 350.00, 13);
(110, 'Mouse', 250.00, 12);