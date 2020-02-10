#!/usr/bin/python3
#coding = utf-8

# 对话框：颜色、字体

import sys

from PyQt5.QtGui     import QIcon
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtWidgets import QFontDialog
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QFileDialog

class UseDialog_Font(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("对话框：颜色、字体")
        self.setWindowIcon(QIcon("image/商标.png"))
        # 打开文本框(可编辑)
        self.text = QTextEdit(self)
        self.text.setGeometry(20, 20, 300, 270)

        self.keyOpenFile = QPushButton("打开文件", self)
        self.keyOpenFile.move(350, 20)
        self.keyColor = QPushButton("选择颜色", self)
        self.keyColor.move(350, 120)
        self.keyFont = QPushButton("选择字体", self)
        self.keyFont.move(350, 70)

        self.keyOpenFile.clicked.connect(self.openFile)
        self.keyColor.clicked.connect(self.selectColor)
        self.keyFont.clicked.connect(self.selectFont)

        self.show()

    def openFile(self):
        # .getOpenFileName(窗口标题, 默认路径, 文件类型)
        # 返回文件路径(字符串)
        fname = QFileDialog.getOpenFileName(self, "打开文件", './', '*')
        if fname[0]:
            # 使用with语句打开文件后、它会自动关闭文件
            with open(fname[0], 'r', encoding='utf-8', errors='ignore') as f:
                self.text.setText(f.read())
    def selectFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text.setCurrentFont(font)
    def selectColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.text.setTextColor(color)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = UseDialog_Font()
    sys.exit(app.exec_())