# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout,QFontDialog,QMenu,QMenuBar,QMainWindow,QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPalette,QIcon
import sys
from socket import *
class WindowDemo(QWidget):
    def __init__(self):
       # 引用父类方法 
        super().__init__()
        # 绑定ip
        HOST = '172.178.8.35'
        # 绑定端口
        PORT = 8000
        # 创建套接字
        self.s = socket()
        # 连接服务器
        self.s.connect((HOST,PORT)) 
       # 创建标签 显示文字
        # 调用推送建议方法
        qqq = self.advice()
        # 标签1
        label1 = QLabel('%s'%qqq) 
        # 标签3
        label3 = QLabel(self) 
        #标签 4
        label4 = QLabel(self) 
        # 设置标签1文本
        self.fontLineEdit = label1
        # 设置标签自动填满背景功能
        label1.setAutoFillBackground(True)
        # 创建调色板类对象
        palette = QPalette()
        # 选择背景颜色
        palette.setColor(QPalette.Window,Qt.green)
        # 把颜色绑定到标签上
        label1.setPalette(palette)
        # 居中显示标签
        label1.setAlignment(Qt.AlignCenter)     
        # 居中显示标签3
        label3.setAlignment(Qt.AlignCenter)
        # 设置标签3提示框文字
        label3.setToolTip('这是图片标签')
        # 设置标签3象图
        label3.setPixmap(QPixmap('k.png'))
        # 打开文件
        p = open('购买建议.txt','rb')   
        # 调出文档中的文字
        data = p.read().decode()
        # 设置标签4文本
        label4.setText('''<a href='#'>%s</a>'''%data)
        # 关闭文件
        p.close()
        # 居右显示标签
        label4.setAlignment(Qt.AlignRight)
        # 设置标签4提示框文字
        label4.setToolTip('这是一个超链接标签')   
        # 在窗口布局添加控件
        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addStretch()
       
        vbox.addWidget(label3)
        vbox.addStretch()
        
        vbox.addWidget(label4)

        # 允许标签4控件访问超链接
        label4.setOpenExternalLinks(False)
        # 点击标签绑定点击槽事件
        label4.linkActivated.connect(self.link_clicked)
        # 鼠标可以选择标签1中的文本
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.setLayout(vbox)
        # 窗口标题文字
        self.setWindowTitle('查询股票的信息')
       
    # 接受服务器推送建议的方法
    def advice(self):
        msg = "A"
        # 向服务器发送请求
        self.s.send(msg.encode())
        # 接受服务器的反馈
        self.data = self.s.recv(1024*8)
        return self.data.decode()
    # 程序图标
    def Icon(self):
        self.setWindowIcon(QIcon("./killer7.ico"))
    # 点击事件方法
    def link_clicked(self):
        # 打印验证
        print("当用鼠标点击laber-4标签时,触发事件")
        # 关闭函数
        qApp = QApplication.instance()
        qApp.quit()
if __name__ == "__main__":
    # 引入外部参数
    app = QApplication(sys.argv)
    # 创建对象
    win = WindowDemo()
    # 调用图标方法
    win.Icon()
    # 展示窗口
    win.show()
    # 关闭窗口
    sys.exit(app.exec())
