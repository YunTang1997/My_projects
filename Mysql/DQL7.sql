-- 进阶7：子查询
/*
含义：
1、出现在其它语句中的select语句，称为子查询或内查询
2、外部的查询语句，称为主查询或外查询

分类：
按子查询出现的位置：
		select后面：
				仅仅支持标量子查询
				
		from后面：
				支持表子查询
				
		where后面或having后面：（重要）
				标量子查询（重要）
				列子查询（重要）
				
				行子查询（用的较少）
				
		exists后面（相关子查询）：
				表子查询
				
按结果集的行列数不同：
		标量子查询（结果只有一行一列）
		列子查询（结果只有一列多行）
		行子查询（结果集有一行多列）
		表子查询（结果一般为多行多列）
*/


/*一、where或having后面
1、标量子查询（单行子查询）
2、列子查询（多行子查询）
3、行子查询（多列多行）

特点：
		1、子查询放在小括号内
		2、子查询一般放在条件的右侧
		3、标量子查询，一般搭配单行操作符使用（>, <, >=, <=, <>）
		4、子查询的执行优先于主查询执行，主查询的条件用到了子查询的结果

列子查询：一般搭配着多行操作符使用（in, any/some, all）
*/

-- 1、标量子查询
-- 案例1：谁的工资比Abel高？
-- 第一步：查询Abel的工资
SELECT salary
FROM employees 
WHERE last_name = 'Abel';

-- 第二步：查询员工的信息，满足salary>第一步的结果
SELECT
	* 
FROM
	employees 
WHERE
	salary > ( SELECT salary FROM employees WHERE last_name = 'Abel' );
	
	
-- 案例2：返回job_id与141号员工相同，salary比143号员工多的员工的姓名，job_id和工资
SELECT
	last_name AS '姓名',
	job_id,
	salary AS '工资' 
FROM
	employees 
WHERE
	job_id = ( SELECT job_id FROM employees WHERE employee_id = 141 ) 
	AND salary > ( SELECT salary FROM employees WHERE employee_id = 143 );
	
	
-- 案例3：返回公司工资最少的员工的last_name, job_id和salary
SELECT
	last_name,
	job_id,
	salary 
FROM
	employees 
WHERE
	salary = ( SELECT MIN( salary ) FROM employees );
	
	
-- 案例4：查询最低工资大于50号部门最低工资的部门id和其最低工资
-- 第一步：查询50号部门的最低工资
SELECT MIN(salary)
FROM employees
WHERE department_id = 50;

-- 第二步：查询所有部门的最低工资
SELECT MIN(salary)
FROM employees
GROUP BY department_id;

-- 第三步：在第二步结果的基础上，筛选满足条件min(salary) > 第一步的结果
SELECT
	department_id,
	MIN( salary ) 
FROM
	employees 
GROUP BY
	department_id 
HAVING
	MIN( salary ) > ( SELECT MIN( salary ) FROM employees WHERE department_id = 50 );
	
	
-- 2、列子查询（多行子查询）
-- 案例1：返回location_id是1400或1700的部门中的所有员工姓名
-- 第一步：查询location_id是1400或1700的部门编号
SELECT DISTINCT
	department_id 
FROM
	departments 
WHERE
	location_id IN ( 1400, 1700 );

-- 第二步：在第一步的基础上，筛选符合的部门编号
SELECT
	last_name 
FROM
	employees 
WHERE
	department_id IN (
	SELECT DISTINCT
		department_id 
	FROM
		departments 
	WHERE
	location_id IN ( 1400, 1700 ));
	
	
SELECT
	last_name 
FROM
	employees 
WHERE
	department_id = ANY(
	SELECT DISTINCT
		department_id 
	FROM
		departments 
	WHERE
	location_id IN ( 1400, 1700 ));
	
	
-- 案例2：返回其它部门中比job_id为IT_PROG部门任一工资低的员工的员工号、姓名、job_id以及salary
-- 第一步
SELECT DISTINCT
	salary 
FROM
	employees 
WHERE
	job_id = 'IT_PROG';
	
-- 第二步
-- 方法一：
SELECT
	employee_id,
	last_name,
	job_id,
	salary 
FROM
	employees 
WHERE
	job_id <> 'IT_PROG' 
	AND salary < ANY ( SELECT DISTINCT salary FROM employees WHERE job_id = 'IT_PROG' );
	

-- 方法二：
SELECT
	employee_id,
	last_name,
	job_id,
	salary 
FROM
	employees 
WHERE
	job_id <> 'IT_PROG' 
	AND salary < ( SELECT MAX(salary) FROM employees WHERE job_id = 'IT_PROG' );
	
	
-- 案例3：返回其它部门中比job_id为IT_PROG部门所有工资都低的员工的员工号、姓名、job_id以及salary
SELECT
	employee_id,
	last_name,
	job_id,
	salary 
FROM
	employees 
WHERE
	job_id <> 'IT_PROG' 
	AND salary < ALL ( SELECT DISTINCT salary FROM employees WHERE job_id = 'IT_PROG' );
	

SELECT
	employee_id,
	last_name,
	job_id,
	salary 
FROM
	employees 
WHERE
	job_id <> 'IT_PROG' 
	AND salary < ( SELECT MIN(salary) FROM employees WHERE job_id = 'IT_PROG' );
	
	
-- 3、行子查询（结果集一行多列或多行多列）
-- 案例：查询员工编号最小并且工资最高的员工信息
-- 第一步：
SELECT
	MIN( employee_id ) 
FROM
	employees;

-- 第二步：
SELECT
	MAX( salary ) 
FROM
	employees;
	
-- 第三步：
-- 方法一：
SELECT
	* 
FROM
	employees 
WHERE
	employee_id = ( SELECT MIN( employee_id ) FROM employees ) 
	AND salary = ( SELECT MAX( salary ) FROM employees );

-- 方法二（行子查询）：
SELECT
	* 
FROM
	employees 
WHERE
	( employee_id, salary ) = ( SELECT MIN( employee_id ), MAX( salary ) FROM employees );


-- 二、select后面
/*
仅仅支持标量子查询
*/
-- 案例1：查询每个部门的员工个数
SELECT
	d.*,
	( SELECT COUNT(*) FROM employees AS e WHERE d.`department_id` = e.`department_id` ) 
FROM
	departments AS d;
	

-- 案例2：查询员工号=102的部门名
SELECT
	department_name 
FROM
	departments AS d
	LEFT JOIN employees AS e ON d.`department_id` = e.`department_id` 
WHERE
	employee_id = 102;
	

SELECT
	( SELECT department_name FROM departments AS d INNER JOIN employees AS e ON d.`department_id` = e.`department_id` WHERE employee_id = 102 );


SELECT
	department_name 
FROM
	departments 
WHERE
	department_id = ( SELECT department_id FROM employees WHERE employee_id = 102 );
	
	
-- 三、from后面
/*
仅仅支持表查询
将子查询充当一张表，要求必须起别名
*/
-- 案例1：查询每个部门的平均工资的工资等级
SELECT
	ROUND( AVG( salary ), 2 ),
	department_id 
FROM
	employees 
GROUP BY
	department_id;
	
SELECT
	ag_dep.*,
	g.grade_level 
FROM
	( SELECT ROUND( AVG( salary ), 2 ) AS ag, department_id FROM employees GROUP BY department_id ) AS ag_dep
	INNER JOIN job_grades AS g ON ag_dep.`ag` BETWEEN lowest_sal 
	AND highest_sal;
	
	
-- 四、exists后面（相关子查询）
/*
语法：
exists(完整的查询语句)
结果：
0或1
*/


-- 案例1：查询有员工的部门名
-- 方法一：
SELECT
	department_name
FROM
	departments
WHERE
	department_id IN ( SELECT department_id FROM employees );

-- 方法二：
SELECT
	department_name 
FROM
	departments AS d 
WHERE
	EXISTS ( SELECT * FROM employees AS e WHERE d.`department_id` = e.`department_id` );
	

-- 案例2：查询没有女朋友的男神信息
-- 方法一：
SELECT
	bo.* 
FROM
	boys AS bo 
WHERE
	bo.`id` NOT IN ( SELECT boyfriend_id FROM beauty );
	
	
-- 方法二：
SELECT
	bo.* 
FROM
	boys AS bo 
WHERE
	NOT EXISTS ( SELECT boyfriend_id FROM beauty AS b WHERE bo.`id` = b.`boyfriend_id`);
	
	
-- 练习1：查询和Zlotkey相同部门的员工姓名和工资 
SELECT
	department_id 
FROM
	employees 
WHERE
	last_name = 'Zlotkey';


SELECT
	last_name,
	salary 
FROM
	employees 
WHERE
	department_id = ( SELECT department_id FROM employees WHERE last_name = 'Zlotkey' );
	
	
-- 练习2：查询工资比公司平均工资高的员工的员工号，姓名和工资
SELECT 
		employee_id, last_name, salary
FROM 
		employees
WHERE 
		salary > (SELECT ROUND(AVG(salary), 2) FROM employees);
		
		
-- 练习3：查询各部门中工资比本部门平均工资高的员工的员工号, 姓名和工资 
SELECT
	ROUND( AVG( salary ), 2 ), department_id
FROM
	employees 
GROUP BY
	department_id;
	
	
SELECT
	employee_id,
	last_name,
	salary,
	e.department_id
FROM
	employees AS e
	INNER JOIN ( SELECT ROUND( AVG( salary ), 2 ) AS ag, department_id FROM employees GROUP BY department_id ) AS avg_sa ON e.`department_id` = avg_sa.`department_id`
WHERE salary > avg_sa.ag;


-- 练习4：查询和姓名中包含字母u的员工在相同部门的员工的员工号和姓名
SELECT DISTINCT
	department_id 
FROM
	employees 
WHERE
	last_name LIKE '%u%';
	

SELECT
	employee_id,
	last_name,
	department_id 
FROM
	employees 
WHERE
	department_id IN ( SELECT DISTINCT department_id FROM employees WHERE last_name LIKE '%u%' );


-- 练习5：查询在部门的location_id为1700的部门工作的员工的员工号
SELECT
	employee_id 
FROM
	employees AS e
	INNER JOIN departments AS d ON e.`department_id` = d.`department_id` 
WHERE
	location_id = 1700;
	
	
SELECT
	employee_id 
FROM
	employees 
WHERE
	department_id = ANY ( SELECT DISTINCT department_id FROM departments WHERE location_id = 1700 );
	

-- 练习6：查询管理者是K_ing的员工姓名和工资
-- 方法一：自连接
SELECT
	e.last_name,
	e.salary 
FROM
	employees AS e
	INNER JOIN employees AS m ON e.`manager_id` = m.`employee_id` 
WHERE
	m.last_name = 'K_ing';


-- 方法二：列子查询
SELECT
	last_name,
	salary 
FROM
	employees 
WHERE
	manager_id IN ( SELECT employee_id FROM employees WHERE last_name = 'K_ing' );


-- 练习7：查询工资最高的员工的姓名，要求first_name和last_name显示为一列，列名为姓.名 
SELECT
	CONCAT( first_name, '.', last_name ) AS '姓.名' 
FROM
	employees 
WHERE
	salary = ( SELECT MAX( salary ) FROM employees );