# Mac OS X

##### 安装软件
* [How to install cscope for Mac OS X 10.6](http://stackoverflow.com/questions/9386127/how-to-install-cscope-for-mac-os-x-10-6)

##### 未分类
```
#!bash
#下载文件
curl -O $Url
```

* Homebrew
* VNC Viewer: http://www.realvnc.com/
##### libxml的头文件位置
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.9.sdk/usr/include/libxml2/libxml/HTMLparser.h

* JAVA HOME
```bash
export JAVA_HOME="/Library/Java/JavaVirtualMachines/jdk1.8.0_25.jdk/Contents/Home/"
```
##### 系统信息
```
#!bash
#系统概况
system_profiler -detailLevel mini 

#CPU信息
sysctl -n machdep.cpu.brand_string
```
##### 启动iNodeService
```
#!bash
sudo /Library/StartupItems/iNodeAuthService/iNodeAuthService start
```

##### ssh挂载
```
#!bash
sshfs -p 9922 zhouzm@devy.ucweb.local:/home1/zhouzm mount/devy/
```
* [FUSE for OS X](http://osxfuse.github.io)

##### 截屏
* 全屏截图：苹果键（花键）+ Shift键 + 3
* 部分截图：苹果键（花键）+ Shift键 + 4

## 与Linux的区别
* 没有adduser/useradd/free命令
* 没有/proc文件系统

## 参考
* [Running Mac OS X's built-in DHCP server](http://www.jacquesf.com/2011/04/mac-os-x-dhcp-server/)