## 配置
```
#!bash
# 启动elasticsearch
cat > config/elasticsearch.yml <<EOF
http.cors.enabled: true
http.cors.allow-origin: "http://usa-mob437:8076"
EOF

./bin/elasticsearch

# 启动logstash
cat > test.conf <<EOF
input { stdin { } }
output {
    stdout { codec => rubydebug }
    redis {
        host => "127.0.0.1"
        port => 6763
        data_type => "list"
        key => "logstash"
    }
    tcp {
        port => 5959
    }
    elasticsearch { host => localhost }
}
EOF
./bin/logstash -f test.conf
```

##### 更改elasticsearch端口
vi elasticsearch-1.4.2/config/elasticsearch.yml  
```
http.port: 8200
```

vi kibana-3.1.2/config.js
```
elasticsearch: "http://"+window.location.hostname+":8200",
```

### grok
* 工具：[Grok Debugger](http://grokdebug.herokuapp.com)


## 参考资料
* [Collect & visualize your logs with Logstash, Elasticsearch & Redis](http://michael.bouvy.net/blog/en/2013/11/19/collect-visualize-your-logs-logstash-elasticsearch-redis-kibana/)
* [Getting started with Logstash](http://logstash.net/docs/1.4.2/tutorials/getting-started-with-logstash)
* [用Kibana和logstash快速搭建实时日志查询、收集与分析系统](http://storysky.blog.51cto.com/628458/1158707)
* [A bit of logstash cooking](https://home.regit.org/2014/01/a-bit-of-logstash-cooking/)
* [Kibana 中文指南](http://kibana.logstash.es)