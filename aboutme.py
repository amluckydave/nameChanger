# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutme.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_about(object):
    def setupUi(self, about):
        about.setObjectName("about")
        about.resize(300, 100)
        self.pushButton = QtWidgets.QPushButton(about)
        self.pushButton.setGeometry(QtCore.QRect(220, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(about)
        self.label.setGeometry(QtCore.QRect(60, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.github = QtWidgets.QLabel(about)
        self.github.setGeometry(QtCore.QRect(80, 50, 141, 20))
        self.github.setAlignment(QtCore.Qt.AlignCenter)
        self.github.setObjectName("github")

        self.retranslateUi(about)
        QtCore.QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        _translate = QtCore.QCoreApplication.translate
        about.setWindowTitle(_translate("about", "Dialog"))
        self.pushButton.setText(_translate("about", "OK"))
        self.label.setText(_translate("about", "NameChanger by EliotXu"))
        self.github.setText(_translate("about", "GitHub"))