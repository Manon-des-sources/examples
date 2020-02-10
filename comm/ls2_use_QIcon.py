#!/usr/bin/python3
#coding = utf-8
# 面向对象的语法就用【 】注释起来

# Icon图标

import sys
# QtWidgets模块包含了一整套UI元素组件，用于建立符合系统风格的classic界面
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui     import QIcon
from PyQt5.QtCore    import QCoreApplication

# QWidget部件是所有PyQt5用户界面对象的基类
class Ico(QWidget):
    def __init__(self):
        # 【子类有了__init__()就不会自动调用基类的__init__()】
        # 【又需要使用基类的__init__()中的变量和实例、就需要使用super()显示调用一下基类的__init__()】
        super().__init__()
        # 【初始化时就调用下面定义的窗口初始化来创建一个初始窗口】
        self.initUI()
    def initUI(self):
        print("def initUI(self):")
        # 窗口大小和位置：(x, y, 宽, 高)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("hello world!")
        # 从ico路径拿到ico图标
        self.setWindowIcon(QIcon("image/商标.png"))
        # self.setWindowIcon(QIcon("image/1002.png"))

        keyClose = QPushButton("Close", self)
        # QCoreApplication包含主事件循环、处理和调度所有事件
        # (.clicked)点击Close键、将发出信号，并将这个信号(.connect)连接到.quit
        keyClose.clicked.connect(QCoreApplication.instance().quit)
        keyClose.resize(70, 30)
        keyClose.move(50, 50)

        self.show()

if __name__ == "__main__":
    # 每个PyQt5应用程序必须创建一个应用程序对象
    # 这里使用命令行参数 创建一个应用程序对象、使得程序可以从命令行启动
    # argv[0] = 应用程序的名字，argv[1:]就是参数列表了
    app = QApplication(sys.argv)
    exe = Ico()
    sys.exit(app.exec_())
