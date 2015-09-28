## Shell
|命令                           | 作用                       |
|-------------------------------|----------------------------|
list                            |显示全部tabe
get 'video', '1234556'          |显示一行
put 't1', 'r1', 'c1', 'value'
count 'video', INTERVAL=> 1     |显示全部key
scan 'video'                    |显示video表全部行
scan 'dn_token', {COLUMNS => ['info:dn', 'info:tk'], LIMIT => 100 }
truncate 'video'                |清空表

## 参考
* [Hadoop Wiki - HBase Shell](https://wiki.apache.org/hadoop/Hbase/Shell)