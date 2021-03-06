# SQL
## 语法
### 库
```
#!mysql
#所有数据库
SHOW databases;

#进入数据库
USE DatabaseName;

#数据库信息
status;

#创建数据库
CREATE DATABASE IF NOT EXISTS TableName;

#数据库字符集设置
SHOW variables LIKE 'character_%';
```

### 表
```
#!mysql
#所有表
SHOW tables;

#所有表的信息
SHOW TABLE status;

#所有列
SHOW columns FROM TableName;

#显示表的结构
DESC TableName;

#改变列的数据类型
ALTER TABLE TableName ALTER COLUMN ColumnName DataType;

#改变默认值为当前时间
ALTER TABLE `video` MODIFY COLUMN `insert_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP;

#增加列() 
ALTER TABLE video ADD COLUMN insert_time DATETIME;
ALTER TABLE `video` add COLUMN `insert_time` timestamp NOT NULL;

#删除列
ALTER TABLE video DROP COLUMN insert_time;

#删除表
DROP TABLE IF EXISTS TableName;
```

### 插入
```mysql
INSERT INTO users(name) VALUES('周志明');
```
  
### 查询
```
#!mysql
#降序排名前10
select * from TableName ORDER BY ColumnName DESC limit 10;

#降序排名10-20
select * from TableName ORDER BY ColumnName DESC limit 10,20;

#每种取值的条目数
select ColumnName, COUNT(*) from TableName GROUP BY ColumnName;

#列的所有取值
select DISTINCT ColumnName from TableName;

#表的行数
SELECT COUNT(*) FROM TableName;

#子查询、联表
select a.id1, a.id2, b.sim_content, b.sim_beh
from (
    select regexp_extract(url, '\/(\\d+)\/\\d+$', 1) as id1, id as id2
    from video_appve
) a
left join sug_wide b
on a.id1=b.id1 and a.id2=b.id2
limit 10;
```

### 更新
```
#!mysql
update video set insert_time=now();
```

## 概念
### 联表
![](/images/sql_join.png)

## 参考
* [ROW_NUMBER() OVER函数的基本用法用法](http://www.cnblogs.com/icebutterfly/archive/2009/08/05/1539657.html)