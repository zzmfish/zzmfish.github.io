```bash
#termcap vt102 ''
termcapinfo xterm 'Co#256:AB=\E[48;5;%dm:AF=\E[38;5;%dm'
hardstatus on 
hardstatus alwayslastline
hardstatus string '%{=b}%{b}%-w%{.BW}%10>[%n %t]%{-}%+w%< %=%{G}%H %{-b}%{w}%Y/%m/%d %c:%s'
vbell off
defscrollback 1000
windows

# 退出vim/nano之后自动刷新屏幕
altscreen on 

# 允许使用sz/rz上传下载文件
zmodem catch

# 使用登录shell
shell -$SHELL
```


#### su切换用户之后screen启动错误：Cannot open your terminal '/dev/pts/24' - please check.
```
#!bash
script /dev/null
```

#### 重新连接screen会话，必要时先detach
```
#!bash
kill -HUP $ScreenPid
#或
screen -r -d
#或
screen -r -x

```

## 参考
* [ubuntu gnome terminal无法使用sz下载文件解决方法](http://www.xuebuyuan.com/1397277.html)