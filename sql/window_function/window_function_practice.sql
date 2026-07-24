-- ============================================================
-- PART A: employees table (ranking functions)
-- ============================================================

-- Q1: For every employee, show their salary rank within their own
-- department, from highest to lowest. Don't worry about ties yet.

SELECT
    employee_id,
    first_name,
    last_name,
    department_id,
    salary,
    hire_date,
    row_number() over(partition by department_id order by salary desc) as row_rank
FROM
    employees;

-- Q2: Now redo Q1, but this time make sure tied salaries share the
-- same rank AND leave a gap afterward (e.g. 1, 1, 3, 4).

SELECT
    employee_id,
    first_name,
    last_name,
    department_id,
    salary,
    hire_date,
    RANK() over(partition by department_id order by salary desc) as row_rank
FROM
    employees;

-- Q3: Redo Q1 again, but this time tied salaries should share the
-- same rank with NO gap afterward (e.g. 1, 1, 2, 3).

SELECT
    employee_id,
    first_name,
    last_name,
    department_id,
    salary,
    hire_date,
    DENSE_RANK() over(partition by department_id order by salary desc) as row_rank
FROM
    employees;

-- Q4: For each employee, show what percentile "bucket" they fall
-- into if you split the ENTIRE company (ignore department) into
-- 4 equal-sized groups by salary.

SELECT
    *,
    NTILE(4) over(order by salary desc) as bucket
FROM
    employees;

-- Q5: Return the top 2 highest-paid employees in each department.
-- If there's a tie for 2nd place, only one of them should show up
-- (pick either one).


SELECT
    employee_id, first_name, last_name, department_id, salary, hire_date
FROM
    (SELECT
        *,
        ROW_NUMBER() OVER(PARTITION BY department_id ORDER BY salary DESC) AS r_no
    FROM
        employees) AS e1
WHERE r_no <= 2;


SELECT
    employee_id, first_name, last_name, department_id, salary, hire_date
FROM
    (SELECT
        *,
        DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS salary_tier,
        ROW_NUMBER() OVER (PARTITION BY department_id, salary ORDER BY employee_id) AS tie_breaker
    FROM
        employees) AS e1
WHERE salary_tier <= 2 AND tie_breaker = 1;

-- Q6: For every employee, add a column showing the highest salary
-- in their department -- repeated on every row, not just the top one.

SELECT
    employee_id, first_name, last_name, department_id, salary,
    MAX(salary) OVER (PARTITION BY department_id) AS highest_salary
FROM employees;

SELECT
    e.employee_id, e.first_name, e.last_name, e.department_id, e.salary,
    d.highest_salary
FROM employees e
JOIN (
    SELECT department_id, MAX(salary) AS highest_salary
    FROM employees
    GROUP BY department_id
) d ON e.department_id = d.department_id;

-- Q7: For every employee, add a column showing the LOWEST salary
-- in their department, repeated on every row.


-- ============================================================
-- PART B: monthly_revenue table (offset + running aggregates)
-- ============================================================

-- Q8: For each region, show each month's revenue next to the
-- PREVIOUS month's revenue in the same row.

-- Q9: For each region, calculate the dollar CHANGE in revenue from
-- the previous month (this month's revenue minus last month's).

-- Q10: For each region, show a running total of revenue from
-- January through the current month.

-- Q11: For each region, calculate a 3-month moving average of
-- revenue (current month + the 2 before it).

-- Q12: For each region, show what fraction (as a %) each month's
-- revenue is of that region's total 6-month revenue.


-- ============================================================
-- PART C: orders table (bringing it together)
-- ============================================================

-- Q13: Return each customer's 2 highest-value orders. Handle ties
-- the same way Q5 did.

-- Q14: For each customer, show a running total of how much they've
-- spent so far, ordered by order date.

-- Q15: For each customer, show how many orders they've placed in
-- total (same number repeated on every row for that customer --
-- don't use GROUP BY).


-- ============================================================
-- PART D: capstone (mixing tables / patterns)
-- ============================================================

-- Q16: For each employee, show how many years after the FIRST hire
-- in their department they were hired (i.e. compare their hire_date
-- to the earliest hire_date in their own department).

-- Q17: Find every employee who is the single highest-paid person
-- in their department -- output just one row per department, no
-- ties allowed in the output.