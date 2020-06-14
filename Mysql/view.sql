-- 视图
/*
含义：虚拟表，和普通表一样使用
musql5.1版本出现的新特性，是通过表动态生成的数据

好处：
重用sql语句
简化复杂的sql操作，不必知道它的查询细节
保护数据，提高安全性


表和视图对比：
					创建语法的关键字        是否实际占用物理空间                  使用
视图				create view             只是保存了sql逻辑       增删改查，但一般不增删改查，只查询
表					create table								 占用               增删改查
*/


-- 一、创建视图
/*
语法：
create view 视图名
as
查询语句;
*/


-- 案例1：查询姓张的学生名和专业名
-- 方法一
SELECT
	studentname,
	majorname 
FROM
	student s INNER JOIN major m ON s.majorid = m.majorid 
WHERE
	s.studentname LIKE '张%';


-- 方法二
CREATE VIEW v1 AS SELECT
studentname,
majorname 
FROM
	student s
	INNER JOIN major m ON s.majorid = m.majorid;
	
SELECT * FROM v1 WHERE studentname LIKE '张%';


-- 案例2：查询姓名中包含a字符的员工名、部门名和工种信息
CREATE VIEW myv1
AS
SELECT last_name, department_name, job_title
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
INNER JOIN jobs j ON e.job_id = j.job_id;


SELECT * FROM myv1 WHERE last_name LIKE '%a%';


-- 案例3：查询各部门的平均工资级别
CREATE VIEW myv2
AS
SELECT AVG(salary) ag, department_id
FROM employees
GROUP BY department_id;

SELECT * FROM myv2;

SELECT
	myv2.ag,
	grade_level 
FROM
	myv2
	INNER JOIN job_grades jg ON myv2.ag BETWEEN jg.lowest_sal 
	AND jg.highest_sal;


-- 案例4：查询平均工资最低的部门信息
SELECT department_id
FROM myv2
WHERE ag = (SELECT MIN(ag) FROM myv2);


SELECT
	* 
FROM
	departments 
WHERE
	department_id = (
	SELECT
		department_id 
	FROM
		myv2 
	WHERE
	ag = ( SELECT MIN( ag ) FROM myv2 ));
	
	
SELECT * FROM myv2 ORDER BY ag ASC LIMIT 1;


-- 案例5：查询平均工资最低的部门名和工资
CREATE VIEW myv3
AS
SELECT * FROM myv2 ORDER BY ag ASC LIMIT 1;

SELECT
	myv3.ag,
	d.department_name 
FROM
	myv3
	INNER JOIN departments d ON myv3.department_id = d.department_id;


-- 二、视图的修改
-- 方式一：
/*
create or repalce view 视图名
as
查询语句;
*/

CREATE [OR REPLACE] VIEW myv3
AS
SELECT AVG(salary), job_id
FROM employees
GROUP BY job_id;


SELECT * FROM myv3;


-- 方式二：
/*
语法：
alter view 视图名
as
查询语句;
*/

ALTER VIEW myv3
AS
SELECT * FROM employees;

SELECT * FROM myv3;


-- 三、删除视图
/*
语法：drop view 视图名1, 视图名2, ...;
*/


-- 四、查看视图
/*
desc 视图名;

show create view myv3;（cmd中结果比较全）
*/


-- 五、视图的更新
/*
1、更新语法：update form [视图名 where 筛选语句];
2、插入语法：insert into 视图名[(字段名)] values();
3、删除语法：delete from [视图名 where 筛选语句];

注意：通过以上语句对视图修改，也会修改原表，所以一般会给视图增加只读权限

具备一下特点的视图不允许更新：
		包含以下关键字的sql语句：分组函数、distinct、group by、having、union或者union all
		常量视图
		Select中包含子查询
		join
		from一个不能更新的视图
		where子句的子查询引用了from子句中的表
*/

