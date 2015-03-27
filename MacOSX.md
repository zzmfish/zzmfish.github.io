# Mac OS X

## 安装软件
* [How to install cscope for Mac OS X 10.6](http://stackoverflow.com/questions/9386127/how-to-install-cscope-for-mac-os-x-10-6)

## 未分类
```
#!bash
#下载文件
curl -O $Url
```

* Homebrew
* 
### libxml的头文件位置
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.9.sdk/usr/include/libxml2/libxml/HTMLparser.h


## 系统信息
```
#!bash
#系统概况
system_profiler -detailLevel mini 

#CPU信息
sysctl -n machdep.cpu.brand_string
```

###### ssh挂载
```
#!bash
sshfs -p 9922 zhouzm@devy.ucweb.local:/home1/zhouzm mount/devy/
```
* [FUSE for OS X](http://osxfuse.github.io)

## 与Linux的区别
* 没有adduser/useradd/free命令
* 没有/proc文件系统