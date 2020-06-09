-- 进阶6：连接查询
/*
含义：又称为多表查询，当查询的字段来自于多个表，就会用到连接查询

笛卡尔乘积现象：表1有m行，表2有n行，结果有m*n行
出现原因：没有添加有效的连接条件
解决办法：添加有效的连接条件


分类：
	按年代分类：
				sql92标准：仅仅支持内连接
				sql99标准（推荐）：支持内连接+外连接（左外和右外）+交叉连接
    按功能分类：
				内连接：
						等值连接
						非等值连接
						自连接
        外连接：
						左外连接
            右外连接
            全外连接
				交叉连接
*/

SELECT 
    *
FROM
    beauty;
    
    
SELECT 
    *
FROM
    boys;
    

-- 一、sql92标准
-- 1、等值连接
/*
1、多表等值连接的结果为多表的交集部分
2、n表连接，至少需要n-1个连接条件
3、多表的顺序没有要求
4、一般需要为表起别名
5、可以搭配前面介绍的所有字句使用，比如排序、分组、筛选
*/

-- 案例1：查询女神名和对应的男神名
SELECT 
    name, boyName
FROM
    beauty,
    boys
WHERE
    beauty.boyfriend_id = boys.id;
    
    
-- 案例2：查询员工名和对应的部门名
SELECT 
    last_name AS '员工名', department_name AS '部门名'
FROM
    departments,
    employees
WHERE
    departments.department_id = employees.department_id;
    

/*
为表起别名:
			提高语句简洁度
            区分多个重名的字段
            
注意：如果为表起了别名，则查询的字段就不能用原来的表名去限定
*/
-- 案例3：查询员工名、工种号、工种名
SELECT 
    last_name AS '员工名',
    e.job_id AS '工种号',
    job_title AS '工种名'
FROM
    employees AS e,
    jobs AS j
WHERE
    e.job_id = j.job_id;


-- 增加筛选条件
-- 案例4：查询有奖金的员工名、部门名
SELECT 
    last_name AS '员工名', department_name AS '部门名'
FROM
    employees AS e,
    departments AS d
WHERE
    e.department_id = d.department_id
        AND e.commission_pct IS NOT NULL;


-- 案例5：查询城市中第二个字符为o的部门名和城市名
SELECT 
    department_name AS '部门名', city AS '城市名'
FROM
    departments AS d,
    locations AS l
WHERE
    d.`location_id` = l.`location_id`
        AND l.`city` LIKE '_o%';


-- 增加分组条件
-- 案例6：查询每个城市的部门个数
SELECT 
    COUNT(*) AS '部门个数', city AS '城市'
FROM
    departments AS d,
    locations AS l
WHERE
    d.`location_id` = l.`location_id`
GROUP BY l.`city`;


-- 案例7：查询有奖金的每个部门的部门名和部门的领导编号和该部门的最低工资
SELECT 
    d.`manager_id` AS '领导编号',
    MIN(salary) AS '最低工资',
    department_name AS '部门名'
FROM
    employees AS e,
    departments AS d
WHERE
    e.`department_id` = d.`department_id`
        AND commission_pct IS NOT NULL
GROUP BY department_name;


-- 增加排序
-- 案例8：查询每个工种的工种名和员工的个数，并且按员工的个数降序
SELECT 
    COUNT(*) AS '员工个数', job_title AS '工种名'
FROM
    employees AS e,
    jobs AS j
WHERE
    e.`job_id` = j.`job_id`
GROUP BY 工种名
ORDER BY 员工个数 DESC;


-- 三表连接
-- 案例9：查询员工名、部门名和所在的城市
SELECT 
    last_name AS '员工名',
    department_name AS '部门名',
    city AS '城市'
FROM
    employees AS e,
    departments AS d,
    locations AS l
WHERE
    e.`department_id` = d.`department_id`
        AND d.`location_id` = l.`location_id`;
        

-- 2、非等值连接
/*

*/

SELECT 
    *
FROM
    job_grades;


-- 案例1：查询员工的工资和工资级别
SELECT 
    salary AS '工资', grade_level AS '工资级别'
FROM
    employees AS e,
    job_grades AS g
WHERE
    e.`salary` BETWEEN g.`lowest_sal` AND g.`highest_sal`;
    

-- 3、自连接
-- 案例1：查询员工名和上级的名称

SELECT 
    e.employee_id AS '员工编号',
    e.last_name AS '员工名',
    m.employee_id AS '领导编号',
    m.last_name AS '领导名称'
FROM
    employees AS e,
    employees AS m
WHERE
    e.`manager_id` = m.`employee_id`;

    
-- 练习


USE myemployees;

SELECT
	MAX(salary) AS '最大工资',
	ROUND(AVG(salary), 2) AS '平均工资'
FROM
	employees;


SELECT
	employee_id,
	job_id,
	last_name
FROM
	employees
ORDER BY
	department_id DESC,
	salary ASC;


SELECT
	job_id
FROM
	employees
WHERE
	job_id LIKE '%a%e%';
	
	
SELECT
	last_name AS '姓名',
	e.department_id AS '部门编号',
	department_name AS '部门名称' 
FROM
	employees AS e,
	departments AS d 
WHERE
	e.`department_id` = d.`department_id`;
	
	
SELECT
	job_id,
	location_id 
FROM
	employees AS e,
	departments AS d 
WHERE
	e.`department_id` = d.`department_id` 
	AND e.`department_id` = 90;
	
	
SELECT
	last_name,
	department_name,
	d.location_id,
	city 
FROM
	employees AS e,
	departments AS d,
	locations AS l 
WHERE
	e.`department_id` = d.`department_id` 
	AND d.`location_id` = l.`location_id` 
	AND e.`commission_pct` IS NOT NULL;
	
	
SELECT
	last_name,
	job_id,
	e.department_id,
	department_name 
FROM
	employees AS e,
	departments AS d,
	locations AS l 
WHERE
	e.`department_id` = d.`department_id` 
	AND d.`location_id` = l.`location_id` 
	AND city = 'Toronto';
	
	
SELECT
	department_name AS '部门名',
	job_title AS '工种名',
	MIN( salary ) AS '最低工资' 
FROM
	employees AS e,
	jobs AS j,
	departments AS d 
WHERE
	e.`job_id` = j.`job_id` 
	AND e.`department_id` = d.`department_id` 
GROUP BY
	工种名,
	部门名;
	
	
SELECT
	COUNT(*) AS '部门个数',
	country_id AS '国家编号' 
FROM
	departments AS d,
	locations AS l 
WHERE
	d.`location_id` = l.`location_id` 
GROUP BY
	国家编号 
HAVING
	COUNT(*) > 2;
	
	
SELECT
	e.last_name AS '员工姓名',
	e.employee_id AS '员工编号',
	m.last_name AS '管理者姓名',
	m.employee_id AS '管理者编号' 
FROM
	employees AS e,
	employees AS m 
WHERE
	e.`manager_id` = m.`employee_id` 
	AND e.`employee_id` = 101;

