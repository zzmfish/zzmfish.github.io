# tornado网站开发

## 安装
`sudo apt-get install python-tornado`  

## hello world
```
#!python
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print self.get_argument('foo')  #get参数
        print self.get_body_argument('foo')  #post参数
        self.write("Hello, world")


application = tornado.web.Application(
    [
        (r"/", MainHandler),
    ],
    static_path='static'
)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
```

## 当前目录作为一个静态网站
```
#!python
import tornado.web

application = tornado.web.Application([
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": "."}),
])
application.listen(8076)
tornado.ioloop.IOLoop.instance().start()
```

##### 请求属性
* 请求path：self.request.path
* 请求ip：


##### 显示日志
```
#!python
import tornado.log
tornado.log.enable_pretty_logging()
```
#### 模板
```
#!python
self.render('main.html', foo=foo)
```


#### 模板语法
```
#!plain
{{ foo }} //变量
{% raw foo %} //变量不要转码
```

### 异步请求处理
* @tornado.web.asynchronous装饰器
* ThreadPoolExecutor
* AsyncHTTPClient

### 参考资料
* [Tornado概览](http://sebug.net/paper/books/tornado/)
* [深入理解Tornado——一个异步web服务器](http://www.cnblogs.com/yiwenshengmei/archive/2011/06/08/understanding_tornado.html)
* [Benchmarking Tornado vs. Twisted Web vs. Tornado on Twisted ](http://programmingzen.com/2009/09/13/benchmarking-tornado-vs-twisted-web-vs-tornado-on-twisted/)
* [对比Tornado和Twisted](http://blog.csdn.net/chenggong2dm/article/details/23344389)


```uml
class web.RequestHandler {
    # _write_buffer = []
}
class httputil.HTTPServerRequest {
    + arguments
}
web.RequestHandler o-- httputil.HTTPServerRequest: request
```