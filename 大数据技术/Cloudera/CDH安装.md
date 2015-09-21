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

sudo apt-get purge 'cloudera-manager-*'
sudo apt-get autoremove

sudo rm -Rf \
    /etc/cloudera* \
    /etc/hadoop* \
    /etc/hive \
    /etc/hive-* \
    /etc/hbase* \
    /etc/spark \
    /etc/solr \
    /etc/oozie \
    /etc/pig \
    /etc/impala \
    /etc/zookeeper \
    /usr/share/cmf/ \
    /var/cache/yum/cloudera* \
    /var/lib/cloudera* \
    /var/lib/cloudera* \
    /var/lib/sqoop* \
    /var/log/cloudera-* \
    /var/run/cloudera* \
    $(NULL)

#清除HDFS目录
sudo rm -rf /dfs/

#关闭7432端口的postres进程
```

## 参考
* [Cloudera Installation and Upgrade](http://www.cloudera.com/content/cloudera/en/documentation/core/latest/topics/installation.html)
* [JDBC driver cannot be found](https://groups.google.com/a/cloudera.org/forum/#!topic/cdh-user/OpXSfmzsnuo)
* [Uninstalling Cloudera Manager and Managed Software](http://www.cloudera.com/content/cloudera/en/documentation/core/latest/topics/cm_ig_uninstall_cm.html)