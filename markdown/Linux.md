# Linux经验技巧

## 系统监控
查看监听端口：`netstat -lnp --inet`  
统计系统调用的耗时：`strace -c -p 程序PID`  
分析进程IO：`iotop`  
查看线程的CPU占用：`top -H -p <进程pid>`  

## 系统管理
增加最大文件数  
1. 编辑`/etc/security/limits.conf`：  
`zhouzm          hard nofile     10240`  
2. 重启，执行命令：`ulimit -n 10240`  
用户管理：`useradd 用户名`  
设置时间: `date -s "20:16"`  

## SSH
ssh挂载：`sshfs -p <端口> <用户名>@<目标主机>:<远程目录> <本地目录>`  
### ssh无密码登录
1. 本机执行`ssh-keygen -t rsa`  
2. 把`~/.ssh/id_rsa.pub`的内容添加到目标主机`~/.ssh/authorized_keys`  
3. 设置目标主文件权限： `chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys`

## 文件管理

查找24小时内修改过的文件: `find -mtime 0`  
查找断开的符号链接： `find . -type l -! -exec test -e {} \; -print`  
解压并更改目录名称：`mkdir <目录> && tar zxf hello.tgz -C <目录> --strip-components 1` 

## 其他
重新连接screen会话，必要时先detach：
```
kill -HUP <screen pid>
screen -d -r
```
bash下编辑命令：输完命令后按`Ctrl`-`x` `Ctrl`-`e`  
脚本退出杀掉所有子进程：`trap "kill 0" SIGINT SIGTERM EXIT`  
上传文件：`rz`  
下载文件：`sz <文件名>`  
小写转大写：`tr '[a-z]' '[A-Z]'`  
显示第100行：`sed '100q;d' <文件名>` 