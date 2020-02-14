# 参考：E:\Git\PyQt_Site\QTableWidget\TableWidget.py

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QLabel, QDateTimeEdit, QComboBox, QSpinBox, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QDateTime, QTimer

# 使用枚举
from enum import Enum, unique
# 这个装饰器可以保证下面这个Enum中不会有value重复的成员
@unique
class tColumn(Enum):
    Name     = 0
    Data     = 1
    DataType = 2
    DataLen  = 3
    Endian   = 4

class ProtocolEditTable(QTableWidget):
    def __init__(self, parent = None):
        super(ProtocolEditTable, self).__init__(parent)
        self.setWindowTitle("Protocol Editor")
        self.setWindowIcon(QIcon("image/Logo.png"))
        self.resize(920, 240)
        self.setColumnCount(5)
        self.setRowCount(1)
        self.setColumnWidth(tColumn.DataType.value, 70)
        self.setColumnWidth(tColumn.DataLen.value, 60)
        self.setColumnWidth(tColumn.Endian.value, 60)
        # 表头
        self.setHorizontalHeaderLabels(["字段名", "数据", "格式", "字节数", "大小端"])
        self.setVerticalHeaderLabels(["0", "1"])
        self.tDataCount = 0
        self.AddRow()

    def AddRow(self):
        rowNum = self.rowCount()
        self.setRowCount(rowNum + 1)
        # 初始化这一行
        self.removeCellWidget(rowNum - 1, 0)
        self.setItem(rowNum - 1, tColumn.Name.value, QTableWidgetItem("帧头"))
        self.setItem(rowNum - 1, tColumn.Data.value, QTableWidgetItem("68"))
        tDataType = QComboBox()
        tDataType.addItems(["Hex", "Dec", "Float", "Double", "String", "BCD", "Fill"])
        self.setCellWidget(rowNum - 1, tColumn.DataType.value, tDataType)
        tDataLength = QSpinBox()
        tDataLength.setRange(0, 1000)
        tDataLength.setValue(1) #设置最开始显示的数字
        tDataLength.setDisplayIntegerBase(10)#这个是显示数字的进制，默认是十进制。
        tDataLength.setSingleStep(1)
        self.setCellWidget(rowNum - 1, tColumn.DataLen.value, tDataLength)
        tDataEndian = QComboBox()
        tDataEndian.addItems(["小端", "大端"])
        self.setCellWidget(rowNum - 1, tColumn.Endian.value, tDataEndian)
        # 下一行
        tButton_AddRow = QPushButton("+", self)
        tButton_AddRow.clicked.connect(self.AddRow)
        self.setCellWidget(rowNum, 0, tButton_AddRow)
        self.tDataCount += tDataLength.value() # 总的字节数
        self.setItem(rowNum, 3, QTableWidgetItem(str(self.tDataCount)))

    def Other(self):
        # 格式 == String: tDataLength 不可修改、程序自动计算 tDataLength
        # Fill格式：填充数据、数据不断重复 Data 字段的内容，总长度不超过 tDataLength
        #           填充的多个数据可用分隔符(空格、逗号、小数点)分开即可、这样可以写115.236之类的IP
        # tDatalength 有变化：tDataCount 自动更新
        # 右键：
        #      删除当前行
        #      在上方插入一行
        #      在下方插入一行
        pass

if __name__ == "__main__":
    App = QApplication(sys.argv)
    ProtocolEdit = ProtocolEditTable()
    ProtocolEdit.show()
    App.exit(App.exec_())