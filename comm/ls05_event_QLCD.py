#!/usr/bin/python3
#coding = utf-8
# 面向对象的语法就用【 】注释起来

# 使用表盘
# 使用滑块
# 使用LCD盘

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
from PyQt5.QtWidgets import QLCDNumber
from PyQt5.QtWidgets import QDial
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QApplication

class SignalsAndSlots_QLCD(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 260)
        self.setWindowTitle("数字表盘")
        self.setWindowIcon(QIcon("image/商标.png"))
        # LCD显示盘
        lcd  = QLCDNumber(self)
        lcd.setGeometry(100, 50, 150, 60)
        # 数字表盘
        dial = QDial(self)
        dial.setGeometry(50, 140, 100, 100)
        # 滑块
        slider = QSlider(self)
        slider.setGeometry(190, 140, 100, 100)
        # dial对象发出信号、lcd对象接收信号，槽是对信号作出反应的方法
        # 发送者和接受者之间通过.connect连接
        dial.valueChanged.connect(lcd.display)
        slider.valueChanged.connect(lcd.display)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = SignalsAndSlots_QLCD()
    sys.exit(app.exec_())