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

## 体系结构
```uml @startuml
node HMaster服务器 as hm {

}

node HRegion服务器 as hs1 {
  database HRegion as hr1
  database HRegion as hr2
}

node HRegion服务器 as hs2 {
  database HRegion as hr3
  database HRegion as hr4
}

[ ZooKeeper ] as zk

hm <--> hs1
hm <--> hs2
zk <..> hm
zk <..> hs1
zk <..> hs2
@enduml
```

### HRegion服务器
* ***HLog***: 存储日志，先写日志（WAL）
* ***HRegion***: 保存一个表里面某段连续的数据
* ***Store***: 储存一个列族的数据
* ***MemStore***: 驻留在内存，数据先更新到MemStore，达到阈值之后再更新到对应的StoreFile
* ***StoreFile（HFile）***: 实际的数据存储

![](/images/HBase_HRegionServer.png)

#### StoreFile（HFile）
* 通过***追加***的方式进行更新数据
* 数据的删除和更新在合并时进行
* 当Store中StoreFile的数量超过阈值会进行***合并***，将多个StoreFile合并成一个StoreFile
* 按照KeyValue存储

#### HLog
* 用于故障恢复

#### HRegion
* 当大小超过阈值就会进行拆分

### HMaster服务器
* 管理Table操作
* 管理HRegion服务器的负载均衡
* 调整HRegion分布
* HRegion服务器停机后负责失效HRegion服务器上的HRegion迁移

### ROOT表和META表
* ***ROOT表***: 保存所有META表的位置
* ***META表***: 保存HRegion标示符和实际HRegion服务器的映射关系
* ***HRegion标识符***: 表名+开始主键+唯一ID

## API
### [Filters](http://hbase.apache.org/book.html#client.filter)

### Coprocessors
#### Observer
#### EndPoint

## 性能优化
### Rowkey设计
* ***越短越好***：节省存储和内存
* ***高位作为散列字段***：数据均衡分布在每个Regionserver

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
* [HBase数据同步到ElasticSearch的方案](http://blog.csdn.net/hengyunabc/article/details/41146115)
* [Coprocessor Introduction](https://blogs.apache.org/hbase/entry/coprocessor_introduction)
* [大数据性能调优之HBase的RowKey设计](http://blog.chedushi.com/archives/9720)