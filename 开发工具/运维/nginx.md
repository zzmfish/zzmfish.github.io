```
#!bash
nginx
nginx -s quit
```


## 配置
```nginx
http {
    server {
        listen   80;
        root   /path/to/root;
        location / {
            index  index.php index.html index.htm;
        }
        location /somedir {
           autoindex on;
        }
            
        #代理
        location /external/query {
            proxy_pass http://mob3032:8022;
            proxy_read_timeout 1800s;
        }
    }
}
```

## 负载均衡
```nginx
http {
    upstream test_server {
        server test1:8882;
        server test2:8882;
        server test3:8882;
        server test4:8882;
    }

    server {
        listen 8881;

        location / {
            proxy_pass http://test_server;
        }
    }
}
```

## 状态码
| 代码 | 描述                      |
|----- |----------                 |
|

## 参考
* [Nginx: How do I forward a http request to another port?](http://serverfault.com/questions/536576/nginx-how-do-i-forward-a-http-request-to-another-port)
* [Using nginx as HTTP load balancer](http://nginx.org/en/docs/http/load_balancing.html)
* [深入NGINX：我们如何设计它的性能和扩展性](http://www.cnbeta.com/articles/402709.htm)
* [Nginx 与 Lua](http://www.ttlsa.com/nginx/nginx-and-lua/)
* [Nginx为什么要造重复的轮子nginScript](http://www.infoq.com/cn/news/2015/10/Nginx-JavaScript-vm)
* [How To Configure Logging and Log Rotation in Nginx on an Ubuntu VPS](https://www.digitalocean.com/community/tutorials/how-to-configure-logging-and-log-rotation-in-nginx-on-an-ubuntu-vps)