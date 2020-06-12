-- 标识列
/*
又称为自增长列
含义：可以不用手动的插入值，系统提供默认的序列值

特点：
1、标识列必须和主键搭配吗？
	不一定，但是要求为一个key
2、一个表中可以有多个标识列吗？
	至多一个标识列
3、标识列的类型
	只能是数值型
4、标识列可以通过SET auto_increment_increment = 3设置步长
	可以通过手动插入值，设置起始
*/


-- 一、创建表时设置标识列
DROP TABLE IF EXISTS tab_identity;

CREATE TABLE tab_identity ( 
	id INT PRIMARY KEY AUTO_INCREMENT, # 创建标识列
	NAME VARCHAR ( 20 ) 
);

TRUNCATE TABLE tab_identity;

INSERT INTO tab_identity VALUES(NULL, 'john');

SELECT * FROM tab_identity;

SHOW VARIABLES LIKE '%auto_increment%'; # 查看自增长步长和偏移量（有些版本不支持）

SET auto_increment_increment = 3; # 设置自增长步长为3


-- 二、修改表时设置标识列
ALTER TABLE tab_identity MODIFY COLUMN id INT PRIMARY KEY AUTO_INCREMENT;


-- 三、修改表时删除标识列
ALTER TABLE tab_identity MODIFY COLUMN id INT PRIMARY KEY;
