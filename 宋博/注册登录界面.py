# -*- coding: utf-8 -*-

import os
from PyQt5.QtCore import QObject,pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sys  
# from 注册登录信息储存数据库 import*
class QlabelDemo(QDialog):  
    def __init__(self ):  
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
       
    #     signal5 = pyqtSignal(dict)
    #     self.signal5.connect(self.signalCall5)
    
    #     self.signal5.emit({'a':'b'})
    # def signalCall5(self,val):
    #     print('signl5',val)
    
    
    # 创建点击事件1
    def link_click1(self):
        print(self.nameEd1.text())
        print(self.nameEd2.text())
        # 打开外部文件
        os.system("用户查询.py")
    # 创建点击事件2
    def link_click2(self):
        print(self.nameEd1.text())
        print(self.nameEd2.text())

    def Icon(self):
        # 程序图标
        self.setWindowIcon(QIcon("./killer7.ico"))

if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    # 创建对象
    labelDemo = QlabelDemo()  
    # 获得图标
    labelDemo.Icon()
    # 展示窗口
    labelDemo.show()  
    # 关闭窗口
    sys.exit(app.exec_())
