-- 变量
/*
系统变量：
				全局变量
					作用域：服务器每次启动将为所有全局变量赋初始值，针对于所有的会话（连接）有效，但是不能跨重启
				会话变量
					作用域：仅仅针对当前会话（连接）有效

自定义变量：
				用户变量
					作用域：针对与当前会话（连接）有效，同于会话变量的作用域
					应用在任何地方，也就是begin end里面或者外面
				局部变量
					仅仅在begin end之间有效
*/


-- 一、系统变量
/*
说明：变量由系统提供，不是用户定义，属于服务器层面
注意：如果是全局级别，则需要加global，如果是会话级别，则需要加session，如果不写，默认session
使用方法：
1、查看所有的系统变量
SHOW VARIABLES;  # 查看会话变量
SHOW GLOBAL VARIABLES;  # 查看全局变量
SHOW SESSION VARIABLES;  # 查看会话变量

2、查看满足条件的部分系统变量
SHOW GLOBAL|[SESSION] VARIABLES LIKE '%char%';

3、查看指定的某个系统变量的值
SELECT @@GLOBAL|[SESSION].系统变量名;

4、为某个系统变量赋值
方式一：
SET GLOBAL|[SESSION] 系统变量名 = 值;
方式二：
SET @@GLOBAL|[SESSION].系统变量名 = 值;
*/


-- 二、自定义变量
-- 1、用户变量
/*
说明：变量是用户自定义的，不是由系统生成的
使用步骤：
	声明
	赋值
	使用（查看、比较、运算等）
*/
-- 1、声明并初始化
-- 方式一：
SET @用户名变量=值;
-- 方式二：
SET @用户名变量:=值;
-- 方式三：
SELECT @用户名变量名:=值;


-- 2、赋值（更新用户名变量的值）
-- 方式一：
SET @用户名变量=值;
SET @用户名变量:=值;
SELECT @用户名变量名:=值;
-- 方式二：
SELECT 字段 INTO @变量名 FROM 表;
	
	
-- 3、使用（查看用户变量的值）
SELECT @用户变量名;


-- 案例：
SELECT COUNT(*) INTO @count FROM employees;
SELECT @count;


-- 2、局部变量
-- 1、声明
DECLARE 变量名 类型;
DECLARE 变量名 类型 DEFAULT 值;

-- 2、赋值（注意和用户变量名的区别）
-- 方式一：
SET 局部变量=值;
SET 局部名变量:=值;
SELECT @局部变量名:=值;
-- 方式二：
SELECT 字段 INTO 局部变量名 FROM 表;

-- 3、使用
SELECT 局部变量名;


对比用户变量和局部变量
								作用域       				定义和使用位置       					            语法
用户变量				当前会话      			会话的任何位置														必须加@符号，不用限定类型
局部变量				begin end中					只能在begin end中，且为第一句话           一般不用加@符号，需要限定类型


案例：声明两个变量并赋初始值，求和，并打印
1、用户变量
SET @m = 1;
SET @n = 2;
SET @sum = @m + @n;
SELECT @sum;


2、局部变量
DECLARE m INT DEFAULT 1;
DECLARE n INT DEFAULT 2;
DECLARE sum INT;
SET sum = m + n;
SELECT sum;
