-- 流程控制结构
/*
顺序结构：程序从上往下依次执行
分支结构：程序从两条或多条路径中选择一条去执行
循环结构：程序在满足一定条件的基础上，重复执行一段代码
*/


-- 一、分支结构
-- 1、if结构
/*
功能：
	实现简单的双支结构
语法：
	IF (表达式1, 表达式2， 表达式3)
执行顺序：
	如果表达式1成立，则IF函数返回表达式2的值，否则返回表达式3的值
应用场景：
	任何地方
*/

/*
功能：
	实现多重分支
语法：
	IF 条件1 THEN 语句1;
	ELSEIF 条件2 THEN 语句2;
	...
	[ELSE 语句n;]
	END IF;
应用场景：
	begin end中
*/


-- 2、case结构
/*
情况1：
	类似于java中switch语句，一般用于实现的等值判断
语法1：
	CASE 变量|表达式|字段
	WHERE 要判断的值 THEN 返回的值1
	WHERE 要判断的值 THEN 返回的值2
	...
	ELSE 要返回的值n
	END;

语法2：
	CASE 变量|表达式|字段
	WHERE 要判断的值 THEN 返回的语句1;
	WHERE 要判断的值 THEN 返回的语句2；
	...
	ELSE 要返回的语句n;
	END CASE;


情况2：
	类似于java中的多重IF语句，一般用于实现区间判断
语法1：
	CASE 
	WHERE 要判断的条件1 THEN 返回的值1
	WHERE 要判断的条件2 THEN 返回的值2
	...
	ELSE 要返回的值n
	END;

语法2：
	CASE 
	WHERE 要判断的条件1 THEN 返回的语句1;
	WHERE 要判断的条件2 THEN 返回的语句2;
	...
	ELSE 要返回的语句n;
	END CASE;
	
	
特点：
	可以作为表达式（语法1），嵌套在其他语句中使用，可以放在任何地方，begin end中或begin end的外面
	可以作为独立的语句（语法2），只能放在begin end中
	如果when中的值满足或条件成立，则执行对应的then后面的语句，并且结束case；如果都不满足，则执行else中的语句或值
	else可以省略，如果else省略了，并且所有的when语句都不满足，则返回null
*/


-- 案例1：创建存储过程，根据传入的成绩，来显示等级，比如传入的成绩：90-100，显示A，80-90，显示B，60-80，显示C，否则，显示D（case作为独立的语句）
DELIMITER $
CREATE PROCEDURE test_case(IN score INT)
BEGIN
	CASE
	WHEN score >= 90 AND score <= 100 THEN SELECT 'A';
	WHEN score >= 80 THEN SELECT 'B';
	WHEN score >= 60 THEN SELECT 'C';
	ELSE SELECT 'D';
	END CASE;
end $

CALL test_case(95);


-- 案例2：创建存储过程，根据传入的成绩，来显示等级，比如传入的成绩：90-100，显示A，80-90，显示B，60-80，显示C，否则，显示D（if实现多重分支结构）
DELIMITER $
CREATE FUNCTION test_if ( score INT ) RETURNS CHAR BEGIN
	IF score >= 90 AND score <= 100 THEN RETURN 'A'; 
		ELSEIF score >= 80 THEN RETURN 'B';
		ELSEIF score >= 60 THEN RETURN 'C';
		ELSE RETURN 'D';
	END IF; 
END $
	
SELECT test_if(86);


-- 二、循环结构
/*
分类：
	while、loop、repeat
循环控制：
	iterate类似于continue，结束本次循环，继续下一次
	leave 类似于break，结束当前循环
*/

/*
while语法：
	[标签:]WHILE 循环条件 DO
		循环体;
	END WHILE[标签];
*/

/*
loop语法：
	[标签:]LOOP
		循环体;
	END LOOP[标签];

可以用来模拟简单的死循环
*/

/*
repeat语法：
	[标签:]REPEAT
		循环体;
	UNTIL 结束循环的条件;
	END REPEAT[标签];
*/


-- 案例1：批量插入，根据次数插入到admin表中多条记录
DELIMITER $
CREATE PROCEDURE pro_while ( IN insertcount INT ) BEGIN
	DECLARE
		i INT DEFAULT 1;
	WHILE
			i <= insertcount DO
			INSERT INTO admin ( username, `password` )
		VALUES
			( CONCAT('Rose', i), '666' );
			SET i = i + 1;
	END WHILE;
END$

CALL pro_while(100);

SELECT * FROM admin;


-- 案例2：批量插入，根据次数插入到admin表中多条记录，如果次数超过次数>20则停止
DELIMITER $ 
CREATE PROCEDURE pro_while1(IN insertcount INT) 
BEGIN
	SET @i=1;
	a:WHILE @i <= insertcount DO
		INSERT INTO admin(username, `password`) VALUES(CONCAT('Tom', @i), '888');
		IF @i >= 20 THEN LEAVE a;
		END IF;
		SET @i = @i + 1;
	END WHILE a;
END$

CALL pro_while1(100);

SELECT * FROM admin;


-- 案例2：批量插入，根据次数插入到admin表中多条记录，偶数次不插入，奇数次插入
TRUNCATE TABLE admin;
DELIMITER $
CREATE PROCEDURE pro_while3(IN insertcount INT)
BEGIN
SET @i=-1;
a:WHILE @i <= insertcount DO
		SET @i = @i + 1;
		IF @i % 2 = 0 THEN ITERATE a;
		END IF;
		INSERT INTO admin(username, `password`) VALUES(CONCAT('Lucy', @i), '999');
	END WHILE a;
END$

CALL pro_while3(100);

SELECT * FROM admin;


-- 经典案例：已知表 stringcontent，其中字段：id 自增长， content varchar(20)，向该表插入指定个数的，随机的连续字符串
DROP TABLE stringcontent;
CREATE TABLE IF NOT EXISTS stringcontent (
	id INT PRIMARY KEY AUTO_INCREMENT,
	content VARCHAR ( 26 )
);


DELIMITER $
CREATE PROCEDURE test_randstr_insert(IN insertcount INT)
BEGIN
	DECLARE i INT DEFAULT 1; # 定义一个循环变量i，表示插入的次数
	DECLARE str VARCHAR(26) DEFAULT 'abcdefghijklmnopqrstuvwxyz';
	DECLARE startindex INT DEFAULT 1; # 代表起始索引
	DECLARE len INT DEFAULT 1; # 代表截取的字符的长度
	WHILE i <= insertcount DO
		SET startindex = FLOOR(RAND() * 26 + 1); # 产生一个随机的整数，代表起始索引1->26
		SET len = FLOOR(RAND() * (26 - startindex + 1) + 1); # 产生一个随机整数，代表截取长度，1->(26 - startindex + 1)
		INSERT INTO stringcontent(content) VALUES(SUBSTR(str, startindex, len));
		SET i = i + 1;
	END WHILE;
END$


CALL test_randstr_insert(10);
SELECT * FROM stringcontent;
