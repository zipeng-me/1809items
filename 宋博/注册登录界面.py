# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中Qlabel例子
   按住 Alt + N , Alt + P , Alt + O , Alt + C 切换组件控件
  
'''
import os
from PyQt5.QtCore import QObject,pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sys  
# from 注册登录信息储存数据库 import*
class QlabelDemo(QDialog):  
    def __init__(self ):  
        super().__init__()
         
        self.setWindowTitle('AID1809')

        nameLb1 = QLabel('账号：', self)
        self.nameEd1 = QLineEdit( self )
        nameLb1.setBuddy(self.nameEd1)
        
        nameLb2 = QLabel('密码：', self)
        self.nameEd2 = QLineEdit( self )
        self.nameEd2.setEchoMode( QLineEdit.Password )
        nameLb2.setBuddy(self.nameEd2)
        
        btnOk = QPushButton('登录')
        btnOk.setCheckable(True)
        btnOk.clicked.connect(self.link_hovered)

        btnCancel = QPushButton('注册')
        btnCancel.setCheckable(True)
        btnCancel.clicked.connect(self.link_hover)

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

    def link_hovered(self):
        print(self.nameEd1.text())
        print(self.nameEd2.text())
        os.system("用户查询.py")
    def link_hover(self):
        print(self.nameEd1.text())
        print(self.nameEd2.text())
        # os.system("用户查询.py")
    def Icon(self):
        # 程序图标
        self.setWindowIcon(QIcon("./killer7.ico"))

if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    labelDemo = QlabelDemo()  
    labelDemo.Icon()
    labelDemo.show()  
    sys.exit(app.exec_())
