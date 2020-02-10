#!/user/bin/python3
# coding = utf-8

# 密码框

import sys

from enum import Enum

from PyQt5.QtCore    import Qt
from PyQt5.QtCore    import QEvent
from PyQt5.QtCore    import QRegExp

from PyQt5.QtGui     import QIcon
from PyQt5.QtGui     import QKeyEvent
from PyQt5.QtGui     import QKeySequence
from PyQt5.QtGui     import QRegExpValidator

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLineEdit


class UsePasswdDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 240, 90)
        self.setWindowTitle("密码框")
        self.setWindowIcon(QIcon("image/商标.png"))

        self.passwdLabel = QLabel("请输入密码", self)
        self.passwdLabel.setGeometry(20, 10, 100, 20)
        self.edit = QLineEdit(self)
        self.edit.setGeometry(20, 30, 200, 20)
        self.edit.installEventFilter(self)

        self.keyConfirm = QPushButton("确定", self)
        self.keyConfirm.move(40, 60)
        self.keyCancel  = QPushButton("取消", self)
        self.keyCancel.move(130, 60)

        # 右键不出现文本复制菜单
        self.edit.setContextMenuPolicy(Qt.NoContextMenu)
        self.edit.setPlaceholderText("密码为6-15位数字和字母(字母开头)")
        self.edit.setEchoMode(QLineEdit.Password)

        self.show()

        # 字母开头 + 数字和字母，最大长度为14位
        register  = QRegExp("^[a-zA-Z][0-9A-Za-Z]{14}$")
        # 验证器
        validator = QRegExpValidator(register, self.edit)
        # 设置约束条件
        self.edit.setValidator(validator)

        # self.keyConfirm.clicked.connect(self.Ok)
        # self.keyCancel.clicked.connect(self.Cancel)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = UsePasswdDialog()
    sys.exit(app.exec_())