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
#203.88.167.174:8081映射到本机8081
ssh -C -N -L 8081:203.88.167.174:8081 bigdata@usa-mob437 -p 9922
```

##### scp
```
#!bash
scp -P $Port $LocalFile $User@$Host:$Path
#如:
scp -P 9922 release.tgz product@localhost:/home/product/workspace/server
```

##### sshfs
```
#!bash
sshfs -o nonempty -p 9922 nemo@slave1: /home/zhouzm/mount/slave1
```

##### 禁止外网登陆
* /etc/pam.d/sshd的account行前面加：
```
account    required     pam_access.so
```

* /etc/security/access.conf增加

```
+ : ALL : 10.0.0.1/8 127.0.0.1/8 LOCAL
- : ALL EXCEPT navi : ALL
```

### 登录日志
/var/log/secure

### 使用密钥对传输加密数据
```bash
#创建秘钥
openssl genrsa -out user_mode_query.key 1024

#创建公钥
openssl rsa -in user_mode_query.key -pubout -out user_mode_query.key.pub

#加密和解密
date +%s  | openssl rsautl -encrypt -inkey user_mode_query.key.pub -pubin | openssl rsautl -decrypt -inkey user_mode_query.key
```

## 参考
* [利用openssl进行RSA加密解密](http://www.cnblogs.com/alittlebitcool/archive/2011/09/22/2185418.html)
* [Putty建立隧道的方法](http://www.putty.ws/putty-tunnel-methods)