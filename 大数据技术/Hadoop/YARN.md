## 概述
* The fundamental idea of MRv2 is to split up the two major functionalities of the JobTracker, resource management and job scheduling/monitoring, into separate daemons. 
* The idea is to have a global ***ResourceManager (RM)*** and per-application ***ApplicationMaster (AM)***. 
* An ***application*** is either a single job in the classical sense of Map-Reduce jobs or a DAG of jobs.

## 组件
### Resource Manager
* 根据集群中容量、队列和资源等限制，将资源分配给各个正在运行的应用

### Node Manager
* 负责启动应用的容器，监控容器的资源使用，并把这些应用信息汇报给调度器
* 对应一个节点

### Application Master
* 负责接收作业，协商获取地一个资源容器用于执行应用的任务主题并为重启失败的应用主题分配容器

### Container
* 将节点的可用资源分割，每一份通过封装组织成系统的一个资源单元
* 每个节点的内存分割成大小固定、地位相同的容器
* 内存容器可以在任务执行过程中互换，从而提高利用率

![](/images/yarn.gif)

## 命令
```
#!bash
yarn application -list
```

## 参考
* [Hadoop 新 MapReduce 框架 Yarn 详解](http://www.ibm.com/developerworks/cn/opensource/os-cn-hadoop-yarn/)
* [Hadoop YARN的发展史与详细解析](http://www.csdn.net/article/2013-12-18/2817842-bd-hadoopyarn)