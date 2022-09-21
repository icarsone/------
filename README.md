## 适用对象：
适用于在内网环境下跨设备快速分享文件
提供文件的主体是安装有python环境的windows、mac、linux
接收文件的设备只需要有一个浏览器即可

## 使用方法（仅在windows上测试过，mac和linux用户请安装python环境并运行py文件）
### 不安装python环境的用法
1、在release中下载程序文件
2、新建一个文件夹
3、新建一个名称为share的文件夹
4、将需要分享的文件拖入share文件夹内
5、双击运行程序即可

### 安装python环境的用法
1、需要先安装python环境，官网链接：https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe
2、将需要分享的文件拖入share文件夹内
3.1、如果不需要二维码功能，那么简单地双击打开"快捷分享+复制ip.bat"文件即可
3.2、如果需要二维码功能，一般来说，需要新安装3个库，在命令行中依次敲入下列命令并回车，然后双击打开"快捷分享+复制ip+二维码显示.bat"即可
# pip3 install qrcode
# pip3 install image
# pip3 install pyperclip 