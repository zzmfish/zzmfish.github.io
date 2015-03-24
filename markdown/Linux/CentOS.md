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