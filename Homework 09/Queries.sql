--Question #1
SELECT e.first_name,e.last_name, e.employee_no,e.gender,s.salary 
	FROM employees AS e 
	LEFT JOIN salaries AS s 
	ON e.employee_no=s.employee_no

--Question #2
SELECT first_name, last_name, hire_date FROM employees
	WHERE hire_date >= '1986-01-01' 
	AND hire_date <= '1986-12-31'
	ORDER BY hire_date
	
--Question #3
SELECT e.first_name,e.last_name, e.employee_no, d.from_date, d.to_date, d.dept_no, s.dept_name
	FROM dept_manager AS d
	LEFT JOIN employees AS e
	ON e.employee_no=d.employee_no
	LEFT JOIN departments AS s
	ON d.dept_no=s.dept_no

--Question #4
SELECT e.first_name,e.last_name, e.employee_no, d.from_date, d.to_date, d.dept_no, s.dept_name
	FROM employees AS e
	INNER JOIN dept_employee AS d
	ON e.employee_no=d.employee_no
	INNER JOIN departments AS s 
	ON d.dept_no=s.dept_no

--Question #5
SELECT first_name, last_name FROM employees
	WHERE first_name = 'Hercules' 
	AND last_name LIKE 'B%'

--Question #6
SELECT e.last_name, e.first_name,d.employee_no,x.dept_name
	FROM employees AS e
	LEFT JOIN dept_employee AS d
	ON e.employee_no=d.employee_no
	LEFT JOIN departments AS x
	ON d.dept_no=x.dept_no
	WHERE d.dept_no = 'd007'
	
--Question #7
SELECT e.first_name,e.last_name, e.employee_no, s.dept_name
	FROM employees AS e
	INNER JOIN dept_employee AS d
	ON e.employee_no=d.employee_no
	INNER JOIN departments AS s 
	ON d.dept_no=s.dept_no
	WHERE dept_name = 'Development' OR dept_name = 'Sales'

--Question #8 
SELECT last_name, COUNT(*) 
	FROM employees
	GROUP BY last_name
	ORDER BY count DESC
