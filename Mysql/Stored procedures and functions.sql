-- 存储过程和函数
/*
存储过程和函数：类似于java中的方法
好处：
1、提高代码的重要性
2、简化操作
*/

-- 存储过程
/*
含义：一组预先编译好的sql语句的集合，理解成批处理语句
1、提高代码的重要性
2、简化操作
3、减少了编译次数并且减少了和数据库服务器的连接次数，提高了效率
*/

-- 一、创建语法
DELIMITER $
CREATE PROCEDURE 存储过程的名字 (参数列表)
BEGIN
		存储过程体（一组合法的sql语句）
END $

/*
注意：
1、参数列表包含三部分
参数模式   参数名    参数类型
IN         stuname   VARCHAR(20)
参数模式：
IN：该参数可以作为输入，也就是说该参数需要调用方传入值
OUT：该参数可以作为输出，也就是该参数可以作为返回值
INOUT：该参数既可以作为输入又可以作为输出，也就是该参数既需要传入值，又可以返回值

2、如果存储过程体仅仅只有一句话，begin end可以省略。
   存储过程体中的每条sql语句的结尾要求必须加分号。
   存储过程体结尾可以使用delimited重新设置。
语法：
	 DELIMITER 结束标记
案例：
	 DELIMITER $
*/

-- 二、调用方法
CALL 存储过程(实参列表);


-- 案例1：插入admin表中五条记录
SELECT * FROM admin;

-- 创建
DELIMITER $
CREATE PROCEDURE myp1 () BEGIN
	INSERT INTO admin ( username, `password` )
	VALUES
		( 'john1', '0000' ),
		( 'lily', '0000' ),
		( 'rose', '0000' ),
		( 'jack', '0000' ),
		( 'tom', '0000' );
	
END $

-- 调用
CALL myp1();


-- 创建带in模式的存储过程
-- 案例2：创建存储过程实现 根据女神名，查询对应的男神信息
DELIMITER $
CREATE PROCEDURE myp2 (
	IN beautyname VARCHAR ( 20 )) BEGIN
	SELECT
		bo.* 
	FROM
		boys bo
		RIGHT JOIN beauty b ON bo.id = b.boyfriend_id 
	WHERE
		b.`name` = beautyname;
	
END $

CALL myp2('柳岩');


-- 案例3：创建存储过程，用户是否登陆成功
DELIMITER $
CREATE PROCEDURE myp4 (
	IN username VARCHAR ( 20 ),
	IN PASSWORD VARCHAR ( 20 )) BEGIN
	
	DECLARE
		result VARCHAR ( 20 ) DEFAULT 0;# 声明并初始化
		
	SELECT
		COUNT(*) INTO result # 赋值
	FROM
		admin 
	WHERE
		username = admin.`password` 
		AND PASSWORD = admin.`password`;
		
	SELECT
		IF(result > 0, '成功', '失败') AS '登陆状态'; # 使用
	
END $

CALL myp4('张飞', '8888');


-- 创建带out模式的存储过程
-- 案例4：根据女神名，返回对应的男神名
DELIMITER $
CREATE PROCEDURE myp5 (
	IN beautyname VARCHAR ( 20 ),
	OUT boyname VARCHAR ( 20 )) BEGIN
	SELECT
		bo.boyName INTO boyname 
	FROM
		boys bo
		RIGHT JOIN beauty b ON bo.id = b.boyfriend_id 
	WHERE
		b.`name` = beautyname;

END $

CALL myp5('柳岩', @bname);
SELECT @bname;


-- 案例5：根据女神名，返回对应的男神名和男神魅力值
DELIMITER $
CREATE PROCEDURE myp6 ( IN beautyname VARCHAR ( 20 ), OUT boyname VARCHAR ( 20 ), OUT userCP INT ) BEGIN
	SELECT
		bo.boyName,
		bo.userCP INTO boyname,
		usercp 
	FROM
		boys bo
		RIGHT JOIN beauty b ON bo.id = b.boyfriend_id 
	WHERE
		b.`name` = beautyname;
	
END $

CALL myp6('柳岩', @bname, @usercp);
SELECT @bname, @usercp;


-- 创建带inout模式的存储过程
-- 案例6：传入a和b两个值，最终a和b都翻倍并返回
DELIMITER $
CREATE PROCEDURE myp7(INOUT a INT, INOUT b INT)
BEGIN
SET a = 2 * a;
SET b = 2 * b;
END$

SET @m=10;
set @n=20;
CALL myp7(@m, @n);
SELECT @m, @n;


-- 二、删除存储过程
语法：DROP PROCEDURE存储过程名
DROP PROCEDURE myp1;
-- 注意：不允许同时删除多个存储过程


-- 三、查看存储过程的信息
SHOW CREATE PROCEDURE myp2;


-- 四、存储过程不允许修改，一般都是删除再创建
