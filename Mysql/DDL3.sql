-- 常见约束
/*
含义：一种限制，用于限制表中的数据，为了保证表中的数据的准确和可靠性

分类：六大约束
			not null：非空，用于保证该字段的值不能为空，比如：姓名、学号等
			default:默认，用于保证该字段有默认值，比如：性别
			primary key：主键，用于保证该字段的值具有唯一性，并且非空，比如：学号、员工编号等
			unique：唯一，用于保证该字段的值具有唯一性，可以为空，比如：座位号
			check：检查约束[mysql中不支持]
			foreign key：外键，用于限制两个表的关系，用于保证该字段的值必须来自于主表的关联列的值
										在从表添加外键约束，用于引用主表中某些列的值

添加约束的时机：
			1、创建表时
			2、修改表时


约束的添加分类：
			列级约束：六大约束在语法上都支持，但外键约束没有效果
			表级约束：除了非空、默认，其它的都支持


主键和唯一的大对比：
				保证唯一性   是否允许为空    一个表中是否可以有多个         是否允许组合
主键        是          不允许             至多一个                  是（不推荐）
唯一        是           允许              可以有多个                是（不推荐）


外键：
			1、要求在从表设置外键关系
			2、从表的外键列的类型和主表的关联列的类型要求一致或兼容
			3、主表的关联列必须是一个key（一般是主键或唯一键）
			4、插入数据时，先插入主表，再插入从表；删除数据时，先删除从表，在删除主表


可以同时加入多个约束，用空格隔开即可
*/


CREATE TABLE 表名(
	字段名 字段类型 列级约束,
	字段名 字段类型,
	表级约束
)


-- 一、创建表时添加约束
-- 1、添加列级约束
/*
直接在字段名和类型后面追加约束类型即可
只支持：默认、非空、主键、唯一
*/


CREATE TABLE stuinfo (
	id INT PRIMARY KEY,# 主键
	stuname VARCHAR ( 20 ) NOT NULL,# 非空
	gender CHAR ( 1 ) CHECK ( gender = '男' OR gender = '女' ),# 检查（不支持）
	seat INT UNIQUE,# 唯一
	age INT DEFAULT 18,# 默认
	majorid INT # 外键
	
);
DESC stuinfo;


CREATE TABLE major ( id INT PRIMARY KEY, majorname VARCHAR ( 20 ) );
DESC major;

-- 查看表中主键、外键、唯一键生成的索引，可以和desc命令结合一起看表的结构
SHOW INDEX FROM stuinfo;


-- 2、添加表级约束
/*
语法：在各个字段的最下面
[constraint 约束名] 约束类型(字段名)

*/
CREATE TABLE stuinfo_new (
	id INT,
	stuname VARCHAR ( 20 ),
	gender CHAR ( 1 ),
	seat INT,
	age INT,
	majorid INT,
	CONSTRAINT pk PRIMARY KEY ( id ),# 主键（mysql主键名改不了，永远是primary）
	CONSTRAINT uq UNIQUE ( seat ),# 唯一
	CONSTRAINT ck CHECK ( gender = '男' OR gender = '女' ),# 检查
	CONSTRAINT fk_stuinfo_major FOREIGN KEY ( majorid ) REFERENCES stuinfo ( id ) # 外键
	
);

SHOW INDEX FROM stuinfo_new;


-- 通用写法
CREATE TABLE stuinfo (
	id INT PRIMARY KEY,
	stuname VARCHAR ( 20 ) NOT NULL,
	gender CHAR ( 1 ),
	age INT DEFAULT 18,
	seat INT UNIQUE,
	majorid INT,
	CONSTRAINT fk_stuinofo_major FOREIGN KEY ( majorid ) REFERENCES major ( id ) 
);


-- 二、修改表时添加约束
/*
1、添加列级约束（语法）不支持约束名：
alter table 表名 modify columns 字段名 字段类型 新约束;
2、添加表级约束（语法）支持约束名：
alter table 表名 add [constraint 约束名] 约束类型(字段名) [外键引用];
*/
DROP TABLE IF EXISTS stuinfo;
CREATE TABLE stuinfo(
	id INT,
	stuname VARCHAR(20),
	gender CHAR(1),
	seat INT,
	age INT,
	majorid INT
);
DESC stuinfo;

-- 1、添加非空约束
ALTER TABLE stuinfo MODIFY COLUMN stuname VARCHAR ( 20 ) NOT NULL;
DESC stuinfo;

-- 2、添加默认约束
ALTER TABLE stuinfo MODIFY COLUMN age INT DEFAULT 18;
DESC stuinfo;

-- 3、添加主键
-- 列级约束
ALTER TABLE stuinfo MODIFY COLUMN id INT PRIMARY KEY;
DESC stuinfo;
-- 表级约束
ALTER TABLE stuinfo ADD PRIMARY KEY ( id );

-- 4、唯一键
-- 列级约束
ALTER TABLE stuinfo MODIFY COLUMN seat INT UNIQUE;
DESC stuinfo;
-- 表级约束
ALTER TABLE stuinfo ADD UNIQUE ( seat );

-- 5、添加外键
-- 仅仅支持表级约束
ALTER TABLE stuinfo ADD FOREIGN KEY ( majorid ) REFERENCES major ( id );


-- 三、修改表时删除约束
-- 1、删除非空约束
ALTER TABLE stuinfo MODIFY COLUMN stuname VARCHAR ( 20 ) NULL;

-- 2、删除默认约束
ALTER TABLE stuinfo MODIFY COLUMN age INT;

-- 3、删除主键
ALTER TABLE stuinfo DROP PRIMARY KEY;

-- 4、删除唯一
ALTER TABLE stuinfo FROM INDEX seat;

-- 5、删除外键约束
ALTER TABLE stuinfo DROP FOREIGN KEY majorid;





