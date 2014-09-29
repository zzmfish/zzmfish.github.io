# Bash

## 参数
```
#!bash
echo $*               #"$1 $2 ..."  
echo $@             #"$1" "$2" "$3"  
echo $#              #参数个数  
shift [n]               #弹出前面n个参数，n默认为1
```

## 内置变量  
```
#!bash
echo $?               #最近执行程序的退出代码  
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
foo=()                                        #定义数组  
foo+=(1)                                   #添加元素    
echo ${foo[*]}                         #所有元素    
echo ${#foo[*]}                      #元素个数  
(IFS=,; echo "${array[*]}")     #逗号连接数组内容  
```

##序列
```
#!bash
echo {1..5}  
echo `seq 1 5`
```

##其他
***.***是***true***的别名