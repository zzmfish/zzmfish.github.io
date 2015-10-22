## 架构
![](/images/GCM.png)

* Google connection server
    * HTTP Connection Server
    * XMPP Connection Server
        * 持久
        * 异步
        * 双向
        * gcm-xmpp.googleapis.com:5235
        * 测试：gcm-preprod.googleapis.com:5236
        * TLS连接
        * SASL PLAIN authentication mechanism using <your_GCM_Sender_Id>@gcm.googleapis.com (GCM sender ID) and the API key as the password
        * 每个sender ID支持1000个连接
        * 控制消息：'ack' or 'nack', or 'control'
* app server
    * HTTP
    * XMPP
* client app
    * 注册：得到注册token
    * 发送upstream消息
    * 接收downstream消息

## 证书
* Sender ID
* API Key
* Application ID: Android use the package name from the app manifest
* Registration Token

## 设置
* 打开Google Developers Console
* 新建项目


## 其他
* Topic Messaging
* Group Messaging

## 链接
* [Google Cloud Messaging: Overview](https://developers.google.com/cloud-messaging/gcm)
* [Google Cloud Messaging: Cloud Connection Server Tutorial](http://www.captechconsulting.com/blogs/google-cloud-messaging-cloud-connection-server-tutorial)
* [Try Cloud Messaging for Android](https://developers.google.com/cloud-messaging/android/start)
* [Implementing an XMPP Connection Server](https://developers.google.com/cloud-messaging/ccs)
* [XMPP Connection Server Reference](https://developers.google.com/cloud-messaging/xmpp-server-ref)
* [gcm_server](https://github.com/writtmeyer/gcm_server)
* [GCMCCSDemo](https://github.com/antoinecampbell/GCMCCSDemo)
* [Google Developers Console](https://console.developers.google.com/project)
* [View & diagnose Google Cloud Messaging (GCM) statistics](https://support.google.com/googleplay/android-developer/answer/2663268?hl=en)
* [XMPP Connection Server Reference](https://developers.google.com/cloud-messaging/xmpp-server-ref)
* [查看和诊断 Google 云消息传递 (GCM) 统计信息](https://support.google.com/googleplay/android-developer/answer/2663268?hl=zh-Hans)