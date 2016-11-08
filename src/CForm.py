# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form2.ui'
#
# Created: Sat May 19 20:13:35 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName(_fromUtf8("widget"))
        widget.setEnabled(True)
        widget.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
        widget.setSizePolicy(sizePolicy)
        widget.setMinimumSize(QtCore.QSize(800, 600))
        widget.setMaximumSize(QtCore.QSize(800, 600))
        self.explora = QtGui.QFileDialog(widget)
        self.bsortir = QtGui.QPushButton(widget)
        self.bsortir.setGeometry(QtCore.QRect(700, 540, 75, 23))
        self.bsortir.setObjectName(_fromUtf8("bsortir"))
        self.visor = QtGui.QGraphicsView(widget)
        self.visor.setGeometry(QtCore.QRect(10, 10, 780, 420))
        self.visor.setSizePolicy(sizePolicy)
        self.visor.setObjectName(_fromUtf8("graphicsView"))
        self.escena = QtGui.QGraphicsScene(widget)
        self.visor.setScene(self.escena)
        self.visor_colors = QtGui.QGraphicsView(widget)
        self.visor_colors.setGeometry(QtCore.QRect(10, 440, 780, 75))
        self.visor_colors.setObjectName(_fromUtf8("graphicsView_2"))
        self.escena_colors = QtGui.QGraphicsScene(widget)
        self.visor_colors.setScene(self.escena_colors)
        self.bbuscar = QtGui.QPushButton(widget)
        self.bbuscar.setGeometry(QtCore.QRect(500, 540, 75, 23))
        self.bbuscar.setObjectName(_fromUtf8("bbuscar"))
        self.TextField = QtGui.QLineEdit(widget)
        self.TextField.setGeometry(QtCore.QRect(200, 540, 111, 20))
        self.TextField.setObjectName(_fromUtf8("TextField"))
        self.label = QtGui.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(150, 540, 51, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.baplicar = QtGui.QPushButton(widget)
        self.baplicar.setGeometry(QtCore.QRect(600, 540, 75, 23))
        self.baplicar.setObjectName(_fromUtf8("baplicar"))

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        widget.setWindowTitle(QtGui.QApplication.translate("widget", "Practica 2 IA", None, QtGui.QApplication.UnicodeUTF8))
        self.bsortir.setText(QtGui.QApplication.translate("widget", "Sortir", None, QtGui.QApplication.UnicodeUTF8))
        self.bbuscar.setText(QtGui.QApplication.translate("widget", "Navegar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("widget", "Valor de k:", None, QtGui.QApplication.UnicodeUTF8))
        self.baplicar.setText(QtGui.QApplication.translate("widget", "Aplicar", None, QtGui.QApplication.UnicodeUTF8))

