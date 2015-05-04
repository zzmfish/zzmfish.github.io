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