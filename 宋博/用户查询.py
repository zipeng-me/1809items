# -*- coding:UTF-8 -*-
import sys,os
from PyQt5.QtWidgets import QMainWindow,QApplication,QHBoxLayout,QPushButton,QWidget,QLineEdit
from PyQt5.QtGui import QIcon
from socket import *
from time import sleep
class MainWindow(QMainWindow):
    def __init__(self):
        # 引用父类
        super().__init__()
        # 窗口尺寸
        self.resize(400,50)

        # 生成状态栏
        # self.status = self.statusBar()
        # 状态栏文字
        # self.status.showMessage('这是状态栏提示',5000)

        # 窗口标题
        self.setWindowTitle('查询股票界面')
        
        # 用户输入栏设置
        self.nameEd1 = QLineEdit()
        
        # 创建一个按钮 按钮上文字显示
        self.button1 = QPushButton('查询')
        self.button2 = QPushButton('退出')
        
        # self.button1.Qsize(20,20)
        # button->setStyleSheet"QPushButton{ font-family:'Microsoft YaHei';font-size:12px;color:#666666;}");
        
        # 将按钮的clicked信号与onButtonClick槽函数关联起来
        self.button1.clicked.connect(self.onButton1Click)
        self.button2.clicked.connect(self.onButton2Click)
        
        # 使按钮水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.nameEd1)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        main_frame = QWidget()
        main_frame.setLayout(layout)       
        self.setCentralWidget(main_frame)

        HOST = '127.0.0.1'
        PORT = 8000
        s = socket()
        s.connect((HOST,PORT)) #连接服务器
    
    def do_refer(self,refer):    
        msg = "C %s"%(refer)
        # 发送请求
        s.send(msg.encode())
        # 等待确认
        data = s.recv(128).decode()
    def Icon(self):
        # 程序图标
        self.setWindowIcon(QIcon("./killer7.ico"))

    def onButton1Click(self):
        # 打印用户输入的账号
        refer = self.nameEd1.text()
        self.do_refer(refer)
        if data == 'OK':
            print("登录成功")
            sleep(0.5)  
        # 打开外部文件
            os.system("数据可视化展示界面.py")
    def onButton2Click(self,s):
        # 关闭套接字
        s.close()
        # 调用Qapplication类中的方法
        qApp = QApplication.instance()
        # 使按钮具有关闭窗口功能
        qApp.quit()
        
if __name__ == "__main__":
    #s 使python 可以从外部获取参数   
    app = QApplication(sys.argv)
    # 生成对象
    form = MainWindow()
    # 调用程序图标方法
    form.Icon()
    # 展示窗口
    form.show()
    # 关闭窗口
    sys.exit(app.exec())