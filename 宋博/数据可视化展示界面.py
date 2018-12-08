# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout,QFontDialog,QMenu,QMenuBar,QMainWindow,QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPalette,QIcon
import sys

class WindowDemo(QWidget):
    def __init__(self):
        
        super().__init__()
       
        label1 = QLabel('''推荐的
                    股票
                    ''') #标签1
        # label2 = QLabel(self) #标签2
        label3 = QLabel(self) #标签3
        label4 = QLabel(self) #标签4
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
        # 设置标签2文本
        # nameLb1 = QLabel('账号：')
        # nameEd1 = QLineEdit( self )
        # nameLb1.setBuddy(nameEd1)
        
        # label2.setText("<a href='#'>选择标题字体大小</a>")
        # 居中显示标签3
        label3.setAlignment(Qt.AlignCenter)
        # 设置标签3提示框文字
        label3.setToolTip('这是图片标签')
        # 设置标签3象图
        label3.setPixmap(QPixmap('./timg.gif'))
        # 设置标签4文本
        label4.setText('''<a href='#'>返回上一级<br>查询股票</a>''')
        # 居右显示标签
        label4.setAlignment(Qt.AlignRight)
        # 设置标签4提示框文字
        label4.setToolTip('这是一个超链接标签')   
        # 在窗口布局添加控件
        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addStretch()

        # vbox.addStretch()
        # mainLayout.addWidget(nameLb1,0,0)
        # mainLayout.addWidget(nameEd1,0,1,1,2)
        
        vbox.addWidget(label3)
        vbox.addStretch()
        
        vbox.addWidget(label4)

        # 允许标签l控件访问超链接
        # label1.setOpenExternalLinks(True)
        # 允许标签4控件访问超链接
        label4.setOpenExternalLinks(False)
        # 点击标签绑定点击槽事件
        label4.linkActivated.connect(link_clicked)
        # 点击标签绑定划过槽事件
        # label2.linkActivated.connect(self.getFont)
        # 鼠标可以选择标签1中的文本
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.setLayout(vbox)
        self.setWindowTitle('查询股票的信息')
    def Icon(self):
        # 程序图标
        self.setWindowIcon(QIcon("./killer7.ico"))
    # def getFont(self):
    #     font,ok = QFontDialog.getFont()
    #     if ok:
    #         self.fontLineEdit.setFont(font)
    #         print(font)

def link_clicked():
    print("当用鼠标点击laber-4标签时,触发事件")
    # sender = self.sender()
    qApp = QApplication.instance()
    qApp.quit()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowDemo()
    win.Icon()
    win.show()
    sys.exit(app.exec())
