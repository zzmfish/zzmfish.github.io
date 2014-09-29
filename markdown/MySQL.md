# MySQL
## 命令
导出表：`mysqldump -u <用户名> -p <库名> <表名> > <文件名>`  
登录：`mysql -u root -p`

## SQL语句
列出数据库：`show databases`  
选择数据库：`use <数据库名>`  
显示数据库信息：`status`  
显示数据库字符集设置：`show variables like 'character_%'`  
列出表：`show tables`  
显示表信息：`show table status`  
显示列名：`show columns from <表名>;`
  
## 查询语句
```
#!mysql
select * from TableName ORDER BY ColumnName DESC limit 10;                    #降序排名前10
select * from TableName ORDER BY ColumnName DESC limit 10,20;                 #降序排名10-20
select ColumnName, COUNT(*) from TableName GROUP BY ColumnName;    #每种取值的条目数
select DISTINCT ColumnName from TableName;                                                    #所有取值
```

## mysql命令
执行sql文件：`source <sql文件名>`