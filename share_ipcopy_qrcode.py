import threading
import socket
from functools import partial  # 导入模块
from http.server import HTTPServer, SimpleHTTPRequestHandler

import qrcode
import pyperclip

def show():
    """
    查询本机ip地址
    :return: ip
    """
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
    img.show()


def server():
    ip = ''
    port = 9999
    # 指定directroy 的路径 ，返回给Handler这个对象，在去调用这个对象
    Handler = partial(SimpleHTTPRequestHandler, directory='./share')
    server = HTTPServer((ip, port), Handler)
    server.serve_forever()


if __name__ == '__main__':
    t = threading.Thread(target=show)
    t.start()

    t = threading.Thread(target=server)
    t.start()