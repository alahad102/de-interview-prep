-- ============================================================
-- Window Functions Practice Database (MySQL)
-- Designed to exercise every pattern in your #5-#10 framework
-- ============================================================

DROP DATABASE IF EXISTS window_practice;
CREATE DATABASE window_practice;
USE window_practice;

-- ------------------------------------------------------------
-- TABLE 1: departments + employees
-- Covers: ROW_NUMBER, RANK, DENSE_RANK, NTILE, FIRST_VALUE, LAST_VALUE
-- Salary ties are intentional -- use them to see RANK vs ROW_NUMBER diverge
-- ------------------------------------------------------------

CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(50) NOT NULL
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department_id INT NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    hire_date DATE NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

INSERT INTO departments (department_name) VALUES
('Sales'), ('Engineering'), ('Marketing');

INSERT INTO employees (first_name, last_name, department_id, salary, hire_date) VALUES
('Alice',  'Nguyen',   1, 90000, '2019-03-01'),
('Bob',    'Turner',   1, 90000, '2020-06-15'),  -- tie with Alice
('Carol',  'Diaz',     1, 75000, '2021-01-10'),
('Dave',   'Kim',      1, 60000, '2022-08-20'),
('Eve',    'Martinez', 2, 120000, '2018-02-01'),
('Frank',  'Lopez',    2, 110000, '2019-09-15'),
('Grace',  'Chen',     2, 110000, '2020-03-05'), -- tie with Frank
('Henry',  'Walsh',    2, 95000, '2021-11-01'),
('Ivy',    'Patel',    3, 80000, '2020-01-15'),
('Jack',   'Ahmed',    3, 80000, '2020-01-15'),  -- exact tie (salary + hire_date)
('Kara',   'Wolfe',    3, 70000, '2021-05-01'),
('Liam',   'Ortiz',    3, 65000, '2022-02-01');

-- ------------------------------------------------------------
-- TABLE 2: monthly_revenue
-- Covers: LAG, LEAD, running SUM/AVG, COUNT OVER, moving average
-- East region has an intentional missing month (April) --
-- save that for gaps-and-islands practice later (pattern #11)
-- ------------------------------------------------------------

CREATE TABLE monthly_revenue (
    revenue_id INT PRIMARY KEY AUTO_INCREMENT,
    region VARCHAR(50) NOT NULL,
    revenue_month DATE NOT NULL,
    revenue DECIMAL(12,2) NOT NULL
);

INSERT INTO monthly_revenue (region, revenue_month, revenue) VALUES
('North', '2024-01-01', 42000),
('North', '2024-02-01', 45500),
('North', '2024-03-01', 41000),
('North', '2024-04-01', 47500),
('North', '2024-05-01', 50200),
('North', '2024-06-01', 48800),
('South', '2024-01-01', 38000),
('South', '2024-02-01', 39500),
('South', '2024-03-01', 41200),
('South', '2024-04-01', 40100),
('South', '2024-05-01', 43000),
('South', '2024-06-01', 44500),
('East',  '2024-01-01', 30500),
('East',  '2024-02-01', 31000),
('East',  '2024-03-01', 29800),
('East',  '2024-05-01', 33000),   -- April is deliberately missing
('East',  '2024-06-01', 34500);

-- ------------------------------------------------------------
-- TABLE 3: orders
-- Covers: Top-N per customer, running totals per customer,
-- FIRST_VALUE/LAST_VALUE, dedup, amount ties for RANK practice
-- ------------------------------------------------------------

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL
);

INSERT INTO orders (customer_id, order_date, amount) VALUES
(1, '2024-01-05', 120.00),
(1, '2024-01-19', 85.50),
(1, '2024-02-02', 220.00),
(1, '2024-02-20', 220.00),  -- tie for top order amount
(1, '2024-03-11', 60.00),
(2, '2024-01-08', 300.00),
(2, '2024-01-28', 150.00),
(2, '2024-02-14', 300.00),  -- tie
(2, '2024-03-01', 95.00),
(3, '2024-01-15', 45.00),
(3, '2024-02-05', 60.00),
(3, '2024-02-25', 75.00),
(3, '2024-03-19', 90.00),
(4, '2024-01-02', 500.00),
(4, '2024-01-30', 130.00),
(4, '2024-02-27', 210.00);

-- ------------------------------------------------------------
-- Quick sanity check -- run this after loading to confirm row counts
-- ------------------------------------------------------------
SELECT 'departments' AS table_name, COUNT(*) AS row_count FROM departments
UNION ALL
SELECT 'employees', COUNT(*) FROM employees
UNION ALL
SELECT 'monthly_revenue', COUNT(*) FROM monthly_revenue
UNION ALL
SELECT 'orders', COUNT(*) FROM orders;