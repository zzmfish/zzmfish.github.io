# Python经验技巧

[TOC]

## 数据类型
### 常量
```
#!python
__builtins__    #全局的内置符号，可以添加删除项  
__file__        #py文件全路径  
__name__        #'__main__'
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
lst.sort()                             #排序
random.shuffle(lst)                    #打乱顺序
del lst[i]                             #删除给定索引的元素
lst.remove(v)                          #删除给定值的元素
lst.insert(0, v)                       #在前面插入
lst.append(v)                          #在后面插入
```  

### 集合
```
#!python
s.add(x) 	  	#添加一个元素
s.remove(x) 	#删除一个元素，或抛出KeyError
s.discard(x) 	#删除一个元素
s.pop()         #弹出一个元素，或抛出KeyError
s.update(s2)    #合并集合
s = s.union(s2) #合并集合
```

## 内置库
### 正则表达式
```
#!python
re.match(pattern, string)      #匹配开头
re.search(pattern, string)     #匹配任意位置  
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
json.dumps(s)         #输出json
base64.b64encode(s)   #输出成base64
urllib.quote(str)     #url编码
urllib.unquote(str)   #url解码
md5.md5(str)          #md5
```

### numpy

## 第三方库
网络爬虫：***Scrapy***  
网站开发：***tornado***  
代码高亮：***Pygments***    
模板引擎：***jinja2***  
矩阵运算：***numpy***  
科学计算：***SciPy***  
作图：***matplotlib***  
线程池：***threadpool***

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
gc.get_referrers(obj)      #得到引用列表
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

## 模块安装
```
#!bash
#源码安装
export PYTHONPATH=$HOME/local/lib/python2.7/site-packages:$PYTHONPATH
python setup.py build
python setup.py install --prefix=$HOME/local

#pip
sudo apt-get install python-pip            #安装pip
pip search $PackageName                    #搜索包
sudo pip install $PackageName              #安装包
sudo pip install --upgrade $PackageName    #更新包
```

## 工具
### PyPy解析器


## 未分类
```
#!python
#美化显示
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)

#深度拷贝
obj2 = copy.deepcopy(obj1)

#类型判断
type(u'123') is unicode
isinstance(u'123', unicode)

#参数解析
import argparse
parser = argparse.ArgumentParser(description='say_hello')
parser.add_argument('--say_hello', dest="say_hello", action='store_true')
parser.add_argument('--table', type=str, default='')
args = parser.parse_args()
return args  

#文件系统
os.makedirs(path)    #递归创建目录
os.listdir(path)     #列出目录内容
glob.glob('*/*.gif')     #列出匹配的文件
```