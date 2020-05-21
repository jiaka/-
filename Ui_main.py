# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\zouyo\Desktop\word\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(730, 370)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 731, 281))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 340, 101, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 340, 93, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 340, 93, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(540, 340, 93, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 340, 93, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(340, 340, 93, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(-10, 340, 131, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(90, 290, 121, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 290, 121, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 290, 121, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(480, 290, 121, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(610, 290, 121, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("Form", "填空题"))
        self.pushButton_2.setText(_translate("Form", "确定"))
        self.pushButton_3.setText(_translate("Form", "上一个"))
        self.pushButton_4.setText(_translate("Form", "下一个"))
        self.pushButton_5.setText(_translate("Form", "帮助"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"right\">答案：</p></body></html>"))
        self.pushButton_6.setText(_translate("Form", "导入题库"))
        self.pushButton_7.setText(_translate("Form", "资助作者"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
