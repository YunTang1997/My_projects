-- 二、sql99语法
/*
语法：
		select 查询列表
		from 表1 别名 [连接类型]
		join 表2 别名
		on 连接条件
		where 筛选条件
		[group by 分组]
		[having 筛选条件]
		[order by 排序列表]
	
内连接（重要）：inner
外连接
			左外（重要）:left [outer]
			右外（重要）:right [outer]
			全外：full [outer]
交叉链接：cross

*/


-- 1、内连接
/*
语法：
		select 查询列表
		from 表1 别名 inner
		join 表2 别名
		on 连接条件
		where 筛选条件
		[group by 分组]
		[having 筛选条件]
		[order by 排序列表]
		

分类：
		等值连接
		非等值连接
		自连接

特点：
1、可以添加排序、分组、筛选
2、inner可以省略
3、筛选条件放在where后面，连接条件放在on后面，提高分离性，便于阅读
4、inner join连接和sql92语法中的等值连接效果是一样的，都是查询多表的交集
*/


-- 等值连接
-- 案例1：查询员工名、部门名（调换位置）
SELECT
	department_name AS '部门名',
	last_name AS '员工名' 
FROM
	employees AS e
	INNER JOIN departments AS d ON e.`department_id` = d.`department_id`;
	
	
-- 案例2：查询部门个数大于3的城市名和部门个数
-- 1、查询每个城市的部门个数
-- 2、在1的结果上筛选满足条件的
SELECT
	city AS 城市名,
	COUNT(*) AS 部门个数 
FROM
	locations AS l
	INNER JOIN departments AS d ON l.`location_id` = d.`location_id` 
GROUP BY
	city 
HAVING
	部门个数 > 3;
	
	
-- 案例3：查询哪个部门的部门员工个数>3的部门名和员工个数，并按个数降序排列
SELECT
	department_name AS 部门名,
	COUNT(*) AS 员工个数 
FROM
	employees AS l
	INNER JOIN departments AS d ON l.`department_id` = d.`department_id` 
GROUP BY
	部门名 
HAVING
	员工个数 > 3 
ORDER BY
	员工个数 DESC;


-- 案例5：查询员工名、部门名、工种名，并安部门名降序
SELECT
	last_name AS 员工名,
	department_name AS 部门名,
	job_title AS 工种名 
FROM
	employees AS e
	INNER JOIN departments AS d ON e.`department_id` = d.`department_id`
	INNER JOIN jobs AS j ON e.`job_id` = j.`job_id` 
ORDER BY
	部门名 DESC;


-- 非等值连接
-- 案例1、查询员工的工资级别
SELECT
	grade_level AS 工资级别 
FROM
	employees AS e
	INNER JOIN job_grades AS j ON e.`salary` BETWEEN j.`lowest_sal` 
	AND j.`highest_sal`;
	
	
-- 自连接
-- 案例1、查询员工的名字、上级的名字
SELECT
	e.last_name AS 员工名,
	m.last_name AS 上级名 
FROM
	employees AS e
	INNER JOIN employees AS m ON e.`manager_id` = m.`employee_id`;



