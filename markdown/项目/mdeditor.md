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

### Markdown-LaTeX扩展
* [链接](https://github.com/justinvh/Markdown-LaTeX)
* 依赖[latex](http://www.latex-project.org/)
* 依赖[dvipng](http://sourceforge.net/projects/dvipng/)、libpng

## 计划
### 支持数学公式
* 使用markdown-latex扩展      --0.5h
* 安装latext、dvipng、libpng  --0.5h


### 界面样式优化
* 弹出设置界面       --1h
* 设置渲染代码样式   --1h
* 设置编辑代码样式   --1h
* 设置页面主题       --1h

### 编辑功能优化
* 创建新文件  --1h
* 文件列表优化  --1h

### UML/Dot图
* 参考markdown-latex  --0.5h
* 错误处理   --1h
* 学习markdown扩展API [链接](https://pythonhosted.org/Markdown/extensions/api.html)    --0.5h
* 编写markdown扩展demo   --1h
* 实现uml显示  --1h
* 实现dot显示  --0.5h
* 实现latex显示  --1h

### 菜单效果
* 用什么库？
* 


## 未分类
#### 不错的CSS效果
* http://tarruda.github.io/bootstrap-datetimepicker/  
* 印象笔记

#### 作图
Gliffy