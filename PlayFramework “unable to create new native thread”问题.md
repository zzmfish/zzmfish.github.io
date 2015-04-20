# PlayFramework “unable to create new native thread”问题

## PlayFramework线程池设置
PlayFramework是通过配置文件`conf/application.conf`来设置线程池大小：

```ini
#Application mode
application.mode=dev

# Execution pool
# ~~~~~
# Default to 1 thread in DEV mode or (nb processors + 1) threads in PROD mode.
#play.pool=10
```

默认是dev模式且只有一个线程。改成prod模式之后默认线程数是CPU核心数+1。也可以手工指定线程池大小。

## “unable to create new native thread”问题
修改成application.mode=prod之后，处理并发请求会出现错误：
```
play.exceptions.JavaExecutionException: unable to create new native thread
        at play.mvc.ActionInvoker.invoke(ActionInvoker.java:228)
        at Invocation.HTTP Request(Play!)
Caused by: java.lang.OutOfMemoryError: unable to create new native thread
        at java.lang.Thread.start0(Native Method)
        at java.lang.Thread.start(Thread.java:714)
        at java.util.concurrent.ThreadPoolExecutor.addWorker(ThreadPoolExecutor.java:949)
        at java.util.concurrent.ThreadPoolExecutor.execute(ThreadPoolExecutor.java:1360)
        at java.util.concurrent.AbstractExecutorService.submit(AbstractExecutorService.java:110)
        at org.apache.hadoop.hbase.client.AsyncProcess.sendMultiAction(AsyncProcess.java:565)
        at org.apache.hadoop.hbase.client.AsyncProcess.submit(AsyncProcess.java:349)
        at org.apache.hadoop.hbase.client.AsyncProcess.submit(AsyncProcess.java:286)
        at org.apache.hadoop.hbase.client.HTable.backgroundFlushCommits(HTable.java:1001)
        at org.apache.hadoop.hbase.client.HTable.flushCommits(HTable.java:1334)
        at org.apache.hadoop.hbase.client.HTable.put(HTable.java:947)
        at controllers.VideoControllerCommon.addOrUpdate(VideoControllerCommon.java:169)
        at controllers.VideoController.add(VideoController.java:31)
        at play.mvc.ActionInvoker.invokeWithContinuation(ActionInvoker.java:524)
        at play.mvc.ActionInvoker.invoke(ActionInvoker.java:475)
        at play.mvc.ActionInvoker.invokeControllerMethod(ActionInvoker.java:451)
        at play.mvc.ActionInvoker.invokeControllerMethod(ActionInvoker.java:446)
        at play.mvc.ActionInvoker.invoke(ActionInvoker.java:160)
        ... 1 more
```

## 原因分析
OutOfMemoryError貌似是内存不足，但通过`play run -Xms256m -Xmx1024m`增大java可用内存并没有解决问题。而且单线程情况下处理几千万请求也没有问题，排除内存泄漏。怀疑是创建linux线程失败。


通过`ps -o thcount <程序Pid>`可以看到一个进程的linux原生线程数。
设置`play.pool=3`，Play程序启动后使用了127个线程。处理大量并发请求很快增加到546个线程，而且出现了“unable to create new native thread”。

`ulimit -u`输出1024，表明用户可以创建1024个进程。linux线程也称为“轻量级进程”，那么ulimit的进程数限制是否会限制线程数量呢？测试表明是会的。

## 解决办法

设置ulimit -u 10240，然后再启动Play网站程序，就不会出现前面的错误。

## 其他疑问

### PlayFramework创建了大量线程
设置`play.pool=10`，Play进程使用1073个线程，后来下降到416个。

使用prod模式和默认play.pool（默认是CPU核心数+1），刚开始处理请求会创建2308个线程，后来下降到451个。

说明PlayFramework会创建大量线程，但原因还不清楚。