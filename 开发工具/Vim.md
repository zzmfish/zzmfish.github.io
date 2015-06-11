# Vim经验技巧

## 查找和替换
查找不分大小写：`/要超找的字符串\c`  
去掉全部script：`:%s/<scrip[^>]*>\_.\{-}<\/script>//g`  

## 正则表达式
`\_.`：匹配任意字符和换行  
`\{-}`：非贪婪匹配  

## 脚本
变量赋值: `left name = 'jay'`  

变量作用域  
`a`：函数参数  
`s`：脚本  
`b`：buffer  
`w`：window  
`g`：全局  

## 代码折叠
折叠{,}
```
#!vim
set foldmarker={,}
set foldmethod=marker
```

## 其他
```
#!vim
'保存语法高亮到html

runtime! syntax/2html.vim

'重新加载文件
edit 

'设置语法高亮语言
set syntax=perl

'使用sudo保存文件
w !sudo tee %
```