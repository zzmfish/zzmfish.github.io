## 基础概念
### RDD（Resilient Distributed Datasets）
* 容错的、并行的数据结构
* 内存数据集
* 访问时指针指向与操作相关的部分
* 可以存储到磁盘和内存中
* 提供丰富的操作：map、flatMap、filter、join、groupBy、reduceByKey


### 分区
* 一个RDD可以包含多个分区，每个分区是一个***dataset片段***
* 可以根据数据记录的key对结构进行分区

##### Narrow Dependency
* 每个分区最多只能被一个Child RDD的一个分区使用（如map操作）
* 支持在同一个cluster node上以管道形式执行多条命令

##### Wide Dependency
* 多个Child RDD分区都可以依赖（如join操作）
* 需要所有的父分区都是可用的
* 可能需要调用类似MapReduce之类的操作进行跨节点传递

### transformation
* 不会真正执行运算
* 继承自RDD的类型（如MappedRDD、FlatMappedRDD）
* 定义了compute函数，在action操作被调用时触发

### action
* 执行运算

### 容错
* 自身是一个不变的数据集
* 记住构建它的操作图
* checkpoint机制

## Spark SQL

### DataFrame
* a distributed collection of data organized into named columns
* equivalent to a table in a relational database
* can be constructed from: structured data files, tables in Hive, external databases, or existing RDDs

### 性能优化
* 内存列存储
* 字节码生成

## 参考
* [spark-programming-guide-zh-cn](https://www.gitbook.com/book/endymecy/spark-programming-guide-zh-cn/details)
* [从Hadoop到Spark的架构实践](http://www.thebigdata.cn/Hadoop/14289.html)
* [sparkSQL1.1入门之一：为什么sparkSQL](http://blog.csdn.net/book_mmicky/article/details/39288715)
* [Spark SQL深度理解篇：模块实现、代码结构及执行流程总览](http://blog.csdn.net/book_mmicky/article/details/39288715)
* [理解Spark的核心RDD](http://www.infoq.com/cn/articles/spark-core-rdd/)
* [平易近人、兼容并蓄——Spark SQL 1.3.0概览](http://www.csdn.net/article/2015-04-03/2824407)
* [Spark 快速入门](http://colobu.com/2014/12/08/spark-quick-start/)
* [Spark SQL 初探： 使用大数据分析2000万数据](http://colobu.com/2014/12/11/spark-sql-quick-start/)
* [【微信分享】梁堰波：主流SQL on Hadoop框架选择](http://www.csdn.net/article/1970-01-01/2825293)
* [Big Data Benchmark](https://amplab.cs.berkeley.edu/benchmark/)