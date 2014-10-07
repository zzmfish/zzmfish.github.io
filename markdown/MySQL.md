# MySQL

## 命令
```
#!bash
#导出表
mysqldump -u $User -p $Database $Table > $File

#登录
mysql -u root -p
```

## SQL语句
```
#!mysql
#所有数据库
show databases;

#进入数据库
use DatabaseName;

#数据库信息
status;

#数据库字符集设置
show variables like 'character_%';

#所有表
show tables;

#表信息
show table status;

#所有列
show columns from TableName;
```
  
## 查询语句
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
```

## mysql命令
执行sql文件：`source <sql文件名>`