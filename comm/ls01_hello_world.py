#!/usr/bin/python3
# coding = utf-8

# 使用try
# 使用命令行参数

import sys
# QtWidgets模块包含了一整套UI元素组件，用于建立符合系统风格的classic界面
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

if __name__ == '__main__':
    # 每个PyQt5应用程序必须创建一个应用程序对象(基于PyQt5.QtWidgets.Qapplication)
    # 这里使用命令行参数 创建一个应用程序对象、使得程序可以从命令行启动
    # argv[0] = 应用程序的名字，argv[1:]就是参数列表了
    app = QApplication(sys.argv)
    try:
        if len(sys.argv) < 2:
            raise ValueError
        else:
            title = " ".join(sys.argv[1:])
    except ValueError:
        title = "hello world!"

    # QWidget部件是所有PyQt5用户界面对象的基类
    w = QWidget()
    # 调整窗口的大小(像素：宽 * 高)
    w.resize(500, 200)
    # 设置窗口在屏幕中的位置(x * y)
    w.move(760, 440)
    # 窗口的标题
    w.setWindowTitle(title)
    # 显示上面设置好的窗口
    w.show()

    # 退出(但不结束主循环main loop)、后面开始接受事件处理
    sys.exit(app.exec_())

    # GUI的事件驱动机制：
    # 没有事件：main loop控制应用程序进入休眠
    # 接到事件：main loop唤醒应用程序
