## 客户端
### Java
```java
//遍历属性
for (Cell cell : result.rawCells()) {
    videoObj.put(new String(CellUtil.cloneQualifier(cell)), new String(CellUtil.cloneValue(cell)));
}
```
### REST
### Thrift

## API
### [Filters](http://hbase.apache.org/book.html#client.filter)

### Coprocessors
* Observer
    * RegionObserver
    * WALObserver
    * MasterObserver
* EndPoint