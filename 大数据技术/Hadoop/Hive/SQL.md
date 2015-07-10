##### 建表
```sql
-- 创建表
CREATE TABLE TableName
    (field1 string, field2 double)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '|';

-- 把查询结果生成新表
CREATE TABLE TableName AS
SELECT field1, field2 from AnotherTable;

-- 把HBase表映射成新表
CREATE EXTERNAL TABLE TableName
(field1 string, field2 string, field3 string)
STORED BY 'org.apache.hadoop.hive.hbase.HBaseStorageHandler'
WITH SERDEPROPERTIES
    ("hbase.columns.mapping"=":key,famaly:column1,family:column2")
TBLPROPERTIES ('hbase.table.name'='HBaseTableName');
```

##### 更新数据
```sql
-- 从txt文件加载数据
LOAD DATA LOCAL INPATH "data.txt"
OVERWRITE INTO TABLE TableName;

-- 加载分区数据
ALTER TABLE TableName
ADD PARTITION (log_date = '2015-06-28', hour = 09)
LOCATION '/project/test/data_file';

-- 删除分区
ALTER TABLE TableName
DROP PARTITION(log_date='2015-06-24');
```

##### 查询数据
```sql
-- transform
SELECT TRANSFORM (hosting_ids, user_id, d) 
USING 'python combine_arrays.py' AS (hosting_ranks_array, user_id, d)
FROM my_table;

-- 查询昨日数据
SELECT * from video
WHERE log_date=to_date(from_unixtime(unix_timestamp() - 3600 * 24));

```

##### 查询信息
```sql
-- 查看表的创建信息
SHOW CREATE TABLE TableName;
        
-- 查看分区
SHOW PARTITIONS TableName;

-- 查看分区信息
DESCRIBE FORMATTED TableName PARTITION (field1='value1', field2='value2');
```

##### 导出和导入
```sql
EXPORT TABLE department TO 'hdfs_exports_location/department';
IMPORT FROM 'hdfs_exports_location/department';
```

## 参考
* [LanguageManual ImportExport](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+ImportExport)