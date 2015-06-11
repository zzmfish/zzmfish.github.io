# Twisted

* 异步模型中，一个任务要想运行必须显式放弃当前运行的任务的控制权  
* 当一个任务出现阻塞时，会让其它可以执行的任务继续执行
* 


* [我看到的最棒的Twisted入门教程！](http://blog.sina.com.cn/s/blog_704b6af70100py9n.html)
* [使用 Twisted Python 和 Treq 进行 HTTP 压力测试](http://www.oschina.net/translate/stress-testing-http-with-twisted-python-and-treq)

## Deferred
* manage the callback sequence
* be called in order when the results are available

![](/images/Twisted_Deferred.png)

```uml @startuml

class EPollReactor

@enduml
```

## 参考
* [Using the Twisted Web Client](https://twistedmatrix.com/documents/14.0.1/web/howto/client.html)
* [Using Threads in Twisted](https://twistedmatrix.com/documents/14.0.1/web/howto/client.html)
* [Deferred Reference](https://twistedmatrix.com/documents/14.0.1/core/howto/defer.html)