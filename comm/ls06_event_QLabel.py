#!/usr/bin/python3
#coding = utf-8
# 面向对象的语法就用【 】注释起来

# 使用文本标签(显示在窗口中的文本)
# 按键处理接口：def keyPressEvent(self, event):

# 事件和信号槽
# 事件模型的三个部分
#   事件来源：应用程序/网络/窗口/定时器等状态变化时会生成事件
#   事件对象：将生成的事件封装在事件源中
#   事件目标：被通知去处理事件
# 槽
#   可以是任何一个Python可调用函数
#   发射连接信号时会调用一个槽

import sys

from PyQt5.QtGui     import QIcon
from PyQt5.QtCore    import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel

class SignalsAndSlots_QLabel(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("方向箭头")
        self.setWindowIcon(QIcon("image/商标.png"))
        # 文本标签
        self.lab = QLabel("方向", self)
        self.lab.setGeometry(150, 100, 50, 50)

        self.show()

    # 自定义事件处理
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.lab.setText('↑')
        elif event.key() == Qt.Key_Down:
            self.lab.setText('↓')
        elif event.key() == Qt.Key_Left:
            self.lab.setText('←')
        elif event.key() == Qt.Key_Right:
            self.lab.setText('→')
        else:
            self.lab.setText('○')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = SignalsAndSlots_QLabel()
    sys.exit(app.exec_())