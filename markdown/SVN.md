# SVN经验技巧

## 工作区
```
#!bash
svn revert <文件>                                                         #撤销本地修改
svn revert $DirName -R                                              #撤销目录修改、撤销添加目录
svn merge -r$Version2:$Version1>                           #回滚代码
svn resolve --accept mine-full  $FileName              #冲突使用本地版本
svn update -r$Version $FileName                            #更新到执行版本
```

## 分支
创建分支：`svn copy <原分支url> <新分支url> -m "message" `  
列出所有tag：`svn ls "^/tags" `  
合并分支：`svn merge <分支url>`  
合并版本间的修改：`svn merge <分支url> -r<版本1>:<版本2> `  

## 其他
切换服务器：`svn switch --relocate <原url> <新url>`