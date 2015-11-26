# mdeditor

@(zzmfish 的笔记本)[我的软件]

## [markdown库](https://pythonhosted.org/Markdown/)
### CodeHilite扩展
* [链接](https://pythonhosted.org/Markdown/extensions/code_hilite.html)
设置样式：
```
pygments_style: 'perldoc'
```
* 依赖[Pygments](http://pygments.org/)
所有样式：
```python
list(pygments.styles.get_all_styles())
```
* [预览](http://help.farbox.com/pygments.html)


## 未分类
#### 不错的CSS效果
* http://tarruda.github.io/bootstrap-datetimepicker/  
* 印象笔记

#### 作图
Gliffy


#### windows错误
```
    Traceback (most recent call last):
      File "D:\Python27\lib\site-packages\tornado\web.py", line 1346, in _execute
        result = method(*self.path_args, **self.path_kwargs)
      File "D:\github\mdeditor-work\file_handler.py", line 21, in get
        text = file_manager.load_file(name) or ''
      File "D:\github\mdeditor-work\file_manager.py", line 49, in load_file
        file_path = self.get_file_path(name)
      File "D:\github\mdeditor-work\file_manager.py", line 31, in get_file_path
        return os.path.join(config.md_dir, '%s.md' % name)
      File "D:\Python27\lib\ntpath.py", line 84, in join
        result_path = result_path + p_path
    UnicodeDecodeError: 'ascii' codec can't decode byte 0xcf in position 3: ordinal not in range(128)

```