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

//遍历数组或属性值
for each (var item in array) {
  ...
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
//节点类型
node.
```

### 日期和时间
```
#!javascript
//时间戳（ms）
var timeStamp = Date.now();
```