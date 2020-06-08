-- 进阶1：基础查询
/*
语法：
SELECT 
    查询列表
FROM
    表名;

特点：

1、查询列表可以是：表中的字段、常量值、表达式、函数
2、查询的结果是一个虚拟的表格（类似于python中的视图）
*/

-- 使用指定的数据库
USE myemployees;


-- 1.查询表中的单个字段
SELECT 
    last_name
FROM
    employees;

-- 2.查询表中的多个字段
SELECT 
    last_name, salary, email
FROM
    employees;

-- 3.查询表中所有字段
-- 方法一：可以更改查询表的顺序
SELECT 
    employee_id,
    first_name,
    last_name,
    email,
    phone_number,
    job_id,
    salary,
    commission_pct,
    manager_id,
    department_id,
    hiredate
FROM
    employees;
    
-- 方法二：不可以更改查询表的顺序
SELECT 
    *
FROM
    employees;
    
-- 4.查询常量值
SELECT 100;
SELECT 'john';


-- 5.查询表达式
SELECT 100 % 98;

-- 6.查询函数
SELECT version();


-- 7.给字段取别名
/*
1、便于理解
2、如果要查询的字段有重名的情况，使用别名可以区分开来
*/

-- 方式一：使用As 
SELECT 100 % 98 AS 结果;

SELECT 
    last_name AS 姓, first_name AS 名
FROM
    employees;

-- 方式二：使用空格
SELECT 
    last_name 姓, first_name 名
FROM
    employees;
    
-- 案例：查询salary，显示列名的别名为out put（当别名中有空格、#等特殊字符，则别名需要用引号，否则会报错）
SELECT 
    salary AS "out put"
FROM
    employees;


-- 8.去重（distinct）
-- 案例：查询员工表中涉及到的所有的部门编号
SELECT DISTINCT
    department_id
FROM
    employees;
    
-- 9.+号的作用
/*
python中+号：
1、运算符，两个操作数都为数值型
2、连接符，只要有一个操作数为字符串

mysql中的+号：
仅仅只有一个功能：运算符
*/

-- 两个操作数都为数值型，则做加法运算
SELECT 100 + 90; 

-- 其中一方为字符型，试图将字符型转换成数值型，如果转换成功，则继续做加法运算
SELECT "123" + 90; 

-- 如果转换失败，则将字符串转换为0
SELECT "john" + 90; 

-- 只要一方为null，结果肯定为null 
SELECT null + 10; 


-- 连接多个字段（concat）
-- 案例：查询员工名和姓连接成一个字段，并显示为 姓名
SELECT 
    CONCAT(last_name, first_name) AS 姓名
FROM
    employees;


-- 如果连接的字段中有值为null（ifnull）
SELECT 
    IFNULL(commission_pct, 0) AS 奖金率, 
    commission_pct
FROM
    employees;
  
  
-- 练习1
SELECT 
    last_name, job_id, salary AS sal
FROM
    employees;
    
SELECT 
    employee_id, last_name, salary * 12 AS 'ANNUAL SALARY'
FROM
    employees;
    
DESC departments;
SELECT 
    *
FROM
    departments;
    
SELECT DISTINCT
    job_id
FROM
    employees;

SELECT 
    CONCAT(employee_id,
            ',',
            first_name,
            ',',
            last_name,
            ',',
            email,
            ',',
            phone_number,
            ',',
            IFNULL(commission_pct, 0)) AS OUT_PUT
FROM
    employees;

