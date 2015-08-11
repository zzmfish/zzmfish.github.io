### 准备
* /etc/hosts文件
* 无密码sudo的帐号


```bash
#添加hadoop账号
sudo useradd hadoop
sudo passwd hadoop

#设置ssh
sudo apt-get install openssh-server

#设置hadoop执行sudo无需密码
echo "hadoop ALL = NOPASSWD: ALL" | sudo tee -a /etc/sudoers

#安装MySQL
echo "create user 'hive'@'%' IDENTIFIED BY '123456';
    create user 'amon'@'%' IDENTIFIED BY '123456';
    create database hive;
    create database amon;
    GRANT ALL PRIVILEGES ON hive.* TO 'hive'@'%' IDENTIFIED BY '123456';
    GRANT ALL PRIVILEGES ON amon.* TO 'amon'@'%' IDENTIFIED BY '123456';
    " | mysql -uroot -p123456

su - hadoop
wget http://archive.cloudera.com/cm5/installer/latest/cloudera-manager-installer.bin
chmod u+x cloudera-manager-installer.bin
sudo ./cloudera-manager-installer.bin
```

* 浏览器打开：http://localhost:7180/
* 选择“Cloudera Express”

### 卸载
```
#!bash
sudo /usr/share/cmf/uninstall-cloudera-manager.sh
sudo rm /etc/cloudera-scm-server/db.properties
sudo rm -Rf /usr/share/cmf /var/lib/cloudera* /var/cache/yum/cloudera* /etc/cloudera*
```

## 参考
* [Cloudera Installation and Upgrade](http://www.cloudera.com/content/cloudera/en/documentation/core/latest/topics/installation.html)
* [JDBC driver cannot be found](https://groups.google.com/a/cloudera.org/forum/#!topic/cdh-user/OpXSfmzsnuo)
* [Uninstalling Cloudera Manager and Managed Software](http://www.cloudera.com/content/cloudera/en/documentation/core/latest/topics/cm_ig_uninstall_cm.html)