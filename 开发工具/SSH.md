##### 无密码登录
```
#!bash
#生成密钥对
ssh-keygen -t rsa

#复制公钥到目标主机
cat ~/.ssh/id_rsa.pub >> $RemoteHome/.ssh/authorized_keys

#设置目标主文件权限
chmod 700 $RemoteHome
chmod 700 $RemoteHome/.ssh
chmod 600 $RemoteHome/.ssh/authorized_keys
```

##### 反向代理
参数：

* -R：反向端口映射
* -N：不执行shell
* -C：压缩
```
#!bash
ssh -C -N -R $Port:$Host:$HostPort $SshUser@$SshHost -p $SshPort
#如把fsvn.ucweb.local:443映射到usa-mob437:9943
ssh -C -N -R 9443:fsvn.ucweb.local:443 bigdata@usa-mob437 -p 9922
```

##### scp
```
#!bash
scp -P $Port $LocalFile $User@$Host:$Path
#如:
scp -P 9922 release.tgz product@localhost:/home/product/workspace/server
```
### 登录日志
/var/log/secure