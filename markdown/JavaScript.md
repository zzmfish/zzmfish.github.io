# JavaScript

## 基本类型
```
#!JavaScript
//类型判断
typeof(n) == 'number';

//连接n个"-"
Array(n+1).join('-');

//字符串匹配
s.match(/^https?:/);

//遍历数组
for (elem of array) {
    do_something(elem);
}

//截取数组前n个元素
arr = arr.slice(1, n);
```

## 函数

```
#!javascript
//匿名函数
(function(){
    ...
})();

```

## 对象
```
#!JavaScript
//定义类
var Cat = {
    name: "大毛",
    makeSound: function(){ alert("喵喵喵"); }
};
//创建实例
var cat1 = Object.create(Cat);

//所有属性
Object.keys(s)

//删除属性
delete obj[prop];
```

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
req.send(data);

```

### 日期和时间
```
#!javascript
//时间戳（ms）
var timeStamp = Date.now();
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

### 未分类
```
#!javascript


//在新窗口输出html
var doc = window.open().document;
doc.open();
doc.write('hello');
doc.close();
```