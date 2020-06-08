-- 外连接
/*
应用场景：用于查询一个表中有，另一个表中没有的记录

特点：
		1、外连接的查询结果为主表中所有记录，
		如果从表中有和它匹配的，则显示匹配的值，
		如果从表中没有和它匹配的，则显示null，
		外连接查询结果=内连接结果+主表中有而从表中没有的记录

		2、左外连接，left join左边的是主表
		右外连接，right join右边的是主表
		
		3、左外和右外交换两个表的顺序，可以实现同样的效果
		
		4、全外连接=内连接的结果+表1中有但表2中没有的+表2中有但表1中没有的
		
		5、交叉连接，就是“笛卡尔乘积”连接
*/
-- 引入：查询男朋友不在男神表的女神名
-- 左外连接
SELECT
	b.`name`,
	bo.* 
FROM
	beauty AS b
	LEFT OUTER JOIN boys AS bo ON b.`boyfriend_id` = bo.`id` 
WHERE
	bo.`id` IS NULL;
	

-- 右外连接
SELECT
	b.`name`,
	bo.* 
FROM
	boys AS bo
	RIGHT OUTER JOIN beauty AS b ON b.`boyfriend_id` = bo.`id` 
WHERE
	bo.`id` IS NULL;
	
	
-- 案例：查询哪个部门没有员工
SELECT
	d.*,
	e.`employee_id` 
FROM
	departments AS d
	LEFT OUTER JOIN employees AS e ON d.`department_id` = e.`department_id` 
WHERE
	e.`employee_id` IS NULL;


-- 全外（mysql不支持）
SELECT
	b.*,
	bo.* 
FROM
	beauty AS b
	FULL OUTER JOIN boys AS bo ON b.`boyfriend_id` = bo.`id`;
	

-- 交叉连接（笛卡尔乘积）
SELECT
	b.*,
	bo.* 
FROM
	beauty AS b
	CROSS JOIN boys AS bo;
	
	
-- sql92和sql99 PK
/*
功能：sql99支持的较多
可读性：sql99实现连接条件和筛选条件分离，可读性较高
*/


-- 练习
-- 1、查询编号>3的女神的男朋友信息，如果有则列出详细，如果没有，用null填充
SELECT
	b.id, b.`name`, bo.*
FROM
	beauty AS b
	LEFT JOIN boys AS bo ON bo.`id` = b.`boyfriend_id` 
WHERE
	b.`id` > 3;


-- 2、查询哪个城市没有部门
SELECT
	city, d.*
FROM
	locations AS l
	LEFT JOIN departments AS d ON l.`location_id` = d.`location_id` 
WHERE
	d.`department_id` IS NULL;


-- 3、查询部门名为SAL或IT的员工信息
SELECT
	e.*, department_name
FROM
	employees AS e
	RIGHT JOIN departments AS d ON e.`department_id` = d.`department_id` 
WHERE
	d.`department_name` IN ( 'SAL', 'IT' );

	
	