#!/usr/bin/python3
#coding = utf-8

# 对话框：输入框

import sys

from PyQt5.QtGui     import QIcon
from PyQt5.QtGui     import QFont
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QTextBrowser

class UseDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(500, 500, 500, 550)
        self.setWindowTitle("使用对话框")
        self.setWindowIcon(QIcon("image/商标.png"))
        
        # 全局字体
        font = QFont("字体", 11)
        self.setFont(font)
        
        self.name = QLabel("姓名：", self)
        self.name.move(20, 20)
        self.nameV = QLabel("陈", self)
        self.nameV.setGeometry(80, 20, 100, 15)
        # 单独设置字体
        # self.nameV.setFont(font)
        self.keyName = QPushButton("修改姓名", self)
        self.keyName.move(250, 20)

        self.age = QLabel("年龄：", self)
        self.age.move(20, 80)
        self.ageV = QLabel("18", self)
        self.ageV.setGeometry(80, 80, 100, 15)
        self.keyage = QPushButton("修改年龄", self)
        self.keyage.move(250, 80)

        self.gender = QLabel("性别：", self)
        self.gender.move(20, 140)
        self.genderV = QLabel("男", self)
        self.genderV.setGeometry(80, 140, 100, 15)
        self.keyGender = QPushButton("修改性别", self)
        self.keyGender.move(250, 140)

        self.tall = QLabel("身高：", self)
        self.tall.move(20, 200)
        self.tallV = QLabel("175", self)
        self.tallV.setGeometry(80, 200, 100, 15)
        self.keytall = QPushButton("修改身高", self)
        self.keytall.move(250, 200)

        self.info = QLabel("基本信息：", self)
        self.info.move(20, 260)
        self.infoV = QTextBrowser(self)
        self.infoV.setGeometry(20, 320, 250, 200)
        self.keyinfo = QPushButton("修改基本信息", self)
        self.keyinfo.move(250, 260)

        self.show()
        self.keyName.clicked.connect(self.showDialog)
        self.keyage.clicked.connect(self.showDialog)
        self.keyGender.clicked.connect(self.showDialog)
        self.keytall.clicked.connect(self.showDialog)
        self.keyinfo.clicked.connect(self.showDialog)

    def showDialog(self):
        sender = self.sender()
        sex = ["男", "女"]
        if sender == self.keyName:
            name, ok = QInputDialog.getText(self, "修改姓名", "请输入姓名：")
            if ok:
                self.nameV.setText(name)
        elif sender == self.keyage:
            # 输入框带增减按钮
            age, ok = QInputDialog.getInt(self, "修改年龄", "请输入年龄：", min = 1)
            if ok:
                self.ageV.setText(str(age))
        elif sender == self.keyGender:
            # 输入框带下拉选择项
            gender, ok = QInputDialog.getItem(self, "修改性别", "请输入性别：", sex)
            if ok and gender in sex:
                self.genderV.setText(gender)
        elif sender == self.keytall:
            # 输入框带增减按钮
            tall, ok = QInputDialog.getDouble(self, "修改身高", "请输入身高：", min = 0.5)
            if ok:
                self.tallV.setText(str(tall))
        elif sender == self.keyinfo:
            info, ok = QInputDialog.getMultiLineText(self, "修改信息", "请输入个人信息：")
            if ok:
                self.infoV.setText(info)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = UseDialog()
    sys.exit(app.exec_())