# JavaScript基础语法

## 类型判断 
```
#!JavaScript
typeof(n) == 'number';
```

## 字符串
```
#!javascript
//正则表达式匹配
s.match(/^https?:/);

//从下标开始的指定数目的字符
s.substr(start, length);

//介于两个指定下标之间的字符
s.substring(start, end);
```

## 数组
### 连接字符串
```
#!javascript
Array(n+1).join('-');
```

### 遍历
```
#!javascipt
for (elem of array) {
    do_something(elem);
}
```

### 截取
```
#!javascript
arr = arr.slice(1, n);
```

### 排序
```
//排序
arr.sort();

//大小写无关的排序
arr.sort(function (a, b) {
    return a.toLowerCase().localeCompare(b.toLowerCase());
});
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