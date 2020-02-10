#!/usr/bin/python3
#coding = utf-8

# 搭建一个有菜单栏的主窗口


import sys

from PyQt5.QtGui     import QIcon

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import qApp

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("主窗口")
        self.setWindowIcon(QIcon("image/商标.png"))

        # 创建状态栏
        self.statusBar().showMessage("准备完成")

        # 创建动作：退出
        exitAct = QAction(QIcon('image/退出.png'), "退出(&E)", self)
        exitAct.setShortcut('Ctrl+Q')
        # 鼠标悬停在退出菜单项上时、更新状态栏文字
        exitAct.setStatusTip("退出程序")
        exitAct.triggered.connect(qApp.quit)

        # 创建菜单项：保存
        saveMenu = QMenu("保存(&S)", self)
        saveAct  = QAction(QIcon("image/保存.png"), "保存...", self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip("保存")
        saveAsAct = QAction(QIcon("image/另存为.png"), "另存为...(&O)", self)
        saveAsAct.setStatusTip("另存为")
        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveAsAct)

        # 创建动作：新建
        newAct = QAction(QIcon("image/新建.png"), "新建(&N)", self)
        newAct.setShortcut('Ctrl+N')

        # 创建菜单栏
        menubar = self.menuBar()
        # 菜单栏添加菜单项：文件
        fileMenu = menubar.addMenu("文件(&F)")
        # 文件菜单项添加动作和子菜单
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        # 增加一条分割线、再在下面添加退出项
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        # 创建工具栏
        toolbar = self.addToolBar("工具栏")
        toolbar.addAction(newAct)
        toolbar.addAction(saveAct)
        toolbar.addAction(exitAct)

        self.show()
    
    # 重新实现系统内的contextMenuEvent()方法
    # 增加右键上下文菜单
    def contextMenuEvent(self, event):
        # 创建菜单
        cmenu   = QMenu(self)
        newAct  = cmenu.addAction("新建")
        openAct = cmenu.addAction("打开")
        quitAct = cmenu.addAction("退出")
        # 鼠标坐标(event.pos())被.mapToGlobal转换为全局屏幕坐标
        # .exec_()方法使用这个全局坐标去显示上下文菜单
        # 上下文菜单的操作结果返回给action
        action  = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            qApp.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = MainWindow()
    sys.exit(app.exec_())