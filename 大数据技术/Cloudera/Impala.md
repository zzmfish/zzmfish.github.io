## 元数组
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

## 性能优化
* 分区
* 使用Parquet格式 [链接](http://www.cloudera.com/content/cloudera/en/documentation/cloudera-impala/latest/topics/impala_parquet.html)

## 参考资料
* [Tuning Impala for Performance](http://www.cloudera.com/content/cloudera/en/documentation/cloudera-impala/latest/topics/impala_performance.html)
* [Impala Performance Guidelines and Best Practices](http://www.cloudera.com/content/cloudera/en/documentation/cloudera-impala/latest/topics/impala_perf_cookbook.html)