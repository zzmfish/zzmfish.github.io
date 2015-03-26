* Xms128m JVM初始分配的堆内存
* Xmx512m JVM最大允许分配的堆内存，按需分配
* XX:PermSize=64M JVM初始分配的非堆内存
* XX:MaxPermSize=128M JVM最大允许分配的非堆内存，按需分配
* 

#### Maven

##### 安装
* 下载解压，设置PATH

##### 定义本地库位置
修改conf/settings.xml加一行：
```
<localRepository>D:/repo/repository</localRepository> 
```