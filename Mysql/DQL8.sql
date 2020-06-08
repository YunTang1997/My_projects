-- 进阶8：分页查询
/*
应用场景：当要显示的数据，一页显示不全，需要分页提交sql请求

语法：
		select 查询列表
		from 表
		[join type join 表2
		on 连接条件
		group by 分组字段
		having 分组后的筛选
		order by 排序的字段]
		limit offets, size;
		
		offest:要显示的目的其实索引（起始索引从0开始，注意在其他情况下索引从1开始）
		size：要显示的条目个数
		
特点：
		1、limit语句放在查询语句的最后
		2、公式：要显示的页数page，每页的条目数size
				
			select 查询列表
			from 表
			limit (page - 1) * size, size;
			
			size=10
			page		每一页开始索引
			1       0			
			2				10
			3				20
		
*/


-- 案例1：查询前五条员工信息
SELECT
	* 
FROM
	employees 
	LIMIT 0,
	5;


SELECT
	* 
FROM
	employees 
	LIMIT 5;


案例2：查询第11条到第25条
SELECT
	* 
FROM
	employees 
	LIMIT 10,
	15;
	
	
-- 案例3：有奖金的员工信息，并且工资较高的前10名
SELECT
	* 
FROM
	employees 
WHERE
	commission_pct IS NOT NULL 
ORDER BY
	salary DESC 
	LIMIT 10;




