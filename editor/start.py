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
       
class SaveFileHandler(tornado.web.RequestHandler):
    def post(self):
        global MD_DIR
        text = self.get_body_argument('text')
        f = self.get_body_argument('f')
        print f
        f = os.path.join(MD_DIR, f)
        open(f, 'w').write(text.encode('utf-8'))
        self.write('OK')
 
class RenderHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_body_argument('text')
        css = open('../style.css', 'r').read()
        html = tools.make_html.make_html(text, css)
        self.write(base64.b64encode(html))
        
from tornado.log import enable_pretty_logging
enable_pretty_logging()
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/GetFile", GetFileHandler),
    (r"/SaveFile", SaveFileHandler),
    (r"/Render", RenderHandler),
])
application.listen(8889)
tornado.ioloop.IOLoop.instance().start()

