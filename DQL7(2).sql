-- 1、查询工资最低的员工信息：last_name, salary
SELECT MIN(salary)
FROM employees;

SELECT
	last_name,
	salary 
FROM
	employees 
WHERE
	salary = ( SELECT MIN( salary ) FROM employees );
	

-- 2、查询平均工资最低的部门信息
SELECT department_id
FROM employees
GROUP BY department_id
ORDER BY AVG(salary) ASC
LIMIT 1;


SELECT
	* 
FROM
	departments 
WHERE
	department_id = ( SELECT department_id FROM employees GROUP BY department_id ORDER BY AVG( salary ) ASC LIMIT 1 );
	
	
-- 3、查询平均工资最低的部门信息和该部门的平均工资
SELECT department_id, AVG(salary) ag_s
FROM employees
GROUP BY department_id
ORDER BY ag_s ASC
LIMIT 1;


SELECT
	d.*,
	deag_s.ag_s 
FROM
	departments d
	INNER JOIN ( SELECT department_id, AVG( salary ) ag_s FROM employees GROUP BY department_id ORDER BY ag_s ASC LIMIT 1 ) deag_s ON d.`department_id` = deag_s.`department_id`;
	
	
-- 4、查询平均工资最高的job信息
SELECT job_id
FROM employees
GROUP BY job_id
ORDER BY AVG(salary) DESC
LIMIT 1;


SELECT
	jobs.* 
FROM
	jobs 
WHERE
	job_id = ( SELECT job_id FROM employees GROUP BY job_id ORDER BY AVG( salary ) DESC LIMIT 1 );
	
	
-- 5、查询平均工资高于公司平均工资的部门有哪些
SELECT AVG(salary) ag_s
FROM employees;


SELECT AVG(salary) deag_s, department_id
FROM employees
GROUP BY department_id;


SELECT
	dep.department_id 
FROM
	( SELECT AVG( salary ) deag_s, department_id FROM employees GROUP BY department_id ) dep
	INNER JOIN ( SELECT AVG( salary ) ag_s FROM employees ) co ON dep.deag_s > co.ag_s;
	
	
SELECT department_name FROM
departments 
WHERE department_id IN (SELECT
	dep.department_id 
FROM
	( SELECT AVG( salary ) deag_s, department_id FROM employees GROUP BY department_id ) dep
	INNER JOIN ( SELECT AVG( salary ) ag_s FROM employees ) co ON dep.deag_s > co.ag_s);


-- 6、查询出公司所有manager的详细信息
SELECT DISTINCT manager_id 
FROM employees;


SELECT
	* 
FROM
	employees 
WHERE
	employee_id IN ( SELECT DISTINCT manager_id FROM employees );
	
	
-- 7、各个部门中最高工资中最低的那个部门的最低工资是多少
SELECT department_id
FROM employees
GROUP BY department_id
ORDER BY MAX(salary) ASC
LIMIT 1;

SELECT
	MIN( salary ) 
FROM
	employees 
WHERE
	department_id = ( SELECT department_id FROM employees GROUP BY department_id ORDER BY MAX( salary ) ASC LIMIT 1 );
	
	
-- 8、查询平均工资最高的部门的manager的详细信息：last_name, department_id, email, salary
SELECT department_id
FROM employees
GROUP BY department_id
ORDER BY AVG(salary) DESC
LIMIT 1;


SELECT DISTINCT manager_id
FROM employees
WHERE department_id = (SELECT department_id
FROM employees
GROUP BY department_id
ORDER BY AVG(salary) DESC
LIMIT 1);


SELECT
	last_name,
	department_id,
	email,
	salary 
FROM
	employees 
WHERE
	employee_id IN (
	SELECT DISTINCT
		manager_id 
	FROM
		employees 
	WHERE
	department_id = ( SELECT department_id FROM employees GROUP BY department_id ORDER BY AVG( salary ) DESC LIMIT 1 ));
