* \\\\vboxsvr

###### linux虚拟机挂载windows共享目录
```
#!bash
sudo mount -t vboxsf $ShareName $MountPoint
#如：
sudo mount -t vboxsf d_drive ~/mount/host_d/
```

## 参考
* [VBox虚拟机与主机(宿主)通讯原理以及socat(套接字猫)简单介绍](http://www.cnblogs.com/wadeyu/p/4657906.html)