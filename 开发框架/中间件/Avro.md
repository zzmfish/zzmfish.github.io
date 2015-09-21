* 目的是建立一个新的，标准性的云计算的数据交换和存储的Protocol
* 显式,declarative的Schema
* 高效二进制的数据表达

### Schema
* Avro-specific方式
* Avro-generic方式

### 序列化
* schema在前面，数据在后面
* 通过扫描schema只对感兴趣的部分作反序列化
* 允许定义数据的排序Order并在序列化的时候遵循这个顺序
* 序列化实现
    * TCompactProtocol: 最高效的二进制序列化协议
    * TBinaryProtocol: 缺省简单二进制序列化协议

### RPC服务
* HttpServer : 缺省,基于Jetty内核的服务
* NettyServer: 新的基于Netty的服务

## 参考
* [Apache Avro 与 Thrift 比较](http://jishu.zol.com.cn/3593.html)