### 准备
* /etc/hosts文件
* 无密码sudo的帐号


```bash
#添加hadoop账号
sudo useradd hadoop
sudo passwd hadoop

#设置hadoop执行sudo无需密码
echo "hadoop ALL = NOPASSWD: ALL" | sudo tee -a /etc/sudoers

su - hadoop
wget http://archive.cloudera.com/cm5/installer/latest/cloudera-manager-installer.bin
chmod u+x cloudera-manager-installer.bin
sudo ./cloudera-manager-installer.bin
```
### 删除
```
#!bash
sudo rm -Rf /usr/share/cmf /var/lib/cloudera* /var/cache/yum/cloudera* /etc/cloudera*
```

## 参考
* [Cloudera Installation and Upgrade](http://www.cloudera.com/content/cloudera/en/documentation/core/latest/topics/installation.html)