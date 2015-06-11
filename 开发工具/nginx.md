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

## 负载均衡
```
http {
    upstream search_server {
        server aliyun-hk-data04:8367;
        server aliyun-hk-data07:8367;
        server aliyun-hk-data08:8367;
        server aliyun-hk-data09:8367;
        server aliyun-hk-data16:8367;
        server aliyun-hk-data17:8367;
        server aliyun-hk-data29:8367;
    }

    server {
        listen 8081;

        location / {
            proxy_pass http://search_server;
        }
    }
}

```

## 参考
* [Nginx: How do I forward a http request to another port?](http://serverfault.com/questions/536576/nginx-how-do-i-forward-a-http-request-to-another-port)
* [Using nginx as HTTP load balancer](http://nginx.org/en/docs/http/load_balancing.html)