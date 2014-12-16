# Python质量保证

### 单元测试
```
class TestSomething(unittest.TestCase):
    def test_something(self):
        self.assertTrue(do_something()
```
执行命令：
```bash
python -m unittest -v $Module
```

### selenium
```
#!python
class Test1(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_case1(self):
        #打开网页
        self.browser.get('http://www.baidu.com')

        #点击按钮
        button = self.browser.find_element_by_id('button1')
        button.click()

        #检查文字
        msg = self.browser.find_element_by_id('msg1')
        self.assertTrue(msg.text.startswith(u'查询完成! '))

```
* [pypi](https://pypi.python.org/pypi/selenium)

### 调试
```python
#设置断点
pdb.set_trace()

#显示堆栈
traceback.print_stack()

#对象引用
gc.get_referrers(obj)      

#对象列表
browsers = objgraph.by_type('MyClass')

#对象引用关系
objgraph.show_backrefs(browsers[0], max_depth=10, filename="MyClass.dot") 

#最多数量的对象
objgraph.show_most_common_types(20)  
```

### 性能分析
```bash
#每一行性能分析
kernprof.py -l -v $PyFile $PyArgs
```