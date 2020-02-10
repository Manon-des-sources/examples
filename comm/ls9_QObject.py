#!/usr/bin/python3
#coding = utf-8
# 面向对象的语法就用【 】注释起来

# 使用鼠标按下接口：def mousePressEvent(self, event):

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
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtCore    import pyqtSignal
from PyQt5.QtCore    import QObject

# 使用pyqtSignal创建一个名为shouMouse的信号
class sendSignal(QObject):
    showMouse = pyqtSignal()

class SignalsAndSlots_QObject(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("发送信号")
        self.setWindowIcon(QIcon("image/商标.png"))
        # 将自定义信号连接到self.shouwYou
        self.sender = sendSignal()
        self.sender.showMouse.connect(self.shouwYou)
        self.show()
    def shouwYou(self):
        QMessageBox.about(self, "鼠标", "你点击鼠标了")
    # mousePressEvent是系统mouse内置接口
    def mousePressEvent(self, event):
        # 点击鼠标时、发出showMouse信号、并调用相应的槽函数
        self.sender.showMouse.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = SignalsAndSlots_QObject()
    sys.exit(app.exec_())
