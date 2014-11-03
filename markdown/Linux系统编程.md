# Linux系统编程

[TOC]

## 文件锁
* 劝告锁
* 强制锁  
***读锁***／***共享锁***：阻止其他写操作；  
***写锁***／***排他锁***：阻止其他任何操作。  
* 共享模式强制锁
* 租借锁

## 网络IO模型
### 阻塞IO
* listen/send/recv

### 非阻塞IO
* fcntl(fd, F_SETFL, O_NONBLOCK)

### 多路复用IO
* select/epoll

### 异步IO
* aio_read/aio_write