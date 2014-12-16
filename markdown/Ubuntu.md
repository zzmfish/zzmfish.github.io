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
```
#!bash
#显示软件信息
sudo apt-cache show -a $Package  

#显示已安装软件
dpkg --get-selections

#显示文件所属软件
apt-file search $File

#添加PPA源
sudo add-apt-repository $Package

#重新安装软件
sudo apt-get install $Package --reinstall  
```

## 系统安装
```
#!bash
#安装windows后恢复Ubuntu引导，先从Ubuntu光盘引导
mount /dev/sda10 /mnt  
grub-install --root-directory=/mnt /dev/sda  
update-grub2 #不是必须
```

#### 启动器文件（后缀方式.desktop）
```
[Desktop Entry]
Version=x.y
Name=ProgramName
Comment=This is my comment
Exec=/home/alex/Documents/exec.sh
Icon=/home/alex/Pictures/icon.png
Terminal=false
Type=Application
Categories=Utility;Application;
```
## 其他
```
#!bash
#查看时间设置
timedatectl status

#查看显卡信息
sudo lshw -class video

#VirtualBox使用usb设备要加入vboxusers组
sudo adduser zhouzm vboxusers  

#安装新字体（包括微软字体）
cp $FontFile ~/.fonts

#解决无法访问.local域名（方法1）
echo "hosts: files dns" >> /etc/nsswitch.conf

#解决无法访问.local域名（方法2）
sudo service avahi-daemon stop
sudo update-rc.d avahi-daemon remove
```
显示分辨率太小，增大`/etc/X11/xorg.conf`的`HorizSync`范围