# Ubuntu经验技巧

标签（空格分隔）： 未分类

---

## 常用软件包
|  用途                                 |        软件包                      | 其他操作            |
|---------                              |------------------                  |----------
|受限软件（视频解码器、ms字体、flash）  | ubuntu-restricted-extras           |
| 32位库                                | <包名>:i386                        |
| ssh服务                               | openssh-server                     |
| fcitx输入法                           | fcitx,fcitx-googlepinyin,im-switch | im-switch -s fcitx  |
| 增加“在终端打开”文件夹菜单            | nautilus-open-terminal             | nautilus -q         |
| wxWidget for Python                   | python-wxgtk2.8


## 软件包管理
显示软件信息：`sudo apt-cache show -a <包名>`  
显示文件所属软件：`apt-file search <文件名>`  
添加PPA源：`sudo add-apt-repository <名称>`  
重新安装软件：`sudo apt-get install <包名> --reinstall`  

## 引导和安装
安装windowns之后恢复ubuntu引导，从ubuntu安装光盘引导  
```
mount /dev/sda10 /mnt  
grub-install --root-directory=/mnt /dev/sda  
update-grub2（不是必要）  
```
---
[硬盘安装](http://askubuntu.com/questions/340156/install-ubuntu-from-iso-image-directly-from-hard-disk-of-a-system-running-linux)  
```
menuentry "Kubuntu ISO" {
    set isofile="/boot/iso/kubuntu-12.04.iso"  
    loopback loop (hd0,8)$isofile  
    linux (loop)/casper/vmlinuz.efi boot=casper iso-scan/filename=$isofile noprompt noeject  
    initrd (loop)/casper/initrd.lz  
}  
```
或  
```
title Install Ubuntu  
root (hd0,0)  
kernel (hd0,0)/vmlinuz.efi boot=casper iso-scan/filename=/ubuntu-13.10-desktop-i386.iso ro quiet splash locale=zh_CN.UTF-8  
initrd (hd0,0)/initrd.lz  
```

## 其他
查看时间设置：`timedatectl status`  
查看显卡信息：`sudo lshw -class video`  
VirtualBox使用usb设备要加入vboxusers组：`sudo adduser zhouzm vboxusers`  
显示分辨率太小，增大`/etc/X11/xorg.conf`的`HorizSync`范围  
安装新字体（包括微软字体）：复制字体文件到`~/.fonts`  
---
无法访问.local内部域名，可编辑`/etc/nsswitch.conf`：`hosts:          files dns`  
或
```
sudo service avahi-daemon stop
sudo update-rc.d avahi-daemon remove
```

