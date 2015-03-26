## 生成RSA密钥

```
#!bash
#生成私钥
openssl genrsa 1024 > private.key

#生成公钥
openssl rsa -in private.key -pubout -out public.key
```