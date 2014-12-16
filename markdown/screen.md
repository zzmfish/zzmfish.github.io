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
```