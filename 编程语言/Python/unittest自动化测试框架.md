项目代码越来越复杂，并且对质量要求越来越高，就开始需要自动化测试。

### 测试框架对比
python有很多自动化测试框架可以选择：  

* python自带的[unittest](https://docs.python.org/2/library/unittest.html)
* 第三方的[Robot Framework](http://robotframework.org/)
* 其他第三方测试框架：PyUnit等

对开发人员来说，一般不想在测试上花太多时间，因此希望这个测试框架容易学习、使用方便，功能不用很强大，但可以满足一般需要。

中间件测试团队是使用Robot Framework，这个测试框架会在python上加一个中间层，并要求使用一种中间语言来编写案例。这种中间语言的好处是方便非开发人员编写测试案例，并且方便系统集成（比如通过图形化的工具创建案例）。但对python开发人员是大大增加了学习和使用的成本，所以开发人员一般不是很想使用。

对于其他第三方测试框架，没有详细了解过。个人觉得如果和python自带的差不多的话，选自带的就好了。

所以还是觉得使用unittest比较好。

### unittest基本使用
unittest的使用非常简单。需要定义TestCase类的派生类，其中每一个“test_”开头的函数都是一个测试案例，如：

```
#!python
import unittest
class Test1(unittest.TestCase):
    def test_case1(self):
        self.assertTrue(True)
        
    def test_case2(self):
        self.assertTrue(True)
```

保存并运行test.py（-v选项是输出详细信息）：
```
#!bash
python -m unittest -v test
```


只执行test.Test1的测试案例：
```
#!bash
python -m unittest -v test.Test1
```

只执行test.Test1.test_case1案例：
```
#!bash
python -m unittest -v test.Test1.test_case1
```

### 结合seleium测试网站
如果要测试网站，可以使用unittest结合[selenium](http://www.seleniumhq.org/)控制浏览器打开网页，并检查网页。selenium提供丰富的API，还可以实现点击按钮、执行js等操作。比如这段代码实现了打开百度网页、检查"百度一下"按钮的自动化测试：
```
#!python
import unittest
from selenium import webdriver

class Test1(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_case1(self):
        self.browser.get('http://www.baidu.com')
        self.browser.find_element_by_xpath(u'//input[@value="百度一下"]')
```

### HTML报告
如果觉得unittest的屏幕输出太单调（或者说混乱），可以使用[HTMLTestRunner](https://pypi.python.org/pypi/HTMLTestRunner)。这个工具可以调用unittest执行测试，把测试结果输出为html文件。打开html可以看到用不同颜色区分的案例测试结果，可以折叠或展开案例，并看到案例对应的屏幕输出。
```
#!bash
python ~/third_party/HTMLTestRunner.py test  #执行test.py
```