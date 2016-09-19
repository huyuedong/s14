# FTP程序

## 需求：
  1. 用户加密认证
  2. 允许同时多用户登录
  3. 每个用户有自己的家目录 ，且只能访问自己的家目录
  4. 对用户进行磁盘配额，每个用户的可用空间不同
  5. 允许用户在ftp server上随意切换目录
  6. 允许用户查看当前目录下文件
  7. 允许上传和下载文件，保证文件一致性
  8. 文件传输过程中显示进度条
  9. 附加功能：支持文件的断点续传

## 环境依赖：

- Python3.0+

## 功能介绍：

- 目前只实现了在当前目录上传和下载功能。

## 运行说明：

找个文件分别放在ftp_server和ftp_client的src目录，测试上传和下载功能。
上传命令：put {filename}
下载命令：get {filename}



## 目录结构：

    homework
    ├── README
    ├── __init__.py
    ├── ftpserver #ftp server程序
    │   ├── conf #配置文件
    │   │   ├── __init__.py
    │   ├── bin #启动程序
    │   │   ├── __init__.py
    │   ├── src #核心程序
    │   │   ├── __init__.py
    │   │   └── ftp_server.py #ftp server主程序
    └── ftpclient #ftp client程序
        ├── __init__.py
        └── ftp_client.py #ftp client执行文件