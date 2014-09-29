# SVN经验技巧

## 工作区
撤销本地修改：`svn revert <文件>`  
回滚代码：`svn merge -r<版本2>:<版本1>`  
解决冲突，使用我的版本：`svn resolve --accept mine-full  <文件>`  
更新到指定版本：`svn update -r<版本> <文件>`  
更新到最新版本：`svn update <文件>`  

## 分支
创建分支：`svn copy <原分支url> <新分支url> -m "message" `  
列出所有tag：`svn ls "^/tags" `  
合并分支：`svn merge <分支url>`  
合并版本间的修改：`svn merge <分支url> -r<版本1>:<版本2> `  

## 其他
切换服务器：`svn switch --relocate <原url> <新url>`