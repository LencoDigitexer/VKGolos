# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 364)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.list = QtWidgets.QComboBox(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(10, 280, 561, 41))
        self.list.setObjectName("list")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 110, 321, 128))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.peer_id = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.peer_id.setObjectName("peer_id")
        self.gridLayout.addWidget(self.peer_id, 0, 0, 1, 1)
        self.person_id = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.person_id.setObjectName("person_id")
        self.gridLayout.addWidget(self.person_id, 0, 1, 1, 1)
        self.request_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.request_2.setObjectName("request_2")
        self.gridLayout.addWidget(self.request_2, 1, 0, 1, 1)
        self.request = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.request.setObjectName("request")
        self.gridLayout.addWidget(self.request, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 321, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.login.setText("")
        self.login.setObjectName("login")
        self.horizontalLayout.addWidget(self.login)
        self.password = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setReadOnly(False)
        self.password.setObjectName("password")
        self.horizontalLayout.addWidget(self.password)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.Join = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Join.setObjectName("Join")
        self.verticalLayout_2.addWidget(self.Join)
        self.console = QtWidgets.QListWidget(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(340, 10, 231, 231))
        self.console.setObjectName("console")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.peer_id.setText(_translate("MainWindow", "ID беседы"))
        self.person_id.setText(_translate("MainWindow", "ID человека"))
        self.request_2.setText(_translate("MainWindow", "Отправить в беседу"))
        self.request.setText(_translate("MainWindow", "Отправить ЛС"))
        self.Join.setText(_translate("MainWindow", "Войти"))


