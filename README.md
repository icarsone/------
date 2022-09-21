## ifs内网环境下跨设备快速分享文件
## 适用对象：
- 提供文件的主体是安装有python环境的windows、mac、linux等平台

- 接收文件的设备只需要有浏览器即可

  

## 使用方法

### 无需安装python环境的用法（仅在windows上测试过）

- 在release中下载程序文件

- 新建一个文件夹，把ifs_gui程序放进去

- 在这个文件夹下再新建一个名称为share的文件夹

- 将需要分享的文件拖入share文件夹内

- 双击运行ifs_gui程序即可
（或者直接下载整个source code，解压，然后执行上述第4、5步即可）
  

### 安装python环境的用法

- 需要先安装python环境，官网链接：https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe

- 将需要分享的文件拖入share文件夹内

- 如果不需要二维码功能，那么简单地双击打开"快捷分享+复制ip.bat"文件即可(windows下)

- 如果需要二维码功能，一般来说，需要新安装3个库，在命令行（powershell）中依次敲入下列命令并回车，然后运行IFS_GUI.py文件即可
```
pip3 install qrcode

pip3 install image

pip3 install pyperclip
```


