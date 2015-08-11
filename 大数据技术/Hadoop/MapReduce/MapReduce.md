## 基本原理

### 初始化
* 每个任务被初始化成一个***Job***，每个Job分为两个阶段：Map阶段和Reduce阶段

### 输入
* `InputSplit`
    * represents the data to be processed by an individual Mapper
    * byte-oriented view
* `RecordReader`
    * reads &lt;key, value&gt; pairs from an InputSplit


### Map
* ***Map阶段***接收<key,value\>形式的输入，产生<key,value\>形式的输出

### Reduce
* ***Reduce阶段***接收<key, (list of values)\>形式的输入，产生<key,value\>形式的输出
* ***shuffle过程***：把相同的key值放在一起

### 输出

![](/images/MapReduce.png)

## 组件
* ***JobTracker***用于管理和调度工作；一个Hadoop集群只有一个JobTracker
* ***TaskTracker***用于执行工作

![](/images/MapReduce_v1.png)

## 命令
##### 编译
```makefile
JARS=$(addprefix /home/hadoop/hadoop-1.2.1/,hadoop-core-1.2.1.jar lib/commons-cli-1.2.jar)
all:
    mkdir -p build
    javac -classpath $(shell echo $(JARS) | sed "s/ /:/") \
        -d build WordCount.java
    jar -cvf wordcount.jar -C build/ .
```
或
```
#!bash
mkdir build
javac -cp $(hadoop classpath) -d build $(find -name *.java)
jar -cvf job.jar -C build/ .
```

##### 运行
```bash
#hadoop jar wordcount.jar org.apache.hadoop.examples.WordCount input output
hadoop jar $JarFile $FullClassName $InputDir $OutputDir

#运行Hadoop流
#hadoop jar contrib/streaming/hadoop-streaming-1.2.1.jar -input input -output output -mapper /bin/cat -reducer /usr/bin/wc
hadoop jar $HadoopStreamJar -input $InputDir -output $OutputDir -mapper $MapperBin -reducer $ReducerBin
```

##### 状态
```bash
#显示作业列表
hadoop job -list
```

##### 管理
```bash
#终止作业
hadoop job -kill $JobId
```


## eclipse
* Project > Properties > Java Build Path > Libraries > Add External Jars添加hadoop的jar

## 参考
* [MapReduce Tutorial](http://hadoop.apache.org/docs/r2.7.1/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)
* [Hadoop MultipleInputs sample usage](http://www.lichun.cc/blog/2012/05/hadoop-multipleinputs-usage/)
* [Accessing Table Data with MapReduce](http://www.cloudera.com/content/cloudera/en/documentation/core/latest/topics/cdh_ig_table_access_mapreduce.html)