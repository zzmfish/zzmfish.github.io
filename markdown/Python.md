# Python经验技巧

[TOC]

## 数据类型
### 常量
```
#!python
__builtins__    #全局的内置符号，可以添加删除项  
__file__         #py文件全路径  
```

### 整数
```
#!python
sys.maxint   #最大整数
```

### 列表
```
#!python
squares = [x**2 for x in range(10)]    #列表推导式
list.sort()                                                  #排序
del list[i]                                                  #删除给定索引的元素
list.remove(v)                                         #删除给定值的元素
```  

### 一般
```
#!python
obj2 = copy.deepcopy(obj1)     #深度拷贝
type(u'123') is unicode              #类型判断
```  
## 内置库
### 正则表达式
```
#!python
re.match(pattern, string)    #匹配开头
re.search(pattern, string)   #匹配任意位置  
re.findall(pattern, string)    #匹配全部
```

### 字符集
```
#!python
f = codecs.open('out.txt', mode="w", encoding="utf-8") #以指定编码打开文件
```

### 数据编码
```
#!python
json.dumps(s)                 #输出json
base64.b64encode(s)   #输出成base64
urllib.quote(str)              #url编码
urllib.unquote(str)         #url解码
```

## 第三方库
网络爬虫：***Scrapy***  
网站开发：***tornado***  
代码高亮：***Pygments***    
模板引擎：***jinja2***  

## 调试分析
### pdb
```
#!python
pdb.set_trace()            #设置断点
```

### traceback
```
#!python
traceback.print_stack()    #显示堆栈
```

### gc
```
#!python
gc.get_referrers(obj)         #得到引用列表
```

### objgraph
```
#!python
import objgraph
browsers = objgraph.by_type('user_browser')
#显示引用关系
objgraph.show_backrefs(browsers[0], max_depth=10, filename="browser.dot") 
objgraph.show_most_common_types(20)  #显示数量最多的类型
```

### line\_profiler
```
#!bash
kernprof.py -l -v $PyFile $PyArgs
```

## 性能优化
### PyPy解析器

## 模块安装
### 编译安装到$HOME/local
```
#!bash
export PYTHONPATH=$HOME/local/lib/python2.7/site-packages:$PYTHONPATH
python setup.py build
python setup.py install --prefix=$HOME/local
```

### pip安装库
```
#!bash
sudo apt-get install python-pip
sudo pip install <库名>
```