# Python常用例程

#### 正则表达式
```python
re.match(pattern, string)      #匹配开头
re.search(pattern, string)     #匹配任意位置  
re.findall(pattern, string)    #匹配全部
```

#### 字符集
```python
f = codecs.open('out.txt', mode="w", encoding="utf-8") #以指定编码打开文件
```

#### 文件系统
```python
os.makedirs(path)    #递归创建目录
os.listdir(path)     #列出目录内容
glob.glob('*/*.gif')     #列出匹配的文件
```

#### 数据编码
```python
json.dumps(s)         #输出json
base64.b64encode(s)   #输出成base64
urllib.quote(str)     #url编码
urllib.unquote(str)   #url解码
md5.md5(str)          #md5
```

#### 参数解析
```python
parser = argparse.ArgumentParser(description='say_hello')
parser.add_argument('--say_hello', dest="say_hello", action='store_true')
parser.add_argument('--table', type=str, default='')
args = parser.parse_args()
```

#### HTTP请求
```
#!python
req = urllib2.Request(url = url, data = data) #data为空则是GET
print urllib2.urlopen(req).read()
```

#### 通过管道调用进程
```
#!python
args = ['java', '-jar', 'plantuml.jar', '-pipe', '-tpng']
pipe = subprocess.Popen(args, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
pipe.stdin.write(input_data)
pipe.stdin.close()
print pipe.stdout.read()
```

#### 调用动态库
```
#!python
api = ctypes.CDLL('libfoo.so', DLFCN.RTLD_LAZY)
api.foo.argtypes = [ctypes.c_char_p, ctypes.c_int]
api.foo.restype = ctypes.c_int
res = api.foo(msg, len(msg)
```

#### 未分类
```python
#美化显示
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)
```