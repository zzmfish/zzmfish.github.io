### 资源管理器（Resource Manager）
#### 调度器（Scheduler）
根据集群中容量、队列和资源等限制，将资源分配给各个正在运行的应用
#### 应用管理器（Application Manager）
负责接收作业，协商获取地一个资源容器用于执行应用的任务主题并为重启失败的应用主题分配容器
### 节点管理器（Node Manager）
* 负责启动应用的容器，监控容器的资源使用，并把这些应用信息汇报给调度器
* 对应一个节点

### 应用主体（Application Master）
* 对应一个应用

### 资源容器
* 将节点的可用资源分割，每一份通过封装组织成系统的一个资源单元
* 每个节点的内存分割成大小固定、地位相同的容器
* 内存容器可以在任务执行过程中互换，从而提高利用率


```uml @startuml

[Resource Manager]

[Node Manager]

[Application Master]

@enduml
```

```
#!bash
yarn application -list
```