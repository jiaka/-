# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import title

class Ui_Dialog(object):
    def changeOpacity(self, myshow):
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.8)
        myshow.setGraphicsEffect(op)
        myshow.setAutoFillBackground(True)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(509, 344)
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 491, 311))
        self.stackedWidget.setStyleSheet("border-radius:10px;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.widget = QtWidgets.QWidget(self.page)
        self.widget.setGeometry(QtCore.QRect(0, 110, 491, 201))
        self.widget.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(87, 209, 185, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:10px;")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 491, 201))
        self.label_3.setStyleSheet("border-image: url(:/pc1/20200227172744.gif);\n"
                                   "border-radius:5px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gif1 = QMovie('20200227172744.gif')
        self.label_3.setMovie(self.gif1)
        self.label_3.setScaledContents(True)
        self.gif1.start()
        self.label_3.setStyleSheet("border-radius:5px;")

        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(147, 160, 101, 36))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(" QPushButton {\n"
"      border:none;\n"
"      border-radius:5px;\n"
"    color: rgb(255, 255, 255);\n"
"      background-color: rgb(225, 215, 255);\n"
"  }\n"
"\n"
"  QPushButton:pressed {\n"
"\n"
"    background-color: rgb(115, 255, 120);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    background-color: rgb(182, 255, 155);\n"
"    \n"
"  }\n"
"\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.changeOpacity(self.pushButton_3)

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(278, 160, 101, 36))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(" QPushButton {\n"
"      border:none;\n"
"      border-radius:5px;\n"
"    color: rgb(255, 255, 255);\n"
"      background-color: rgb(225, 215, 255);\n"
"  }\n"
"\n"
"  QPushButton:pressed {\n"
"\n"
"    background-color: rgb(115, 255, 120);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    background-color: rgb(182, 255, 155);\n"
"    \n"
"  }\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.changeOpacity(self.pushButton)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(165, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(97, 97, 97);\n"
"border-radius:5px;")
        self.label_5.setObjectName("label_5")
        self.changeOpacity(self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(137, 115, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    border:none;\n"
"    border-radius:5px;\n"
"    background-color: rgb(240, 255, 254);\n"
"    \n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.changeOpacity(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(137, 68, 251, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    color: rgb(154, 255, 147);\n"
"    border:none;\n"
"    border-radius:5px;\n"
"    background-color: rgb(240, 255, 254);\n"
"    padding:2px 4px\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.changeOpacity(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(84, 115, 41, 41))
        self.label_2.setStyleSheet("border-image: url(:/pc1/1211536.png);\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(175, 226, 219, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:10px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.changeOpacity(self.label_2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(84, 68, 41, 41))
        self.label.setStyleSheet("border-image: url(:/pc1/1211510.png);\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(175, 226, 219, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.changeOpacity(self.label)
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 491, 111))
        self.label_4.setStyleSheet("border-image: url(:/pc1/71ac313729d219d39c64405e0049dc1e.gif);\n"
"border-radius:10px;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gif = QMovie('71ac313729d219d39c64405e0049dc1e.gif')
        self.label_4.setMovie(self.gif)
        self.label_4.setScaledContents(True)
        self.gif.start()
        self.pushButton_6 = QtWidgets.QPushButton(self.page)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 10, 21, 21))
        self.pushButton_6.setStyleSheet("QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.page)
        self.pushButton_7.setGeometry(QtCore.QRect(420, 10, 21, 21))
        self.pushButton_7.setStyleSheet("QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.widget_2 = QtWidgets.QWidget(self.page_2)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 491, 311))
        self.widget_2.setStyleSheet("background-image: url(:/pc1/123.jpg);")
        self.widget_2.setObjectName("widget_2")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(110, 10, 61, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("方正舒体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_6.setFont(font)
        self.label_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("color: rgb(115, 115, 115);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(110, 60, 61, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("方正舒体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_7.setFont(font)
        self.label_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(110, 210, 61, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("方正舒体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_8.setFont(font)
        self.label_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(110, 160, 61, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("方正舒体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_9.setFont(font)
        self.label_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 60, 231, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("color: rgb(115, 115, 115);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 210, 231, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("color: rgb(115, 115, 115);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 160, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("color: rgb(115, 115, 115);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 260, 111, 41))
        font = QtGui.QFont()
        font.setFamily("方正舒体")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 20, 31, 31))
        self.pushButton_4.setStyleSheet("border-image: url(:/pc1/1157313.gif);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(180, 110, 231, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("color: rgb(115, 115, 115);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(110, 110, 61, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("方正舒体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_10.setFont(font)
        self.label_10.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(False)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        self.label_11.setGeometry(QtCore.QRect(420, 20, 19, 19))
        self.label_11.setStyleSheet("border-radius:8px;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        self.label_13.setGeometry(QtCore.QRect(420, 120, 19, 19))
        self.label_13.setStyleSheet("border-radius:8px;")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 160, 61, 41))
        font = QtGui.QFont()
        font.setFamily("方正舒体")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_15 = QtWidgets.QLabel(self.widget_2)
        self.label_15.setGeometry(QtCore.QRect(420, 70, 19, 19))
        self.label_15.setStyleSheet("border-radius:8px;")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.widget_2)
        self.label_17.setGeometry(QtCore.QRect(420, 220, 19, 19))
        self.label_17.setStyleSheet("border-radius:8px;")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.stackedWidget.addWidget(self.page_2)

        # self.changeOpacity(self.pushButton_3)
        # self.changeOpacity(self.pushButton)
        # self.changeOpacity(self.label_5)
        # self.changeOpacity(self.label_2)
        # self.changeOpacity(self.label)
        # self.changeOpacity(self.lineEdit_2)
        # self.changeOpacity(self.lineEdit)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_3.setText(_translate("Dialog", "注册"))
        self.pushButton.setText(_translate("Dialog", "登录"))
        self.label_5.setText(_translate("Dialog", "百   题   斩"))
        self.label_6.setText(_translate("Dialog", "用户名"))
        self.label_7.setText(_translate("Dialog", "邮箱"))
        self.label_8.setText(_translate("Dialog", "密码"))
        self.label_9.setText(_translate("Dialog", "验证码"))
        self.pushButton_2.setText(_translate("Dialog", "注册"))
        self.label_10.setText(_translate("Dialog", "手机号"))
        self.pushButton_5.setText(_translate("Dialog", "发送"))


