# Scrapy

## 创建项目
```
#!bash
scrapy startproject $ProjectName


```

## 定义爬虫
spiders/hellospider.py:
```
#!python
import scrapy.contrib.spiders as spiders

class TencentSpider(spiders.CrawlSpider):  
    name = "hello_spider"  
    start_urls = [  
        "http://www.pconline.com.cn"  
    ]  
  
    def parse_item(self, response):
        print response
```

## 开始爬取
```
#!bash
scrapy crawl $SpiderName
```