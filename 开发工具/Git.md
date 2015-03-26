# Git经验技巧

## 初始化
```
#!bash
#初始化仓库
git init
```

## 分支
```
#!bash
#列出所有分支
git branch

#切换到主线
git checkout master

#列出所有里程碑
git tag

#检出tag
git checkout $TagName

#显示origin远程分支
git remote show origin

#跟踪分支
git branch --set-upstream-to=origin/$BranchName $BranchName

#推送到远程分支
git push origin $BranchName

#删除远程分支
git push origin --delete $BranchName
```

## 工作区
```
#!bash
#保存当前工作进度
git stash

#提交所有本地变更的文件
git commit -a  

#修改提交注释
git commit --amend  

#显示引用对应的提交ID
git rev-parse  
```

## 历史
```
#!bash
#显示修改的文件名
git log --name-status

#使用工具对比
git difftool $File
```

## 子模组
```
#!bash
#添加子模组
git submodule add $GitUrl $LocalPath

#检出子模组
git submodule init    #注册到.git/config
git submodule update

#子模组状态
git submodule status
```

##设置
```
#!bash
#对比工具为vimdiff
git config --global diff.tool vimdiff


#显示中文文件名
git config --global core.quotepath false
```

## git svn
```
#!bash
#安装新版git
sudo apt-get install libsvn-perl
make configure
./configure --prefix=$HOME/local
make -j3
make install
```

## GitHub
* [Creating Project Pages manually](https://help.github.com/articles/creating-project-pages-manually/)


## 其他
***master***：分支master中的最新提交  
***HEAD***：版本库的最近一次提交  
图形工具：***gitg***