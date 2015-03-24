###### 基本概念
* ***JobTracker***用于管理和调度工作；一个Hadoop集群只有一个JobTracker
* ***TaskTracker***用于执行工作
* 每个任务被初始化成一个***Job***，每个Job分为两个阶段：Map阶段和Reduce阶段
* ***Map阶段***接收<key,value\>形式的输入，产生<key,value\>形式的输出
* ***Reduce阶段***接收<key, (list of values)\>形式的输入，产生<key,value\>形式的输出
* ***shuffle过程***：把相同的key值放在一起
* partition过程

```uml @startuml
node 客户端 {
    [JobClient]
    [MapReduce程序]
}

node JobTracker节点 {
    [JobTracker]
}

node TaskTracker节点 {
    [TaskTracker]
    [JVM]
}

node HDFS节点 {
    [HDFS]
}

客户端 --> HDFS: 复制作业资源
MapReduce程序 -> JobClient
JobClient --> JobTracker: 提交作业
JobTracker -> TaskTracker: 心跳通讯
JobTracker --> HDFS: 获取输入分割
TaskTracker -> JVM: 发布
TaskTracker --> HDFS: 获取作业资源
JVM --> HDFS: 输出
@enduml
```

###### 编译jar
```
#!makefile
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
###### 运行作业
```
#!bash
hadoop jar $JarFile $FullClassName $InputDir $OutputDir
#如hadoop jar wordcount.jar org.apache.hadoop.examples.WordCount input output
```

###### 运行Hadoop流
```
#!bash
hadoop jar $HadoopStreamJar -input $InputDir -output $OutputDir -mapper $MapperBin -reducer $ReducerBin
#如hadoop jar contrib/streaming/hadoop-streaming-1.2.1.jar -input input -output output -mapper /bin/cat -reducer /usr/bin/wc
```

###### Hadoop Pipes


###### 查看作业状态
```
#!bash
mapred job -list
```


###### eclipse设置
* Project > Properties > Java Build Path > Libraries > Add External Jars添加hadoop的jar