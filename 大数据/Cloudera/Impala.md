## 查询流程
![](/images/impala.jpg)

## 元数据
* 表的定义
* HDFS物理块的位置
* 原数组缓存
* INVALIDATE METADATA命令：新表、删除表、HDFS均衡
* REFRESH命令：新文件

## 统计数据
### 表格统计
* COMPUTE STATS
* DROP STATS
* SHOW TABLE STATS
* SHOW COLUMN STATS

### 列统计

## 组件

### Impala Daemon
* impalad 
* 每个节点，传递查询请求和结果
* --load_catalog_in_background=false：等待元数据加载完成才处理请求

### The Impala Statestore
* statestored
* 每集群一个
* 检查deamon的状况

### Impala Catalog Service
* catalogd
* 转播元数据，通过statestore转发
* 每集群一个，和statestore在同一个节点
* 1.2以上，impala本身的操作不需要refresh

```
#!bash
#刷新元数据
impala-shell -r -q "quit;"


#更新统计数据，帮助性能优化
echo "compute STATS $TableName;" impala-shell
```

## Ubuntu安装impala-udf-dev
```bash
sudo wget 'http://archive.cloudera.com/cdh5/ubuntu/trusty/amd64/cdh/cloudera.list' \
    -O /etc/apt/sources.list.d/cloudera.list
sudo apt-get update
sudo apt-get install impala-udf-dev
sudo rm /etc/apt/sources.list.d/cloudera.list
sudo apt-get update
```
## 性能优化
* 分区
* 使用Parquet格式 [链接](http://www.cloudera.com/content/cloudera/en/documentation/cloudera-impala/latest/topics/impala_parquet.html)

## 参考资料
* [Cloudera Impala Guide](http://www.cloudera.com/content/cloudera/en/documentation/core/latest/topics/impala.html)
* [Tuning Impala for Performance](http://www.cloudera.com/content/cloudera/en/documentation/cloudera-impala/latest/topics/impala_performance.html)
* [Impala Performance Guidelines and Best Practices](http://www.cloudera.com/content/cloudera/en/documentation/cloudera-impala/latest/topics/impala_perf_cookbook.html)
* [What’s Next for Impala: More Reliability, Usability, and Performance at Even Greater Scale](http://blog.cloudera.com/blog/2015/07/whats-next-for-impala-more-reliability-usability-and-performance-at-even-greater-scale/)
* [New SQL Choices in the Apache Hadoop Ecosystem: Why Impala Continues to Lead](http://blog.cloudera.com/blog/2014/05/new-sql-choices-in-the-apache-hadoop-ecosystem-why-impala-continues-to-lead/)
* [User-Defined Functions (UDFs)](http://www.cloudera.com/content/cloudera/en/documentation/cloudera-impala/latest/topics/impala_udf.html)
* [Impala与Hive的比较](http://tech.uc.cn/?p=1803)
* [Configuring Impala to Work with JDBC (CDH5.1)](http://www.cloudera.com/content/cloudera/en/documentation/cdh5/v5-1-x/Impala/Installing-and-Using-Impala/ciiu_impala_jdbc.html)