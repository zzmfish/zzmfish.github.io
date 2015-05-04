* \\\\vboxsvr

###### linux虚拟机挂载windows共享目录
```
#!bash
sudo mount -t vboxsf $ShareName $MountPoint
#如：
sudo mount -t vboxsf d_drive ~/mount/vbox_share/
```