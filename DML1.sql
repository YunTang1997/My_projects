-- DML语言
/*
数据操作语言：
插入：insert
修改：update
删除：delete
*/

-- 一、插入语言
-- 方式一（经典方式）
/*
语法：
insert into 表名(列名, ...) values(值,...)
*/

-- 1、插入的值的类型要与列的类型一致或者兼容
INSERT INTO beauty ( id, `name`, sex, borndate, phone, photo, boyfriend_id )
VALUES
	( 13, '唐艺昕', '女', '1990-4-23', '18999999999', NULL, 2 );


-- 2、不可以为null值的列必须插入值。可以为null值的列如何插入值？
-- 方式一
INSERT INTO beauty ( id, `name`, sex, borndate, phone, photo, boyfriend_id )
VALUES
	( 13, '唐艺昕', '女', '1990-4-23', '18999999999', NULL, 2 );

-- 方式二
INSERT INTO beauty ( id, `name`, phone )
VALUES
	( 14, '娜扎', '1389999999' );


-- 3、列的顺序是否可以调换
INSERT INTO beauty ( `name`, sex, id, phone )
VALUES
	( '蒋欣', '女', 16, 110 );
	

-- 4、列数和值的个数必须一致


-- 5、可以省略列名，默认所有列，而且列的顺序和表中列的顺序一致
INSERT INTO beauty
VALUES
	( 18, '张飞', '男', NULL, '119', NULL, NULL );
	
	
-- 方式二
/*
语法：
insert into 表名
set 列名=值, 列名=值, ...
*/

INSERT INTO beauty 
SET id = 19,
`name` = '刘涛',
phone = '999';


-- 两种方式的差异
-- 1、方式一支持插入多行，方式二不支持
INSERT INTO beauty
VALUES
	( 23, '唐艺昕1', '女', '1990-4-23', '18999999999', NULL, 2 ),
	( 24, '唐艺昕2', '女', '1990-4-23', '18999999999', NULL, 2 ),
	( 25, '唐艺昕3', '女', '1990-4-23', '18999999999', NULL, 2 );


-- 2、方式一支持子查询，方式二不支持
INSERT INTO beauty ( id, `name`, phone ) 
SELECT 26, '宋茜', '118';


INSERT INTO beauty(id, `name`, phone)
SELECT id, boyName, '1234567'
FROM boys WHERE id < 3;


-- 二、修改语句
/*
1、修改单表的记录（重要）
语法：
update 表名
set 列=新值, 新值, ...
where 筛选条件;

2、修改多表的记录（补充）
语法：
sql92语法： 
update 表1 别名, 表2 别名
set 列=值, ...
where 连接条件
and 筛选条件;

sql99语法：
update 表1 别名
inner|left|right join 表2, 别名
on 连接条件
set 列=值, ...
where 筛选条件;
*/


-- 1、修改单表的记录
-- 案例1：修改beauty表中姓唐的女神电话为1389988899

UPDATE beauty 
SET phone = '1389988899' 
WHERE
	`name` LIKE '唐%';


案例2：修改boys表中id号为2的姓名为张飞，魅力值为10
UPDATE boys 
SET boyName = '张飞',
userCP = 10 
WHERE
	id = 2;
	
	
-- 2、修改多表的记录
-- 案例一：修改张无忌的女朋友的手机号为144
UPDATE boys AS bo
INNER JOIN beauty AS b ON b.boyfriend_id = bo.id 
SET b.phone = '144' 
WHERE
	bo.boyName = '张无忌';
	
	
-- 案例二：修改没有男朋友的女神的男朋友编号都为2
UPDATE beauty AS b
LEFT JOIN boys AS bo ON b.boyfriend_id = bo.id 
SET b.boyfriend_id = 2 
WHERE
	bo.id IS NULL;
	
	
-- 三、删除语句
/*
方式一：delete （删除满足条件的全部行）
语法：
1、单表的删除（重要）
delete from 表名 where 筛选条件;

2、多表的删除
sql92语法：
delete 表1(别名), 表2(别名)
from 表1 别名, 表2 别名
where 连接条件
and 筛选条件;

sql99语法：
delete 表1(别名), 表2(别名)
from 表1 别名 inner|left|right join 表2 别名 on 连接条件
where 筛选条件


方式二：truncate（不能与where连用，使用会删除整张表）
语法：truncate table 表名;
*/

-- 方式一：delete
-- 1、单表的删除
-- 案例1：删除手机号以9结尾的女生信息
DELETE 
FROM
	beauty 
WHERE
	phone LIKE '%9';
	

-- 2、多表删除
-- 案例1：删除张无忌的女朋友的信息
DELETE b
FROM
	beauty AS b
	INNER JOIN boys AS bo ON bo.id = b.boyfriend_id 
WHERE
	bo.boyName = '张无忌';


-- 案例2：散出黄晓明的信息以及他女朋友的信息
DELETE b,
bo 
FROM
	beauty AS b
	INNER JOIN boys AS bo ON b.boyfriend_id = bo.id 
WHERE
	bo.boyName = '黄晓明';


-- 方式二：truncat语句
-- 案例：将魅力值>100的男神信息删除


-- 两种方法pk（面试题）
/*
1、delete 可以添加where条件，trunncat不行
2、truncat删除，效率要高
3、假如要删除表中有自增长列，
	如果用delete删除后，再插入数据，自增长列的值从断点开始，
	而truncat删除后，再插入数据，自增长列的值从1开始
4、truncat删除没有返回值（不返回几行受影响），delete删除有返回值
5、truncat删除不能回滚，delete删除可以回滚

*/