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
所有取值：`select DISTINCT <列名> from <表名>;`  
降序排名前10：`select * from <表名> ORDER BY <列名> DESC limit 10;`  
降序排名10-20：`select * from <表名> ORDER BY <列名> DESC limit 10,20;`  
每天条目数：`select date, COUNT(*) from <表名> GROUP BY date;`  

## mysql命令
执行sql文件：`source <sql文件名>`  
