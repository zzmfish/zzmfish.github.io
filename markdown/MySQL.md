# MySQL

## 终端命令
```
#!bash
#导出表
mysqldump -u $User -p $Database $Table > $File

#登录
mysql -u root -p
```

## mysql命令
```
source FileName;
tee FileName;
```

## 数据库
```
#!mysql
#所有数据库
SHOW databases;

#进入数据库
USE DatabaseName;

#数据库信息
status;

#数据库字符集设置
SHOW variables LIKE 'character_%';
```

## 表
```
#!mysql
#所有表
SHOW tables;

#所有表的信息
SHOW TABLE status;

#所有列
SHOW columns FROM TableName;

#表的结构
DESC  TableName;
```
  
## 查询数据
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
```

## 索引
* 最左前缀匹配原则

## 未分类
* explain
* SQL_NO_CACHE