#!/usr/bin/python3
#coding = utf-8

# 窗口布局(水平框布局 和 垂直框布局)
# 做一个小部件可以自适应拉伸的窗口

import sys

from PyQt5.QtGui     import QIcon

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout   # 水平方向布局
from PyQt5.QtWidgets import QVBoxLayout   # 垂直方向布局

class ViewLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("小部件可以自适应拉伸的窗口")
        # 放置三个按钮：默认在右下角
        keyScissor = QPushButton("剪刀", self)
        keyRock    = QPushButton("石头", self)
        keyPaper   = QPushButton("布",   self)
        # 创建水平框布局(可伸缩的空间)
        hbox = QHBoxLayout()
        # 水平框：增加拉伸因子(伸缩量 = 1)
        # 水平框：增加三个按钮，拉伸因子会将三个按钮所在的水平空白空间按比例分布(2:1:1:2)
        # 水平框伸缩后、这个比例不变、这就保持了按键之间的相对位置和相对于窗体的位置不变(自适应)
        hbox.addStretch(2)
        hbox.addWidget(keyScissor)
        hbox.addStretch(1)
        hbox.addWidget(keyRock)
        hbox.addStretch(1)
        hbox.addWidget(keyPaper)
        hbox.addStretch(2)
        # 窗口垂直布局
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        # 将水平布局放置在垂直布局中
        # 只有一个垂直空间比例：垂直布局的拉伸因子会将水平框推到窗口的底部
        vbox.addLayout(hbox)
        # 以上面的配置来设置窗口主要布局
        self.setLayout(vbox)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = ViewLayout()
    app.exit(app.exec_())