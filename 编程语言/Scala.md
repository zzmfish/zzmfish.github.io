## 语法
### 类型
##### 字符串
```scala
//连接列表成一个字符串
lines.mkString("\n")
```
### 函数
```scala
//一般函数
def info(message:String) : Unit = {
    println(message)
}
```

### 类
```scala
//定义类
class ReaderThread(inputStream: InputStream) extends Runnable {
    var result = ""

    override def run(): Unit = {
        result = readStream(inputStream)
    }
}
```

### 异常
```scala
//抛出异常
throw new IllegalArgumentException

//处理异常
try {
    val f = new FileReader("input.txt")
} catch {
    case ex: FileNotFoundException =>{
        println("Missing file exception")
    }
    case ex: IOException => {
        println("IO Exception")
    }
}
```
## 参考
* [Scala能否成为Java杀手？](http://hb.qq.com/a/20120418/001400.htm)
* [Scala创始人：创造比Java更好的语言](http://developer.51cto.com/art/200905/124636.htm)
* [Scala IDE for Eclipse](http://scala-ide.org/download/current.html)
* [Scala with Maven](http://docs.scala-lang.org/tutorials/scala-with-maven.html)
* [Scala 常用语法](http://www.cnblogs.com/fxjwind/p/3338829.html)
* [Concrete Mutable Collection Classes](http://docs.scala-lang.org/overviews/collections/concrete-mutable-collection-classes.html)
* [Getting Started with Scala](http://www.scala-lang.org/old/node/166)
* [Scala API](http://www.scala-lang.org/api/current/#package)
* [Scala - How to open and read files in Scala](http://alvinalexander.com/scala/scala-how-open-read-files-scala-examples)
* [使用SBT构建Scala应用](https://github.com/CSUG/real_world_scala/blob/master/02_sbt.markdown)