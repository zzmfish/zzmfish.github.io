# 广告智能识别程序开发

[TOC]

## 目标
能够根据其他广告过滤软件输出的结果，训练模型并形成对应的广告智能识别，一期的准确率达到85%以上

## 特征
|                                         |JavaScript    | Iframe | 图片   | Flash     |
|-----------                           |-----------------|------------|------    |------       |
|容器id/class包含"ad"    |                       | Y          | Y         | Y            |
|在异域网站出现次数多 | Y                   | Y         |              |               |
|条形                                 |                      |            | 比较多 | 比较多  |
|absolute/fixed定位       |                      | Y          | 比较多 | 比较多  |
| 在正文外                       |                       | Y          | Y          | Y            |

* 大网站都采用站内的广告平台
* 小网站都采用第三方广告平台


## 工具
* [Adblock Plus for Firefox](https://github.com/adblockplus/adblockplus)
* [abpcrawler](https://github.com/adblockplus/abpcrawler)
* [buildtools](https://github.com/adblockplus/buildtools)

##  Firefox Add-on SDK

### [安装](https://developer.mozilla.org/en-US/Add-ons/SDK/Tutorials/Installation)
```
#!bash
wget https://ftp.mozilla.org/pub/mozilla.org/labs/jetpack/jetpack-sdk-latest.tar.gz
tar zxf jetpack-sdk-latest.tar.gz
cd addon-sdk-1.17
source bin/activate
```

### 创建项目
```
#!bash
mkdir $AddOnDir
cd $AddOnDir
cfx init
```

### 运行
```
#!bash
cfx run
cfx -p dev run
```

### 打包
```
#!bash
cfx xpi
```

### 参考
* [SDK说明](https://developer.mozilla.org/en-US/Add-ons/SDK)
* [child_process.spawn](https://developer.mozilla.org/en-US/Add-ons/SDK/Low-Level_APIs/system_child_process)