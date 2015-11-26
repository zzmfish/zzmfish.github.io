* TB级数据库和GB级字符串
* 动态类型
* 线程安全（可关闭）
* 多进程可同时读数据库
* 写数据库使用文件锁（其他操作返回SQLITE_BUSY）
* 不要带着数据库fork进程
* 每秒50k+的INSERT
* 事务会等待数据写到磁盘
* 使用BEGIN...COMMIT 加快INSERT