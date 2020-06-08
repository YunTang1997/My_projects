-- 进阶5：分组查询
/*
语法：
	select 分组函数, 列(要求出现在group by的后面)
    from 表
    [where 筛选条件]
    group by 分组的列表
    [order by 子句]
    
注意：
	查询列表必须特殊，要求是分组函数和group by后出现的字段
    
特点：
	1、分组查询中的筛选条件分为两类
						数据源                       位置                            关键字
	分组前的筛选        原始表                       group by子句的前面              where
    分组后的筛选        分组后的结果集               group by子句的后面              having
    
    a、分组函数做条件肯定是放在having子句中
    b、能用分组前筛选的，优先选用分组前筛选
    2、group by子句支持单个字段分组，多个字段分组（多个字段之间用逗号隔开没有顺序要求），表达式或函数（用的较少）
    3、也可以添加排序（排序放在分组查询最后面）
*/

-- 引入：查询每个部门的平均工资
SELECT 
    ROUND(AVG(salary), 2), department_id
FROM
    employees
GROUP BY department_id;


-- 简单的分组查询
-- 案例1：查询每个工种的最高工资
SELECT 
    MAX(salary), job_id
FROM
    employees
GROUP BY job_id;


-- 案例2：查询每个位置上的部门个数
SELECT 
    COUNT(*), location_id
FROM
    departments
GROUP BY location_id;


-- 添加筛选条件
-- 案例1：查询邮箱中包含a的字符的，每个部门的平均工资
SELECT 
    ROUND(AVG(salary), 2) AS '平均工资', department_id
FROM
    employees
WHERE
    email LIKE '%a%'
GROUP BY department_id;


-- 案例2：查询有奖金的每个领导手下员工的最高工资
SELECT 
    MAX(salary) AS '最高工资', manager_id
FROM
    employees
WHERE
    commission_pct IS NOT NULL
GROUP BY manager_id;


-- 添加复杂的筛选条件
-- 案例1：查询哪个部门的员工个数>2
/*
分解：
	1、查询每个部门的员工数
    SELECT 
    COUNT(*), department_id
	FROM
    employees
	GROUP BY department_id;
    2、根据1的结果进行筛选，查询哪个部门的员工个数>2
*/

SELECT 
    COUNT(*), department_id
FROM
    employees
GROUP BY department_id
HAVING COUNT(*) > 2;


-- 案例2：查询每个工种有奖金的员工的最高工资>12000的工种编号和最高工资
/*
分解：
	1、查询每个工种有奖金的员工的最高工资
	SELECT 
		MAX(salary) AS '最高工资', job_id
	FROM
		employees
	WHERE
		commission_pct IS NOT NULL
	GROUP BY job_id; 

	2、根据1的结果继续筛选，最高工资>12000
*/

SELECT 
    MAX(salary) AS '最高工资', job_id
FROM
    employees
WHERE
    commission_pct IS NOT NULL
GROUP BY job_id
HAVING MAX(salary) > 12000;


-- 案例3：查询领导编号>102的每个领导手下的最低工资>5000的领导编号是哪些，以及其最低工资
SELECT 
    MIN(salary) AS '最低工资', manager_id
FROM
    employees
WHERE
    manager_id > 102
GROUP BY manager_id
HAVING MIN(salary) > 5000;


-- 按表达式或函数分组
-- 案例：按员工姓名的长度分组，查询每一组的员工个数，筛选员工个数>5
SELECT 
    COUNT(*) AS '员工个数', LENGTH(last_name)
FROM
    employees
GROUP BY LENGTH(last_name)
HAVING 员工个数 > 5;


-- 按多个字段进行分组
-- 案例：查询每个部门每个工种的员工的平均工资
-- 分组字段调换顺序没有影响
SELECT 
    ROUND(avg(salary), 2) AS '平均工资',
    department_id,
    job_id
FROM
    employees
GROUP BY department_id , job_id;


-- 添加排序
-- 案例：查询每个部门每个工种的员工的平均工资并按工资由高到低排序
SELECT 
    ROUND(AVG(salary), 2) AS '平均工资', department_id, job_id
FROM
    employees
GROUP BY department_id , job_id
ORDER BY 平均工资 DESC;


-- 练习
SELECT 
    MAX(salary) AS '最大工资',
    MIN(salary) AS '最小工资',
    ROUND(AVG(salary), 2) AS '平均工资',
    SUM(salary) AS '总工资',
    job_id
FROM
    employees
GROUP BY job_id
ORDER BY job_id ASC;


SELECT 
    MAX(salary) - MIN(salary) AS DIFFERENCE
FROM
    employees;


SELECT 
    MIN(salary) AS '最低工资', manager_id
FROM
    employees
WHERE
    manager_id IS NOT NULL
GROUP BY manager_id
HAVING 最低工资 > 6000;


SELECT 
    COUNT(*) AS '员工数量',
    ROUND(AVG(salary), 2) AS '平均工资',
    department_id AS '部门编号'
FROM
    employees
GROUP BY 部门编号
ORDER BY 平均工资 DESC;


SELECT 
    COUNT(*) AS '员工人数', job_id
FROM
    employees
GROUP BY job_id;