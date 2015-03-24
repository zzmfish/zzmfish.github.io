```
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
screen -d -r
```