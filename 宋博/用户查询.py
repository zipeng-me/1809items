# -*- coding:UTF-8 -*-
import sys,os
from PyQt5.QtWidgets import QMainWindow,QApplication,QHBoxLayout,QPushButton,QWidget,QLineEdit
from PyQt5.QtGui import QIcon
from socket import *
from time import sleep
import stock_single
class MainWindow(QMainWindow):
    def __init__(self):
        # 引用父类
        super().__init__()
        # 窗口尺寸
        self.resize(400,50)
        # 窗口标题
        self.setWindowTitle('查询股票界面')        
        # 用户输入栏设置
        self.nameEd1 = QLineEdit()      
        # 创建一个按钮 按钮上文字显示
        self.button1 = QPushButton('查询')
        self.button2 = QPushButton('退出')
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
        # 绑定ip
        HOST = '172.178.8.35'
        # 绑定端口
        PORT = 8000
        # 创建套接字
        self.s = socket()
        #连接服务器
        self.s.connect((HOST,PORT)) 
    # 登录方法
    def do_refer(self,refer):    
        msg = "C %s"%(refer)
        # 发送请求
        self.s.send(msg.encode())
        # 接受购买建议
        self.data1 = self.s.recv(1024*5).decode()
        # 接受股票k线信息
        data = self.s.recv(1024*8)
        # 调用解析k线数据方法
        data = self.decode_k_data(data.decode())
        # 打印购买建议
        print(self.data1)
        # 调用stock_single.py中的StockSingle方法
        ss = stock_single.StockSingle(refer,data)
        ss.draw_k(refer)
        # 打印k线数据
        print(data)      
    # 解析k线数据方法
    def decode_k_data(self,data):
        lst = data.split()
        lst_temp = []
        for i in lst:
            t = i.split(',')
            lst_temp.append((t[0], float(t[1]), float(t[2]), 
            float(t[3]), float(t[4])))
        return lst_temp
    # 程序图标
    def Icon(self): 
        self.setWindowIcon(QIcon("./killer7.ico"))
    # 查询按钮点击方法
    def onButton1Click(self):
        # 打印用户输入股票代码
        refer = self.nameEd1.text()
        # 把股票代码发给服务器
        self.do_refer(refer)
        if self.data1:
            # 书写本地文件
            p = open('购买建议.txt','wb')
            # 把购买建议写入文档
            p.write(self.data1.encode())
            # 关闭文件
            p.close()
            # 睡眠保证别的程序运行结束
            sleep(2)  
            # 打开外部文件
            os.system("数据可视化展示界面.py")
    # 退出按钮点击方法
    def onButton2Click(self):
        # 关闭套接字
        self.s.close()
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
    
