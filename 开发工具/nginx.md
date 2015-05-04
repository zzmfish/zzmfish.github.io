```
#!bash
nginx
nginx -s quit
```


## 静态目录
```
server {
        listen   80;
        root   /path/to/root;
        location / {
                index  index.php index.html index.htm;
        }
        location /somedir {
               autoindex on;       //显示文件列表
        }
}
```

## 参考
* [Nginx: How do I forward a http request to another port?](http://serverfault.com/questions/536576/nginx-how-do-i-forward-a-http-request-to-another-port)