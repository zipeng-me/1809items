# -*- coding:UTF-8 -*-
import sys,os
from PyQt5.QtWidgets import QMainWindow,QApplication,QHBoxLayout,QPushButton,QWidget,QLineEdit
from PyQt5.QtGui import QIcon
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

        self.nameEd1 = QLineEdit()
        
        
        # 创建一个按钮 按钮上文字显示
        self.button1 = QPushButton('查询')
        self.button2 = QPushButton('退出')
        # self.button1.Qsize(20,20)
        # button->setStyleSheet"QPushButton{ font-family:'Microsoft YaHei';font-size:12px;color:#666666;}");
        # 将按钮的clicked信号与onButtonClick槽函数关联起来
        self.button1.clicked.connect(self.onButtonClick)
        self.button2.clicked.connect(self.onButtonClic)
        # 使按钮水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.nameEd1)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)
    def Icon(self):
        # 程序图标
        self.setWindowIcon(QIcon("./killer7.ico"))
    def onButtonClick(self):
        # 创建发送信号的对象
        
        print(self.nameEd1.text())
        sender = self.sender()
        # 点击关闭窗口打印文字
        print(sender.text()+'按下了')
        os.system("数据可视化展示界面.py")
        # 调用Qapplication类中的方法
        # qApp = QApplication.instance()
        # 使按钮具有关闭窗口功能
        # qApp.quit()
    def onButtonClic(self):
        # 创建发送信号的对象
        sender = self.sender()
        # 点击关闭窗口打印文字
        print(sender.text()+'按下了')
        # os.system("数据可视化展示界面.py")
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