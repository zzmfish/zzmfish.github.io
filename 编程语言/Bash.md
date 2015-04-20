# Bash

## 参数
```
#!bash
$*             #"$1 $2 ..."  
$@             #"$1" "$2" "$3"  
$#             #参数个数  
shift [n]      #弹出前面n个参数，n默认为1
```

## 内置变量  
```
#!bash
$?                  #上一个程序的退出代码  
${BASH_SOURCE[0]}   #脚本文件路径
```

## 语法
case语法：
```
#!bash
case expression in
    pattern1 )
        statements ;;
    pattern2 )
        statements ;;
    * )
        statements ;;
esac
```

## 数据类型
### 数组
```
#!bash
foo=()                          #定义数组  
foo+=(1)                        #添加元素    
echo ${foo[*]}                  #所有元素    
echo ${#foo[*]}                 #元素个数  
jars=(lib/*.jar)                #文件列表作为数组
(IFS=,; echo "${array[*]}")     #逗号连接数组内容  
```

##序列
```
#!bash
echo {1..5}  
echo `seq 1 5`
```

## 文本
```
#!bash
#多行输入
cat>test1<<EOF
hello
EOF

#文件按行处理
cat $inputFile | while read line; do
    echo "$line"
done > $outputFile

#显示高亮
echo -e "\033[1mhello\033[0m"

#字符串匹配
[[ abb == a* ]]

#字符串替换
${string//substring/replacement}
```

## 进程
```
#!bash
#退出时杀死进程组
trap "kill 0" SIGINT SIGTERM EXIT

#执行另一个程序替换bash
exec $Program $Arguments
```
##其他
***.***是***true***的别名

```
#!bash
#让函数可被子进程继承
declare -x -f $FunctionName

#检测函数是否存在
declare -F -f $FunctionName

#计时
t0=$(date +%s)
t=$(($(date +%s)-$t0))
```

## 参考资料
* [linux shell 字符串操作（长度，查找，替换）详解](http://www.cnblogs.com/chengmo/archive/2010/10/02/1841355.html)