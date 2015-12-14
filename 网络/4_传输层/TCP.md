# TCP
## 原理
### 建立连接
![](/images/tcp_connect.png)

### 传输数据
![](/images/tcp_transport.gif)

### 断开连接
![](/images/tcp_disconnect.png)

## 其他
* 端口
* 序号：解决网络包乱序问题
* ACK：解决丢包问题
* 滑动窗口：流量控制
* 建立连接要3次握手，断开连接要4次握手
* SYN Flood攻击


```
#!bash
#端口扫描
nmap 127.0.0.1
```

## 参考
* [浅析TCP握手欺骗](http://www.infoq.com/cn/news/2015/12/TCP-Handshake-cheat)