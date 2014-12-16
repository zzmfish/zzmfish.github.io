### ssh无密码登录
```
#!bash
#生成密钥对
ssh-keygen -t rsa

#复制公钥到目标主机
cat ~/.ssh/id_rsa.pub >> $RemoteHome/.ssh/authorized_keys

#设置目标主文件权限
chmod 700 $RemoteHome/.ssh
chmod 600 $RemoteHome/.ssh/authorized_keys
```