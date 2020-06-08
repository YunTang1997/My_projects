-- 分组函数
/*
功能：用作统计使用，又称为聚合函数或者统计函数或组函数

分类：
sum 求和、avg 平均值、max 最大值、min 最小值、count 计算个数

特点：
1、sum、avg一般用于处理数值型，max、min、count可以处理任何类型
2、以上函数均忽略null值
3、可以和distinct函数（去重）搭配使用
4、一般使用count(*)用作统计函数
5、和分组函数一同查询的字段要求是group by后的字段
*/


-- 1、简单的使用
SELECT 
    SUM(salary)
FROM
    employees;

SELECT 
    AVG(salary)
FROM
    employees;

SELECT 
    MIN(salary)
FROM
    employees;

SELECT 
    MAX(salary)
FROM
    employees;

SELECT 
    COUNT(salary)
FROM
    employees;

SELECT 
    SUM(salary) AS '和', ROUND(AVG(salary), 2) AS '平均'
FROM
    employees;
    

-- 2、和distinct搭配
-- 统计有多少种工资
SELECT 
    COUNT(DISTINCT salary)
FROM
    employees;
    

-- 3、count函数的详细介绍
SELECT 
    COUNT(salary)
FROM
    employees;

-- 统计指定表有多少行，只要一行中有一个非null值就认为是一行
SELECT 
    COUNT(*)
FROM
    employees;

-- 统计指定表有多少行，将表增添一列1（某一行中有非null值就为1），将1换为其它数也行
SELECT 
    COUNT(1)
FROM
    employees;

-- 效率：
/*
MYISAM存储引擎下，count(*)效率高
INNODB存储引擎下，count(*)和count(1)的效率差不多，比count('字段')要高一些
*/


-- 练习
SELECT 
    MAX(salary) AS '工资最大值',
    MIN(salary) AS '工资最小值',
    ROUND(AVG(salary), 2) AS '工资平均值',
    SUM(salary) AS '工资总和'
FROM
    employees;
    
    
SELECT 
    DATEDIFF(MAX(hiredate), MIN(hiredate)) AS 'DIFFRENCE'
FROM
    employees;
    

SELECT 
    COUNT(*) AS '个数'
FROM
    employees
WHERE
    department_id = 90;
