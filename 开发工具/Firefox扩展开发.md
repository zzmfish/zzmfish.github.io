#  Firefox扩展开发

## 安装和设置SDK
### 下载和解压
```
#!bash
wget https://ftp.mozilla.org/pub/mozilla.org/labs/jetpack/jetpack-sdk-latest.tar.gz
tar zxf jetpack-sdk-latest.tar.gz
```
### 设置环境
每次开发前都要一次，只在当前终端生效：
```
cd addon-sdk-1.17
source bin/activate
```
终端提示符会出现”(firefox-addon-sdk-1.7)“字样，表示设置生效。

## 开发扩展


### 创建项目
```
#!bash
#先创建目录，目录名同时也是扩展名称
mkdir $AddOnName
cd $AddOnName
#初始化扩展，生成一些目录和文件，可以编译成Firefox扩展，但没有实际功能
cfx init
```

### 开发功能
lib/main.js是扩展入口文件，一般从这里开始修改。可以参考这个[例子](https://developer.mozilla.org/en-US/Add-ons/SDK/Tutorials/Getting_started)。

## 测试运行
### 使用干净profile  
运行过程中任何Firefox设置都不会保留：
```
cfx run
```
### 使用指定profile
可以安装其他扩展，任何Firefox设置都会保留。比如使用名为dev的profile：
```
cfx -p dev run
```
当前目录下会生成名dev的目录，里面保存了profile数据，注意不要提交到svn。

## 调试
点击工具栏菜单上的”***附加组件***“按钮，进入“***附加组建管理器***”，选“***扩展***”，点击对应扩展旁边的”***调试***“按钮，点”***确定***“允许连接，即进入调试界面，可以设置断点、查看变量值等。


## 打包发布
打包成xpi文件，在Firefox打开这个文件，即可以安装扩展。
```
#!bash
cfx xpi
```

## 参考
* [安装](https://developer.mozilla.org/en-US/Add-ons/SDK/Tutorials/Installation)
* [child_process.spawn](https://developer.mozilla.org/en-US/Add-ons/SDK/Low-Level_APIs/system_child_process)