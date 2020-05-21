# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(687, 472)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(14, 10, 663, 446))
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setStyleSheet(" QWidget#stackedWidget{\n"
"        color:#232C51;\n"
"        background-color: rgb(170, 170, 127);\n"
"        border-top:1px solid darkGray;\n"
"        border-bottom:1px solid darkGray;\n"
"        border-right:1px solid darkGray;\n"
"        border-top-right-radius:10px;\n"
"        border-bottom-right-radius:10px;\n"
"        border-top-left-radius:10px;\n"
"        border-bottom-left-radius:10px;\n"
"    }")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.textBrowser = QtWidgets.QTextBrowser(self.page)
        self.textBrowser.setGeometry(QtCore.QRect(140, 2, 521, 331))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"color: rgb(255, 255, 255);\n"
"        border-top:1px solid darkGray;\n"
"        border-bottom:1px solid darkGray;\n"
"        border-right:1px solid darkGray;\n"
"        border-top-right-radius:10px;\n"
"        border-bottom-right-radius:10px;\n"
"        border-top-left-radius:10px;\n"
"        border-bottom-left-radius:10px;\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_19 = QtWidgets.QPushButton(self.page)
        self.pushButton_19.setGeometry(QtCore.QRect(150, 294, 71, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet(" QPushButton {\n"
"      border:none;\n"
"      border-radius:5px;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"      \n"
"    background-color: rgb(0, 170, 127);\n"
"  }\n"
"\n"
"  QPushButton:pressed {\n"
"font: 9pt \"黑体\";\n"
"    background-color: rgb(115, 255, 120);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(170, 170, 127);\n"
"  }\n"
"\n"
"")
        self.pushButton_19.setObjectName("pushButton_19")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.page)
        self.stackedWidget_2.setGeometry(QtCore.QRect(140, 340, 521, 101))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.stackedWidget_2.setFont(font)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.page_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 60, 521, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(196, 37))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(" QPushButton {\n"
"      border:none;\n"
"      border-radius:5px;\n"
"    color: rgb(255, 255, 255);\n"
"      \n"
"    background-color: rgb(0, 170, 127);\n"
"  }\n"
"\n"
"  QPushButton:pressed {\n"
"font: 9pt \"黑体\";\n"
"    background-color: rgb(115, 255, 120);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"  }\n"
"\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(196, 37))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(" QPushButton {\n"
"      border:none;\n"
"      border-radius:5px;\n"
"    color: rgb(255, 255, 255);\n"
"      \n"
"    background-color: rgb(0, 170, 127);\n"
"  }\n"
"\n"
"  QPushButton:pressed {\n"
"font: 9pt \"黑体\";\n"
"    background-color: rgb(115, 255, 120);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"  }\n"
"\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.page_3)
        self.stackedWidget_3.setGeometry(QtCore.QRect(0, 0, 521, 61))
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page_6)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 531, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_A = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_A.setMinimumSize(QtCore.QSize(55, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_A.setFont(font)
        self.pushButton_A.setStyleSheet(" QPushButton {\n"
"      border:none;\n"
"      border-radius:5px;\n"
"    color: rgb(255, 255, 255);\n"
"      \n"
"    background-color: rgb(0, 170, 127);\n"
"  }\n"
"\n"
"  QPushButton:pressed {\n"
"font: 13pt \"黑体\";\n"
"    background-color: rgb(115, 255, 120);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"  }\n"
"\n"
"")
        self.pushButton_A.setObjectName("pushButton_A")
        self.horizontalLayout.addWidget(self.pushButton_A)
        self.pushButton_B = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_B.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_B.setFont(font)
        self.pushButton_B.setStyleSheet(" QPushButton {\n"
"      border:none;\n"
"      border-radius:5px;\n"
"    color: rgb(255, 255, 255);\n"
"      \n"
"    background-color: rgb(0, 170, 127);\n"
"  }\n"
"\n"
"  QPushButton:pressed {\n"
"font: 13pt \"黑体\";\n"
"    background-color: rgb(115, 255, 120);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"  }\n"
"\n"
"")
        self.pushButton_B.setObjectName("pushButton_B")
        self.horizontalLayout.addWidget(self.pushButton_B)
        self.pushButton_C = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_C.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_C.setFont(font)
        self.pushButton_C.setStyleSheet(" QPushButton {\n"
"      border:none;\n"
"      border-radius:5px;\n"
"    color: rgb(255, 255, 255);\n"
"      \n"
"    background-color: rgb(0, 170, 127);\n"
"  }\n"
"\n"
"  QPushButton:pressed {\n"
"font: 13pt \"黑体\";\n"
"    background-color: rgb(115, 255, 120);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"  }\n"
"\n"
"")
        self.pushButton_C.setObjectName("pushButton_C")
        self.horizontalLayout.addWidget(self.pushButton_C)
        self.pushButton_D = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_D.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_D.setFont(font)
        self.pushButton_D.setStyleSheet(" QPushButton {\n"
"      border:none;\n"
"      border-radius:5px;\n"
"    color: rgb(255, 255, 255);\n"
"      \n"
"    background-color: rgb(0, 170, 127);\n"
"  }\n"
"\n"
"  QPushButton:pressed {\n"
"font: 13pt \"黑体\";\n"
"    background-color: rgb(115, 255, 120);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"  }\n"
"\n"
"")
        self.pushButton_D.setObjectName("pushButton_D")
        self.horizontalLayout.addWidget(self.pushButton_D)
        self.stackedWidget_3.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.page_7)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 521, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("      border:none;\n"
"      border-radius:5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("      border:none;\n"
"      border-radius:5px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("      border:none;\n"
"      border-radius:5px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(121, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("      border:none;\n"
"      border-radius:5px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_3.addWidget(self.lineEdit_4)
        self.stackedWidget_3.addWidget(self.page_7)
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 60, 196, 37))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(" QPushButton {\n"
"      border:none;\n"
"      border-radius:5px;\n"
"    color: rgb(255, 255, 255);\n"
"      \n"
"    background-color: rgb(0, 170, 127);\n"
"  }\n"
"\n"
"  QPushButton:pressed {\n"
"font: 9pt \"黑体\";\n"
"    background-color: rgb(115, 255, 120);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"  }\n"
"\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_9.setGeometry(QtCore.QRect(320, 60, 196, 37))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(" QPushButton {\n"
"      border:none;\n"
"      border-radius:5px;\n"
"    color: rgb(255, 255, 255);\n"
"      \n"
"    background-color: rgb(0, 170, 127);\n"
"  }\n"
"\n"
"  QPushButton:pressed {\n"
"font: 9pt \"黑体\";\n"
"    background-color: rgb(115, 255, 120);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"  }\n"
"\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.pushButton_10 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_10.setGeometry(QtCore.QRect(310, 60, 196, 37))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet(" QPushButton {\n"
"      border:none;\n"
"      border-radius:5px;\n"
"    color: rgb(255, 255, 255);\n"
"      \n"
"    background-color: rgb(0, 170, 127);\n"
"  }\n"
"\n"
"  QPushButton:pressed {\n"
"font: 9pt \"黑体\";\n"
"    background-color: rgb(115, 255, 120);\n"
"  }\n"
"\n"
"  QPushButton:hover {\n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"  }\n"
"\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.label = QtWidgets.QLabel(self.page_5)
        self.label.setGeometry(QtCore.QRect(0, 0, 311, 91))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.stackedWidget_2.addWidget(self.page_5)
        self.gridLayoutWidget = QtWidgets.QWidget(self.page)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 131, 441))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_more = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_more.setFont(font)
        self.pushButton_more.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_more.setStyleSheet("QPushButton{border:none;color:white;}\n"
"\n"
"    QPushButton:hover{border-left:4px solid red;font-weight:700;font-size:16px;\n"
"        font-family: \"黑体\";}")
        self.pushButton_more.setObjectName("pushButton_more")
        self.gridLayout.addWidget(self.pushButton_more, 9, 0, 1, 5)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{border:none;color:white;}\n"
"\n"
"    QPushButton:hover{border-left:4px solid red;font-weight:700;font-size:16px;\n"
"        font-family: \"黑体\";}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 8, 0, 1, 5)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_15.setEnabled(True)
        self.pushButton_15.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("QPushButton{border:none;color:white;}\n"
"\n"
"    QPushButton:hover{border-left:4px solid red;font-weight:700;font-size:18px;\n"
"        font-family: \"黑体\";}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 0, 0, 1, 5)
        self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_16.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("QPushButton{border:none;color:white;}\n"
"\n"
"    QPushButton:hover{border-left:4px solid red;font-weight:700;font-size:18px;\n"
"        font-family: \"黑体\";}")
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 1, 0, 1, 5)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{border:none;color:white;}\n"
"\n"
"    QPushButton:hover{border-left:4px solid red;font-weight:700;font-size:16px;\n"
"        font-family: \"黑体\";}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 4, 0, 1, 5)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{border:none;color:white;}\n"
"\n"
"    QPushButton:hover{border-left:4px solid red;font-weight:700;font-size:16px;\n"
"        font-family: \"黑体\";}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 7, 0, 1, 5)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{border:none;color:white;}\n"
"\n"
"    QPushButton:hover{border-left:4px solid red;font-weight:700;font-size:16px;\n"
"        font-family: \"黑体\";}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 5, 0, 1, 5)
        spacerItem = QtWidgets.QSpacerItem(42, 25, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 5)
        self.pushButton_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setMinimumSize(QtCore.QSize(21, 21))
        self.pushButton_17.setMaximumSize(QtCore.QSize(21, 21))
        self.pushButton_17.setStyleSheet("QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}")
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 2, 1, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setMinimumSize(QtCore.QSize(21, 21))
        self.pushButton_18.setMaximumSize(QtCore.QSize(21, 22))
        self.pushButton_18.setStyleSheet("QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}")
        self.pushButton_18.setText("")
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 2, 3, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.page)
        self.progressBar.setGeometry(QtCore.QRect(220, 300, 441, 21))
        self.progressBar.setStyleSheet("QProgressBar{border:None;\n"
"    height:30;                         \n"
"    font: 10pt \"黑体\";\n"
"    background-color:rgb(0, 170, 127);\n"
"                              text-align:right;\n"
"                              color:rgb(255,255,255);\n"
"                              border-radius:0px;}\n"
"\n"
"                              QProgressBar::chunk{\n"
"                              border-radius:5px;  \n"
"                              border:1px solid rgb(0, 170, 127);\n"
"                              background-color:white;\n"
"                              width:8px;margin:0.5px;}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.page_2)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 671, 445))
        self.treeWidget.setStyleSheet("QTreeView {\n"
"    outline: 0px;\n"
"    background: rgb(47, 64, 78);\n"
"}\n"
"QTreeView::item {\n"
"    min-height: 12px;\n"
"}\n"
"QTreeView::item:hover {\n"
"    background: rgb(41, 56, 71);\n"
"}\n"
"QTreeView::item:selected {\n"
"    background: rgb(41, 56, 71);\n"
"}\n"
"\n"
"QTreeView::item:selected:active{\n"
"    background: rgb(41, 56, 71);\n"
"}\n"
"QTreeView::item:selected:!active{\n"
"    background: rgb(41, 56, 71);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children {\n"
"    background: rgb(41, 56, 71);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    background: green;\n"
"}\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    background: rgb(47, 64, 78);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed {\n"
"    background: rgb(47, 64, 78);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:has-siblings {\n"
"    background: rgb(41, 56, 71);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings {\n"
"    background: rgb(41, 56, 71);\n"
"}\n"
"QTreeView:branch:hover {\n"
"    background: rgb(41, 56, 71);\n"
"}\n"
"QTreeView:branch:selected {\n"
"    background: rgb(41, 56, 71);\n"
"}\n"
"")
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_19.setText(_translate("Form", "提示"))
        self.pushButton_3.setText(_translate("Form", "上一题"))
        self.pushButton_4.setText(_translate("Form", "下一题"))
        self.pushButton_A.setText(_translate("Form", "A"))
        self.pushButton_B.setText(_translate("Form", "B"))
        self.pushButton_C.setText(_translate("Form", "C"))
        self.pushButton_D.setText(_translate("Form", "D"))
        self.pushButton_8.setText(_translate("Form", "上一题"))
        self.pushButton_9.setText(_translate("Form", "下一题"))
        self.pushButton_10.setText(_translate("Form", "再来一次"))
        self.pushButton_more.setText(_translate("Form", "的"))
        self.pushButton_7.setText(_translate("Form", "资助作者"))
        self.pushButton_15.setText(_translate("Form", "个人中心"))
        self.pushButton_6.setText(_translate("Form", "导入题库"))
        self.pushButton.setText(_translate("Form", "填空题"))
        self.pushButton_5.setText(_translate("Form", "帮助"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "新建列"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "新建项目"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Form", "新建项目"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("Form", "新建子项目"))
        self.treeWidget.topLevelItem(1).child(0).child(0).setText(0, _translate("Form", "新建子项目"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("Form", "新建项目"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("Form", "新建子项目"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("Form", "新建项目"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

