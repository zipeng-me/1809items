# -*- coding:utf-8 -*-
'''服务器
服务器功能如下：

'''
import socket
import select
import queue
import sys
import pymysql
from analysis import Analysis

# 服务器
class Server(Analysis):
    # 初始化
    def __init__(self, ip, port):
        self.__IP = ip
        self.__PORT = port
        # 地址
        self.__ADDR = (self.__IP, self.__PORT)
        # 创建套接字
        self.runServer()
        self.create_epoll()
        # 加载股票分析信息
        # Analysis()

    # 创建服务器套接字
    def runServer(self):
        # 创建TCP/IP套接字
        self.sockfd = socket.socket()
        # 设置地址复用
        self.sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 设置地址非阻塞
        self.sockfd.setblocking(False)
        # 绑定地址
        self.sockfd.bind(self.__ADDR)
        # 监听
        self.sockfd.listen(10)

    # 创建epoll
    def create_epoll(self):
        # 超时阻塞时间
        self.TIMEOUT = 10
        # 创建epoll对象
        self.epoll = select.epoll()
        # 注册服务器
        self.epoll.register(self.sockfd.fileno(), select.EPOLLIN)
        # 用于保存客户端消息的字典
        self.messages = {}
        # 用于存放文件句柄和套接字对象的字典
        self.dict_sockfd = {self.sockfd.fileno():self.sockfd}

    # 多路复用，处理客户端连接
    def handle(self):
        while True:
            # 轮询连接事件
            events = self.epoll.poll(self.TIMEOUT)
            # 如果无连接，重新轮询
            if not events:
                continue
            # 如果有，处理连接事件
            for fd, event in events:
                # 把对应句柄的套接字对象从字典中取出
                sockfd = self.dict_sockfd[fd]
                # 如果是服务器的套接字，处理新连接
                if sockfd is self.sockfd:
                    # 连接
                    self.conn, self.addr = self.sockfd.accept()
                    # 将新连接设置为非阻塞
                    self.conn.setblocking(False)
                    # 注册新连接
                    self.epoll.register(self.conn.fileno(), select.EPOLLIN)
                    # 把新连接的句柄和套接字添加到字典中
                    self.dict_sockfd[self.conn.fileno()] = self.conn
                    # 以对象为键，创建队列，保存连接信息
                    self.messages[self.conn] = queue.Queue()
                # 处理关闭事件
                elif event & select.EPOLLHUP:
                    # 注销
                    self.epoll.unregister(fd)
                    # 删除队列内的信息
                    del self.messages[self.dict_sockfd[fd]]
                    # 关闭套接字
                    self.dict_sockfd[fd].close()
                    # 删除字典信息
                    del self.dict_sockfd[fd]
                # 处理读事件
                elif event & select.EPOLLIN:
                    # 接收数据
                    data = sockfd.recv(1024)
                    # 将数据放入对应字典
                    self.messages[sockfd].put(data)
                    # 修改为写事件
                    self.epoll.modify(fd, select.EPOLLOUT)
                # 处理写事件
                elif event & select.EPOLLOUT:
                    try:
                        # 从字典中获取数据
                        msg = self.messages[sockfd].get_nowait().decode()
                    except queue.Empty:
                        # 如果无数据可获取，就修改为读事件
                        self.epoll.modify(fd, select.EPOLLIN)
                    else:
                        # 处理数据
                        # 登录
                        if msg is None:
                            return
                        elif msg[0] == 'L':
                            self.login(sockfd)
                        # 注册
                        elif msg[0] == 'R':
                            self.register(sockfd)
                        # 查询
                        elif msg[0] == 'A':
                            self.check(sockfd)

    # 注册
    def login(self, sockfd):
        sockfd.send('登录'.encode())

    # 登录
    def register(self, sockfd):
        sockfd.send('注册'.encode())

    # 查询
    def check(self, sockfd):
        # 客户端启动后，推送信息
        sockfd.send('600660'.encode())

    # 关闭服务器
    def serverClose(self):
        # 注销
        self.epoll.unregister(self.sockfd.fileno())
        # 关闭epoll
        self.epoll.close()
        # 关闭服务端套接字
        self.sockfd.close()
        # 关闭进程
        sys.exit(0)

if __name__ == "__main__":
    s = Server('localhost', 8000)
    s.handle()
    