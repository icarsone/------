import socket,qrcode,image,pyperclip,os,sys,threading
import tkinter
from tkinter import *
from PIL import ImageTk, Image
from time import sleep
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler

def get_qrcode():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    # 默认端口为9999，要修改的话修改在server方法的port里面一起修改
    url ="http://"+ip+":9999"
    pyperclip.copy(url)
    img = qrcode.make(url)
    img.save("ipaddress.jpg")
    return url

def server():
    ip = ''
    port = 9999
    # 指定directroy 的路径 ，返回给Handler这个对象，再去调用这个对象
    Handler = partial(SimpleHTTPRequestHandler, directory='./share')
    server = HTTPServer((ip, port), Handler)
    server.serve_forever()


class buttons:
    def __init__(self):
        root = Tk()
        root.title("内网快速分享")  # 设置窗口标题
        root.geometry("600x600")  # 设置窗口大小 注意：是x 不是*

        url = get_qrcode()


        # 图片说明
        img = ImageTk.PhotoImage(Image.open("ipaddress.jpg"))
        self.qrcode = Label(root, image = img, )
        self.qrcode.pack(pady=(5,5))

        # '''按钮样式'''
        self.bts = Button(root, text='结束分享',height=3,width=20, command=self.Button_text_switch)
        self.bts.pack( )
        
        # 文字说明
        self.note = Label(root, text="2、请检查是否在同一个局域网\将需要分享的文件放入share文件夹下")
        self.note.pack(pady=(10,5),side=tkinter.BOTTOM,anchor="sw")

        self.url = Label(root, text="1、内网地址已经复制到您的剪贴板,直接粘贴发给朋友"+url+"或者扫描上方二维码👆")
        self.url.pack(pady=(5,5),side=tkinter.BOTTOM,anchor="sw")




        root.mainloop()
    # 按钮开关设置
    def Button_text_switch(self):
        os.remove("ipaddress.jpg")
        sys.exit()

if __name__ == '__main__':
    t1 = threading.Thread(target=server)
    t1.daemon = True
    t1.start()
    # t2 = threading.Thread(target=get_qrcode)
    # t2.daemon = True
    # t2.start()
    buttons()