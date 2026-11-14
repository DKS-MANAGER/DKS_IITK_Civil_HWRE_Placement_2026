-- =============================================================================
-- TREDENCE DATA SCIENCE PRACTICE SCHEMA: RETAIL & CPG DECISION INTELLIGENCE
-- Standard: Compatible with PostgreSQL, SQLite, MySQL 8.0, Snowflake, Databricks
-- =============================================================================

DROP TABLE IF EXISTS transaction_items;
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS promotions;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS stores;
DROP TABLE IF EXISTS customers;

-- 1. Stores Dimension
CREATE TABLE stores (
    store_id VARCHAR(10) PRIMARY KEY,
    store_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    store_format VARCHAR(30) NOT NULL -- 'Supermarket', 'Hypermarket', 'Express'
);

-- 2. Products Dimension
CREATE TABLE products (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    sub_category VARCHAR(50) NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    cost_price DECIMAL(10, 2) NOT NULL
);

-- 3. Customers Dimension
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    signup_date DATE NOT NULL,
    loyalty_tier VARCHAR(20) NOT NULL -- 'Bronze', 'Silver', 'Gold'
);

-- 4. Promotions Dimension
CREATE TABLE promotions (
    promo_id VARCHAR(10) PRIMARY KEY,
    promo_name VARCHAR(100) NOT NULL,
    discount_pct DECIMAL(5, 2) NOT NULL,
    channel VARCHAR(30) NOT NULL -- 'Mailer', 'In-Store Display', 'App Coupon'
);

-- 5. Transactions Header Fact
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    store_id VARCHAR(10) REFERENCES stores(store_id),
    transaction_date DATE NOT NULL,
    total_amount DECIMAL(12, 2) NOT NULL,
    payment_method VARCHAR(30) NOT NULL
);

-- 6. Transaction Items Line Fact
CREATE TABLE transaction_items (
    item_id INT PRIMARY KEY,
    transaction_id INT REFERENCES transactions(transaction_id),
    product_id VARCHAR(10) REFERENCES products(product_id),
    promo_id VARCHAR(10) REFERENCES promotions(promo_id),
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    line_total DECIMAL(10, 2) NOT NULL
);

-- =============================================================================
-- SEED DATA INSERTION
-- =============================================================================

INSERT INTO stores VALUES 
('STR_101', 'Tredence Fresh Indiranagar', 'Bengaluru', 'Karnataka', 'Supermarket'),
('STR_102', 'Tredence Express HSR', 'Bengaluru', 'Karnataka', 'Express'),
('STR_201', 'Tredence Hyper Gachibowli', 'Hyderabad', 'Telangana', 'Hypermarket'),
('STR_301', 'Tredence OMR Metro', 'Chennai', 'Tamil Nadu', 'Supermarket');

INSERT INTO products VALUES
('PRD_01', 'Organic Whole Milk 1L', 'Dairy', 'Milk', 65.00, 48.00),
('PRD_02', 'Greek Yogurt 400g', 'Dairy', 'Yogurt', 120.00, 85.00),
('PRD_03', 'Artisan Sourdough Loaf', 'Bakery', 'Bread', 95.00, 60.00),
('PRD_04', 'Colombian Dark Roast Coffee 250g', 'Beverages', 'Coffee', 450.00, 310.00),
('PRD_05', 'Almond Butter 350g', 'Spreads', 'Nut Butter', 550.00, 390.00);

INSERT INTO customers VALUES
(1001, 'Aditi Sharma', '2023-01-10', 'Gold'),
(1002, 'Rohan Verma', '2023-03-15', 'Silver'),
(1003, 'Priya Nair', '2023-06-20', 'Bronze'),
(1004, 'Vikram Mehta', '2023-08-01', 'Gold'),
(1005, 'Ananya Das', '2024-01-05', 'Bronze'); -- Inactive after signup test

INSERT INTO promotions VALUES
('PRM_00', 'No Promotion', 0.00, 'None'),
('PRM_10', 'Weekend Flash Sale 10%', 10.00, 'App Coupon'),
('PRM_20', 'CPG Brand Launch 20%', 20.00, 'In-Store Display');

INSERT INTO transactions VALUES
(5001, 1001, 'STR_101', '2024-01-15', 580.00, 'UPI'),
(5002, 1001, 'STR_101', '2024-01-22', 450.00, 'Credit Card'),
(5003, 1002, 'STR_102', '2024-01-18', 130.00, 'Cash'),
(5004, 1003, 'STR_201', '2024-01-20', 1100.00, 'Credit Card'),
(5005, 1004, 'STR_301', '2024-01-25', 95.00, 'UPI');

INSERT INTO transaction_items VALUES
(9001, 5001, 'PRD_01', 'PRM_00', 2, 65.00, 130.00),
(9002, 5001, 'PRD_04', 'PRM_00', 1, 450.00, 450.00),
(9003, 5002, 'PRD_04', 'PRM_00', 1, 450.00, 450.00),
(9004, 5003, 'PRD_01', 'PRM_00', 2, 65.00, 130.00),
(9005, 5004, 'PRD_05', 'PRM_20', 2, 440.00, 880.00),
(9006, 5004, 'PRD_02', 'PRM_10', 2, 108.00, 216.00),
(9007, 5005, 'PRD_03', 'PRM_00', 1, 95.00, 95.00);
