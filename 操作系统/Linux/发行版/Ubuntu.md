# Ubuntu

##### 软件管理
###### apt软件源
```
#!bash
#显示软件信息
sudo apt-cache show -a $PackageName  

#显示已安装软件
dpkg --get-selections

#显示文件所属软件
apt-file search $FileName

#显示已安装软件包包含的文件
sudo dpkg-query -L $PackageName

#显示未安装软件包包含的文件
sudo apt-get install apt-file
sudo apt-file update
sudo apt-file list $PackageName

#添加PPA源
sudo add-apt-repository $PackageName

#重新安装软件
sudo apt-get install $PackageName --reinstall 

#解决/var/lib/dpkg/available损坏
sudo dpkg --clear-avail

#解决/var/lib/dpkg/status损坏
cp /var/lib/dpkg/status-old /var/lib/dpkg/status
```

###### 常用软件包
|  用途                                 |        软件包                      | 其他操作            |
|---------                              |------------------                  |----------
|受限软件（视频解码器、ms字体、flash）  | ubuntu-restricted-extras           |
| 32位库                                | <包名>:i386                        |
| ssh服务                               | openssh-server                     |
| fcitx输入法                           | fcitx,fcitx-googlepinyin,im-switch | im-switch -s fcitx  |
| 增加“在终端打开”文件夹菜单            | nautilus-open-terminal             | nautilus -q         |
| wxWidget for Python                   | python-wxgtk2.8

###### 自动启动
从`/usr/share/applications`复制应用程序的desktop文件到`~/.config/autostart`

##### 系统安装
```
#!bash
#安装windows后恢复Ubuntu引导，先从Ubuntu光盘引导
mount /dev/sda10 /mnt  
grub-install --root-directory=/mnt /dev/sda  
update-grub2 #不是必须
```

### 显卡问题
```
#!bash
#检查桌面是否使用3d加速
/usr/lib/nux/unity_support_test -p

#查看显卡信息
sudo lshw -class video
```

##### 显示分辨率太小
增大`/etc/X11/xorg.conf`的`HorizSync`范围

##### nvidia驱动导致无法启动

进入恢复模式卸载：

```
#!bash
mount /dev/sda10 / -o remount,rw
apt-dpkg --get-selections | grep nvidia
apt-get remove --purge nvidia-XXX
```

##### 疑难问题
```
#!bash
#解决无法访问.local域名（方法1）
echo "hosts: files dns" >> /etc/nsswitch.conf

#解决无法访问.local域名（方法2）
sudo service avahi-daemon stop
sudo update-rc.d avahi-daemon remove

#解决顶栏没有显示时间
killall unity-panel-service
```

##### 其他
```
#!bash
#查看时间设置
timedatectl status

#VirtualBox使用usb设备要加入vboxusers组
sudo adduser zhouzm vboxusers  

#安装新字体（包括微软字体）
cp $FontFile ~/.fonts
```