```
#!bash
#列出文件
hadoop dfs -ls
hadoop dfs -ls $DirName

#创建目录
hadoop dfs -mkdir $DirName

#上传文件
hadoop dfs -put $LocalFiles $DirName

#下载文件
hadoop dfs -get $DirName $LocalDir

#下载合并的文件
hadoop dfs -getmerge $DirName $LocalFile

#删除目录
hadoop dfs -rm -r $DirName

#显示文件
hadoop dfs -cat $FileName

#显示目录所占空间
hdfs dfs -du -s -h $DirName

#检查文件存在
hdfs dfs -test -e $FileName
```

## 权限
* 类似POSIX模型
* 支持ACL

## 参考
* [HDFS Permissions Guide](http://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsPermissionsGuide.html)
* [HDFS High Availability Using the Quorum Journal Manager](https://hadoop.apache.org/docs/r2.4.1/hadoop-project-dist/hadoop-hdfs/HDFSHighAvailabilityWithQJM.html)
* [浅析Hadoop Secondary NameNode，CheckPoint Node，Backup Node](http://itindex.net/detail/43805-hadoop-secondary-namenode)
* [漫谈HADOOP HDFS BALANCER](http://www.cnblogs.com/gpcuster/archive/2011/02/16/1956555.html)
* [HDFS原理及操作](http://www.thebigdata.cn/QiTa/14598.html)