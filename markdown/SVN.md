# SVN经验技巧

## 工作区
```
#!bash
#撤销本地修改
svn revert $File

#撤销目录修改、撤销添加目录
svn revert $Dir -R

#回滚代码
svn merge -r$Version2:$Version1>

#冲突使用本地版本
svn resolve --accept mine-full  $File

#更新到指定版本
svn update -r$Version $File
```

## 分支
```
#!bash
#创建分支
svn copy $Path1 $Path2 -m $Message

#列出所有tag
svn ls "^/tags"

#合并分支
svn merge $Path

#合并版本间的修改
svn merge $Path -r$Version1:$Version2
```

## 其他
```
#!bash
#切换服务器
svn switch --relocate $Url1 $Url2
```