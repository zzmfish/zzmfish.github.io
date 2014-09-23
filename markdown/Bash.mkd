# Bash

## 参数
`$*`表示"$1 $2 ..."  
`$@`表示"$1" "$2" "$3"  
`$#`表示参数个数  
`shift [n]`：弹出前面n个参数，n默认为1


## 内置变量  
`$?`表示最近执行程序的退出代码  

## 语法
case语法：
```
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
`foo=()`：定义数组  
`foo+=(1)`：添加元素    
`${foo[*]}`：所有元素    
`${#foo[*]}`：元素个数  
`(IFS=,; echo "${array[*]}")`：逗号连接数组内容  

##序列
`{1..5}`  
`seq 1 5`
