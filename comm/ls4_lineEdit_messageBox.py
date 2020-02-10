#!/usr/bin/python3
#coding = utf-8
# 面向对象的语法就用【 】注释起来

# 使用枚举类型
# 使用正则表达式匹配数字
# 信息弹出框(普通、警告、重要)
# 使用文本框
# 链接信号槽

import sys

# 正则表达式模块
import re
# 总结
# ^ 匹配字符串的开始。
# $ 匹配字符串的结尾。
# \b 匹配一个单词的边界。
# \d 匹配任意数字。
# \D 匹配任意非数字字符。
# x? 匹配一个可选的 x 字符 (换言之，它匹配 1 次或者 0 次 x 字符)。
# x* 匹配0次或者多次 x 字符。
# x+ 匹配1次或者多次 x 字符。
# x{n,m} 匹配 x 字符，至少 n 次，至多 m 次。
# (a|b|c) 要么匹配 a，要么匹配 b，要么匹配 c。
# (x) 一般情况下表示一个记忆组 (remembered group)。你可以利用 re.search 函数返回对象的 groups() 函数获取它的值。
# 正则表达式中的"点号"通常意味着 “匹配任意单字符”

# QtWidgets模块包含了一整套UI元素组件，用于建立符合系统风格的classic界面
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QLineEdit

from PyQt5.QtGui import QIcon
from random      import randint

# 增加unique、不允许Enum中出现数值相同的成员
from enum import Enum, unique

@unique
class ErrInfo(Enum):
    listLenIsZero = -1

# QWidget部件是所有PyQt5用户界面对象的基类
class inputNumber(QWidget):
    def __init__(self):
        # 【子类有了__init__()就不会自动调用基类的__init__()】
        # 【又需要使用基类的__init__()中的变量和实例、就需要使用super()显示调用一下基类的__init__()】
        super().__init__()
        self.initUI()
        self.num = randint(1, 100)

    def initUI(self):
        # 窗口大小和位置：(x, y, 宽, 高)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("猜数游戏")
        self.setWindowIcon(QIcon("image/商标.png"))

        self.keyConfirm = QPushButton("猜数字", self)
        # "猜数字"按钮的大小
        self.keyConfirm.setGeometry(115, 15., 70, 30)
        # 鼠标悬浮在"猜数字"按钮上时会显示下面的文本
        self.keyConfirm.setToolTip("<b>点击这里猜数字</b>")
        # (.clicked)点击"猜数字"按钮、将发出信号，并将这个信号(.connect)连接到self.showMessage
        self.keyConfirm.clicked.connect(self.showMessage)

        # 文本编辑栏
        self.text = QLineEdit("在这里输入数字", self)
        # 选择全部输入文本
        self.text.selectAll()
        # 聚焦功能用于选中全部文本、方便即时输入
        self.text.setFocus()
        self.text.setGeometry(80, 50, 150, 30)

        self.show()

    def showMessage(self):
        # 检查输入是否是纯数字
        if self.text.text().isdigit():
            print("输入的是纯数字")
        else:
            print("输入的不是纯数字")
        # 只要输入文本里面有数字就行、我们取第一个数字来用
        inputStr = self.text.text()
        print("输入 = %s" %(inputStr), "")
        # # 匹配浮点数
        # inputList = re.findall(r"\d+\.?\d*", inputStr)
        # 匹配正整数
        inputList = re.findall(r"\d+", inputStr)
        print(inputList, inputList.__len__())
        if inputList.__len__() == 0:
            inputNumber = ErrInfo.listLenIsZero
        else:
            inputNumber = int(inputList[0])
            print("数字 = %d" %(inputNumber), "")
        # 输入结果
        if inputNumber == ErrInfo.listLenIsZero:
            # .warning:弹出信息框(警告)
            QMessageBox.warning(self, "Note", "请输入数字")
            self.num = randint(1, 100)
            self.text.clear()
            self.text.setFocus()
        elif inputNumber > self.num:
            # .about:弹出信息框(普通)
            QMessageBox.about(self, "看结果", "猜大了")
            self.text.setFocus()
        elif inputNumber < self.num:
            QMessageBox.about(self, "看结果", "猜小了")
            self.text.setFocus()
        else:
            # .critical:弹出信息框(重要)
            QMessageBox.critical(self, "看结果", "答对了，下一轮")
            self.num = randint(1, 100)
            self.text.clear()
            self.text.setFocus()

    # 关闭QWidget会生成QCloseEvent
    # 这里用event来接收main.loop的事件
    def closeEvent(self, event):
        # .question(self, title, text, keyList, selectKey)
        replay = QMessageBox.question(self, "确认", "确认退出吗", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if replay == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    # 每个PyQt5应用程序必须创建一个应用程序对象
    # 这里使用命令行参数 创建一个应用程序对象、使得程序可以从命令行启动
    # argv[0] = 应用程序的名字，argv[1:]就是参数列表了
    app = QApplication(sys.argv)
    exe = inputNumber()
    # 调用exec_()方法时、应用程序进入主循环main.loop
    # 退出(但不结束主循环main loop)、后面开始接受事件处理
    sys.exit(app.exec_())

    # GUI的事件驱动机制：
    # 没有事件：main loop控制应用程序进入休眠
    # 接到事件：main loop唤醒应用程序