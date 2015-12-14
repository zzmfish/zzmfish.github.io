# Docker

## 和VM的区别
![](/images/vm-vs-docker.png)

## 使用
```bash
# 安装
curl -sSL https://get.docker.com/ | sh
# 添加用户到组（需重启）
sudo usermod -aG docker $USER
# 运行
docker run -t -i ubuntu /bin/bash
# 列出容器
docker ps -a
```



## 参考
* [Docker：利用Linux容器实现可移植的应用部署](http://www.infoq.com/cn/articles/docker-containers)
* [Docker —— 从入门到实践](https://www.gitbook.com/book/yeasy/docker_practice/details)
* [Docker 在 Coding WebIDE 项目中的运用](https://blog.coding.net/blog/Docker-use-in-Coding-WebIDE)
* [谁是容器中的“战斗机”？Docker与Chef、LXC等容器对比](http://www.csdn.net/article/2014-05-14/2819773/1)