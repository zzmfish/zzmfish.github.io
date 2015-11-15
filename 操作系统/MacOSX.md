## 命令

```bash
#系统概况
system_profiler -detailLevel mini 

#CPU信息
sysctl -n machdep.cpu.brand_string

#启动iNodeService
sudo /Library/StartupItems/iNodeAuthService/iNodeAuthService start
```

## 软件
* [VNC Viewer](http://www.realvnc.com/)
* [FUSE for OS X](http://osxfuse.github.io)


## 开发
* ***libxml头文件：*** /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.9.sdk/usr/include/libxml2/libxml/HTMLparser.h
* ***JAVA HOME目录：***/Library/Java/JavaVirtualMachines/jdk1.8.0_25.jdk/Contents/Home/

## 快捷键
| 功能   | 快捷键                    | 说明 |
|------  |--------                   |------|
全屏截图 |`command` + `shift` + `3`  |保存到桌面上
部分截图 |`command` + `shift` + `4`  |保存到桌面上

## 对比Linux
* 缺少命令：adduser、useradd、free
* 缺少目录：/proc

## 参考
* [Running Mac OS X's built-in DHCP server](http://www.jacquesf.com/2011/04/mac-os-x-dhcp-server/)
* [Mac OS X，糟透了的软件安装体验](http://ksmx.me/broken-user-experience-of-installation-applications-on-mac-os-x/)
* [简洁优雅的Mac OS X软件安装体验 - homebrew-cask](http://ksmx.me/homebrew-cask-cli-workflow-to-install-mac-applications/)
* [How to install cscope for Mac OS X 10.6](http://stackoverflow.com/questions/9386127/how-to-install-cscope-for-mac-os-x-10-6)