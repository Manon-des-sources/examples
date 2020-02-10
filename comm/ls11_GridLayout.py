#!/usr/bin/python3
#coding = utf-8

# 窗口布局(网格布局)
# 做一个小部件可以自适应拉伸的窗口

# 网格布局(行row,列column)
# .-----------------------------.
# | 0,0 | 0,1 | 0,2 | 0,3 | 0,4 |
# |-----|-----|-----|-----|-----|
# | 1,0 | 1,1 | 1,2 | 1,3 | 1,4 |
# |-----|-----|-----|-----|-----|
# | 2,0 | 2,1 | 2,2 | 2,3 | 2,4 |
# |-----|-----|-----|-----|-----|
# | 3,0 | 3,1 | 3,2 | 3,3 | 3,4 |
# |-----|-----|-----|-----|-----|
# | 4,0 | 4,1 | 4,2 | 4,3 | 4,4 |
# .-----------------------------.

import sys

from PyQt5.QtGui     import QIcon

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLCDNumber

class ViewLayout_Grid(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("网格布局")
        self.setWindowIcon(QIcon("image/商标.png"))
        # 创建一个网格布局
        grid = QGridLayout()
        # 以上面的配置来设置窗口布局
        self.setLayout(grid)
        # 创建一个LCD显示窗
        self.lcd = QLCDNumber()
        # 向网格中添加窗口小部件
        grid.addWidget(self.lcd, 0, 0, 3, 0)
        grid.setSpacing(10)

        names = ['Cls', 'Bc', '',  'Close',
                 '7',   '8',  '9', '/',
                 '4',   '5',  '6', '*',
                 '1',   '2',  '3', '-',
                 '0',   '.',  '=', '+']
        positions = [(i,j) for i in range(4,9) for j in range(0,4)]
        # positions = [(i,j) for i in range(4,9) for j in range(4,8)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            # 以names[]中的元素名创建按钮
            button = QPushButton(name)
            # 将按钮放到网格中、位置
            grid.addWidget(button, *position)
            button.clicked.connect(self.Cli)
        self.show()

    def Cli(self):
        senderText = self.sender().text()
        ls = ['/', '*', '-', '=', '+']
        if senderText in ls:
            self.lcd.display('A')
        else:
            self.lcd.display(senderText)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = ViewLayout_Grid()
    app.exit(app.exec_())