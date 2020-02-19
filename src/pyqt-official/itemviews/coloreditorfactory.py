#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited
## Copyright (C) 2010 Hans-Peter Jansen <hpj@urpla.net>.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


from PyQt5.QtCore import pyqtProperty, Qt, QVariant
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QApplication, QComboBox, QGridLayout,
        QItemEditorCreatorBase, QItemEditorFactory, QTableWidget,
        QTableWidgetItem, QWidget)


class ColorListEditor(QComboBox):
    def __init__(self, widget=None):
        super(ColorListEditor, self).__init__(widget)

        self.populateList()

    def getColor(self):
        color = self.itemData(self.currentIndex(), Qt.DecorationRole)
        return color

    def setColor(self, color):
        self.setCurrentIndex(self.findData(color, Qt.DecorationRole))

    # 添加属性(属性的数据类型: QColor)
    color = pyqtProperty(QColor, getColor, setColor, user=True)

    # 颜色列表
    def populateList(self):
        # colorNames: Returns a QStringList containing the color names Qt knows about
        for i, colorName in enumerate(QColor.colorNames()):
            color = QColor(colorName)
            self.insertItem(i, colorName)
            # Qt::DecorationRole: The data to be rendered as a decoration in the form of an icon. (QColor, QIcon or QPixmap)
            self.setItemData(i, color, Qt.DecorationRole)


class ColorListItemEditorCreator(QItemEditorCreatorBase):
    def createWidget(self, parent):
        return ColorListEditor(parent)


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # The class provides widgets for editing item data in views and delegates
        factory = QItemEditorFactory()
        # Registers an item editor creator specified by creator for the given userType of data
        factory.registerEditor(QVariant.Color, ColorListItemEditorCreator())
        # Sets the default item editor factory to the given factory. 
        # Both new and existing delegates will use the new factory
        QItemEditorFactory.setDefaultFactory(factory)

        self.createGUI()

    def createGUI(self):
        tableData = [
            ("Alice", QColor('valiceblue')),
            ("Neptun", QColor('aquamarine')),
            ("Ferdinand", QColor('springgreen'))
        ]

        table = QTableWidget(3, 2)
        table.setHorizontalHeaderLabels(["Name", "Hair Color"])
        table.verticalHeader().setVisible(False)
        table.resize(150, 50)

        for i, (name, color) in enumerate(tableData):
            # Constructs a table item with the given text
            nameItem  = QTableWidgetItem(name)
            colorItem = QTableWidgetItem()
            colorItem.setData(Qt.DisplayRole, color)  # 显示角色：颜色
            table.setItem(i, 0, nameItem)
            table.setItem(i, 1, colorItem)
        # 根据内容自动调整某列的列宽
        table.resizeColumnToContents(0)
        # 将最后一列填充满表格
        table.horizontalHeader().setStretchLastSection(True)

        layout = QGridLayout()
        # Adds the given widget to the cell grid at row, column. 
        # The top-left position is (0, 0) by default.
        layout.addWidget(table, 0, 0)
        # QWidget.setLayout: Sets the layout manager for this widget to layout.
        self.setLayout(layout)
        self.setWindowTitle("Color Editor Factory")


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
