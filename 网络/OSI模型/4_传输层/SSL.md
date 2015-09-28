## TLS握手

```uml @startuml
note right of Client
1)支持的协议版本
2)支持的加密方法
3)支持的压缩方法
4)随机数1
end note

Client -> Server
activate Server

Client <-- Server
deactivate Server

note right of Client #aqua
1)确认加密通信协议版本
2)确认加密方法
3)服务器证书
4)随机数2
//5)请求客户端证书(不是必需)//
end note

note right of Client
1)随机数3
2)编码变更通知
3)客户端握手结束通知(hash值)
//4)客户端证书(不是必需)//
end note

Client -> Server
activate Server
    Server -> Server: 生成**会话密钥**
    activate Server
    deactivate Server
Client <-- Server

deactivate Server

note right of Client #aqua
1)编码改变通知
2)服务器握手结束通知(hash值)
end note

@enduml
```

## 证书
### 内容
* 网站地址
* 加密公钥
* 证书的颁发机构

## 其他
* SSLStrip

## 参考
* [SSL/TLS协议运行机制的概述](http://www.ruanyifeng.com/blog/2014/02/ssl_tls.html)
* [浏览器如何验证SSL证书？](http://zhidao.baidu.com/link?url=zBDZomtpzkVsW78Yyf-OhpDAjnhCnEJzT6ZEiQheN1l95pggNf3fq9SL2MAgEbfsj9VJvTvmW3yZFlpf3eCF6_)

## 问题
* 怎样使用会话密钥