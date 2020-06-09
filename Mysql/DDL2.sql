-- 常见的数据类型
/*
数值型：
			整数
			小数：
					定点数
					浮点数
					
字符型：
			比较短的文本：char、varchar
			比较长的文本：text、blob(较长的二进制数)

日期型：
*/

-- 一、整型
/*
分类：
tinyint, smallint, mediumint, int/integer, bigint
1        2         3          4            8

特点：
1、如果不设置无符号还是有符号，默认是有符号，如果想设置无符号，需要添加unsigned关键字
2、如果插入的数值超出了整型的范围，会报Out of range，并且有些版本数据库会插入临界值，有些版本不会
3、如果不设置长度，会有默认长度，长度代表的是显示的最大宽度，如果不够会用0在左边填充，需要用到zerofill关键字，使用了它之后默认为无符号型
*/

-- 1、如何设置无符号和有符号
CREATE TABLE tab_int(
	t1 INT(7) ZEROFILL,
	t2 INT(7) ZEROFILL
);

DESC tab_int;

INSERT INTO tab_int VALUES(-123456);
INSERT INTO tab_int VALUES(-123456, -123456);
INSERT INTO tab_int VALUES(2147483648, 4294967296);
INSERT INTO tab_int VALUES(123, 123);

SELECT * FROM tab_int;

DROP TABLE IF EXISTS tab_int;


-- 二、小数
/*
分类：
1、浮点型
float(M,D)
double(M,D)
2、定点型
dec(M,D)
decimal(M,D)

特点：
1、M和D
M：整数部位+小数部位的有效数字为M
D：小数部位的有效数字（超出会四舍五入）
如果超过有些版本数据库会插入临界值，有些版本不会

2、M和D都可以省略
如果是decimal，则M默认为10，D默认为0
如果是float和double，则会根据插入的数值的精度来决定精度

3、定点型的精度较高，如果要求插入数值精度较高，如货币运算等则考虑用定点型
*/
DROP TABLE IF EXISTS tab_float;

CREATE TABLE tab_float(
	f1 FLOAT(5,2),
	f2 DOUBLE(5,2),
	f3 DECIMAL(5,2)
);

DESC tab_float;

INSERT INTO tab_float VALUES(123.45, 123.45, 123.45);
INSERT INTO tab_float VALUES(123.456, 123.456, 123.456);
INSERT INTO tab_float VALUES(123.4, 123.4, 123.4);
INSERT INTO tab_float VALUES(1523.4, 1523.4, 1523.4);

SELECT * FROM tab_float;


-- 整型和浮点型选用原则
/*
所选择的类型越简单越好，能保存数值的类型越小越好
*/


-- 三、字符型
/*
较短的文本：
char（固定长度的字符）
varchar（可变长度的字符）

特点：
					写法					M的意思								       特点							空间消耗			效率
char			char(M)   		最大字符数（默认为1可省略）  固定长度的字符		比较消耗			高
vachar		varchar(M) 		最大字符数 （不可省略）      可变长度的字符   比较节省      低

其他：
binary和varbinary用于保存较短的二进制
enum用于保存枚举
set用于保存集合


较长的文本：
text
blob（较大的二进制数）

*/


-- 枚举型（一次只能插入列表中的一个元素）
CREATE TABLE tab_char(
	c1 ENUM('a', 'b', 'c')
);

INSERT INTO tab_char VALUES('a');
INSERT INTO tab_char VALUES('b');
INSERT INTO tab_char VALUES('c');
INSERT INTO tab_char VALUES('d');
INSERT INTO tab_char VALUES('A'); # 不区分大小写
SELECT * FROM tab_char;


-- set型（一次能插入列表中的多个元素）
CREATE TABLE tab_set(
	s1 SET('a', 'b', 'c', 'd')
);

INSERT INTO tab_set VALUES('a');
INSERT INTO tab_set VALUES('A,B'); # 不区分大小写
INSERT INTO tab_set VALUES('a,c,d');
SELECT * FROM tab_set;


-- 四、日期型
/*
分类：
date 只保存日期
time 只保存时间
year 只保存年

datetime 保存日期+时间
timestamp 保存日期+时间

特点：
							字节     	范围     			时区的影响
datetime			8					1000-9999 		不受
timestam 			4					1970-2038  		受
*/

CREATE table tab_date(
	t1 DATETIME,
	T2 TIMESTAMP
);

INSERT INTO tab_date VALUES(NOW(), NOW());
SELECT * FROM tab_date;

SHOW VARIABLES LIKE 'time_zone'; # 查看时区
SET time_zone = '+9:00';  # 更改时区为东九区
