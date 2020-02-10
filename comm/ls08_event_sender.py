#!/usr/bin/python3
#coding = utf-8
# 面向对象的语法就用【 】注释起来

# 使用枚举的成员名及其数值
# 获取事件发送者
# 链接信号槽

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
from PyQt5.QtWidgets import QPushButton

from random import randint
from enum   import Enum, unique
# 增加unique、不允许Enum中出现数值相同的成员
@unique
# Player.Scissor.value才是一个整数
class Player(Enum):
    Scissor = 1
    Paper   = 2
    Rock    = 3

class SignalsAndSlots_sender(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("use sender")
        keyScissor = QPushButton("剪刀", self)
        keyScissor.setGeometry(30, 180, 50, 50)

        keyPaper   = QPushButton("布",   self)
        keyPaper.setGeometry(170, 180, 50, 50)

        keyRock    = QPushButton("石头", self)
        keyRock.setGeometry(100, 180, 50, 50)

        # 发送者和接受者之间通过.connect连接到同一个信号槽.buttonClicked
        keyScissor.clicked.connect(self.buttonClicked)
        keyPaper.clicked.connect(self.buttonClicked)
        keyRock.clicked.connect(self.buttonClicked)

        self.show()

    def buttonClicked(self):
        compter = randint(1, 3)
        player  = 0
        # 获取信号的发送者
        sender  = self.sender()
        if sender.text() == "剪刀":
            player = Player.Scissor.value
        elif sender.text() == "石头":
            player = Player.Rock.value
        else:
            player = Player.Paper.value
        print(player, compter)
        # 判断结果
        if player == compter:
            QMessageBox.about(self, "结果", "平手")
        elif player == Player.Scissor.value and compter == Player.Rock.value:
            QMessageBox.about(self, "结果", "电脑：石头，电脑赢了")
        elif player == Player.Rock.value and compter == Player.Paper.value:
            QMessageBox.about(self, "结果", "电脑：布， 电脑赢了")
        elif player == Player.Paper.value and compter == Player.Scissor.value:
            QMessageBox.about(self, "结果", "电脑：剪刀， 电脑赢了")
        elif player == Player.Scissor.value and compter == Player.Paper.value:
            QMessageBox.about(self, "结果", "电脑：石头，玩家赢了")
        elif player == Player.Rock.value and compter == Player.Scissor.value:
            QMessageBox.about(self, "结果", "电脑：布， 玩家赢了")
        elif player == Player.Paper.value and compter == Player.Rock.value:
            QMessageBox.about(self, "结果", "电脑：剪刀， 玩家赢了")
        else:
            QMessageBox.warning(self, "Note", "电脑：未知")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = SignalsAndSlots_sender()
    sys.exit(app.exec_())