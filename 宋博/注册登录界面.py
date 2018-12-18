# -*- coding: utf-8 -*-
import os
from PyQt5.QtCore import QObject,pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sys  
from socket import *
# from 注册登录信息储存数据库 import*
class QlabelDemo(QDialog):  
    def __init__(self ):  
        # 继承父类方法
        super().__init__()
        # 窗口标题
        self.setWindowTitle('AID1809')
        # 创建“账号”标签
        nameLb1 = QLabel('账号：', self)
        # 创建“账号”输入栏
        self.nameEd1 = QLineEdit( self )
        # 把标签和输入栏关联起来
        nameLb1.setBuddy(self.nameEd1)
        # 创建“密码”标签
        nameLb2 = QLabel('密码：', self)
        # 创建“密码”输入栏
        self.nameEd2 = QLineEdit( self )
        # 输入栏加密
        self.nameEd2.setEchoMode( QLineEdit.Password )
        # 把标签和输入栏关联起来
        nameLb2.setBuddy(self.nameEd2)
        # 创建“登录”按钮
        btnOk = QPushButton('登录')
        # 创建检查信号
        btnOk.setCheckable(True)
        # 创建点击信号绑定槽信号
        btnOk.clicked.connect(self.link_click1)
        # 创建“注册”按钮
        btnCancel = QPushButton('注册')
        # 创建检查信号
        btnCancel.setCheckable(True)
        # 创建点击信号绑定槽信号
        btnCancel.clicked.connect(self.link_click2)

        # 布局
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLb1,0,0)
        mainLayout.addWidget(self.nameEd1,0,1,1,2)
        
        mainLayout.addWidget(nameLb2,1,0)
        mainLayout.addWidget(self.nameEd2,1,1,1,2)
         
        mainLayout.addWidget(btnOk,2,1)
        mainLayout.addWidget(btnCancel,2,2) 
       
        # 绑定ip
        HOST = '172.178.8.35'
        # 绑定端口
        PORT = 8000
        # 创建套接字
        self.s = socket()
        # 连接服务器
        self.s.connect((HOST,PORT)) 

    # 创建登录点击事件1
    def link_click1(self):
        # 获得用户输入的账号
        name = self.nameEd1.text()
        # 获得用户输入的密码
        passwd = self.nameEd2.text()
        # 调用登入方法
        self.do_login(name,passwd)
        # 接受服务器反馈
        if self.data == 'OK':
            print("登录成功")  
            # 打开外部文件
            os.system("用户查询.py")
    # 创建注册点击事件2
    def link_click2(self):
        # 获得用户输入的账号
        name = self.nameEd1.text()
        # 获得用户输入的密码
        passwd = self.nameEd2.text()
        # 调用注册方法
        self.do_register(name,passwd)
    # 登录方法
    def do_login(self,name,passwd):
        msg = "L %s %s"%(name,passwd)
        # 向服务器发送请求
        self.s.send(msg.encode())
        # 接受服务器的反馈
        self.data = self.s.recv(128).decode()
    # 注册方法
    def do_register(self,name,passwd):    
        msg = "R %s %s"%(name,passwd)
        # 向服务器发送请求
        self.s.send(msg.encode())
    # 图标方法
    def Icon(self):
        # 程序图标
        self.setWindowIcon(QIcon("./killer7.ico"))

if __name__ == "__main__":  
    # 获得外部参数
    app = QApplication(sys.argv)  
    # 创建对象
    labelDemo = QlabelDemo()  
    # 获得图标
    labelDemo.Icon()
    # 展示窗口
    labelDemo.show()  
    # 关闭窗口
    sys.exit(app.exec_())
