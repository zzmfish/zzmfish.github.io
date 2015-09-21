```
#!bash
yum update
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