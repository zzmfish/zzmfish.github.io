#!/usr/bin/python
#encoding=utf-8
import base64
import os
import os.path
import tornado.ioloop
import tornado.web
import tools.make_html

MD_DIR = '../markdown'

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        global MD_DIR
        files = os.listdir(MD_DIR)
        self.render('main.html', files=files)

class GetFileHandler(tornado.web.RequestHandler):
    def get(self):
        global MD_DIR
        f = self.get_argument('f')
        text = ''
        if f:
            text = open(os.path.join(MD_DIR, f), 'r').read()
        self.write(text)
       
class RenderHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_body_argument('text')
        css = open('../style.css', 'r').read()
        html = tools.make_html.make_html(text, css)
        self.write(base64.b64encode(html))
        
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/GetFile", GetFileHandler),
    (r"/Render", RenderHandler),
])
application.listen(8888)
tornado.ioloop.IOLoop.instance().start()

