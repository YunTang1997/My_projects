-- 进阶4：常见的函数
/*
概念：类似于python中的方法，将一组逻辑语句封装在方法体中，对外暴露方法名

好处：
1、隐藏了实现的具体细节
2、提高代码的重用性

调用：
SELECT 
    函数名(实参列表)
[FROM
    表];
    
特点：
1、叫什么（函数名）
2、干什么（函数功能）

分类：
1、单行函数，如：cancat、length、ifnull等
2、分组函数（功能做统计使用，又称为统计函数、聚合函数、组函数）

常见函数：
		字符函数：
        length
        concat
        substr
        instr
        trim
        upper
        lower
        lpad
        rpad
        replace
        
        数学函数：
        round
        ceil
        floor
        truncate
        mod
        
        日期函数：
        now
        curdate
        curtime
        year
        month
        monthname
        day
        hour
        minute
        second
        str_to_date
        date_format
				datediff
        
        其它函数：
        version
        database
        user
				password
				MD5
        
        控制函数：
        if 
        case
*/

-- 1、字符函数

-- length  获取参数值的字节个数
SELECT length('john');
SELECT length('张三丰');

-- utf8一个字母占一个字节，一个汉字占3个字节
SHOW VARIABLES LIKE '%char%';


-- concat 拼接字符串
SELECT 
    CONCAT(last_name, '_', first_name) AS '姓名'
FROM
    employees;
    

-- upper、lower
SELECT UPPER('john');

SELECT LOWER('joHn');

-- 示例：将姓变大写，名变小写，然后拼接
SELECT 
    CONCAT(UPPER(last_name), '_', LOWER(first_name)) AS '姓名'
FROM
    employees;
    
    
-- substr、substring
-- mysql中索引从1开始

-- 截取从指定索引处后面的所有字符
SELECT substr('李莫愁爱上了陆展元', 7) out_put;

-- 截取从指定索引处指定字符长度的字符
SELECT substr('李莫愁爱上了陆展元', 1, 3) out_put;


-- 案例：姓名中首字母大写，其它字符小写然后用_拼接，显示出来
SELECT 
    CONCAT(UPPER(SUBSTR(last_name, 1, 1)),
            '_',
            LOWER(SUBSTR(last_name, 2))) AS '姓名'
FROM
    employees;
    

-- instr 返回子串第一次出现的索引，如果找不到返回0
SELECT 
    INSTR('杨不悔爱上了殷六侠',
            '殷六侠') AS out_put;
    
    
-- trim 去掉前、尾相应的字符
SELECT LENGTH(TRIM('   张翠山    ')) AS out_put;

SELECT TRIM('a' FROM 'aaaaaaaaaaaaaaaaaa张aaaaa翠山aaaaaaaaaaaaaa') AS out_put;


-- lpad 用指定的字符实现左填充指定的长度（不是字节数）
SELECT LPAD('殷素素', 10, '*') AS out_put;

-- 如果给定的字符数超过了要求的字符数，就会从右边截断到相应的字符数
SELECT LPAD('殷素素', 2, '*') AS out_put;


-- rpad 用指定的字符实现右填充指定的长度（不是字节数）
SELECT RPAD('殷素素', 10, '*') AS out_put;

SELECT RPAD('殷素素', 2, '*') AS out_put;


-- replace 替换
SELECT 
    REPLACE('张无忌爱上了周芷若',
        '周芷若',
        '赵敏') AS out_put;


-- 2、数学函数

-- round 四舍五入
SELECT ROUND(1.45);

SELECT ROUND(- 1.55);

SELECT ROUND(1.567, 2);


-- ceil 向上取整，返回>=该参数的最小整数
SELECT CEIL(1.45);

SELECT CEIL(- 1.65);


-- floor 向下取整，返回<=该参数的最大整数
SELECT floor(-9.99);


-- truncate 截断
SELECT TRUNCATE(1.69999, 1);


-- mod 取余
-- mod(a, b): a-a/b*b
SELECT MOD(-10, -3);

SELECT 10 % 3;


-- 3、日期函数

-- now 返回当前系统日期+时间
SELECT NOW();


-- curdate 返回当前系统日期，不包含时间
SELECT CURDATE();


-- curtime 返回当前时间，不包含日期
SELECT CURTIME();


-- 可以指获取指定的部分，年、月、日、小时、分钟、秒
SELECT YEAR(NOW()) AS 年;

SELECT year('1988-1-1') as 年;

SELECT 
    YEAR(hiredate)
FROM
    employees;
    

SELECT MONTH(NOW()) AS 月;
SELECT MONTHNAME(NOW()) AS 月;


-- str_to_date 将字符通过指定的格式转换为日期
SELECT STR_TO_DATE('1988-3-2', '%Y-%c-%d') AS out_put;

-- 查询入职信息为1992-4-3的员工信息
SELECT 
    *
FROM
    employees
WHERE
    hiredate = STR_TO_DATE('4-3 1992', '%c-%d %Y');
    

-- data_format将日期转化为字符
SELECT DATE_FORMAT(NOW(), '%y年%m月%d日') AS out_put;


-- 查询有奖金的员工名和入职日期（xx月/xx日 xx年）
SELECT 
    last_name AS '员工名',
    DATE_FORMAT(hiredate, '%m月/%d日 %Y年') AS '入职日期'
FROM
    employees
WHERE
    commission_pct IS NOT NULL;
    

-- 4、其它函数

SELECT VERSION();

SELECT DATABASE();

SELECT USER();


-- 5、流程控制函数

-- .if 函数：if else 的效果
SELECT IF(10 < 5, '大', '小');

SELECT 
    last_name,
    commission_pct,
    IF(commission_pct IS NULL,
        '没奖金',
        '有奖金') AS 备注
FROM
    employees;
    
    
-- case函数的使用一：switch case 的效果
/*
java中：
switch(变量或表达式){
case 常量1：语句1; break;
...
default:语句n; break;
}

mysql中：
case 要判断的字段或表达式
when 常量1 then 要显示的值1或语句1;（如果是值就不用加;，如果是表达式就需要加;）
when 常量2 then 要显示的值2或语句2;
...
else 要显示的值n或语句n;
end
*/

/*案例：查询员工的工资，要求：
部门号=30，显示的工资为1.1倍
部门号=40，显示的工资为1.2倍
部门号=50，显示的工资为1.3倍
其他部门，显示的工资为原工资
*/
SELECT 
    salary AS '原始工资',
    department_id,
    CASE department_id
        WHEN 30 THEN salary * 1.1
        WHEN 40 THEN salary * 1.2
        WHEN 50 THEN salary * 1.3
        ELSE salary
    END AS '新工资'
FROM
    employees;

-- case 函数的使用二：类似于 多重if
/*
case 
when 条件1 then 要显示的值1或者语句1;
when 条件2 then 要显示的值2或者语句2;
...
else 要显示的值或者语句;
end
*/

-- 案例：查询员工的工资的情况
/*
如果工资>20000,显示A级别
如果工资>15000,显示B级别
如果工资>10000,显示C级别
否则，显示D级别
*/
SELECT 
    salary AS '工资',
    CASE
        WHEN salary > 20000 THEN 'A'
        WHEN salary > 15000 THEN 'B'
        WHEN salary > 10000 THEN 'C'
        ELSE 'D'
    END AS '工资等级'
FROM
    employees;
    

-- 练习
SELECT NOW();


SELECT 
    employee_id AS '员工号',
    last_name AS '姓名',
    salary AS '工资',
    salary * 1.2 AS 'NEW salary'
FROM
    employees;
    
SELECT 
    last_name, LENGTH(last_name) AS '名字的长度'
FROM
    employees
ORDER BY SUBSTR(last_name, 1, 1) ASC;


SELECT 
    CONCAT(last_name,
            ' earns ',
            salary,
            ' monthly but wants ',
            salary * 3) AS 'dream salary'
FROM
    employees;


SELECT 
    last_name,
    job_id AS 'job',
    CASE job_id
        WHEN 'AD_PRES' THEN 'A'
        WHEN 'ST_MAN' THEN 'B'
        WHEN 'IT_PROG' THEN 'C'
        WHEN 'SA_PRE' THEN 'D'
        WHEN 'ST_CLERK' THEN 'E'
        ELSE job_id
    END AS 'grade'
FROM
    employees
WHERE
    job_id = 'AD_PRES';
    
    

    











    
