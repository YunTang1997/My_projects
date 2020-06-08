-- 进阶2：条件查询
/*
语法：
SELECT 
    查询列表
FROM
    表名
WHERE
    筛选条件;
    
分类：
1、按条件表达式筛选：条件运算符：> < = （!= <>） >= <=
2、按逻辑表达式筛选：逻辑运算符：&& || ！and or not
3、模糊查询：ilke between and in is null
*/

-- 1.按条件表达式筛选
-- 案例1：查询工资>12000的员工信息
SELECT 
	*
FROM
    employees
WHERE
    salary > 12000;

-- 案例2：查询部门编号不等于90号的员工名和部门编号
SELECT 
    employee_id, department_id
FROM
    employees
WHERE
    department_id != 90;
    
    
-- 2.按逻辑表示筛选
-- 案例1：查询部门编号不是在90到110之间，或者工资高于15000的员工信息
SELECT 
    *
FROM
    employees
WHERE
    NOT (90 <= department_id
        AND department_id <= 110)
        OR salary > 15000;


-- 3.模糊查询
/*
like
特点：
1、一般和通配符搭配使用。
	通配符：
		% 任意多个字符，包含0个字符
        _ 任意单个字符

between and
特点：
1、提升代码简洁度
2、包含临界值
3、临界值不要调换顺序

in 
特点：
1、提升语句简洁度
2、in列表的值类型必须一致或兼容
3、不能使用通用符

is null、is not null
特点：
1、=或者<>不能用于判断null值
2、is null或者is not null 可以判断null值
*/

-- like
-- 案例1：查询员工名中包含字符a的员工信息
SELECT 
    *
FROM
    employees
WHERE
    last_name LIKE '%a%';
    
-- 案例2：查询员工名中第三个字符为e，第五个字符为a的员工名和工资
SELECT 
    last_name, salary
FROM
    employees
WHERE
    last_name LIKE '__e_a%';

-- 案例3：查询员工名中第二个字符串为_的员工名
-- 方法一
SELECT 
    last_name
FROM
    employees
WHERE
    last_name LIKE '_\_%';

-- 方法二
-- escape关键词表示后面的符号为转义符
SELECT 
    last_name
FROM
    employees
WHERE
    last_name LIKE '_$_%' ESCAPE '$';

-- between and
-- 案例3：查询员工编号在100到120之间的员工信息
-- 方法一
SELECT 
    *
FROM
    employees
WHERE
    employee_id >= 100
        AND employee_id <= 120;
	
-- 方法二
SELECT 
    *
FROM
    employees
WHERE
    employee_id BETWEEN 100 AND 120;

-- in 
-- 案例4：查询员工的工种编号是IT_PROG、AD_VP、AD_PRES中的一个的员工名和工种编号
-- 方法一
SELECT 
    last_name, job_id
FROM
    employees
WHERE
    job_id = 'IT_PROG' OR job_id = 'AD_VP'
        OR job_id = 'AD_PRES';


-- 方法二
SELECT 
    last_name, job_id
FROM
    employees
WHERE
    job_id IN ('IT_PROG' , 'AD_VP', 'AD_PRES');
    

-- is null、is not null
-- 案例1：查询没有奖金的员工名和奖金率
SELECT 
    last_name, commission_pct
FROM
    employees
WHERE
    commission_pct IS NULL;
    

-- 案例2：查询有奖金的员工名和奖金率
SELECT 
    last_name, commission_pct
FROM
    employees
WHERE
    commission_pct IS NOT NULL;
    
    
-- 安全等于（<=>），判断是否等于null或者数值，如果等于返回true，但可读性很差
SELECT 
    last_name, commission_pct
FROM
    employees
WHERE
    commission_pct <=> NULL;
    

-- 练习2
-- 查询员工为176号的员工的姓名、部门号和年薪
SELECT 
    last_name,
    department_id,
    salary * 12 * (1 + IFNULL(commission_pct, 0)) AS 年薪
FROM
    employees
WHERE
    employee_id = 176;
    
-- 选择工资不在5000到12000的员工的姓名和工资 
SELECT 
    last_name, salary
FROM
    employees
WHERE
    NOT (salary BETWEEN 5000 AND 12000);
    

-- 选择姓名中有字母a和e的员工姓名 
SELECT 
    last_name
FROM
    employees
WHERE
    last_name LIKE '%a%e%';
    

-- 显示出表employees的manager_id是100,101,110 的员工姓名、职位 
SELECT 
    last_name, job_id
FROM
    employees
WHERE
    manager_id IN (100 , 101, 110);


-- 查询没有奖金，且工资小于18000的salary，last_name
SELECT 
    salary, last_name
FROM
    employees
WHERE
    salary < 18000
        AND commission_pct IS NULL;
 
 
SELECT 
    *
FROM
    employees
WHERE
    job_id != 'IT' OR salary = 12000;
    

desc departments;


SELECT DISTINCT
    location_id
FROM
    departments;
    













