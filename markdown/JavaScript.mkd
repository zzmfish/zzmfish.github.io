# JavaScript
url编码：`encodeURIComponent`  
保存文件：[FileSaver.js](https://github.com/eligrey/FileSaver.js)
### http请求
```
var req = new XMLHttpRequest();
req.open('GET', url);
req.onreadystatechange = function() {
    if (req.readyState == 4 && req.status == 200) {`
        //得到req.responseText;
    }
}
req.send();
```
### http POST请求
```
var req_content = 'text=' + encodeURIComponent(document.getElementById('Editor').textContent);
var req = new XMLHttpRequest();
req.open('POST', '/Render', false);
req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
req.setRequestHeader("Content-length", req_content.length);
req.setRequestHeader("Connection", "close");
req.onreadystatechange = function() {
    if (req.readyState == 4) {
        if (req.status == 200) {
            document.getElementById('Renderer').src = 'data:text/html;base64,' + req.responseText;
        }
        rendering = false;
    }
}
req.send(req_content);
```

访问iframe子文档：`iframeElem.contentDocument`  

## 参考资料
* [W3School jQuery教程](http://www.w3school.com.cn/jquery/index.asp)
