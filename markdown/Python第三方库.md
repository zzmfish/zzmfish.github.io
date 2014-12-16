# python第三方库

## 安装
#### 源码安装
```bash
export PYTHONPATH=$HOME/local/lib/python2.7/site-packages:$PYTHONPATH
python setup.py build  #或build_ext，不知有什么区别
python setup.py install --prefix=$HOME/local
```

#### pip
```bash
sudo apt-get install python-pip            #安装pip
pip search $PackageName                    #搜索包
sudo pip install $PackageName              #安装包
sudo pip install --upgrade $PackageName    #更新包
```

### 第三方库
网络爬虫：***Scrapy***  
网站开发：***tornado***  
代码高亮：***Pygments***    
模板引擎：***jinja2***  
矩阵运算：***numpy***  
科学计算：***SciPy***  
作图：***matplotlib***  
线程池：***threadpool***