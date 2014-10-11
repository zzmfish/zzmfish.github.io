# Linux经验技巧

## 系统监控
```
#!bash
#查看监听端口
netstat -lnp --inet

#统计系统调用的耗时
strace -c -p $Pid

#分析进程IO
iotop

#查看线程的CPU占用
top -H -p $Pid
```

## 系统管理
```
#!bash
# 增加最大文件数
echo "zhouzm hard nofile 10240" >> /etc/security/limits.conf
restart
ulimit -n 10240

# 添加用户
useradd $UserName

# 设置时间
date -s "20:16"
```

## SSH
```
#!bash
#挂载远程目录
sshfs -p $Port $User@$Host:$Path $LocalPath
```
### ssh无密码登录
1. 本机生成密钥对
```
#!bash
ssh-keygen -t rsa
```  
2. 把`~/.ssh/id_rsa.pub`的内容添加到目标主机`~/.ssh/authorized_keys`  
3. 设置目标主文件权限：
```
#!bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

## 文件管理
```
#!bash
#查找24小时内修改过的文件
find -mtime 0

#查找断开的符号链接
find . -type l -! -exec test -e {} \; -print

#解压并更改目录名称
mkdir $DirName
tar zxf hello.tgz -C $DirName --strip-components 1
```

## 其他
```
#!bash
#重新连接screen会话，必要时先detach
kill -HUP $ScreenPid && screen -d -r

#脚本退出杀掉所有子进程
trap "kill 0" SIGINT SIGTERM EXIT

#小写转大写
tr '[a-z]' '[A-Z]'

#显示第100行
sed '100q;d' $File

#输出匹配的组
echo "a=1 b=2 c=3" | sed "s/.*b=\([0-9]\).*/\1/" #匹配b=2，输出2

#上传文件
rz

#下载文件
sz $File
```
bash下编辑命令：输完命令后按***Ctrl-x Ctrl-e***