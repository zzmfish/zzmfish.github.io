# SVN经验技巧


##### 添加
```bash
#添加目录，但不添文件
svn add --depth=empty $DirName
svn add -N $Dir
```
##### 更新
```bash
#更新到指定版本
svn update -r$Version $FileName
```

##### 撤销
```
#!bash
#撤销本地修改
svn revert $File

#撤销目录修改、撤销添加目录
svn revert $Dir -R
```

##### 属性
```bash
#添加可执行属性
svn propset svn:executable ON $FileName
```

##### 合并
```bash
#合并分支
svn merge $BranchPath

#合并版本间的修改
svn merge $BranchPath -r$Version1:$Version2

#回滚
svn merge -r$Version2:$Version1

#冲突使用本地版本
svn resolve --accept mine-full  $FileName

#显示合并信息
svn mergeinfo .
svn propget svn:mergeinfo .
svn propget -r$Version svn:mergeinfo .
```
##### 分支
```
#!bash
#创建分支
svn copy $Path1 $Path2 -m $Message

#列出所有tag
svn ls "^/tags"
```

##### 外部引用
```bash
#引用外部文件  
#格式：svn路径（可使用相对路径） 本地路径
svn propedit svn:externals  .
```
##### 服务器
```
#!bash
#切换服务器
svn switch --relocate $Url1 $Url2
```

## 编译安装
```
#!bash
#安装apr
wget http://mirrors.ibiblio.org/apache//apr/apr-1.5.1.tar.gz
tar zxf apr-1.5.1.tar.gz
cd apr-1.5.1
./configure --prefix=$HOME/zhouzm/local
make
make install

#安装apr-utils
wget http://apache.fayea.com//apr/apr-util-1.5.4.tar.gz
tar zxf apr-util-1.5.4.tar.gz
cd apr-util-1.5.4
./configure --prefix=/home/bigdata/zhouzm/local --with-apr=$HOME/zhouzm/local
make
make install

#安装scons
wget http://sourceforge.net/projects/scons/files/scons/2.3.4/scons-2.3.4.tar.gz/download
tar zxf scons-2.3.4.tar.gz
cd scons-2.3.4
python setup.py build
python setup.py install --prefix=$HOME/zhouzm/local/
cd -

#安装serf
wget http://serf.googlecode.com/svn/src_releases/serf-1.3.8.tar.bz2
tar jxf serf-1.3.8.tar.bz2 
cd serf-1.3.8
scons APR=/home/bigdata/zhouzm/local/bin/apr-1-config APU=/home/bigdata/zhouzm/local OPENSSL=/usr PREFIX=$HOME/zhouzm/local
scons install
cd -

#安装subversion
wget http://apache.mirrors.hoobly.com/subversion/subversion-1.8.11.tar.bz2
tar jxf subversion-1.8.11.tar.bz2
cd subversion-1.8.11
wget http://www.sqlite.org/sqlite-amalgamation-3071501.zip
unzip sqlite-amalgamation-3071501.zip
mv sqlite-amalgamation-3071501 sqlite-amalgamation
./configure --prefix=/home/bigdata/zhouzm/local --with-serf=yes
make
make install


```