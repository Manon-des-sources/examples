#!/usr/bin/python3
#coding = utf-8

# 对话框：颜色、字体

import sys

from PyQt5.QtGui     import QIcon
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtPrintSupport import QPageSetupDialog
from PyQt5.QtPrintSupport import QPrintDialog
from PyQt5.QtPrintSupport import QPrinter

class UseDialog_Font(QWidget):
    def __init__(self):
        super().__init__()
        # 取得打印机
        self.printer = QPrinter()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("对话框：文件操作")
        self.setWindowIcon(QIcon("image/商标.png"))
        # 打开文本框(可编辑)
        self.text = QTextEdit(self)
        self.text.setGeometry(20, 20, 300, 270)

        self.keyOpenFile = QPushButton("打开文件", self)
        self.keyOpenFile.move(350, 20)
        self.keyOpenFile.clicked.connect(self.openFileDialog)

        self.keyopenFiles = QPushButton("打开多个文件", self)
        self.keyopenFiles.move(350, 70)
        self.keyopenFiles.clicked.connect(self.openFilesDialog)

        self.keySaveFile = QPushButton("保存文件", self)
        self.keySaveFile.move(350, 120)
        self.keySaveFile.clicked.connect(self.saveFileDialog)

        self.keyPageSetup = QPushButton("页面设置", self)
        self.keyPageSetup.move(350, 170)
        self.keyPageSetup.clicked.connect(self.pageSetupDialog)

        self.keyPrint = QPushButton("打印", self)
        self.keyPrint.move(350, 220)
        self.keyPrint.clicked.connect(self.printDialog)

        self.show()

    def openFileDialog(self):
        # .getOpenFileName(窗口标题, 默认路径, 文件类型)
        # 返回文件路径(字符串)
        fname = QFileDialog.getOpenFileName(self, "打开文件", './', '*')
        print(fname)
        if fname[0]:
            # 使用with语句打开文件后、它会自动关闭文件
            with open(fname[0], 'r', encoding='utf-8', errors='ignore') as f:
                self.text.setText(f.read())
    
    def openFilesDialog(self):
        # 返回文件路径(字符串)列表
        fnames = QFileDialog.getOpenFileNames(self, "打开多个文件", './', '*')
        print(fnames)
        if fnames[0]:
            for fname in fnames[0]:
                with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
                    self.text.append(f.read())
    
    def saveFileDialog(self):
        fname = QFileDialog.getSaveFileName(self, "保存文件", './', "Text file (*.txt)")
        if fname[0]:
            with open(fname[0], 'w', encoding='utf-8', errors='ignore') as f:
                # .toPlainText()用于获取QTextEdit的内容
                f.write(self.text.toPlainText())

    def pageSetupDialog(self):
        pageSetupDialog = QPageSetupDialog(self.printer, self)
        pageSetupDialog.exec_()

    def printDialog(self):
        printDialog = QPrintDialog(self.printer, self)
        if QDialog.Accepted == printDialog.exec_():
            # 打印机选择完成后、调用QTextEdit的打印方法进行打印
            self.text.print(self.printer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = UseDialog_Font()
    sys.exit(app.exec_())