-- TCL
/*
transaction control language 事务控制语言

事务：
一个或一组语句组成一个执行单元，这个执行单元要么全部执行，要么全部不执行。
特性（ACID）：
1、原子性：指事务是一个不可分割的工作单位，事务中的操作要么都发生，要么都不发生。
2、一致性：事务必须使数据库从一个一致性状态变换到另外一个一致性状态。
3、隔离性：事务的隔离性是指一个事务的执行不能被其他事务干扰，即一个事务内部的操作及使用的数据对并发的其他						事务是隔离的，并发执行的各个事务之间不能互相干扰。
4、持久性：持久性是指一个事务一旦被提交，它对数据库中数据的改变就是永久性的，接下来的其他操作和数据库故障						不应该对其有任何影响。


事务的创建：
隐式事务：事务没有明显的开启和结束的标记
比如insert、update、delete语句

显示事务：事务具有明显的开启和结束标记
前提：必须先设置自动提交功能为禁用
语法：
	SET AUTOCOMMIT = 0; 仅对此次操作有效，下次还需要手动关闭
	
	START TRANSACTION; 事务开启语句，可写可不写
	
	编写事务中的sql语句(SELECT INSERT UPDATE DELETE);
	语句1;
	语句2;
	...
	
	STOP TRANSACTION; 事务结束
	COMMIT; 若无异常，提交事务
	ROLLBACK; 若发生异常，回滚事务
	

事务的隔离级别：
read uncommitted：出现脏读、不可重复读、幻读
read committed：避免出现脏读，无法避免不可重复读和幻读
repeatable read：避免出现脏读和不可重复读，但是无法避免幻读
serializable：全部避免
mysql中默认：repeatable read
oracle中默认：read committed

相关命令：
查看隔离级别：
mysql8.0中：
select @@transaction_isolation;
mysql5.6中：
select @@tx_isolation;

设置隔离级别：
set session|global transacton isolation level 隔离级别;
*/


SHOW ENGINES;

SHOW VARIABLES LIKE '%autocommit%'; # 查看自动提交功能状态


-- 创建事务的演示：
DROP TABLE IF EXISTS account;

CREATE TABLE account(
	id INT PRIMARY KEY AUTO_INCREMENT,
	username VARCHAR( 20 ),
	balance DOUBLE
);

INSERT INTO account ( username, balance )
VALUES
	( '张无忌', 1000 ),
	( '赵敏', 1000 );
	

-- 开启事务
SET AUTOCOMMIT = 0;
START TRANSACTION;

-- 编写一组事务的语句
UPDATE account SET balance = 500 WHERE username = '张无忌';
UPDATE account SET balance = 1500 WHERE username = '赵敏';

-- 结束事务（要么提交，要么回滚）
COMMIT;


SELECT * FROM account;


