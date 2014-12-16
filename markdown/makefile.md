# Makefile
```
#!makefile
#后缀替换
OBJS=$(SRCS:.cpp=.o)

#依赖规则
#“%”表示文件名，“$<”表示依赖目标，“$@”表示目标
%.o : %.c
    $(CC) -c $(CFLAGS) $(CPPFLAGS) $< -o $@
```