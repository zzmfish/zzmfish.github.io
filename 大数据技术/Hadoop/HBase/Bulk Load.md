## Bulk Load
* 直接准备和加载HFile到RegionServers
* 
### 过程
* 提取数据到HDFS
* 把数据转换成HFile：MapReduce
    * Mapper
        * Key：row key
        * Value：KeyValue、Put或者Delete
    * Reducer：由HBase处理
* 把HFile加载到HBase