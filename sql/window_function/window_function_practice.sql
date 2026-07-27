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


SELECT employee_id, first_name, last_name, department_id, salary, hire_date
FROM 
    (SELECT
        e.*,
        ROW_NUMBER() OVER(PARTITION BY department_id ORDER BY salary DESC) as rw,
        RANK() OVER(PARTITION BY department_id ORDER BY salary DESC) as rnk,
        DENSE_RANK() OVER(PARTITION BY department_id ORDER BY salary DESC) as drnk
    FROM
        employees as e) as t1
WHERE (t1.rw = t1.rnk AND t1.drnk < 3);


SELECT
    employee_id, first_name, last_name, department_id, salary, hire_date
FROM
    (SELECT
        *,
        DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS salary_tier,
        ROW_NUMBER() OVER (PARTITION BY department_id, salary ORDER BY employee_id) AS tie_breaker
    FROM
        employees) AS e1
WHERE salary_tier <= 2 AND tie_breaker = 1
ORDER BY employee_id;

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

SELECT 
    e.*,
    min(salary) over(PARTITION BY department_id) as min_salary
FROM
    employees as e;

-- ============================================================
-- PART B: monthly_revenue table (offset + running aggregates)
-- ============================================================

-- Q8: For each region, show each month's revenue next to the
-- PREVIOUS month's revenue in the same row.

SELECT *,
       LAG(revenue,1,'N/A') OVER(PARTITION BY region) as Previous_revenue
FROM
    monthly_revenue
ORDER BY revenue_id;


-- Q9: For each region, calculate the dollar CHANGE in revenue from
-- the previous month (this month's revenue minus last month's).

SELECT
    *,
    (revenue - LAG(revenue) OVER(PARTITION BY region ORDER BY revenue_month)) as revenue_change
FROM
    monthly_revenue

-- Q10: For each region, show a running total of revenue from
-- January through the current month.

select m.*,
    sum(revenue) over(PARTITION BY region ORDER BY revenue_month) as running_total_revenue
from
    monthly_revenue as m;

-- alternate way

select m.*,
    sum(revenue) over w as running_total_revenue
from
    monthly_revenue as m

window w as (PARTITION BY region ORDER BY revenue_month);

-- Q11: For each region, calculate a 3-month moving average of
-- revenue (current month + the 2 before it).

SELECT
    m.*,
    avg(revenue) over(PARTITION BY region ORDER BY revenue_month
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg
FROM
    monthly_revenue as m;


--alternate

SELECT
    m.*,
    CASE
        WHEN COUNT(*) OVER (PARTITION BY region ORDER BY revenue_month
                            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) < 3
        THEN 'N/A'
        ELSE CAST(AVG(revenue) OVER (PARTITION BY region ORDER BY revenue_month
                                      ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS CHAR)
    END AS moving_avg
FROM monthly_revenue AS m;

-- Q12: For each region, show what fraction (as a %) each month's
-- revenue is of that region's total 6-month revenue.

SELECT 
    m.*,
    round(revenue / sum(revenue) OVER(PARTITION BY region) * 100, 1) as pct_of_region_total
FROM
    monthly_revenue as m


--Alternate version

SELECT 
    m.*,
    round(revenue / sum(revenue) OVER w * 100, 1) as pct_of_region_total
FROM
    monthly_revenue as m
window w as (partition by region order by revenue_month rows BETWEEN unbounded PRECEDING and unbounded following)



-- ============================================================
-- PART C: orders table (bringing it together)
-- ============================================================

-- Q13: Return each customer's 2 highest-value orders. Handle ties
-- the same way Q5 did.

SELECT order_id, customer_id, order_date, amount
FROM
    (SELECT
        *,
        DENSE_RANK() OVER(PARTITION BY customer_id ORDER BY amount desc) as amount_rank,
        row_number() OVER(PARTITION BY customer_id, amount ORDER BY order_id) as tie_breaker
    FROM
        orders) as t1
WHERE 
    (amount_rank <= 2 AND tie_breaker = 1)
ORDER BY customer_id, amount DESC;


-- Q14: For each customer, show a running total of how much they've
-- spent so far, ordered by order date.

SELECT
    o.*,
    sum(amount) OVER(PARTITION BY customer_id ORDER BY order_date) as total_sum
FROM
    orders as o;

-- Q15: For each customer, show how many orders they've placed in
-- total (same number repeated on every row for that customer --
-- don't use GROUP BY).

SELECT
    o.*,
    count(order_id) OVER(PARTITION BY customer_id) as total_order_placed
FROM
    orders as o;


-- ============================================================
-- PART D: capstone (mixing tables / patterns)
-- ============================================================

-- Q16: For each employee, show how many years after the FIRST hire
-- in their department they were hired (i.e. compare their hire_date
-- to the earliest hire_date in their own department).

--my solution 

SELECT
    employee_id, 
    concat(first_name,' ', last_name) as full_name,
    department_id, 
    salary, 
    hire_date, (YEAR(hire_date) - first_employee_year) as joining_after
FROM
    (SELECT
        *,
        FIRST_VALUE(year(hire_date)) OVER(PARTITION BY department_id ORDER BY hire_date) as first_employee_year
    FROM
        employees
    ORDER BY department_id, hire_date) as t1
order by department_id;

-- alternate better approach

SELECT
    employee_id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    department_id,
    salary,
    hire_date,
    TIMESTAMPDIFF(YEAR, first_hire_date, hire_date) AS joining_after
FROM
    (SELECT
        *,
        FIRST_VALUE(hire_date) OVER (PARTITION BY department_id ORDER BY hire_date) AS first_hire_date
    FROM employees) AS t1
ORDER BY department_id;

--most optimal alternate solution

SELECT
    employee_id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    department_id,
    salary,
    hire_date,
    TIMESTAMPDIFF(YEAR, MIN(hire_date) OVER (PARTITION BY department_id), hire_date) AS joining_after
FROM employees
ORDER BY department_id;


-- Q17: Find every employee who is the single highest-paid person
-- in their department -- output just one row per department, no
-- ties allowed in the output.

SELECT
    employee_id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    department_id,
    salary,
    hire_date
FROM
    (SELECT
        e.*,
        DENSE_RANK() OVER(PARTITION BY department_id order by salary desc) as salary_rank,
        row_number() OVER(PARTITION BY department_id, salary order by employee_id) as tie_breaker
    FROM
        employees as e) as t1
WHERE   
    salary_rank = 1
    AND
    tie_breaker = 1;