## 简介
* 实时分布式搜索和分析引擎
* 面向文档(document oriented)
* 使用JSON做为文档序列化格式
* 反向索引

### 概念比较
|关系数据库  |ElasticSearch|
|------------|-------------|
|库          |索引
|表          |类型
|行          |文档
|列          |字段

## 操作
### 索引
* PUT /<索引>/<类型>/id

### 检索
* GET /<索引>/<类型>/id
* GET /<索引>/<类型>/_search
* 过滤器(filter)

### 全文搜索
* 相关性(relevance)

### 短语搜索

### 高亮搜索

### 聚合
在数据基础上生成复杂的统计，类似SQL的GROUP BY



## 集群
### 集群
* 一个集群中有多个节点，其中有一个为***主节点***
* 主节点可以通过***选举***产生

### 节点
* 运行的Elasticsearch实例

### 分片(shards)
* 把一个完整的索引分成多个分片，分布到不同的节点上

### 副本
* 设置多个索引的副本
* 提高系统的***容错性***
* 对搜索请求进行***负载均衡***，提高的查询效率

### 恢复（Recovery）
* 在有节点加入或退出时会根据机器的负载对索引分片进行重新分配
* 挂掉的节点重新启动时也会进行数据恢复

### 数据源（River）

### Gateway
* 索引的持久化存储方式
* 先把索引存放到内存中，当内存满了时再持久化到硬盘

### discovery.zen
* 自动发现节点机制
* 通过广播寻找存在的节点，再通过多播协议来进行节点之间的通信，同时也支持点对点的交互

### Transport
内部节点或集群与客户端的交互方式

## 其他
### Optimistic Concurrency Control

## 参考
* [与Costin Leau谈论Elasticsearch，大数据及Hadoop](http://www.infoq.com/cn/articles/costin-elasticsearch-bigdata)
* [Elasticsearch 权威指南](http://es.xiaoleilu.com)
* [乐观的并发控制（optimistic concurrency control）](http://www.bubuko.com/infodetail-182303.html)
* [Glossary of terms](http://www.elastic.co/guide/en/elasticsearch/reference/1.x/glossary.html)
* [GitHub使用elasticsearch遇到的一些问题及解决方法](http://devres.zoomquiet.io/data/20130616115216/index.html)
* [Elasticsearch数据架构及基本特点 ](http://chuansong.me/n/1133212)
* [Mastering Elasticsearch(中文版) ](http://shgy.gitbooks.io/mastering-elasticsearch/content/)
* [Elasticsearch的备份和恢复](http://keenwon.com/1393.html)