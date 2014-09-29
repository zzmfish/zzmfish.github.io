# Git经验技巧

## 初始化
初始化仓库：`git init`  

## 分支
列出所有分支：`git branch`  
切换到主线：`git checkout master`  
列出所有里程碑：`git tag`
显示origin远程分支：`git remote show origin`  
跟踪分支：`git branch --set-upstream-to=origin/<分支名> <分支名>`  
推送到远程分支：`git push origin <分支名>`  

## 工作区
保存当前工作进度：`git stash`  
提交所有本地变更的文件：`git commit -a`  
修改提交注释：`git commit --amend`  

使用工具对比：`git difftool <文件名>`  
显示引用对应的提交ID：`git rev-parse`  

## 子模组
添加子模组：`git submodule add <git路径> <本地路径>`  
检出子模组：`git submodule init`  
更新子模组：`git submodule update`  

##设置
对比工具为vimdiff：`git config --global diff.tool vimdiff`  
显示中文文件名：`git config --global core.quotepath false`  

## 其他
`master`：分支master中的最新提交  
`HEAD`：版本库的最近一次提交  
图形工具：`gitg`