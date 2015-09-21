# Maven

## 安装
* 下载解压，设置PATH
* 定义本地库位置
修改conf/settings.xml加一行：
```
<localRepository>D:/repo/repository</localRepository> 
```

## 创建项目
```
#!bash
mvn archetype:generate \
    -DgroupId=com.mycompany.helloworld \
    -DartifactId=helloworld \
    -Dpackage=com.mycompany.helloworld \
    -Dversion=1.0-SNAPSHOT
```

## 目录结构

|文件            |作用
|------          |-----------------
pom.xml         |描述项目，配置插件和管理依赖关系
src
test
target/xxx.jar
target/classes/
target/test-classes/


## 构建项目
```bash
#编译
mvn compile

#打包
mvn package
```

## 概念
### POM（Project Object Model）
* 项目所有的配置都放置在 POM 文件中

### Maven插件
* 一个***目标***是一个工作单元
* ***插件***是一个或者多个目标的集合

### Maven生命周期
* ***生命周期***指项目的构建过程，它包含了一系列的有序的***阶段***
* 插件目标可以绑定到生命周期阶段上

##### 默认生命周期

|阶段                   |目标               |
|-----------------      |-------------------|
process-resources       |resources:resources
compile                 |compiler:compile
process-classes         |默认无目标
process-test-resources  |resources:testResources
test-compile            |compiler:testCompile
test                    |surefire:test
prepare-package         |默认无目标
package                 |jar:jar

### Maven 依赖管理
* 依赖关系是在POM的`dependencies`部分中定义
* ***传递依赖***是指把被依赖jar文件的依赖关系纳入最终解决的依赖关系链中
* ***scope***决定依赖关系的适用范围

### Maven库
* maven***远程库***有maven的核心插件和可供下载的jar文件
* ***本地库***是指 maven 下载了插件或者 jar 文件后存放在本地机器上的拷贝
* 通过`mvn install`命令把项目安装到本地库
* 其他项目可以通过maven坐标和本地库的项目建立依赖关系
* [MVN Repository](http://mvnrepository.com)

## 参考
* [Maven Getting Started Guide](https://maven.apache.org/guides/getting-started/)
* [Maven in 5 Minutes](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
* [Using the CDH 5 Maven Repository](http://www.cloudera.com/content/cloudera/en/documentation/core/latest/topics/cdh_vd_cdh5_maven_repo.html)
* [Maven实战（一）——坐标规划](http://www.infoq.com/cn/news/2010/12/xxb-maven-1)