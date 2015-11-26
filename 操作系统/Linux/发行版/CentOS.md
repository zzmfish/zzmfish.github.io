```
#!bash
yum update
```

###### 安装
```bash
#安装和启动图形界面
sudo yum -y groups install "GNOME Desktop"
startx

#安装开发工具
sudo yum groupinstall "Development Tools"

#安装内核头文件（VirtualBox模块需要）
sudo yum install kernel-devel
```
###### 关闭防火墙
```
#!bash
sudo echo "-A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport $Port -j ACCEPT" >> /etc/sysconfig/iptables
sudo service iptables restart
```

###### 安装中文字体
```
#!bash
sudo yum install cjkuni-fonts-common cjkuni-uming-fonts cjkuni-ukai-fonts cjkuni-fonts-ghostscript bitmap-fangsongti-fonts
```

## 参考
* [Centos 7/Windows 7 Dual Boot Problem](http://www.experts-exchange.com/OS/Linux/Q_28517724.html)
* [CentOS 6 / RHCE 6 禁用IPv6协议模块](http://www.ttlsa.com/linux/centos6-rhce6-disables-the-ipv6-protocol-module/)