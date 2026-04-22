QUESTIONS = [
    # ======================= BEGINNER =======================
    {
        "id": 1,
        "level": 1,
        "topic": "SELECT Basics",
        "title": "Select All Columns",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Marketing', 60000),
    (3, 'Charlie', 'Engineering', 95000);""",
        "question": "Write a query to select *all columns* for every employee.",
        "correct_answer": "SELECT * FROM employees",
        "explanation": "The asterisk (*) is a wildcard that selects every column from the specified table.",
        "hint": "Use the asterisk (*) after SELECT.",
    },
    {
        "id": 2,
        "level": 1,
        "topic": "SELECT Basics",
        "title": "Select Specific Columns",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Marketing', 60000),
    (3, 'Charlie', 'Engineering', 95000);""",
        "question": "Write a query to get only the *name* and *salary* of all employees.",
        "correct_answer": "SELECT name, salary FROM employees",
        "explanation": "List the column names separated by commas after SELECT to retrieve only those columns.",
        "hint": "Write column names separated by commas.",
    },
    {
        "id": 3,
        "level": 1,
        "topic": "Filtering with WHERE",
        "title": "Filter by Department",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Marketing', 60000),
    (3, 'Charlie', 'Engineering', 95000);""",
        "question": "Select the *name* and *salary* of employees who work in the 'Engineering' department.",
        "correct_answer": "SELECT name, salary FROM employees WHERE department = 'Engineering'",
        "explanation": "The WHERE clause filters rows based on a condition. Only rows where the condition is true are returned.",
        "hint": "Add a WHERE clause comparing department to 'Engineering'.",
    },
    {
        "id": 4,
        "level": 1,
        "topic": "Filtering with WHERE",
        "title": "Filter by Salary Range",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Marketing', 60000),
    (3, 'Charlie', 'Engineering', 95000);""",
        "question": "Select all columns for employees with a salary *greater than* 70000.",
        "correct_answer": "SELECT * FROM employees WHERE salary > 70000",
        "explanation": "Comparison operators like >, <, >=, <= can be used in WHERE to filter numeric data.",
        "hint": "Use the > operator in the WHERE clause.",
    },
    {
        "id": 5,
        "level": 1,
        "topic": "Sorting with ORDER BY",
        "title": "Sort by Salary",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Marketing', 60000),
    (3, 'Charlie', 'Engineering', 95000);""",
        "question": "Select all employees ordered by *salary in descending order*.",
        "correct_answer": "SELECT * FROM employees ORDER BY salary DESC",
        "explanation": "ORDER BY sorts results. DESC means descending (highest first). ASC is the default.",
        "hint": "Use ORDER BY with the DESC keyword.",
    },
    {
        "id": 6,
        "level": 1,
        "topic": "Limiting Results",
        "title": "Top 2 Earners",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Marketing', 60000),
    (3, 'Charlie', 'Engineering', 95000);""",
        "question": "Get the *top 2 highest paid* employees (name and salary only).",
        "correct_answer": "SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 2",
        "explanation": "LIMIT restricts the number of rows returned. Combine it with ORDER BY DESC to get the top N.",
        "hint": "Use ORDER BY ... DESC followed by LIMIT 2.",
    },
    {
        "id": 7,
        "level": 1,
        "topic": "DISTINCT Values",
        "title": "Unique Departments",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Marketing', 60000),
    (3, 'Charlie', 'Engineering', 95000);""",
        "question": "Write a query that returns the *unique* department names from the employees table.",
        "correct_answer": "SELECT DISTINCT department FROM employees",
        "explanation": "DISTINCT removes duplicate values so only unique department names are returned.",
        "hint": "Use the DISTINCT keyword after SELECT.",
    },
    {
        "id": 8,
        "level": 1,
        "topic": "AND / OR Conditions",
        "title": "Engineering AND High Salary",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Marketing', 60000),
    (3, 'Charlie', 'Engineering', 95000);""",
        "question": "Select the names of employees in 'Engineering' with a salary *greater than* 85000.",
        "correct_answer": "SELECT name FROM employees WHERE department = 'Engineering' AND salary > 85000",
        "explanation": "AND requires both conditions to be true. OR would return rows where either condition is true.",
        "hint": "Combine two conditions with the AND operator.",
    },
    {
        "id": 9,
        "level": 1,
        "topic": "Pattern Matching with LIKE",
        "title": "Names Starting with A",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Marketing', 60000),
    (3, 'Anna', 'HR', 55000);""",
        "question": "Select all columns for employees whose *name starts with 'A'*.",
        "correct_answer": "SELECT * FROM employees WHERE name LIKE 'A%'",
        "explanation": "The % wildcard matches any sequence of characters. 'A%' matches any string starting with A.",
        "hint": "Use LIKE with the pattern 'A%'.",
    },
    {
        "id": 10,
        "level": 1,
        "topic": "IN and BETWEEN",
        "title": "Specific Departments",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Marketing', 60000),
    (3, 'Charlie', 'HR', 55000);""",
        "question": "Select names of employees in the 'Engineering' or 'Marketing' departments using the IN operator.",
        "correct_answer": "SELECT name FROM employees WHERE department IN ('Engineering', 'Marketing')",
        "explanation": "IN checks whether a value matches any value in a list, making multiple OR conditions cleaner.",
        "hint": "Use WHERE department IN (...).",
    },
    {
        "id": 11,
        "level": 1,
        "topic": "NULL Handling",
        "title": "Find Missing Emails",
        "schema": """CREATE TABLE customers (
    id INTEGER,
    name TEXT,
    email TEXT
);

INSERT INTO customers (id, name, email)
VALUES
    (1, 'Alice', 'alice@example.com'),
    (2, 'Bob', NULL),
    (3, 'Charlie', 'charlie@example.com');""",
        "question": "Select all columns for customers whose *email is NULL*.",
        "correct_answer": "SELECT * FROM customers WHERE email IS NULL",
        "explanation": "NULL is not a value, so you must use IS NULL or IS NOT NULL. Using = NULL will not work.",
        "hint": "Use IS NULL, not = NULL.",
    },
    {
        "id": 12,
        "level": 1,
        "topic": "Aggregate Functions",
        "title": "Average Salary",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Marketing', 60000),
    (3, 'Charlie', 'Engineering', 95000);""",
        "question": "Calculate the *average salary* across all employees.",
        "correct_answer": "SELECT AVG(salary) FROM employees",
        "explanation": "Aggregate functions like AVG, SUM, COUNT, MIN, MAX compute a single result from a set of rows.",
        "hint": "Use the AVG() function.",
    },
    {
        "id": 13,
        "level": 1,
        "topic": "Aggregate Functions",
        "title": "Total Employees",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Marketing', 60000),
    (3, 'Charlie', 'Engineering', 95000);""",
        "question": "Count the *total number of employees*.",
        "correct_answer": "SELECT COUNT(*) FROM employees",
        "explanation": "COUNT(*) counts all rows in the table. COUNT(column) counts non-NULL values in that column.",
        "hint": "Use COUNT(*).",
    },
    {
        "id": 14,
        "level": 1,
        "topic": "GROUP BY",
        "title": "Count per Department",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Marketing', 60000),
    (3, 'Charlie', 'Engineering', 95000);""",
        "question": "Show the *department* and the *number of employees* in each department.",
        "correct_answer": "SELECT department, COUNT(*) FROM employees GROUP BY department",
        "explanation": "GROUP BY groups rows that have the same values into summary rows, allowing aggregate functions per group.",
        "hint": "Use GROUP BY department with COUNT(*).",
    },
    {
        "id": 15,
        "level": 1,
        "topic": "Aliases",
        "title": "Rename Output Columns",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES
    (1, 'Alice', 90000),
    (2, 'Bob', 60000);""",
        "question": "Select name and salary, but rename the salary column in the output to *annual_income*.",
        "correct_answer": "SELECT name, salary AS annual_income FROM employees",
        "explanation": "The AS keyword lets you assign a temporary alias to a column or table for readability.",
        "hint": "Use the AS keyword after the column name.",
    },

    # ======================= INTERMEDIATE =======================
    {
        "id": 16,
        "level": 2,
        "topic": "INNER JOIN",
        "title": "Employee Departments",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department_id INTEGER
);

CREATE TABLE departments (
    id INTEGER,
    name TEXT
);

INSERT INTO employees (id, name, department_id)
VALUES
    (1, 'Alice', 1),
    (2, 'Bob', 2),
    (3, 'Charlie', 1);

INSERT INTO departments (id, name)
VALUES
    (1, 'Engineering'),
    (2, 'Marketing');""",
        "question": "Select employee *name* and their department *name* using an INNER JOIN.",
        "correct_answer": "SELECT employees.name, departments.name FROM employees INNER JOIN departments ON employees.department_id = departments.id",
        "explanation": "INNER JOIN returns only rows where there is a match in both tables based on the join condition.",
        "hint": "JOIN employees and departments on department_id = id.",
    },
    {
        "id": 17,
        "level": 2,
        "topic": "LEFT JOIN",
        "title": "All Employees with Departments",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department_id INTEGER
);

CREATE TABLE departments (
    id INTEGER,
    name TEXT
);

INSERT INTO employees (id, name, department_id)
VALUES
    (1, 'Alice', 1),
    (2, 'Bob', 2),
    (3, 'Charlie', NULL);

INSERT INTO departments (id, name)
VALUES
    (1, 'Engineering'),
    (2, 'Marketing');""",
        "question": "List *all* employees and their department names. If an employee has no department, show NULL.",
        "correct_answer": "SELECT employees.name, departments.name FROM employees LEFT JOIN departments ON employees.department_id = departments.id",
        "explanation": "LEFT JOIN returns all rows from the left table, and matched rows from the right table. Unmatched right rows produce NULL.",
        "hint": "Use a LEFT JOIN from employees to departments.",
    },
    {
        "id": 18,
        "level": 2,
        "topic": "RIGHT JOIN",
        "title": "All Departments with Employees",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department_id INTEGER
);

CREATE TABLE departments (
    id INTEGER,
    name TEXT
);

INSERT INTO employees (id, name, department_id)
VALUES
    (1, 'Alice', 1),
    (2, 'Bob', 1);

INSERT INTO departments (id, name)
VALUES
    (1, 'Engineering'),
    (2, 'HR');""",
        "question": "List department names and employee names for *all departments*, even if they have no employees.",
        "correct_answer": "SELECT departments.name, employees.name FROM employees RIGHT JOIN departments ON employees.department_id = departments.id",
        "explanation": "RIGHT JOIN returns all rows from the right table and matched rows from the left. Note: SQLite does not support RIGHT JOIN natively, but this question tests conceptual knowledge.",
        "hint": "Use RIGHT JOIN with departments on the right side.",
    },
    {
        "id": 19,
        "level": 2,
        "topic": "SELF JOIN",
        "title": "Employee Managers",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    manager_id INTEGER
);

INSERT INTO employees (id, name, manager_id)
VALUES
    (1, 'Alice', 3),
    (2, 'Bob', 3),
    (3, 'Charlie', NULL);""",
        "question": "Select each employee's name alongside their manager's name using a self join.",
        "correct_answer": "SELECT e.name AS employee, m.name AS manager FROM employees e JOIN employees m ON e.manager_id = m.id",
        "explanation": "A self join joins a table to itself using aliases to distinguish the two instances.",
        "hint": "Join employees to itself with aliases e and m on e.manager_id = m.id.",
    },
    {
        "id": 20,
        "level": 2,
        "topic": "Subqueries in WHERE",
        "title": "Above Average Salary",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES
    (1, 'Alice', 90000),
    (2, 'Bob', 60000),
    (3, 'Charlie', 95000);""",
        "question": "Select names of employees whose salary is *above the company average*.",
        "correct_answer": "SELECT name FROM employees WHERE salary > (SELECT AVG(salary) FROM employees)",
        "explanation": "A subquery in the WHERE clause lets you filter rows based on an aggregate result dynamically.",
        "hint": "Use a subquery that computes AVG(salary).",
    },
    {
        "id": 21,
        "level": 2,
        "topic": "Subqueries in FROM",
        "title": "Department Averages",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Engineering', 80000),
    (3, 'Charlie', 'Marketing', 60000);""",
        "question": "From a subquery that returns department and average salary, select departments where the average salary > 75000.",
        "correct_answer": "SELECT department, avg_salary FROM (SELECT department, AVG(salary) AS avg_salary FROM employees GROUP BY department) WHERE avg_salary > 75000",
        "explanation": "Subqueries in the FROM clause let you treat a query result as a temporary table for further filtering.",
        "hint": "Use a subquery in FROM with AVG(salary) grouped by department.",
    },
    {
        "id": 22,
        "level": 2,
        "topic": "Subqueries in SELECT",
        "title": "Salary vs Average",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES
    (1, 'Alice', 90000),
    (2, 'Bob', 60000),
    (3, 'Charlie', 95000);""",
        "question": "Select each employee's name, salary, and the *company average salary* as a column next to it.",
        "correct_answer": "SELECT name, salary, (SELECT AVG(salary) FROM employees) AS company_average FROM employees",
        "explanation": "A scalar subquery in SELECT returns a single value repeated for every row in the outer query.",
        "hint": "Put a subquery returning AVG(salary) directly in the SELECT list.",
    },
    {
        "id": 23,
        "level": 2,
        "topic": "UNION",
        "title": "Combine Results",
        "schema": """CREATE TABLE table_a (val TEXT);
CREATE TABLE table_b (val TEXT);

INSERT INTO table_a (val) VALUES ('Alice'), ('Bob');
INSERT INTO table_b (val) VALUES ('Bob'), ('Charlie');""",
        "question": "Write a query that returns all unique names from both table_a and table_b combined.",
        "correct_answer": "SELECT val FROM table_a UNION SELECT val FROM table_b",
        "explanation": "UNION combines result sets and removes duplicates. UNION ALL keeps duplicates.",
        "hint": "Use UNION between two SELECT statements.",
    },
    {
        "id": 24,
        "level": 2,
        "topic": "INSERT",
        "title": "Add New Employee",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000);""",
        "question": "Insert a new employee: id=2, name='Bob', department='Marketing', salary=60000.",
        "correct_answer": "INSERT INTO employees (id, name, department, salary) VALUES (2, 'Bob', 'Marketing', 60000)",
        "explanation": "INSERT INTO adds new rows. Specify the columns and values explicitly for clarity and safety.",
        "hint": "Use INSERT INTO ... VALUES ... syntax with the given values.",
    },
    {
        "id": 25,
        "level": 2,
        "topic": "UPDATE",
        "title": "Give a Raise",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES
    (1, 'Alice', 90000),
    (2, 'Bob', 60000);""",
        "question": "Give Alice a 10% raise. Update her salary by multiplying it by 1.10.",
        "correct_answer": "UPDATE employees SET salary = salary * 1.10 WHERE name = 'Alice'",
        "explanation": "UPDATE modifies existing rows. Always use a WHERE clause to avoid updating every row accidentally.",
        "hint": "Use UPDATE with SET salary = salary * 1.10 and a WHERE clause.",
    },
    {
        "id": 26,
        "level": 2,
        "topic": "DELETE",
        "title": "Remove Employee",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES
    (1, 'Alice', 90000),
    (2, 'Bob', 60000);""",
        "question": "Delete the employee named 'Bob' from the table.",
        "correct_answer": "DELETE FROM employees WHERE name = 'Bob'",
        "explanation": "DELETE removes rows. Without WHERE, all rows are deleted. Use WHERE to target specific rows.",
        "hint": "Use DELETE FROM with a WHERE clause for Bob.",
    },
    {
        "id": 27,
        "level": 2,
        "topic": "CASE Expressions",
        "title": "Salary Category",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES
    (1, 'Alice', 90000),
    (2, 'Bob', 60000),
    (3, 'Charlie', 45000);""",
        "question": "Select name and a new column 'category' that is 'High' if salary >= 80000, else 'Low'.",
        "correct_answer": "SELECT name, CASE WHEN salary >= 80000 THEN 'High' ELSE 'Low' END AS category FROM employees",
        "explanation": "CASE lets you add conditional logic inside a query, similar to IF/ELSE in programming languages.",
        "hint": "Use CASE WHEN ... THEN ... ELSE ... END.",
    },
    {
        "id": 28,
        "level": 2,
        "topic": "String Functions",
        "title": "Uppercase Names",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT
);

INSERT INTO employees (id, name)
VALUES
    (1, 'Alice'),
    (2, 'Bob');""",
        "question": "Return employee names converted to *uppercase*.",
        "correct_answer": "SELECT UPPER(name) FROM employees",
        "explanation": "String functions like UPPER, LOWER, LENGTH operate on text values within SQL queries.",
        "hint": "Use the UPPER() function.",
    },
    {
        "id": 29,
        "level": 2,
        "topic": "COALESCE",
        "title": "Replace NULL",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    phone TEXT
);

INSERT INTO employees (id, name, phone)
VALUES
    (1, 'Alice', '555-1234'),
    (2, 'Bob', NULL);""",
        "question": "Select id and phone, but show 'N/A' when the phone is NULL.",
        "correct_answer": "SELECT id, COALESCE(phone, 'N/A') FROM employees",
        "explanation": "COALESCE returns the first non-NULL value from its arguments, useful for providing defaults.",
        "hint": "Use COALESCE(phone, 'N/A').",
    },
    {
        "id": 30,
        "level": 2,
        "topic": "Multiple JOINs",
        "title": "Employee Project Details",
        "schema": """CREATE TABLE employees (id INTEGER, name TEXT);
CREATE TABLE projects (id INTEGER, title TEXT);
CREATE TABLE employee_projects (employee_id INTEGER, project_id INTEGER);

INSERT INTO employees (id, name) VALUES (1, 'Alice'), (2, 'Bob');
INSERT INTO projects (id, title) VALUES (1, 'Alpha'), (2, 'Beta');
INSERT INTO employee_projects (employee_id, project_id) VALUES (1, 1), (1, 2), (2, 1);""",
        "question": "List employee names alongside the project titles they are assigned to.",
        "correct_answer": "SELECT employees.name, projects.title FROM employees JOIN employee_projects ON employees.id = employee_projects.employee_id JOIN projects ON employee_projects.project_id = projects.id",
        "explanation": "You can chain multiple JOINs to connect data across several related tables.",
        "hint": "Join employees -> employee_projects -> projects.",
    },

    # ======================= ADVANCED =======================
    {
        "id": 31,
        "level": 3,
        "topic": "Window Functions - ROW_NUMBER",
        "title": "Rank Employees by Salary",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES
    (1, 'Alice', 90000),
    (2, 'Bob', 60000),
    (3, 'Charlie', 95000);""",
        "question": "Assign a unique rank to each employee ordered by salary descending using ROW_NUMBER().",
        "correct_answer": "SELECT name, salary, ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank FROM employees",
        "explanation": "ROW_NUMBER() assigns a unique sequential integer to rows within a partition based on the ORDER BY in the OVER clause.",
        "hint": "Use ROW_NUMBER() OVER (ORDER BY salary DESC).",
    },
    {
        "id": 32,
        "level": 3,
        "topic": "Window Functions - RANK",
        "title": "Rank with Ties",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES
    (1, 'Alice', 90000),
    (2, 'Bob', 90000),
    (3, 'Charlie', 95000);""",
        "question": "Rank employees by salary descending. Employees with the same salary should share the same rank.",
        "correct_answer": "SELECT name, salary, RANK() OVER (ORDER BY salary DESC) AS rank FROM employees",
        "explanation": "RANK() gives the same rank to ties and leaves a gap in the ranking sequence. DENSE_RANK() does not leave gaps.",
        "hint": "Use RANK() instead of ROW_NUMBER().",
    },
    {
        "id": 33,
        "level": 3,
        "topic": "Window Functions - LEAD/LAG",
        "title": "Compare to Previous",
        "schema": """CREATE TABLE sales (
    month TEXT,
    revenue INTEGER
);

INSERT INTO sales (month, revenue)
VALUES
    ('Jan', 10000),
    ('Feb', 12000),
    ('Mar', 11000);""",
        "question": "Show month, revenue, and the *previous month's revenue* using LAG().",
        "correct_answer": "SELECT month, revenue, LAG(revenue) OVER (ORDER BY month) AS prev_revenue FROM sales",
        "explanation": "LAG() accesses data from a previous row in the same result set without a self join. LEAD() looks ahead.",
        "hint": "Use LAG(revenue) OVER (ORDER BY month).",
    },
    {
        "id": 34,
        "level": 3,
        "topic": "Common Table Expressions (CTE)",
        "title": "High Earners CTE",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES
    (1, 'Alice', 90000),
    (2, 'Bob', 60000),
    (3, 'Charlie', 95000);""",
        "question": "Use a WITH clause (CTE) to define high earners as those with salary > 80000, then select their names.",
        "correct_answer": "WITH high_earners AS (SELECT name, salary FROM employees WHERE salary > 80000) SELECT name FROM high_earners",
        "explanation": "CTEs with WITH let you define temporary result sets that can be referenced within the main query, improving readability.",
        "hint": "Define a CTE named high_earners, then SELECT from it.",
    },
    {
        "id": 35,
        "level": 3,
        "topic": "Recursive CTE",
        "title": "Generate Number Series",
        "schema": """-- No tables needed""",
        "question": "Use a recursive CTE to generate numbers 1 through 5.",
        "correct_answer": "WITH RECURSIVE numbers(n) AS (SELECT 1 UNION ALL SELECT n + 1 FROM numbers WHERE n < 5) SELECT n FROM numbers",
        "explanation": "Recursive CTEs reference themselves to iterate. They are great for hierarchical data and generating sequences.",
        "hint": "Use WITH RECURSIVE and UNION ALL with a termination condition WHERE n < 5.",
    },
    {
        "id": 36,
        "level": 3,
        "topic": "Correlated Subquery",
        "title": "Highest Salary per Department",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Engineering', 80000),
    (3, 'Charlie', 'Marketing', 70000);""",
        "question": "Select employees who have the *highest salary in their department* using a correlated subquery.",
        "correct_answer": "SELECT name, department, salary FROM employees e WHERE salary = (SELECT MAX(salary) FROM employees WHERE department = e.department)",
        "explanation": "A correlated subquery runs once for each row in the outer query, referencing columns from the outer table.",
        "hint": "Use a subquery in WHERE that references e.department and finds MAX(salary).",
    },
    {
        "id": 37,
        "level": 3,
        "topic": "EXISTS",
        "title": "Employees with Projects",
        "schema": """CREATE TABLE employees (id INTEGER, name TEXT);
CREATE TABLE projects (id INTEGER, title TEXT, employee_id INTEGER);

INSERT INTO employees (id, name) VALUES (1, 'Alice'), (2, 'Bob');
INSERT INTO projects (id, title, employee_id) VALUES (1, 'Alpha', 1);""",
        "question": "Select names of employees who have *at least one project* using EXISTS.",
        "correct_answer": "SELECT name FROM employees e WHERE EXISTS (SELECT 1 FROM projects p WHERE p.employee_id = e.id)",
        "explanation": "EXISTS checks whether a subquery returns any rows. It stops at the first match, making it efficient.",
        "hint": "Use EXISTS with a correlated subquery matching employee_id.",
    },
    {
        "id": 38,
        "level": 3,
        "topic": "Window Functions - RANK with PARTITION",
        "title": "Top Product per Region",
        "schema": """CREATE TABLE sales (
    region TEXT,
    product TEXT,
    amount INTEGER
);

INSERT INTO sales (region, product, amount)
VALUES
    ('North', 'A', 100),
    ('North', 'B', 200),
    ('South', 'A', 150),
    ('South', 'B', 300);""",
        "question": "Select region, product, and amount for the top-selling product in each region using a window function.",
        "correct_answer": "SELECT region, product, amount FROM (SELECT region, product, amount, RANK() OVER (PARTITION BY region ORDER BY amount DESC) AS rnk FROM sales) WHERE rnk = 1",
        "explanation": "RANK() with PARTITION BY ranks rows within each group separately. Filtering for rnk = 1 gives the top item per region.",
        "hint": "Use RANK() OVER (PARTITION BY region ORDER BY amount DESC) in a subquery.",
    },
    {
        "id": 39,
        "level": 3,
        "topic": "Window Functions - NTILE",
        "title": "Salary Quartiles",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES
    (1, 'Alice', 40000),
    (2, 'Bob', 50000),
    (3, 'Charlie', 60000),
    (4, 'Diana', 70000),
    (5, 'Eve', 80000),
    (6, 'Frank', 90000),
    (7, 'Grace', 100000),
    (8, 'Henry', 110000);""",
        "question": "Divide employees into 4 salary quartiles and show name, salary, and their quartile number.",
        "correct_answer": "SELECT name, salary, NTILE(4) OVER (ORDER BY salary) AS quartile FROM employees",
        "explanation": "NTILE(n) distributes rows into n roughly equal buckets based on the specified ordering.",
        "hint": "Use NTILE(4) OVER (ORDER BY salary).",
    },
    {
        "id": 40,
        "level": 3,
        "topic": "Window Frames",
        "title": "Running Total",
        "schema": """CREATE TABLE sales (
    month TEXT,
    revenue INTEGER
);

INSERT INTO sales (month, revenue)
VALUES
    ('Jan', 10000),
    ('Feb', 12000),
    ('Mar', 11000);""",
        "question": "Calculate a running total of revenue using SUM() as a window function.",
        "correct_answer": "SELECT month, revenue, SUM(revenue) OVER (ORDER BY month ROWS UNBOUNDED PRECEDING) AS running_total FROM sales",
        "explanation": "Window frames like ROWS UNBOUNDED PRECEDING define a sliding window of rows for the aggregate to operate on.",
        "hint": "Use SUM(revenue) OVER with ROWS UNBOUNDED PRECEDING.",
    },
    {
        "id": 41,
        "level": 3,
        "topic": "PIVOT (Conceptual)",
        "title": "Revenue by Month",
        "schema": """CREATE TABLE sales (
    month TEXT,
    revenue INTEGER
);

INSERT INTO sales (month, revenue)
VALUES
    ('Jan', 10000),
    ('Feb', 12000),
    ('Mar', 11000);""",
        "question": "Pivot the data so months become columns. Select Jan, Feb, Mar as columns with revenue. (Use CASE)",
        "correct_answer": "SELECT SUM(CASE WHEN month = 'Jan' THEN revenue END) AS Jan, SUM(CASE WHEN month = 'Feb' THEN revenue END) AS Feb, SUM(CASE WHEN month = 'Mar' THEN revenue END) AS Mar FROM sales",
        "explanation": "When PIVOT is unavailable, conditional aggregation with CASE inside SUM can pivot rows into columns.",
        "hint": "Use SUM(CASE WHEN month = 'X' THEN revenue END) for each month.",
    },
    {
        "id": 42,
        "level": 3,
        "topic": "Advanced Filtering",
        "title": "Second Highest Salary",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES
    (1, 'Alice', 90000),
    (2, 'Bob', 80000),
    (3, 'Charlie', 95000);""",
        "question": "Find the *second highest salary* in the company using a subquery.",
        "correct_answer": "SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees)",
        "explanation": "To find the Nth highest, you can nest aggregates or use window functions. Here MAX with a subquery finds second place.",
        "hint": "Select MAX(salary) where salary is less than the overall MAX.",
    },
    {
        "id": 43,
        "level": 3,
        "topic": "Advanced JOINs",
        "title": "Anti Join",
        "schema": """CREATE TABLE employees (id INTEGER, name TEXT);
CREATE TABLE projects (id INTEGER, title TEXT, employee_id INTEGER);

INSERT INTO employees (id, name) VALUES (1, 'Alice'), (2, 'Bob');
INSERT INTO projects (id, title, employee_id) VALUES (1, 'Alpha', 1);""",
        "question": "Select employees who are *not* assigned to any project (anti join).",
        "correct_answer": "SELECT name FROM employees e WHERE NOT EXISTS (SELECT 1 FROM projects p WHERE p.employee_id = e.id)",
        "explanation": "An anti join returns rows from one table that have no match in another. NOT EXISTS is a clean way to express this.",
        "hint": "Use NOT EXISTS with a subquery on projects.",
    },
    {
        "id": 44,
        "level": 3,
        "topic": "Window Functions - PARTITION BY",
        "title": "Rank Within Department",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Engineering', 80000),
    (3, 'Charlie', 'Marketing', 70000);""",
        "question": "Rank employees by salary *within each department* using PARTITION BY.",
        "correct_answer": "SELECT name, department, salary, RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank FROM employees",
        "explanation": "PARTITION BY divides the result set into partitions. The window function is applied independently within each partition.",
        "hint": "Use RANK() OVER (PARTITION BY department ORDER BY salary DESC).",
    },
    {
        "id": 45,
        "level": 3,
        "topic": "Complex CTE",
        "title": "Hierarchical Data",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    manager_id INTEGER
);

INSERT INTO employees (id, name, manager_id)
VALUES
    (1, 'CEO', NULL),
    (2, 'VP', 1),
    (3, 'Manager', 2);""",
        "question": "Use a recursive CTE to list each employee with their *management level* (depth from CEO).",
        "correct_answer": "WITH RECURSIVE hierarchy AS (SELECT id, name, manager_id, 1 AS level FROM employees WHERE manager_id IS NULL UNION ALL SELECT e.id, e.name, e.manager_id, h.level + 1 FROM employees e JOIN hierarchy h ON e.manager_id = h.id) SELECT name, level FROM hierarchy",
        "explanation": "Recursive CTEs are perfect for tree/hierarchy traversal. The anchor finds the root, and the recursive member walks down the tree.",
        "hint": "Anchor selects the CEO (manager_id IS NULL), then recursively JOIN employees on manager_id.",
    },
    {
        "id": 46,
        "level": 1,
        "topic": "Aggregate Functions",
        "title": "Count Names",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT
);

INSERT INTO employees (id, name)
VALUES
    (1, 'Alice'),
    (2, 'Bob'),
    (3, 'Alice');""",
        "question": "Count how many rows have a non-NULL name.",
        "correct_answer": "SELECT COUNT(name) FROM employees",
        "explanation": "COUNT(column) counts non-NULL values in that specific column.",
        "hint": "Use COUNT(name) instead of COUNT(*).",
    },
    {
        "id": 47,
        "level": 1,
        "topic": "Filtering with WHERE",
        "title": "OR Condition",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT
);

INSERT INTO employees (id, name, department)
VALUES
    (1, 'Alice', 'Engineering'),
    (2, 'Bob', 'Marketing'),
    (3, 'Charlie', 'Sales');""",
        "question": "Select names of employees in 'Engineering' OR 'Sales'.",
        "correct_answer": "SELECT name FROM employees WHERE department = 'Engineering' OR department = 'Sales'",
        "explanation": "OR returns rows where at least one condition is true.",
        "hint": "Use OR between two department conditions.",
    },
    {
        "id": 48,
        "level": 1,
        "topic": "Sorting with ORDER BY",
        "title": "Sort by Multiple Columns",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, department, salary)
VALUES
    (1, 'Engineering', 90000),
    (2, 'Marketing', 60000),
    (3, 'Engineering', 80000);""",
        "question": "Order employees by department ascending, then by salary descending.",
        "correct_answer": "SELECT * FROM employees ORDER BY department ASC, salary DESC",
        "explanation": "You can specify multiple columns in ORDER BY. The second column breaks ties in the first.",
        "hint": "Use ORDER BY department ASC, salary DESC.",
    },
    {
        "id": 49,
        "level": 1,
        "topic": "Limiting Results",
        "title": "Pagination",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT
);

INSERT INTO employees (id, name)
VALUES
    (1, 'Alice'),
    (2, 'Bob'),
    (3, 'Charlie'),
    (4, 'Diana');""",
        "question": "Skip the first 2 employees and return the next 2 (name only).",
        "correct_answer": "SELECT name FROM employees LIMIT 2 OFFSET 2",
        "explanation": "OFFSET skips the specified number of rows before starting to return rows.",
        "hint": "Use LIMIT 2 OFFSET 2.",
    },
    {
        "id": 50,
        "level": 1,
        "topic": "DISTINCT Values",
        "title": "Count Unique Names",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT
);

INSERT INTO employees (id, name)
VALUES
    (1, 'Alice'),
    (2, 'Bob'),
    (3, 'Alice');""",
        "question": "Count the number of unique names in the table.",
        "correct_answer": "SELECT COUNT(DISTINCT name) FROM employees",
        "explanation": "COUNT(DISTINCT column) counts unique non-NULL values in that column.",
        "hint": "Use COUNT(DISTINCT name).",
    },
    {
        "id": 51,
        "level": 1,
        "topic": "Pattern Matching with LIKE",
        "title": "Names Ending with 'e'",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT
);

INSERT INTO employees (id, name)
VALUES
    (1, 'Alice'),
    (2, 'Bob'),
    (3, 'Charlie');""",
        "question": "Select all columns for employees whose name ends with 'e'.",
        "correct_answer": "SELECT * FROM employees WHERE name LIKE '%e'",
        "explanation": "'%e' matches any string ending with the letter 'e'.",
        "hint": "Use LIKE '%e'.",
    },
    {
        "id": 52,
        "level": 1,
        "topic": "IN and BETWEEN",
        "title": "IN with IDs",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT
);

INSERT INTO employees (id, name)
VALUES
    (1, 'Alice'),
    (2, 'Bob'),
    (3, 'Charlie');""",
        "question": "Select names for employees with ids 1 or 3 using IN.",
        "correct_answer": "SELECT name FROM employees WHERE id IN (1, 3)",
        "explanation": "IN works with numbers too, not just strings.",
        "hint": "Use WHERE id IN (1, 3).",
    },
    {
        "id": 53,
        "level": 1,
        "topic": "IN and BETWEEN",
        "title": "Salary Range",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES
    (1, 'Alice', 50000),
    (2, 'Bob', 60000),
    (3, 'Charlie', 75000);""",
        "question": "Select names with salary BETWEEN 55000 AND 70000.",
        "correct_answer": "SELECT name FROM employees WHERE salary BETWEEN 55000 AND 70000",
        "explanation": "BETWEEN is inclusive, meaning it includes both boundary values.",
        "hint": "Use WHERE salary BETWEEN 55000 AND 70000.",
    },
    {
        "id": 54,
        "level": 1,
        "topic": "NULL Handling",
        "title": "Find Non-NULL Phones",
        "schema": """CREATE TABLE customers (
    id INTEGER,
    name TEXT,
    phone TEXT
);

INSERT INTO customers (id, name, phone)
VALUES
    (1, 'Alice', '555-1234'),
    (2, 'Bob', NULL);""",
        "question": "Select all columns for customers whose phone is NOT NULL.",
        "correct_answer": "SELECT * FROM customers WHERE phone IS NOT NULL",
        "explanation": "IS NOT NULL filters out rows where the column has no value.",
        "hint": "Use IS NOT NULL.",
    },
    {
        "id": 55,
        "level": 1,
        "topic": "Aggregate Functions",
        "title": "Minimum Salary",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES
    (1, 'Alice', 90000),
    (2, 'Bob', 60000),
    (3, 'Charlie', 95000);""",
        "question": "Find the minimum salary among all employees.",
        "correct_answer": "SELECT MIN(salary) FROM employees",
        "explanation": "MIN() returns the smallest value in a set.",
        "hint": "Use the MIN() function.",
    },
    {
        "id": 56,
        "level": 1,
        "topic": "Aggregate Functions",
        "title": "Maximum Salary",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES
    (1, 'Alice', 90000),
    (2, 'Bob', 60000),
    (3, 'Charlie', 95000);""",
        "question": "Find the maximum salary among all employees.",
        "correct_answer": "SELECT MAX(salary) FROM employees",
        "explanation": "MAX() returns the largest value in a set.",
        "hint": "Use the MAX() function.",
    },
    {
        "id": 57,
        "level": 1,
        "topic": "GROUP BY",
        "title": "Group and Order",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, department, salary)
VALUES
    (1, 'Engineering', 90000),
    (2, 'Marketing', 60000),
    (3, 'Engineering', 80000);""",
        "question": "Show department and average salary, ordered by average salary descending.",
        "correct_answer": "SELECT department, AVG(salary) AS avg_salary FROM employees GROUP BY department ORDER BY avg_salary DESC",
        "explanation": "You can combine GROUP BY with ORDER BY to sort aggregated results.",
        "hint": "Use GROUP BY department and ORDER BY AVG(salary) DESC.",
    },
    {
        "id": 58,
        "level": 1,
        "topic": "HAVING",
        "title": "Filter Groups",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, department, salary)
VALUES
    (1, 'Engineering', 90000),
    (2, 'Marketing', 60000),
    (3, 'Engineering', 80000);""",
        "question": "Show departments having more than 1 employee.",
        "correct_answer": "SELECT department FROM employees GROUP BY department HAVING COUNT(*) > 1",
        "explanation": "HAVING filters groups after aggregation, unlike WHERE which filters rows before.",
        "hint": "Use HAVING COUNT(*) > 1 after GROUP BY.",
    },
    {
        "id": 59,
        "level": 1,
        "topic": "HAVING",
        "title": "High Average Departments",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, department, salary)
VALUES
    (1, 'Engineering', 90000),
    (2, 'Marketing', 60000),
    (3, 'Engineering', 80000);""",
        "question": "Show departments with an average salary greater than 75000.",
        "correct_answer": "SELECT department FROM employees GROUP BY department HAVING AVG(salary) > 75000",
        "explanation": "HAVING can use aggregate functions like AVG to filter grouped results.",
        "hint": "Use HAVING AVG(salary) > 75000.",
    },
    {
        "id": 60,
        "level": 1,
        "topic": "SELECT Basics",
        "title": "Simple Calculation",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES
    (1, 'Alice', 90000),
    (2, 'Bob', 60000);""",
        "question": "Select name and salary divided by 12 as monthly_salary.",
        "correct_answer": "SELECT name, salary / 12 AS monthly_salary FROM employees",
        "explanation": "You can perform arithmetic operations directly in the SELECT list.",
        "hint": "Use salary / 12 AS monthly_salary.",
    },
    {
        "id": 61,
        "level": 2,
        "topic": "INNER JOIN",
        "title": "Join with Aliases",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    dept_id INTEGER
);

CREATE TABLE departments (
    id INTEGER,
    dept_name TEXT
);

INSERT INTO employees (id, name, dept_id)
VALUES (1, 'Alice', 1), (2, 'Bob', 2);

INSERT INTO departments (id, dept_name)
VALUES (1, 'Engineering'), (2, 'Marketing');""",
        "question": "Select employee name and department name using table aliases e and d.",
        "correct_answer": "SELECT e.name, d.dept_name FROM employees e JOIN departments d ON e.dept_id = d.id",
        "explanation": "Aliases shorten table names and make queries more readable, especially with joins.",
        "hint": "Use FROM employees e JOIN departments d ON ...",
    },
    {
        "id": 62,
        "level": 2,
        "topic": "LEFT JOIN",
        "title": "Unassigned Employees",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    dept_id INTEGER
);

CREATE TABLE departments (
    id INTEGER,
    dept_name TEXT
);

INSERT INTO employees (id, name, dept_id)
VALUES (1, 'Alice', 1), (2, 'Bob', NULL);

INSERT INTO departments (id, dept_name)
VALUES (1, 'Engineering');""",
        "question": "Find employees who are not assigned to any department using LEFT JOIN.",
        "correct_answer": "SELECT e.name FROM employees e LEFT JOIN departments d ON e.dept_id = d.id WHERE d.id IS NULL",
        "explanation": "When a LEFT JOIN finds no match, columns from the right table are NULL. Filtering on IS NULL finds unmatched rows.",
        "hint": "Use LEFT JOIN and filter WHERE d.id IS NULL.",
    },
    {
        "id": 63,
        "level": 2,
        "topic": "CROSS JOIN",
        "title": "All Combinations",
        "schema": """CREATE TABLE colors (color TEXT);
CREATE TABLE sizes (size TEXT);

INSERT INTO colors (color) VALUES ('Red'), ('Blue');
INSERT INTO sizes (size) VALUES ('S'), ('M');""",
        "question": "Generate all possible color-size combinations using a CROSS JOIN.",
        "correct_answer": "SELECT color, size FROM colors CROSS JOIN sizes",
        "explanation": "CROSS JOIN returns the Cartesian product: every row from the first table paired with every row from the second.",
        "hint": "Use CROSS JOIN between colors and sizes.",
    },
    {
        "id": 64,
        "level": 2,
        "topic": "Subqueries in WHERE",
        "title": "Subquery with IN",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT
);

CREATE TABLE projects (
    id INTEGER,
    employee_id INTEGER
);

INSERT INTO employees (id, name, department)
VALUES (1, 'Alice', 'Engineering'), (2, 'Bob', 'Marketing');

INSERT INTO projects (id, employee_id)
VALUES (1, 1);""",
        "question": "Select names of employees who have a project using a subquery with IN.",
        "correct_answer": "SELECT name FROM employees WHERE id IN (SELECT employee_id FROM projects)",
        "explanation": "IN with a subquery checks if a value exists in the subquery result set.",
        "hint": "Use WHERE id IN (SELECT employee_id FROM projects).",
    },
    {
        "id": 65,
        "level": 2,
        "topic": "Subqueries in WHERE",
        "title": "Above Department Maximum",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES (1, 'Alice', 'Engineering', 90000), (2, 'Bob', 'Marketing', 60000), (3, 'Charlie', 'Engineering', 70000);""",
        "question": "Select employees in Engineering whose salary is greater than the MAX salary in Marketing.",
        "correct_answer": "SELECT name, salary FROM employees WHERE department = 'Engineering' AND salary > (SELECT MAX(salary) FROM employees WHERE department = 'Marketing')",
        "explanation": "A subquery with MAX lets you compare against an aggregate from a different subset of data.",
        "hint": "Use a subquery that finds MAX(salary) in Marketing.",
    },
    {
        "id": 66,
        "level": 2,
        "topic": "INSERT",
        "title": "Insert Multiple Rows",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES (1, 'Alice', 90000);""",
        "question": "Insert two new employees in a single statement: (2, 'Bob', 60000) and (3, 'Charlie', 70000).",
        "correct_answer": "INSERT INTO employees (id, name, salary) VALUES (2, 'Bob', 60000), (3, 'Charlie', 70000)",
        "explanation": "SQLite supports inserting multiple rows with a single VALUES clause separated by commas.",
        "hint": "Use VALUES (row1), (row2).",
    },
    {
        "id": 67,
        "level": 2,
        "topic": "UPDATE",
        "title": "Update with Subquery",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER,
    department TEXT
);

INSERT INTO employees (id, name, salary, department)
VALUES (1, 'Alice', 60000, 'Engineering'), (2, 'Bob', 60000, 'Marketing');""",
        "question": "Give all employees in Engineering a 10% raise using an UPDATE with a WHERE clause.",
        "correct_answer": "UPDATE employees SET salary = salary * 1.10 WHERE department = 'Engineering'",
        "explanation": "UPDATE can target specific rows using WHERE, and SET can reference current column values.",
        "hint": "Use SET salary = salary * 1.10 WHERE department = 'Engineering'.",
    },
    {
        "id": 68,
        "level": 2,
        "topic": "DELETE",
        "title": "Delete Low Earners",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES (1, 'Alice', 90000), (2, 'Bob', 50000), (3, 'Charlie', 60000);""",
        "question": "Delete employees with salary less than 60000.",
        "correct_answer": "DELETE FROM employees WHERE salary < 60000",
        "explanation": "DELETE with a WHERE clause removes only rows matching the condition.",
        "hint": "Use DELETE FROM ... WHERE salary < 60000.",
    },
    {
        "id": 69,
        "level": 2,
        "topic": "CASE Expressions",
        "title": "Grade Salaries",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES (1, 'Alice', 90000), (2, 'Bob', 60000), (3, 'Charlie', 45000);""",
        "question": "Classify salaries as 'High' if >= 80000, 'Medium' if >= 60000, else 'Low'.",
        "correct_answer": "SELECT name, CASE WHEN salary >= 80000 THEN 'High' WHEN salary >= 60000 THEN 'Medium' ELSE 'Low' END AS grade FROM employees",
        "explanation": "CASE evaluates conditions in order and returns the result for the first true condition.",
        "hint": "Use multiple WHEN ... THEN clauses in CASE.",
    },
    {
        "id": 70,
        "level": 2,
        "topic": "String Functions",
        "title": "Name Length",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT
);

INSERT INTO employees (id, name)
VALUES (1, 'Alice'), (2, 'Bob');""",
        "question": "Select each name and its character length.",
        "correct_answer": "SELECT name, LENGTH(name) FROM employees",
        "explanation": "LENGTH() returns the number of characters in a string.",
        "hint": "Use the LENGTH() function.",
    },
    {
        "id": 71,
        "level": 2,
        "topic": "Numeric Functions",
        "title": "Rounded Average",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    salary REAL
);

INSERT INTO employees (id, salary)
VALUES (1, 50000.5), (2, 60000.3);""",
        "question": "Calculate the average salary rounded to 1 decimal place.",
        "correct_answer": "SELECT ROUND(AVG(salary), 1) FROM employees",
        "explanation": "ROUND(value, digits) rounds a number to the specified number of decimal places.",
        "hint": "Use ROUND(AVG(salary), 1).",
    },
    {
        "id": 72,
        "level": 2,
        "topic": "Date Functions",
        "title": "Extract Year",
        "schema": """CREATE TABLE events (
    id INTEGER,
    event_date TEXT
);

INSERT INTO events (id, event_date)
VALUES (1, '2024-03-15'), (2, '2023-07-20');""",
        "question": "Extract the year from event_date using SQLite date function.",
        "correct_answer": "SELECT id, strftime('%Y', event_date) AS year FROM events",
        "explanation": "SQLite uses strftime() to format dates. '%Y' extracts the 4-digit year.",
        "hint": "Use strftime('%Y', event_date).",
    },
    {
        "id": 73,
        "level": 2,
        "topic": "Complex Conditions",
        "title": "Mixed AND OR",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES (1, 'Alice', 'Engineering', 90000), (2, 'Bob', 'Marketing', 80000), (3, 'Charlie', 'Engineering', 70000);""",
        "question": "Select names of Engineering employees with salary > 75000 OR Marketing employees with salary > 85000.",
        "correct_answer": "SELECT name FROM employees WHERE (department = 'Engineering' AND salary > 75000) OR (department = 'Marketing' AND salary > 85000)",
        "explanation": "Parentheses control the order of evaluation when mixing AND and OR.",
        "hint": "Use parentheses to group (department AND salary) conditions.",
    },
    {
        "id": 74,
        "level": 2,
        "topic": "EXISTS",
        "title": "Departments with Employees",
        "schema": """CREATE TABLE departments (id INTEGER, name TEXT);
CREATE TABLE employees (id INTEGER, dept_id INTEGER);

INSERT INTO departments (id, name) VALUES (1, 'Engineering'), (2, 'HR');
INSERT INTO employees (id, dept_id) VALUES (1, 1);""",
        "question": "Select department names that have at least one employee using EXISTS.",
        "correct_answer": "SELECT name FROM departments d WHERE EXISTS (SELECT 1 FROM employees e WHERE e.dept_id = d.id)",
        "explanation": "EXISTS efficiently checks for the existence of related rows without returning data from the subquery.",
        "hint": "Correlate the subquery with d.id.",
    },
    {
        "id": 75,
        "level": 2,
        "topic": "Multiple JOINs",
        "title": "Three Table Join",
        "schema": """CREATE TABLE customers (id INTEGER, name TEXT);
CREATE TABLE orders (id INTEGER, customer_id INTEGER, product_id INTEGER);
CREATE TABLE products (id INTEGER, title TEXT);

INSERT INTO customers (id, name) VALUES (1, 'Alice');
INSERT INTO orders (id, customer_id, product_id) VALUES (1, 1, 1);
INSERT INTO products (id, title) VALUES (1, 'Laptop');""",
        "question": "Show customer name and product title by joining all three tables.",
        "correct_answer": "SELECT customers.name, products.title FROM customers JOIN orders ON customers.id = orders.customer_id JOIN products ON orders.product_id = products.id",
        "explanation": "Chain multiple JOINs to traverse many-to-many or one-to-many relationships across tables.",
        "hint": "Join customers -> orders -> products.",
    },
    {
        "id": 76,
        "level": 3,
        "topic": "Window Functions - SUM OVER",
        "title": "Department Totals with Window",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Engineering', 80000),
    (3, 'Charlie', 'Marketing', 60000);""",
        "question": "Show each employee's name, salary, and their department's total salary using a window function.",
        "correct_answer": "SELECT name, salary, SUM(salary) OVER (PARTITION BY department) AS dept_total FROM employees",
        "explanation": "SUM() OVER with PARTITION BY calculates an aggregate within each partition without collapsing rows.",
        "hint": "Use SUM(salary) OVER (PARTITION BY department).",
    },
    {
        "id": 77,
        "level": 3,
        "topic": "Window Functions - Running Total",
        "title": "Year-to-Date Revenue",
        "schema": """CREATE TABLE sales (
    month TEXT,
    revenue INTEGER
);

INSERT INTO sales (month, revenue)
VALUES
    ('Jan', 10000),
    ('Feb', 12000),
    ('Mar', 11000);""",
        "question": "Calculate a running total of revenue up to the current row.",
        "correct_answer": "SELECT month, revenue, SUM(revenue) OVER (ORDER BY month ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS ytd FROM sales",
        "explanation": "ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW defines a cumulative window.",
        "hint": "Use ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW.",
    },
    {
        "id": 78,
        "level": 3,
        "topic": "Window Functions - FIRST_VALUE",
        "title": "First Employee by Hire",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    hire_date TEXT
);

INSERT INTO employees (id, name, hire_date)
VALUES
    (1, 'Alice', '2020-01-15'),
    (2, 'Bob', '2019-06-10'),
    (3, 'Charlie', '2021-03-20');""",
        "question": "Show each employee's name and the name of the first hired employee using FIRST_VALUE.",
        "correct_answer": "SELECT name, FIRST_VALUE(name) OVER (ORDER BY hire_date) AS first_hired FROM employees",
        "explanation": "FIRST_VALUE returns the first value in the window frame according to the specified ordering.",
        "hint": "Use FIRST_VALUE(name) OVER (ORDER BY hire_date).",
    },
    {
        "id": 79,
        "level": 3,
        "topic": "Window Functions - LAST_VALUE",
        "title": "Latest Hire per Department",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    hire_date TEXT
);

INSERT INTO employees (id, name, department, hire_date)
VALUES
    (1, 'Alice', 'Engineering', '2020-01-15'),
    (2, 'Bob', 'Engineering', '2022-08-01'),
    (3, 'Charlie', 'Marketing', '2021-03-20');""",
        "question": "Show department and the latest hire date in each department using LAST_VALUE.",
        "correct_answer": "SELECT department, LAST_VALUE(hire_date) OVER (PARTITION BY department ORDER BY hire_date ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS latest_hire FROM employees",
        "explanation": "LAST_VALUE returns the last value in the window frame. You may need to adjust the frame to include all rows in the partition.",
        "hint": "Use PARTITION BY department with a frame that includes all rows.",
    },
    {
        "id": 80,
        "level": 3,
        "topic": "Common Table Expressions (CTE)",
        "title": "Multiple CTEs",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES
    (1, 'Alice', 90000),
    (2, 'Bob', 60000),
    (3, 'Charlie', 95000);""",
        "question": "Use two CTEs: one for average salary, one for high earners above that average. Select the high earners.",
        "correct_answer": "WITH avg_sal AS (SELECT AVG(salary) AS val FROM employees), high_earners AS (SELECT name, salary FROM employees WHERE salary > (SELECT val FROM avg_sal)) SELECT * FROM high_earners",
        "explanation": "You can define multiple CTEs separated by commas and reference earlier CTEs in later ones.",
        "hint": "Define avg_sal first, then high_earners referencing avg_sal.",
    },
    {
        "id": 81,
        "level": 3,
        "topic": "Recursive CTE",
        "title": "Countdown",
        "schema": "-- No tables needed",
        "question": "Use a recursive CTE to generate numbers from 10 down to 1.",
        "correct_answer": "WITH RECURSIVE countdown(n) AS (SELECT 10 UNION ALL SELECT n - 1 FROM countdown WHERE n > 1) SELECT n FROM countdown",
        "explanation": "Recursive CTEs can count down by subtracting in the recursive member and stopping with a WHERE condition.",
        "hint": "Start at 10 and recursively subtract 1 while n > 1.",
    },
    {
        "id": 82,
        "level": 3,
        "topic": "Correlated Subquery",
        "title": "Above Department Average",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Engineering', 80000),
    (3, 'Charlie', 'Marketing', 70000);""",
        "question": "Select employees who earn more than the average salary of their own department.",
        "correct_answer": "SELECT name, department, salary FROM employees e WHERE salary > (SELECT AVG(salary) FROM employees WHERE department = e.department)",
        "explanation": "A correlated subquery references the outer query's row to compute a per-group comparison dynamically.",
        "hint": "The subquery should reference e.department.",
    },
    {
        "id": 83,
        "level": 3,
        "topic": "Set Operations",
        "title": "INTERSECT",
        "schema": """CREATE TABLE q1_sales (product TEXT);
CREATE TABLE q2_sales (product TEXT);

INSERT INTO q1_sales (product) VALUES ('Laptop'), ('Mouse');
INSERT INTO q2_sales (product) VALUES ('Mouse'), ('Keyboard');""",
        "question": "Find products that were sold in both Q1 and Q2 using INTERSECT.",
        "correct_answer": "SELECT product FROM q1_sales INTERSECT SELECT product FROM q2_sales",
        "explanation": "INTERSECT returns only rows that appear in both result sets.",
        "hint": "Use SELECT ... INTERSECT SELECT ...",
    },
    {
        "id": 84,
        "level": 3,
        "topic": "Set Operations",
        "title": "EXCEPT",
        "schema": """CREATE TABLE q1_sales (product TEXT);
CREATE TABLE q2_sales (product TEXT);

INSERT INTO q1_sales (product) VALUES ('Laptop'), ('Mouse');
INSERT INTO q2_sales (product) VALUES ('Mouse'), ('Keyboard');""",
        "question": "Find products sold in Q1 but NOT in Q2 using EXCEPT.",
        "correct_answer": "SELECT product FROM q1_sales EXCEPT SELECT product FROM q2_sales",
        "explanation": "EXCEPT returns rows from the first query that are not present in the second query.",
        "hint": "Use SELECT ... EXCEPT SELECT ...",
    },
    {
        "id": 85,
        "level": 3,
        "topic": "Advanced CASE",
        "title": "Department Bonus",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Marketing', 60000);""",
        "question": "Show name and a bonus column: 10% of salary for Engineering, 5% for others.",
        "correct_answer": "SELECT name, CASE WHEN department = 'Engineering' THEN salary * 0.10 ELSE salary * 0.05 END AS bonus FROM employees",
        "explanation": "CASE can compute different expressions based on conditions, not just return static values.",
        "hint": "Use CASE WHEN department = 'Engineering' THEN ... ELSE ... END.",
    },
    {
        "id": 86,
        "level": 3,
        "topic": "Subqueries in SELECT",
        "title": "Count per Row",
        "schema": """CREATE TABLE departments (id INTEGER, name TEXT);
CREATE TABLE employees (id INTEGER, dept_id INTEGER);

INSERT INTO departments (id, name) VALUES (1, 'Engineering'), (2, 'Marketing');
INSERT INTO employees (id, dept_id) VALUES (1, 1), (2, 1), (3, 2);""",
        "question": "Select department name and the count of employees in that department using a subquery in SELECT.",
        "correct_answer": "SELECT name, (SELECT COUNT(*) FROM employees WHERE dept_id = departments.id) AS emp_count FROM departments",
        "explanation": "A correlated scalar subquery in SELECT returns one value per outer row.",
        "hint": "Use a subquery that counts employees where dept_id matches departments.id.",
    },
    {
        "id": 87,
        "level": 3,
        "topic": "SELF JOIN",
        "title": "Employee Pairs",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT
);

INSERT INTO employees (id, name, department)
VALUES
    (1, 'Alice', 'Engineering'),
    (2, 'Bob', 'Engineering'),
    (3, 'Charlie', 'Marketing');""",
        "question": "List all pairs of employees in the same department using a self join (avoid pairing with self).",
        "correct_answer": "SELECT a.name, b.name FROM employees a JOIN employees b ON a.department = b.department AND a.id < b.id",
        "explanation": "A self join paired with a.id < b.id generates unique pairs without duplicates or self-pairing.",
        "hint": "Join on department and a.id < b.id.",
    },
    {
        "id": 88,
        "level": 3,
        "topic": "Window Functions - Multiple",
        "title": "Rank and Total",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Engineering', 80000),
    (3, 'Charlie', 'Marketing', 70000);""",
        "question": "Show name, salary, department total, and rank within department using two window functions.",
        "correct_answer": "SELECT name, salary, SUM(salary) OVER (PARTITION BY department) AS dept_total, RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank FROM employees",
        "explanation": "You can use multiple window functions in the same SELECT, even with different OVER clauses.",
        "hint": "Use SUM() OVER for the total and RANK() OVER for the ranking.",
    },
    {
        "id": 89,
        "level": 3,
        "topic": "CTE with Aggregation",
        "title": "Department Summary CTE",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, department, salary)
VALUES
    (1, 'Alice', 'Engineering', 90000),
    (2, 'Bob', 'Engineering', 80000),
    (3, 'Charlie', 'Marketing', 60000);""",
        "question": "Use a CTE to compute average salary per department, then select departments with avg > 75000.",
        "correct_answer": "WITH dept_avg AS (SELECT department, AVG(salary) AS avg_sal FROM employees GROUP BY department) SELECT department FROM dept_avg WHERE avg_sal > 75000",
        "explanation": "CTEs let you build complex queries step by step, reusing intermediate results.",
        "hint": "Define a CTE with GROUP BY, then filter it in the main query.",
    },
    {
        "id": 90,
        "level": 3,
        "topic": "Window Functions - Dense Rank",
        "title": "Dense Rank by Salary",
        "schema": """CREATE TABLE employees (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (id, name, salary)
VALUES
    (1, 'Alice', 90000),
    (2, 'Bob', 90000),
    (3, 'Charlie', 80000);""",
        "question": "Rank employees by salary using DENSE_RANK so ties share a rank with no gaps.",
        "correct_answer": "SELECT name, salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rnk FROM employees",
        "explanation": "DENSE_RANK gives the same rank to ties but does not leave gaps in the ranking sequence, unlike RANK().",
        "hint": "Use DENSE_RANK() OVER (ORDER BY salary DESC).",
    },
]

LEVEL_LABELS = {
    1: "🟢 Beginner",
    2: "🟡 Intermediate",
    3: "🔴 Advanced",
}

LEVEL_EMOJI = {
    1: "🟢",
    2: "🟡",
    3: "🔴",
}


def get_question_by_id(question_id: int):
    for q in QUESTIONS:
        if q["id"] == question_id:
            return q
    return None


def get_topics(level: int) -> list:
    seen = []
    for q in QUESTIONS:
        if q["level"] == level and q["topic"] not in seen:
            seen.append(q["topic"])
    return seen


def get_questions_by_topic(level: int, topic: str) -> list:
    return [q for q in QUESTIONS if q["level"] == level and q["topic"] == topic]


def get_next_question_id(current_id: int) -> int | None:
    idx = next((i for i, q in enumerate(QUESTIONS) if q["id"] == current_id), None)
    if idx is not None and idx + 1 < len(QUESTIONS):
        return QUESTIONS[idx + 1]["id"]
    return None
