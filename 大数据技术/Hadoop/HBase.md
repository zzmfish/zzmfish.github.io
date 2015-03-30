* 基于列存储的分布式数据库
* 使用HDFS存储数据
* 使用MapReduce处理数据
* 大：上亿行，百万列
* 稀疏：null值不占用存储空间
* 多个版本
* 都是字符串类型

## 操作
* Get
* Put
* Scan
* Delete

### [Filters](http://hbase.apache.org/book.html#client.filter)

### Coprocessors
#### Observer
#### EndPoint
## 第三方工具
### Phoenix
a relational database layer over HBase delivered as a client-embedded JDBC driver targeting low latency queries over HBase data.
### [Lily HBase Indexer](http://ngdata.github.io/hbase-indexer/)
quickly and easily search for any content stored in HBase.

### [Solr](http://lucene.apache.org/solr/)
open source enterprise search platform built on Apache Lucene

### [Cloudera Search](http://www.cloudera.com/content/cloudera/en/products-and-services/cdh/search.html)
brings full-text, interactive search and scalable, flexible indexing to CDH and your enterprise data hub.

## 参考
* [Apache HBase Reference Guide](http://hbase.apache.org/book.html)
* [HBase_简介_(来自京东很不错)](http://wenku.baidu.com/view/9cfe96eb240c844769eaeed1.html)
* [Phoenix Performance](http://phoenix.apache.org/performance.html)
* [Using HBase Coprocessors to Index Columns in an Elasticsearch Cluster](http://www.slideshare.net/cloudera/hbasecon-2013-session-3b)
* [使用HBase和Solr配置存储与索引](http://database.51cto.com/art/201408/449223.htm)
## 疑问
* secondary index