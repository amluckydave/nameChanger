# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'invoice_changer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 190)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 50, 281, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.openPushButton.setObjectName("openPushButton")
        self.horizontalLayout.addWidget(self.openPushButton)
        self.addrLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.addrLineEdit.setFont(font)
        self.addrLineEdit.setText("")
        self.addrLineEdit.setFrame(False)
        self.addrLineEdit.setObjectName("addrLineEdit")
        self.horizontalLayout.addWidget(self.addrLineEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 70, 281, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.changePushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.changePushButton.setObjectName("changePushButton")
        self.horizontalLayout_2.addWidget(self.changePushButton)
        self.progressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 120, 281, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.reminderLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.reminderLineEdit.setGeometry(QtCore.QRect(10, 140, 281, 22))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.reminderLineEdit.setFont(font)
        self.reminderLineEdit.setText("")
        self.reminderLineEdit.setFrame(False)
        self.reminderLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.reminderLineEdit.setObjectName("reminderLineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuRoolback = QtWidgets.QMenu(self.menuBar)
        self.menuRoolback.setObjectName("menuRoolback")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSeparator = QtWidgets.QMenu(self.menuBar)
        self.menuSeparator.setObjectName("menuSeparator")
        MainWindow.setMenuBar(self.menuBar)
        self.actionConfirm = QtWidgets.QAction(MainWindow)
        self.actionConfirm.setObjectName("actionConfirm")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.plusAction = QtWidgets.QAction(MainWindow)
        self.plusAction.setObjectName("plusAction")
        self.minusAction = QtWidgets.QAction(MainWindow)
        self.minusAction.setObjectName("minusAction")
        self.menuRoolback.addAction(self.actionConfirm)
        self.menuHelp.addAction(self.actionAbout)
        self.menuSeparator.addAction(self.plusAction)
        self.menuSeparator.addAction(self.minusAction)
        self.menuBar.addAction(self.menuSeparator.menuAction())
        self.menuBar.addAction(self.menuRoolback.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openPushButton.setText(_translate("MainWindow", "Open"))
        self.addrLineEdit.setPlaceholderText(_translate("MainWindow", "Select a folder to change nane"))
        self.changePushButton.setText(_translate("MainWindow", "Change"))
        self.reminderLineEdit.setPlaceholderText(_translate("MainWindow", "Waiting to change..."))
        self.menuRoolback.setTitle(_translate("MainWindow", "Rollback"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuSeparator.setTitle(_translate("MainWindow", "Separator"))
        self.actionConfirm.setText(_translate("MainWindow", "Confirm?"))
        self.actionAbout.setText(_translate("MainWindow", "About NameChanger"))
        self.plusAction.setText(_translate("MainWindow", "+"))
        self.minusAction.setText(_translate("MainWindow", "-"))
