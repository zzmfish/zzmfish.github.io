# JavaScript常用例程

## DOM
```
#!javascript
//删除节点
node.removeChild(child);
```

### 发送请求
```
#!javascript
//异步POST请求
var req = new XMLHttpRequest(); 
req.onreadystatechange = function() {
    if (req.readyState == 4) { //loaded
        if (req.status == 200) { //ok
            console.log(req.responseText); //应答内容
        }
    }
}       
req.open("POST", url, true);
req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
req.send(data);

```

### 日期和时间
```
#!javascript
//UTC时间戳（ms）
var timeStamp = Date.now();

//当地时间戳（ms）
var nowDate = new Date();
var nowTime = nowDate.getTime() - nowDate.getTimezoneOffset() * 60000;

//解析日期时间为unix时间戳（ms）
Date.parse(startTimeInput.value) 
```

### 坐标
```
#!javascript
//视窗滚动位置
window.scrollX;
window.scrollY;

//视窗大小
window.innerWidth;
window.innerHeight;

//元素相对视窗的位置
elem.getBoundingClientRect()
```

### 数据处理
```
#!javascript
//解析JSON
var obj = eval('(' + json + ')');

//URL编码
var data = encodeURIComponent(value);
```

### 事件处理
```
//DOMContentLoaded
document.addEventListener("DOMContentLoaded", function(event) {
    alert('document is loaded!');
});

```

#### 当前脚本路径
```
#!javascript
var scripts = document.getElementsByTagName("script"),
var src = scripts[scripts.length-1].src;
//or
var src = document.currentScript;
```

#### XPath
```
#!javascript
var result = document.evaluate('//input',
    document,
    null/*命名空间*/,
    XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE,
    null/*结果集，null为新建*/);
```

### 未分类
```
#!javascript


//在新窗口输出html
var doc = window.open().document;
doc.open();
doc.write('hello');
doc.close();
```

## 第三方库
|  名称                                 | 说明 | 
|------                                 |      |
| [jquery](http://jquery.com)           |
| [jquery-cookie](https://github.com/carhartl/jquery-cookie) |
| [Bootstrap](http://getbootstrap.com/) | Bootstrap is the most popular HTML, CSS, and JS framework for developing responsive, mobile first projects on the web.       |

### jQuery
```
#!javascript
//设置html
$('#myid').html('hello');
```