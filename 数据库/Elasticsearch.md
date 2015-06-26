[TOC]

## 简介
* 面向文档(document oriented)
* 文档格式：JSON
* 全文索引

![](/images/Elasticsearch.png)

## 概念
### 与关系数据库的概念对比
|关系数据库  |ElasticSearch|
|------------|-------------|
|库          |索引
|表          |类型
|行          |文档
|列          |字段

### 索引
* ES把数据存放到一个或者多个索引中
* 用Lucene实现索引中数据的读写
* 一个ES索引对应多个Lucene索引：分片和备份

```
#!bash
#删除索引
curl -XDELETE 'http://localhost:9200/$IndexName/'
```

### 文档


## 操作
### 状态
```
#!bash
#显示全部索引
curl 'http://localhost:9200/_stats/indices?pretty'

#显示索引的状态
curl 'http://localhost:9200/$IndexName/_stats?pretty'
```
### 索引
* PUT /<索引>/<类型>/id

### 检索
```
#!bash
#根据id检索文档
curl 'http://localhost:9200/$IndexName/$TypeName/$DocId?pretty'
```
### 搜索
```
#!bash
#检索全部文档（默认10个）
curl 'http://localhost:9200/$IndexName/$TypeName/_search?pretty'

#检索100个
curl 'http://localhost:9200/$IndexName/$TypeName/_search?pretty&size=100'
```

#### 全文搜索
* 相关性(relevance)

#### 短语搜索

#### 高亮搜索

### 聚合
在数据基础上生成复杂的统计，类似SQL的GROUP BY

## 集群

![](/images/Elasticsearch_Cluster.png)

### 集群
* 一个集群中有多个节点，其中有一个为***主节点***

### 节点
* 运行的Elasticsearch实例
* 一个节点会被***选举***为主节点
* 主节点管理集群的变更（索引、节点等）

### 分片
* 一个分片就是一个Lucene实例
* 把一个完整的索引分成多个分片，分布到不同的节点上
* 主分片的数量需在创建索引时定义
* 路由：目标分片 = hash(_id) % 主分片的数量
* 开销：分发搜索命令到每个分片以及分片结果的合并

### 副本
* 设置多个索引的副本
* 提高系统的***容错性***
* 对搜索请求进行***负载均衡***，提高的查询效率
* 副本的数量可以随时更新设置

## 组件
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

## 用户查询语言DSL
### 打分因素
* 文档权重
* 域权重
* 调整因子
* 逆文档频率
* 长度归一化
* 词频
* 查询归一化因子

### 默认打分算法

![](/images/lucene_score_formula.png)

* coord(q,d)：基于文档中包含查询关键词个数的调整因子
* queryNorm(q)：查询语句中每一个查询词权重的平方和
* norm(t,d)：域越的文本越长，因子的权重越低


## API
### Bulk

## 工具
### elasticsearch-head
* 安装：./bin/plugin -install mobz/elasticsearch-head
* 运行：http://localhost:9200/_plugin/head/

## 参考
* [Elasticsearch 权威指南](http://es.xiaoleilu.com)
* [Mastering Elasticsearch(中文版) ](http://shgy.gitbooks.io/mastering-elasticsearch/content/)
* [与Costin Leau谈论Elasticsearch，大数据及Hadoop](http://www.infoq.com/cn/articles/costin-elasticsearch-bigdata)
* [乐观的并发控制（optimistic concurrency control）](http://www.bubuko.com/infodetail-182303.html)
* [Glossary of terms](http://www.elastic.co/guide/en/elasticsearch/reference/1.x/glossary.html)
* [GitHub使用elasticsearch遇到的一些问题及解决方法](http://devres.zoomquiet.io/data/20130616115216/index.html)
* [Elasticsearch数据架构及基本特点 ](http://chuansong.me/n/1133212)
* [Elasticsearch的备份和恢复](http://keenwon.com/1393.html)
* [elasticsearch suggest 的几种使用](http://www.cnblogs.com/jiuyuehe/p/3840821.html)
* [elasticsearch索引模块缓存](http://www.dongming8.cn/?p=74)
* [Elasticsearch全文搜索 (一) - 基础概念和match查询](http://blog.csdn.net/dm_vincent/article/details/41693125)