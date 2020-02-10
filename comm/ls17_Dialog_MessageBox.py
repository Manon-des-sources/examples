#!/usr/bin/python3
#coding = utf-8

# 对话框：消息对话框

import sys

from PyQt5.QtGui     import QIcon
from PyQt5.QtGui     import QPixmap
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QMessageBox
# QMessageBox提供的对话框可用于通知或询问用户并接收答案

class UseMessageBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 330, 300)
        self.setWindowTitle("使用消息对话框")
        self.setWindowIcon(QIcon("image/商标.png"))

        self.msgLabel = QLabel("我们的消息框", self)
        self.msgLabel.move(20, 20)
        
        self.keyTip = QPushButton("提示", self)
        self.keyTip.move(20, 70)
        self.keyTip.clicked.connect(self.infoBox)

        self.keyAsk = QPushButton("询问", self)
        self.keyAsk.move(120, 70)
        self.keyAsk.clicked.connect(self.questionBox)

        self.keyWarning = QPushButton("警告", self)
        self.keyWarning.move(220, 70)
        self.keyWarning.clicked.connect(self.warningBox)

        self.keyCritical = QPushButton("错误", self)
        self.keyCritical.move(20, 140)
        self.keyCritical.clicked.connect(self.CriticalBox)

        self.keyRelation = QPushButton("关于", self)
        self.keyRelation.move(120, 140)
        self.keyRelation.clicked.connect(self.relationBox)

        self.keyAboutQt = QPushButton("关于Qt", self)
        self.keyAboutQt.move(220, 140)
        self.keyAboutQt.clicked.connect(self.aboutQtBox)

        self.show()

    # 静态方式创建对话框
    def infoBox(self):
        reply = QMessageBox.information(self, "提示", "这是一个消息提示对话框", 
                                         QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Ok:
            self.msgLabel.setText("你选择了Ok!")
        elif reply == QMessageBox.Close:
            self.msgLabel.setText("你选择了Close!")
        else:
            self.msgLabel.setText("程序错误：不存在的选择")
            print(reply)
            self.msgLabel.setText("程序错误：不存在的选择")
            print(reply)

    # 静态方式创建对话框
    def questionBox(self):
        reply = QMessageBox.question(self, "询问", "这是一个询问消息对话框，默认为No",
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.msgLabel.setText("你选择了Yes!")
        elif reply == QMessageBox.No:
            self.msgLabel.setText("你选择了No!")
        elif reply == QMessageBox.Cancel:
            self.msgLabel.setText("你选择了Cancel!")
        else:
            self.msgLabel.setText("程序错误：不存在的选择")
            print(reply)

    # 基于属性产生消息对话框
    def warningBox(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("警告")
        # 设置警告图标(可选：QMessageBox.Warning、QMessageBox.Information、QMessageBox.Question、QMessageBox.Critical)
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("这是一个警告消息对话框")
        # 扩展信息
        msgBox.setInformativeText("出现更改、需要保存吗?")
        # 创建自定义按钮
        save   = msgBox.addButton("保存", QMessageBox.AcceptRole)
        noSave = msgBox.addButton("不保存", QMessageBox.RejectRole)
        cancel = msgBox.addButton("取消", QMessageBox.DestructiveRole)
        msgBox.setDefaultButton(save)
        # 创建一个复选框(不打钩)
        checkBox = QCheckBox("所有文档都按此操作")
        # 将复选框设置到对话框上
        msgBox.setCheckBox(checkBox)
        # 将复选框状态变化信号连接到槽函数
        checkBox.stateChanged.connect(self.check)
        # 显示对话框、并返回操作结果
        reply = msgBox.exec()
        if reply == QMessageBox.AcceptRole:
            self.msgLabel.setText("你选择了保存")
        elif reply == QMessageBox.RejectRole:
            self.msgLabel.setText("你选择了不保存")
        else:
            self.msgLabel.setText("你选择了取消")

    def CriticalBox(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("错误")
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("这是一个错误消息对话框")
        msgBox.setStandardButtons(QMessageBox.Retry | QMessageBox.Abort | QMessageBox.Ignore)
        msgBox.setDefaultButton(QMessageBox.Retry)
        # Show Details...按钮及其提示信息
        msgBox.setDetailedText("这是详细信息：系统错误1156")
        reply = msgBox.exec()
        if reply == QMessageBox.Retry:
            self.msgLabel.setText("你选择了Retry")
        elif reply == QMessageBox.Abort:
            self.msgLabel.setText("你选择了Abort")
        else:
            self.msgLabel.setText("你选择了Ignore")

    def relationBox(self):
        msgBox = QMessageBox(QMessageBox.NoIcon, "美女", "马丁娜·加西亚")
        msgBox.setIconPixmap(QPixmap("image/马丁娜·加西亚.png"))
        msgBox.exec()

    def aboutQtBox(self):
        QMessageBox.aboutQt(self, "关于Qt")

    def check(self):
        # 判断是否被选中(布尔值)
        if self.sender().isChecked():
            self.msgLabel.setText("已打钩")
        else:
            self.msgLabel.setText("不打钩")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = UseMessageBox()
    sys.exit(app.exec_())