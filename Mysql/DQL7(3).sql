-- 一、查询每个专业的学生人数
SELECT
	majorid,
	COUNT(*) 
FROM
	student 
GROUP BY
	majorid;
	
	
-- 二、查询参加考试的学生中，每个学生的平均分、最高分
SELECT
	student.studentno,
	ROUND( AVG( score ), 1 ),
	MAX( score ) 
FROM
	student
	INNER JOIN result ON student.`studentno` = result.`studentno` 
GROUP BY
	student.`studentno`;
	
	
-- 三、查询姓张的每个学生的最低分大于60的学号、姓名
-- 方法一
SELECT studentno, studentname
FROM student
WHERE studentname LIKE '张%';


SELECT
	new_t.studentno,
	studentname 
FROM
	( SELECT studentno, studentname FROM student WHERE studentname LIKE '张%' ) new_t
	INNER JOIN result r ON new_t.`studentno` = r.`studentno` 
GROUP BY
	new_t.studentno 
HAVING
	MIN( score ) > 60;


-- 方法二
SELECT
	s.studentno,
	s.studentname 
FROM
	student s
	INNER JOIN result r ON s.`studentno` = r.`studentno` 
WHERE
	s.studentname LIKE '张%' 
GROUP BY
	s.studentno 
HAVING
	MIN( score ) > 60;


-- 四、查询专业生日在“1988-1-1”后的学生姓名、专业名称
SELECT
	studentname,
	majorname 
FROM
	student s
	INNER JOIN major m ON s.`majorid` = m.`majorid` 
WHERE
	DATEDIFF( borndate, '1988-1-1' ) > 0;
	
	
-- 五、查询每个专业的男生人数和女生人数分别是多少
-- 方法一：
SELECT  COUNT(*), sex, majorid
FROM student
GROUP BY majorid, sex;


-- 方法二：
SELECT
	majorid,
	( SELECT COUNT(*) FROM student WHERE sex = '男' AND majorid = s.`majorid` ) '男',
	( SELECT COUNT(*) FROM student WHERE sex = '女' AND majorid = s.`majorid` ) '女' 
FROM
	student s 
GROUP BY
	s.majorid;
	
	
-- 六、查询专业和张翠山一样的学生的最低分
SELECT majorid 
FROM student
WHERE studentname = '张翠山';



SELECT studentno
FROM student
WHERE majorid = (SELECT majorid 
FROM student
WHERE studentname = '张翠山');


SELECT
	MIN( score ) 
FROM
	result 
WHERE
	studentno IN (
	SELECT
		studentno 
	FROM
		student 
WHERE
	majorid = ( SELECT majorid FROM student WHERE studentname = '张翠山' ));
	
	
-- 七、查询大于60分的学生的姓名、密码、专业名
SELECT studentno
FROM result
WHERE score > 60;


SELECT s.studentname, loginpwd, majorname
FROM student s
INNER JOIN major m
ON s.`majorid` = m.`majorid`
WHERE studentno IN (SELECT studentno
FROM result
WHERE score > 60);


-- 八、按邮箱位数分组，查询每组的学生个数
SELECT
	COUNT(*),
	LENGTH( email ) 
FROM
	student 
GROUP BY
	LENGTH( email );
	

-- 九、查询学生名、专业名、分数
SELECT
	s.studentname,
	majorname,
	score 
FROM
	student s
	INNER JOIN major m ON s.`majorid` = m.`majorid`
	LEFT JOIN result r ON s.`studentno` = r.`studentno`;
	

-- 十、查询哪个专业没有学生，分别用左连接和右连接实现
SELECT
	majorname 
FROM
	major m
	LEFT JOIN student s ON m.`majorid` = s.`majorid` 
WHERE
	s.`studentno` IS NULL;
	
	
SELECT
	majorname 
FROM
	student s
	RIGHT JOIN major m ON m.`majorid` = s.`majorid` 
WHERE
	s.`studentno` IS NULL;
	
	
-- 十一、查询没有成绩的学生人数
SELECT
	COUNT(*) 
FROM
	student s
	LEFT JOIN result r ON s.`studentno` = r.`studentno` 
WHERE
	r.`id` IS NULL;

