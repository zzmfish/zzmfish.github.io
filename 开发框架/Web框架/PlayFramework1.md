## 安装
* 解压
* 设置PATH和PLAY_PATH
## 创建项目
```
#!bash
play new play_helloworld
cd play_helloworld/
play eclipsify
play run
```

## 路由
* 把请求转到对应的action调用
* `conf/routes`文件定义

```
#HTTP方法    url模式               action调用
GET          /clients/:id          controllers.Clients.show(id: Long)
```

## 请求处理
### Action
* java方法
* 处理请求
* 返回`play.mvc.Result`

### Controller
* 继承`play.mvc.Controller`
* 组合多个action方法

### Result
* 表示HTTP应答：状态码、头部、主体

## 线程池
* Netty boss/worker线程池
* Play内部线程池：默认为CPU核心数
* Play默认线程池：action使用，默认为CPU核心数
* Akka线程池

## 运行
```
play run -Xms256M -Xmx1024M
```

## 未分类
* 程序路径：Play.applicationPath
* 通过命令行指定端口：play run --http.port=8080

### conf/log4j.properties
```
log4j.rootLogger=ERROR, Console, RollingAppender

log4j.logger.play=DEBUG

# Console
log4j.appender.Console=org.apache.log4j.ConsoleAppender
log4j.appender.Console.layout=org.apache.log4j.PatternLayout
log4j.appender.Console.layout.ConversionPattern=%d{ABSOLUTE} %-5p ~ %m%n

# Rolling files
log4j.appender.RollingAppender=org.apache.log4j.DailyRollingFileAppender
log4j.appender.RollingAppender.File=logs/msg_send_server.log
log4j.appender.RollingAppender.DatePattern='.'yyyy-MM-dd
log4j.appender.RollingAppender.layout=org.apache.log4j.PatternLayout
log4j.appender.RollingAppender.layout.ConversionPattern=%p %d - %m%n
```

## 参考
* [Actions, Controllers and Results](https://www.playframework.com/documentation/2.3.x/JavaActions)
* [HTTP routing](https://www.playframework.com/documentation/2.3.x/JavaRouting)
* [Handling asynchronous results](https://www.playframework.com/documentation/2.3.x/JavaAsync)
* [致Play Framework开发者们的一封信](http://blog.jobbole.com/16631/)
* [Play Framework 2.0几宗罪](http://www.bloggern.com/7069.html)
* [谁能说说Play与Grails的异同与优劣？](http://www.zhihu.com/question/19681587)
* [Play 1.3.x Documentation](https://www.playframework.com/documentation/1.3.x/home)
* [‘Hello World’ tutorial — Your first Play application](https://www.playframework.com/documentation/1.3.x/firstapp)
* [Understanding Play thread pools](https://www.playframework.com/documentation/2.3.x/ThreadPools)