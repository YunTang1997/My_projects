-- DDL
/*
数据定义语言

库和表的管理

一、库的管理
创建、修改、删除

二、表的管理
创建、修改、删除

创建：create
修改：alter
删除：drop

*/


-- 一、库的管理
-- 1、库的创建
/*
语法:
creat database [if not exists] 库名;
*/


-- 1、库的创建
-- 案例：创建库books
-- 方式一
CREATE DATABASE books;

-- 方式二（增加容错）
CREATE DATABASE IF NOT EXISTS books;


-- 2、库的修改
-- 修改库名
-- 以前的写法，现在不建议（会导致数据的丢失，可以直接关闭mysql服务，然后去data文件夹改）：
-- RENAME DATABASE books TO 新库名;

-- 更改库的字符集
ALTER DATABASE books CHARACTER 
SET gbk;


-- 3、库的删除
DROP DATABASE books;
DROP DATABASE IF EXISTS books;


-- 二、表的管理
-- 1、表的创建
/*
语法：
create table 表名(
		列名 列的类型[（长度）约束],
		列名 列的类型[（长度）约束],
		列名 列的类型[（长度）约束],
		...
		列名 列的类型[（长度）约束]
);
*/
-- 案例：创建表book
CREATE TABLE [IF NOT EXISTS] book(
				id INT, # 编号
				b_name VARCHAR(20), # 图书名
				price DOUBLE, # 价格
				authorId INT,  # 作者Id
				publishDate DATETIME # 出版日期
			
);

DESC book;


CREATE TABLE author(
				id INT,
				au_name VARCHAR(20),
				nation VARCHAR(20)
);

DESC author;


-- 2、表的修改
/*
alter table 表名 [change|modify|add|drop|rename to] column 列名 列类型 约束
修改列名
修改列的类型或约束
添加新列
删除列
修改表名
*/
ALTER TABLE book CHANGE COLUMN publishDate pubDate DATETIME; # 修改列名
DESC book;

ALTER TABLE book MODIFY COLUMN pubDate TIMESTAMP; # 修改pubDate列的类型为时间戳
DESC book;

ALTER TABLE author ADD COLUMN annual DOUBLE; # 添加新的列
DESC author;

ALTER TABLE author DROP COLUMN annual; # 列的删除
ALTER TABLE author DROP IF EXISTS annual;
DESC author;

ALTER TABLE author RENAME TO book_author; # 修改表名
DESC book_author;


-- 3、表的删除
DROP TABLE book_author;
DROP TABLE IF EXISTS book_author;


-- 通用写法：
DROP DATABASE IF EXISTS 旧库名;
CREATE DATABASE 新库名;

DROP TABLE IF EXISTS 旧表名;
CREATE DATABASE 新表名;


-- 4、表的复制
INSERT INTO book_author 
VALUES(1, '村上村树', '日本'),
(2, '莫言', '中国'),
(3, '冯唐', '中国'),
(4, '金庸', '中国');

SELECT * FROM book_author;

-- 仅仅复制表的结构
CREATE TABLE copy LIKE book_author;

-- 复制表的结构+数据
CREATE TABLE copy2 
SELECT * FROM book_author;

-- 复制表的结构+部分数据
CREATE TABLE copy3 
SELECT id, au_name 
FROM book_author 
WHERE nation = '中国';
	
-- 复制表的部分结构（where条件判断为false即可，即不选中任何数据）
CREATE TABLE copy4 
SELECT id, au_name
FROM book_author
WHERE 0;