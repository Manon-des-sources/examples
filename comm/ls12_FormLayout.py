#!/usr/bin/python3
#coding = utf-8

# 窗口布局(表单布局)
# 做一个小部件可以自适应拉伸的窗口


import sys

from PyQt5.QtGui     import QIcon

from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout


class ViewLayout_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("表单布局")
        self.setWindowIcon(QIcon("image/商标.png"))
        # 创建一个表单
        formlayout   = QFormLayout()
        nameLabel    = QLabel("姓名")
        nameLineEdit = QLineEdit("")
        introductionLabel   = QLabel("简介")
        introductionLinEdit = QLineEdit("")
        introductionLinEdit.setBaseSize(100, 200)
        # 将Label添加到表单行中
        formlayout.addRow(nameLabel, nameLineEdit)
        formlayout.addRow(introductionLabel, introductionLinEdit)
        # 设置layout
        self.setLayout(formlayout)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = ViewLayout_Form()
    app.exit(app.exec_())