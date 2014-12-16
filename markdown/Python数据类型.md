# Python数据类型

#### 常量
```python
__builtins__    #全局的内置符号，可以添加删除项  
__file__        #py文件全路径  
__name__        #'__main__'
```

#### 整数
```python
sys.maxint   #最大整数
```

#### 列表
```python
squares = [x**2 for x in range(10)]    #列表推导式
lst.sort()                             #排序
random.shuffle(lst)                    #打乱顺序
del lst[i]                             #删除给定索引的元素
lst.remove(v)                          #删除给定值的元素
lst.insert(0, v)                       #在前面插入
lst.append(v)                          #在后面插入
```  

#### 集合
```python
s.add(x)        #添加一个元素
s.remove(x)     #删除一个元素，或抛出KeyError
s.discard(x)    #删除一个元素
s.pop()         #弹出一个元素，或抛出KeyError
s.update(s2)    #合并集合
s = s.union(s2) #合并集合
```

#### 对象拷贝
```python
obj2 = copy.deepcopy(obj1)
```

#### 类型判断
```python
type(u'123') is unicode
isinstance(u'123', unicode)
```
