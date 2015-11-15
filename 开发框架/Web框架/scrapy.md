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

## 爬取网页时序图

```uml
@startuml
START -> ExecutionEngine: _next_request
activate ExecutionEngine
    ExecutionEngine -> ExecutionEngine: _next_request_from_scheduler
    activate ExecutionEngine
        ExecutionEngine -> ExecutionEngine: _download
        activate ExecutionEngine
            ExecutionEngine -> Downloader: fetch
            activate Downloader
                Downloader -> DownloaderMiddlewareManager: download
                activate DownloaderMiddlewareManager

                    DownloaderMiddlewareManager -> DownloaderMiddlewareManager: process_request
                    activate DownloaderMiddlewareManager

                        DownloaderMiddlewareManager -> Downloader: _enqueue_request
                        activate Downloader

                            Downloader -> Downloader: _download
                            activate Downloader
                                Downloader -> DownloadHandlers: download_request
                                activate DownloadHandlers

                                    DownloadHandlers -> HTTP11DownloadHandler: download_request
                                    activate HTTP11DownloadHandler

                                        HTTP11DownloadHandler -> ScrapyAgent: download_request
                                        activate ScrapyAgent
                                        HTTP11DownloadHandler <- ScrapyAgent: download_request
                                        deactivate ScrapyAgent

                                    DownloadHandlers <- HTTP11DownloadHandler: download_request
                                    deactivate HTTP11DownloadHandler

                                Downloader <- DownloadHandlers: download_request
                                deactivate DownloadHandlers
                            deactivate Downloader

                        DownloaderMiddlewareManager <- Downloader: _enqueue_request
                        deactivate Downloader

                    deactivate DownloaderMiddlewareManager

                    DownloaderMiddlewareManager -> RedirectMiddleware: process_response
                    activate RedirectMiddleware
                    DownloaderMiddlewareManager <- RedirectMiddleware: process_response
                    deactivate RedirectMiddleware

                Downloader <- DownloaderMiddlewareManager: download
                deactivate DownloaderMiddlewareManager

            ExecutionEngine <- Downloader: fetch
            deactivate Downloader
        deactivate ExecutionEngine
    deactivate ExecutionEngine

START <- ExecutionEngine: _next_request
deactivate ExecutionEngine
@enduml
```