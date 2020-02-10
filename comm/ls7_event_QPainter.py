#!/usr/bin/python3
#coding = utf-8
# 面向对象的语法就用【 】注释起来

# 绘图窗口
# 鼠标事件：def mouseMoveEvent(self, event):
# 绘图事件：def paintEvent(self, event):

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
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication

from PyQt5.QtGui     import QPainter
from PyQt5.QtGui     import QColor

class SiSignalsAndSlots_QPainter(QWidget):
    # 全局变量
    distance_from_center = 0
    def __init__(self):
        super().__init__()
        self.initUI()
        # 不启用跟踪鼠标的话、就需要长按鼠标左键
        # self.setMouseTracking(True)
    def initUI(self):
        self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle("Qt绘图")
        self.setWindowIcon(QIcon("image/商标.png"))
        # 文本标签
        self.label = QLabel(self)
        self.label.resize(500, 40)
        self.show()
        self.pos = None

    def mouseMoveEvent(self, event):
        distance_from_center = round((((event.y() - 250) ** 2) + 
                                      ((event.x() - 500) ** 2)) ** 0.5)
        self.label.setText("坐标：(x: %d, y: %d)" % (event.x(), event.y()) + 
                           "离中心点距离：" + str(distance_from_center))
        self.pos = event.pos()
        self.update()

    def paintEvent(self, event):
        if self.pos:
            q = QPainter(self)
            # 画线：(start.x, start.y, end.x, end.y)
            q.drawLine(0, 0, self.pos.x(), self.pos.y())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    evt = SiSignalsAndSlots_QPainter()
    sys.exit(app.exec_())