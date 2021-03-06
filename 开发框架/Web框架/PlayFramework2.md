```bash
#指定运行端口
./activator "~run 8080"

#指定运行端口和配置文件
./activator -Dconfig.file=conf/application_dev.conf -Dhttp.port=8031 run

#运行测试案例
./activator "test-only TestUserModelSQLMaker"
```


## 参考
* [Create a Debug Configuration](https://gist.github.com/xiongmaomaomao/39f99486f9f5c5212ff2)
* [Filters](https://www.playframework.com/documentation/2.3.x/ScalaHttpFilters)
* [Scala 常用语法](http://www.cnblogs.com/fxjwind/p/3338829.html)
* [Play 2.3.x documentation](https://www.playframework.com/documentation/2.3.x/Home)
* [Setting up your preferred IDE](https://www.playframework.com/documentation/2.3.x/IDE)
* [The Logging API](https://www.playframework.com/documentation/2.3.x/ScalaLogging)
* [Intercepting requests](https://www.playframework.com/documentation/2.3.x/ScalaInterceptors)
* [PlayFramework API](https://www.playframework.com/documentation/2.3.x/api/scala/index.html#package)