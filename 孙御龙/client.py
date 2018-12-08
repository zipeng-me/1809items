# -*- coding:utf-8 -*-
'''客户端
客户端功能：

'''
import socket
import sys
from analysis import Analysis

class Client(Analysis):
    # 初始化
    def __init__(self, ip, port):
        self.__IP = ip
        self.__PORT = port
        # 地址
        self.__ADDR = (self.__IP, self.__PORT)
        # 连接服务器
        self.runClient()
        self.sockfd.send(b'A')
        # 接收服务器推送消息
        self.TMSG = self.sockfd.recv(4096)
        # 显示推送消息
        print('股票信息：', self.TMSG.decode())
    
    # 创建TCP/IP套接字
    def runClient(self):
        # 创建套接字
        self.sockfd = socket.socket()
        # 连接服务器
        self.sockfd.connect(self.__ADDR)

    # 操作
    def operation(self):
        while True:
            print('1.登录  2.注册  3.查询  q.退出')
            # 输入选项
            cmd = input('>> ')
            # 如果选项不符，重新输入
            if cmd not in ['1', '2', '3', 'q']:
                print('不存在该选项，请重新输入：')
                continue
            # 登录
            elif cmd == '1':
                self.sockfd.send(b'L')
                self.login()
            # 注册
            elif cmd == '2':
                self.sockfd.send(b'R')
                self.register()
            # 查询
            elif cmd == '3':
                self.check()
            # 退出
            elif cmd == 'q':
                self.closeClient()
    
    # 登录
    def register(self):
        msg = self.sockfd.recv(128)
        print(msg.decode())

    # 注册
    def login(self):
        msg = self.sockfd.recv(128)
        print(msg.decode())

    # 查询
    def check(self):
        code = input('请输入要查询的股票代码：')
        try:
            up, ten, days = self.analysis(code)
            radio = round(ten/up, 2)
        except Exception:
            print('无法获取股票数据，请换一只股票')
        else:
            print('股票指标符合度：%s%%，时间间隔：%s天' % (radio*100, days))

    # 关闭客户端
    def closeClient(self):
        # 关闭套接字
        self.sockfd.close()
        # 关闭进程
        sys.exit(0)


if __name__ == "__main__":
    c = Client('localhost', 8000)
    c.operation()