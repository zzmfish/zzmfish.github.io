## 特性
* k/v类型
* list，set，hash等数据类型
* SWAP：只交换value
    * Blocking VM
    * Threaded VM

### 数据类型
#### 列表
* 插入元素：LPUSH、RPUSH
* 获取元素：BLPOP
* 获取范围：LRANGE
* 限制长度：LTRIM
* 最多2^32 - 1个元素
* 访问两端元素很快
* 访问中间元素很慢

#### 集合
#### 哈希
#### 有序集合
### 虚拟内存
* 不赞成使用

### 数据持久化
#### RDB
* 定时快照
* 单文件
* fork

#### AOF
* 记录每个操作
* fsync：无/每秒/每操作
* 后台线程
* 追加文件，容错
* 自动压缩
* 容易解析的格式


### 主从复制
```
#配置从服务器
slaveof 192.168.1.1 6379
```

## 使用方法

#### 下载
```
wget http://download.redis.io/releases/redis-2.8.19.tar.gz
```
#### 编译
```
make
```

#### 运行
```
./src/redis-server
./src/redis-server --port 6379
./src/redis-server redis.conf --port 6379
```

#### 删除一定模式的key
```
#!bash
redis-cli keys beh_sim_* | xargs redis-cli del
```
默认端口6379

#### 性能测试：
```
./redis-benchmark -q -n 100000
```

#### 命令
| 命令             | 作用            |
|------            |------           |
|scan 0 count 10   |显示0-10个key
|info keyspace     |显示key的数量
|flushdb           |清空数据库
|keys *            |显示全部key


#### python接口
* https://pypi.python.org/pypi/redis/

## 资料
* [Redis Quick Start](http://redis.io/topics/quickstart)
* [How fast is Redis?](http://redis.io/topics/benchmarks)
* [Data types](http://redis.io/topics/data-types)