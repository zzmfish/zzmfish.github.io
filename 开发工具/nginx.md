```
#!bash
nginx
nginx -s quit
```



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