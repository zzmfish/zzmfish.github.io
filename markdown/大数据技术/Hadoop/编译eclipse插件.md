#### 解压hadoop-1.2.1

#### diff src/contrib/build-contrib.xml

```diff
62c62
<   <property name="javac.deprecation" value="off"/>
---
>   <property name="javac.deprecation" value="on"/>
```

#### diff src/contrib/eclipse-plugin/build.properties
```diff
20a21,22
> eclipse.home = /Users/zhouzhiming/local/eclipse
> version=1.2.1
```

#### diff src/contrib/eclipse-plugin/build.xml
```diff
44a45,47
>     <fileset dir="${hadoop.root}">
>       <include name="**/*.jar" />
>     </fileset>
60a64
>      includeantruntime="on"
69,70c73,79
<     <copy file="${hadoop.root}/build/hadoop-core-${version}.jar" tofile="${build.dir}/lib/hadoop-core.jar" verbose="true"/>
<     <copy file="${hadoop.root}/build/ivy/lib/Hadoop/common/commons-cli-${commons-cli.version}.jar"  todir="${build.dir}/lib" verbose="true"/>
---
>     <copy file="${hadoop.root}/hadoop-core-${version}.jar" tofile="${build.dir}/lib/hadoop-core.jar" verbose="true"/>
>     <copy file="${hadoop.root}/lib/commons-cli-${commons-cli.version}.jar"  tofile="${build.dir}/lib/commons-cli.jar" verbose="true"/>
>     <copy file="${hadoop.root}/lib/commons-configuration-1.6.jar"  tofile="${build.dir}/lib/commons-configuration.jar" verbose="true"/>
>     <copy file="${hadoop.root}/lib/commons-httpclient-3.0.1.jar"  tofile="${build.dir}/lib/commons-httpclient.jar" verbose="true"/>
>     <copy file="${hadoop.root}/lib/commons-lang-2.4.jar"  tofile="${build.dir}/lib/commons-lang.jar" verbose="true"/>
>     <copy file="${hadoop.root}/lib/jackson-core-asl-1.8.8.jar"  tofile="${build.dir}/lib/jackson-core-asl.jar" verbose="true"/>
>     <copy file="${hadoop.root}/lib/jackson-mapper-asl-1.8.8.jar"  tofile="${build.dir}/lib/jackson-mapper-asl.jar" verbose="true"/>

```


#### 编译
```bash
cd src/contrib/eclipse-plugin
ant
```
将build/contrib/eclipse-plugin/hadoop-eclipse-plugin-1.2.1.jar复制到eclipse/plugins下