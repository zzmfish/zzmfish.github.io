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
        print self.request.path         #请求path
        print self.get_argument('foo')  #get参数
        print self.get_body_argument('foo')  #post参数
        self.write("Hello, world")


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
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
```



```uml
class web.RequestHandler
class httputil.HTTPServerRequest {
    + arguments
}
web.RequestHandler o-- httputil.HTTPServerRequest: request
```