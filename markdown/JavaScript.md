# JavaScript

## 定义类
```
#!JavaScript
var Cat = {
    name: "大毛",
    makeSound: function(){ alert("喵喵喵"); }
};
//创建实例
var cat1 = Object.create(Cat);
```

## 其他
```
#!JavaScript
typeof(n) == 'nunber';       //类型判断
Array(n+1).join('-') //连接n个"-"
```