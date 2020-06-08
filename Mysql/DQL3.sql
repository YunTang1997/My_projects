-- 进阶3：排序查询
/*
语法：
SELECT 
    查询列表
FROM
    表
（WHERE
    筛选条件）
ORDER BY 排序列表 ASC（升序，可省略） | DESC（降序）

特点：
1、ASC表示升序，DESC表示降序，不写默认表示升序
2、ORDER BY子句中可以支持单个字段、多个字段、表达式、函数、别名
3、ORDER BY子句一般是放在查询语句的最后面，但是LIMIT子句除外
*/

-- 案例一
SELECT 
    *
FROM
    employees
ORDER BY salary DESC;


SELECT 
    *
FROM
    employees
ORDER BY salary ASC;


-- 案例二
SELECT 
    *
FROM
    employees
WHERE
    department_id >= 90
ORDER BY hiredate ASC;


-- 案例3 
-- 方式一：按表达式
SELECT 
    *, salary * 12 * (1 + ifnull(commission_pct, 0)) AS '年薪'
FROM
    employees
ORDER BY salary * 12 * (1 + ifnull(commission_pct, 0)) DESC;

-- 方式二：按别名
SELECT 
    *, salary * 12 * (1 + ifnull(commission_pct, 0)) AS '年薪'
FROM
    employees
ORDER BY '年薪' DESC;


-- 案例4
-- 按函数
SELECT 
    last_name, LENGTH(last_name) AS '字节长度', salary
FROM
    employees
ORDER BY LENGTH(last_name) ASC;


-- 案例6：查询员工信息，要求先按工资排序（升序），再按员工编号排序（降序）
SELECT 
    *
FROM
    employees
ORDER BY salary ASC , employee_id DESC;


-- 练习
SELECT 
    last_name,
    department_id,
    salary * 12 * (1 + IFNULL(commission_pct, 0)) AS '年薪'
FROM
    employees
ORDER BY '年薪' DESC , last_name ASC;


SELECT 
    last_name, salary
FROM
    employees
WHERE
    NOT (salary BETWEEN 8000 AND 17000)
ORDER BY salary DESC;


SELECT 
    *, LENGTH(email)
FROM
    employees
WHERE
    email LIKE '%e%'
ORDER BY LENGTH(email) DESC , department_id ASC;







