```
#!bash
nginx
nginx -s quit
```


## 静态目录
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

## 参考
* [Nginx: How do I forward a http request to another port?](http://serverfault.com/questions/536576/nginx-how-do-i-forward-a-http-request-to-another-port)
* [Using nginx as HTTP load balancer](http://nginx.org/en/docs/http/load_balancing.html)
* [深入NGINX：我们如何设计它的性能和扩展性](http://www.cnbeta.com/articles/402709.htm)