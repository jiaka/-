# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QRegExpValidator, QCursor
import sys, os
from os import remove
import re

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
    print(os.environ['PATH'])
from main2 import Ui_Form
from random import shuffle
from Childwindows import help
from login import Ui_Dialog
import leancloud
import difflib

class Dialog(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.setWindowOpacity(0.8)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setupUi(self)
        self.init()
        # leancloud.init("p59BJ2ir6Ct48x1WVyi9gBNj-gzGzoHsz", "nnxC80N5JtE5tatW5DGQH8TD")

    def init(self):
        self.label_11.setVisible(False)
        self.label_15.setVisible(False)
        self.label_13.setVisible(False)
        self.label_17.setVisible(False)

        self.pushButton_6.setToolTip('关闭')
        self.pushButton_6.clicked.connect(self.close)
        self.pushButton_7.setToolTip('最小化')
        self.pushButton_7.clicked.connect(self.showMinimized)

        # 设置文本允许出现的字符内容
        reg_pnum = QRegExp(r"^1[35678]\d{9}$")
        # 自定义文本验证器
        pValidator = QRegExpValidator(self)
        # 设置属性
        pValidator.setRegExp(reg_pnum)
        self.lineEdit_7.setValidator(pValidator)

        reg_email = QRegExp(r"^[\w][a-zA-Z0-9.]{4,19}@[a-zA-Z0-9]{2,3}.com")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg_email)
        self.lineEdit_4.setValidator(pValidator)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def box(self, e):  # 消息：警告
        QMessageBox.warning(self, "警告", e, QMessageBox.Yes)

    def correct(self, label):
        pass

    def fault(self, label):
        pass

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        self.stackedWidget.setCurrentWidget(self.page_2)

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        self.stackedWidget.setCurrentWidget(self.page)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        user = leancloud.User()
        username1 = self.lineEdit.text()
        passwd = self.lineEdit_2.text()
        try:
            if '@' in username1:
                user.login(email=username1, password=passwd)
            else:
                user.login(username=username1, password=passwd)
            self.close()
        except:
            pass

    @pyqtSlot()
    def on_pushButton_2_clicked(self):

        password = self.lineEdit_3.text()
        username = self.lineEdit_5.text()
        email = self.lineEdit_4.text()
        phonenumber = self.lineEdit_7.text()
        num = self.lineEdit_6.text()

        user = leancloud.User()
        user.set_username(username)
        user.set_password(password)
        user.set_mobile_phone_number(phonenumber)
        user.set_email(email)

        user.sign_up()

    # 发送验证码
    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        phonenumber = self.lineEdit_7.text()
        # leancloud.init("p59BJ2ir6Ct48x1WVyi9gBNj-gzGzoHsz", "nnxC80N5JtE5tatW5DGQH8TD")
        # leancloud.cloudfunc.request_sms_code(phonenumber)

    @pyqtSlot()
    def on_lineEdit_3_editingFinished(self):
        self.label_11.setVisible(True)

        self.label_11.setStyleSheet("border-image: url(:/pc1/0010.jpg);\n"
                                    "border-radius:8px;")

    @pyqtSlot()
    def on_lineEdit_4_editingFinished(self):
        self.label_15.setVisible(True)

        self.label_15.setStyleSheet("border-image: url(:/pc1/0010.jpg);\n"
                                    "border-radius:8px;")

    @pyqtSlot()
    def on_lineEdit_7_editingFinished(self):
        self.label_13.setVisible(True)

        self.label_13.setStyleSheet("border-image: url(:/pc1/0010.jpg);\n"
                                    "border-radius:8px;")

    @pyqtSlot()
    def on_lineEdit_5_editingFinished(self):
        self.label_17.setVisible(True)

        self.label_17.setStyleSheet("border-image: url(:/pc1/0010.jpg);\n"
                                    "border-radius:8px;")


class Form(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Form, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        # 分别存储选择题，填空题，简答题的题目和答案
        self.xuan = {}
        self.tian = {}
        self.jian = {}
        self.tixin = []
        self.ti = {}
        self.result = {}  # 存放回答结果，用来显示答题报告
        self.result_1 = {}  # 存放回答结果，用来记分和回显
        self.soc = {'xuan': 2, 'tian': 2, 'jian': 5}  # 题型的分值
        # 题库文件的文件名
        self.file = "tiku.txt"
        self.num = 0
        # 读取题库文件，默认显示选择题
        self.configure()
        self.get_tiku1()
        self.stackedWidget_3.setCurrentWidget(self.page_6)
        # try:
        #     self.init()
        #     self.UI_tiku()
        # except:
        #     pass
        # 当前题型的标志
        self.now_falg = 0
        # print(self.tian)
        # print(self.tian[self.item_tian[self.num]])

    # 配置一些控件
    def configure(self):
        self.pushButton_18.setToolTip('关闭')
        self.pushButton_18.clicked.connect(self.close)
        self.pushButton_17.setToolTip('最小化')
        self.pushButton_17.clicked.connect(self.showMinimized)
        self.lineEdit.returnPressed.connect(self.line_function)
        self.lineEdit_2.returnPressed.connect(self.line1_function)
        self.lineEdit_3.returnPressed.connect(self.line2_function)
        self.lineEdit_4.returnPressed.connect(self.line3_function)


    def box(self, e):  # 消息：警告
        QMessageBox.warning(self, "警告", e, QMessageBox.Yes)

    def init(self):
        # try:
        #     fp = open("xuan.txt", 'r', encoding='utf-8')
        #     self.xuan = eval(fp.read())
        #     self.len_xuan = len(self.xuan)
        #     self.item_xuan = list(self.xuan.keys())
        #     shuffle(self.item_xuan)
        #     fp1 = open("tian.txt", 'r', encoding='utf-8')
        #     self.tian = eval(fp1.read())
        #     self.len_tian = len(self.tian)
        #     self.item_tian = list(self.tian.keys())
        #     shuffle(self.item_tian)
        #     fp.close()
        #     fp1.close()
        #     os.remove("xuan.txt")
        #     os.remove("tian.txt")
        # except:
        try:
            self.get_tiku()
            fp = open("xuan.txt", 'r', encoding='utf-8')
            self.xuan = eval(fp.read())
            self.len_xuan = len(self.xuan)
            self.item_xuan = list(self.xuan.keys())
            shuffle(self.item_xuan)
            fp1 = open("tian.txt", 'r', encoding='utf-8')
            self.tian = eval(fp1.read())
            self.len_tian = len(self.tian)
            # 题目列表
            self.item_tian = list(self.tian.keys())
            shuffle(self.item_tian)
            fp.close()
            fp1.close()
            remove("xuan.txt")
            remove("tian.txt")
        except:
            self.box("没有题库文件，请点击导入题库。如果您是第一次使用，请将题库文件放在软件的同级目录并命名为tiku.txt.\n您可以查看帮助来建立您的题库文件。")

    def UI_tiku(self, x='', y=''):
        try:
            if self.now_falg == 2:
                self.textBrowser.setText(x[:-2] + '\n')
                for i in y:
                    self.textBrowser.append(i)
            else:
                if self.num < self.len_xuan:
                    self.textBrowser.setText(self.item_xuan[self.num])
                    self.textBrowser.append(self.xuan[self.item_xuan[self.num]][1][:-1])
                    self.textBrowser.append(self.xuan[self.item_xuan[self.num]][2][:-1])
                    self.textBrowser.append(self.xuan[self.item_xuan[self.num]][3][:-1])
                    self.textBrowser.append(self.xuan[self.item_xuan[self.num]][4][:-1])
                else:
                    self.textBrowser.setText("选择题答题完毕")
        except:
            pass

    def get_tiku1(self):
        temp = ''
        with open(self.file, 'r', encoding='utf-8') as fp:
            all = fp.readlines()
            flag = -1
            for x in all:
                if x[0] in ['#', '$', '%', '&']:
                    if x[0] == '#':  # 选择
                        flag = 0
                    elif x[0] == '$':  # 填空
                        flag = 1
                    elif x[0] == '%':  # 简答
                        flag = 2
                    elif x[0] == '&':   # 多选
                        flag = 3
                    else:
                        flag = -1
                    continue
                if flag == 0:
                    if x[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        self.ti[x] = []
                        self.tixin.append(0)
                        temp = x
                    else:
                        self.ti[temp].append(x)
                elif flag == 1:
                    if x[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and len(x) > 7:
                        self.ti[x] = []
                        self.tixin.append(1)
                        temp = x
                    else:
                        self.ti[temp].append(x)
                elif flag == 2:
                    if x[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        self.ti[x] = [[x], []]
                        self.tixin.append(2)
                        temp = x
                        temp1 = 0
                    elif x[0] == "答":
                        temp1 = 1
                        self.ti[temp][temp1].append(x)
                    else:
                        self.ti[temp][temp1].append(x)
                else:
                    pass
            print(self.ti)
            print(self.tixin)
        self.len_ti = len(self.ti.keys())
        self.progressBar.setMaximum(self.len_ti)
        self.progressBar.setMinimum(0)
        self.progressBar.reset()
        self.key = list(self.ti.keys())
        self.value = list(self.ti.values())


    def get_tiku2(self):
        with open(self.file, "r", encoding='utf-8') as fp:
            txt = fp.readlines()
            y = ''
            for x in txt:
                if x[0] in ['t', 'x', 'j', 'd']:
                    y = x
                    self.ti[x] = []
                else:
                    if y[0] == 't':
                        self.ti[y].append(x[1:-1])
                    else:
                        self.ti[y].append(x)

        self.len_ti = len(self.ti.keys())
        self.progressBar.setMaximum(self.len_ti)
        self.progressBar.setMinimum(0)
        self.progressBar.reset()
        self.key = list(self.ti.keys())
        self.value = list(self.ti.values())



    # 可以传一个参
    def total(self):
        if self.now_falg == 2 and self.num < self.len_ti:
            y = self.tixin[self.num]
            if y == 0:
                self.stackedWidget_2.setCurrentWidget(self.page_3)
                self.stackedWidget_3.setCurrentWidget(self.page_6)
                self.UI_tiku(self.key[self.num], self.value[self.num])
            elif y == 1:
                self.stackedWidget_2.setCurrentWidget(self.page_3)
                self.stackedWidget_3.setCurrentWidget(self.page_7)
                self.textBrowser.setText(self.key[self.num])
                self.clearline()
            elif y == 2:
                self.stackedWidget_2.setCurrentWidget(self.page_8)
                self.clearedit()
            else:
                return -1
        else:
            self.num = 0
            self.stackedWidget_2.setCurrentWidget(self.page_5)
            self.show_result()
        self.progressBar.setValue(self.num)
        self.progressBar.setFormat('{}/{}'.format(self.num, self.len_ti))


    def get_tiku(self):
        try:
            with open(self.file, "r", encoding='utf-8') as fp:
                txt = fp.readlines()
                for x in txt:
                    if x[0] == 't':
                        self.tian[x[1:]] = []
                        y = x[1:]
                    elif x[0] == 'x':
                        self.xuan[x[1:-2]] = [x[-2:-1]]
                        y = x[1:-2]
                    elif x[0] == 'j':
                        self.jian[x] = []
                        y = x
                    elif x[0] == '?':
                        self.tian[y].append(x[1:-1])
                    elif x[0] == '#':
                        self.jian[y].append(x)
                    elif x[0] in ["A", "B", "C", "D"]:
                        self.xuan[y].append(x)
                    else:
                        continue
            with open("xuan.txt", "w", encoding='utf-8') as fp:
                fp.write(str(self.xuan))
            with open("tian.txt", "w", encoding='utf-8') as fp:
                fp.write(str(self.tian))
        except:
            self.box("没有题库文件，请点击导入题库。如果您是第一次使用，请将题库文件放在软件的同级目录并命名为tiku.txt.\n\n\n您可以查看帮助来建立您的题库文件。")

    @pyqtSlot()
    def on_pushButton123333_clicked(self):
        num = 0

    @pyqtSlot()
    def on_pushButton_clicked(self):
        # # try:
        # if self.pushButton.text() == "选择题":
        #     self.pushButton.setText("填空题")
        #     self.stackedWidget_3.setCurrentWidget(self.page_6)           # 跳转到四个按钮
        #     # self.line.releaseKeyboard()
        #     # self.line1.setEnabled(False)
        #     # self.line1.setVisible(False)
        #     shuffle(self.item_xuan)
        #     self.num = 0
        #     self.UI_tiku()
        #     self.now_falg = 0
        # elif self.pushButton.text() == "填空题":
        #     self.pushButton.setText("测试模式")
        #     self.stackedWidget_3.setCurrentWidget(self.page_7)           # 跳转到四个输入框
        #     shuffle(self.item_tian)
        #     self.textBrowser.setText(self.item_tian[0])
        #     self.now_falg = 1
        #     self.num = 0
        # else:
        #     self.pushButton.setText("选择题")
        self.now_falg = 2
        self.num = 0
        self.get_tiku1()
        self.total()

    # except:
    #     self.box("运行出错，请联系开发者。出错编号：001")

    def xuan_panduan(self, y):
        if self.now_falg == 2:
            x = self.key[self.num][-2]

            if self.num in self.result:
                del self.result[self.num]
            if self.num in self.result_1:
                del self.result_1[self.num]
            if x == y:
                self.result[self.num] = ['yes', self.key[self.num][:-1]] + [i[:-1] for i in self.value[self.num]] + [
                    "<font color=\"#55ff7f\">{}</font>".format('回答正确'),'\n\n']
                self.result_1[self.num] = [y, self.soc['xuan'],self.soc['xuan']]
            else:
                self.result[self.num] = ['no', self.key[self.num][:-1]] + [i[:-1] for i in self.value[self.num]] + [
                    "<font color=\"#FF0000\">{}</font> ".format("回答错误，您错选了 {}".format(y)), '\n\n']
                self.result_1[self.num] = [y, 0,self.soc['xuan']]

            self.num += 1
            self.total()
        else:
            x = self.xuan[self.item_xuan[self.num]][0]
            len = self.len_xuan

            if x == y:
                self.num += 1
                if self.num >= len:
                    self.num = 0
                self.UI_tiku()
            else:
                self.textBrowser.append('x')

    def jiandapanduan(self):
        text = self.textEdit.toPlainText()
        rat = difflib.SequenceMatcher(None, text, ''.join(self.value[self.num][1])).quick_ratio()
        if rat > 0.95:
            rat = 1
        if self.num in self.result:
            del self.result[self.num]
        if self.num in self.result_1:
            del self.result_1[self.num]
        self.result[self.num] = ['yes'] + [i[:-1] for i in self.value[self.num][0]] + ["标准答案："] + [i[:-1] for i in self.value[self.num][1]] + [
                    "<font color=\"#55ff7f\">{}</font>".format('您的答案：'), text, "相似度：{}".format(round(rat, 3)), "\n\n"]
        self.result_1[self.num] = [text, round(rat,3)*self.soc['jian'], self.soc['jian']]

    @pyqtSlot()
    def on_pushButton_A_clicked(self):
        self.xuan_panduan('A')

    @pyqtSlot()
    def on_pushButton_B_clicked(self):
        self.xuan_panduan('B')

    @pyqtSlot()
    def on_pushButton_C_clicked(self):
        self.xuan_panduan('C')

    @pyqtSlot()
    def on_pushButton_D_clicked(self):
        self.xuan_panduan('D')

    def show_result(self):
        self.textBrowser.setText(' ')
        for i in range(self.len_ti):
            if i in self.result:
                for x in range(1, len(self.result[i])):
                    self.textBrowser.append(self.result[i][x])
            else:
                y = self.tixin[i]
                self.textBrowser.append("<font color=\"#FF0000\">{}</font> ".format('此题您没有作答'))
                if y == 0:
                    self.textBrowser.append(self.key[i][:])
                    for j in self.value[i]:
                        self.textBrowser.append(j)
                    self.textBrowser.append('\n')
                elif y == 1:
                    self.textBrowser.append(self.key[i][:])
                    self.textBrowser.append('正确答案为：'+str(self.value[i]))
                    self.textBrowser.append('\n')


        self.textBrowser.append('\n\n')
        sum = 0
        sum1 = 0
        for k in self.result_1:
            sum += self.result_1[k][1]
            sum1 += self.result_1[k][2]
        self.label.setText('总分数为{}分, 您获得的总分数为{}分\n获得的百分制为{}分\n使用时间'.format(sum1,round(sum, 3),round(round(sum, 3)/sum1*100, )))


    def clearedit(self):
        if self.num == self.len_ti - 1:
            self.pushButton_9.setText('提交')
        self.textBrowser.setText("")
        for str in self.value[self.num][0]:
            self.textBrowser.append(str)
        if self.num in self.result_1:
            self.textEdit.setText(self.result_1[self.num][0])
        else:
            self.textEdit.clear()

    # 清理填写的答案
    def clearline(self):
        if self.now_falg == 2:
            print(2)
            if self.num == self.len_ti - 1:
                self.pushButton_9.setText('提交')
            self.textBrowser.setText(self.key[self.num][:])
            if self.num in self.result_1:
                self.lineEdit.setText(self.result_1[self.num][0][0])
                self.lineEdit_2.setText(self.result_1[self.num][0][1])
                self.lineEdit_3.setText(self.result_1[self.num][0][2])
                self.lineEdit_4.setText(self.result_1[self.num][0][3])
            else:
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
                self.lineEdit_3.setText('')
                self.lineEdit_4.setText('')
        elif self.now_falg == 1:
            if self.num == self.len_tian:
                self.num = 0
                shuffle(self.item_tian)
                self.item_tian.insert(0, "填空题答完了，点击下一个重新答题。")
                self.pushButton_2.setEnabled(False)
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.textBrowser.setText(self.item_tian[self.num])
        else:
            print(12)

    # 填空上一题
    @pyqtSlot()
    def on_pushButton_8_clicked(self):
        self.num -= 1
        if self.num <= 0:
            self.num = 0
        if self.pushButton_9.text() == '提交':
            self.pushButton_9.setText('下一题')
        self.total()
        self.clearline()

    # 填空下一题
    @pyqtSlot()
    def on_pushButton_9_clicked(self):
        if self.now_falg == 2:
            self.tian_panduan1111()
            self.num += 1
            if self.num >= self.len_ti:
                self.num = 0
            self.clearline()
            self.total()
        else:
            self.num += 1
            if self.num >= self.len_tian:
                self.num = 0
                shuffle(self.item_tian)
            self.clearline()

    # 简答上一题
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.jiandapanduan()
        self.num -= 1
        if self.num <= 0:
            self.num = 0
        if self.pushButton_9.text() == '提交':
            self.pushButton_9.setText('下一题')
        self.total()

    # 简答下一题
    @pyqtSlot()
    def on_pushButton_11_clicked(self):
        print(1)
        self.jiandapanduan()
        print(2)
        self.num += 1
        self.total()
        print(self.num)


    # 上一题
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        try:
            self.num -= 1
            if self.num <= 0:
                self.num = 0
            if self.now_falg == 2:
                if self.pushButton_9.text() == '提交':
                    self.pushButton_9.setText('下一题')
                self.total()
            elif self.now_falg == 1:
                self.clearline()
            else:
                self.UI_tiku()
        except:
            self.box("运行出错，请联系开发者！错误编码：003")

    # 下一题
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        try:
            if self.now_falg == 2:
                self.num += 1
                self.total()
            elif self.now_falg == 1:
                self.num += 1
                if self.num >= self.len_tian:
                    self.num = 0
                    shuffle(self.item_tian)
                self.clearline()
            else:
                self.num += 1
                if self.num >= self.len_xuan:
                    self.num = 0
                    shuffle(self.item_xuan)
                self.UI_tiku()
        except:
            self.box("运行出错，请联系开发者！错误编码：004")



    # 再来一次
    @pyqtSlot()
    def on_pushButton_10_clicked(self):
        self.stackedWidget_2.setCurrentWidget(self.page_3)
        self.progressBar.reset()
        self.result_1.clear()
        self.result.clear()
        self.total()


    # 提示
    @pyqtSlot()
    def on_pushButton_19_clicked(self):
        try:
            if self.now_falg == 0:
                self.textBrowser.append(self.xuan[self.item_xuan[self.num]][0])
            elif self.now_falg == 2:
                self.textBrowser.append('\n测试中...')
            else:
                self.tian_panduan()
        except:
            self.box("运行出错，请联系开发者！错误编码：002")



    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        try:
            self.chile_Win = help.ChildWindow()
            self.chile_Win.show()
            self.chile_Win.exec_()
        except:
            self.box("运行出错，请联系开发者！错误编码：005")

    # 选择题库
    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        try:
            self.file = QFileDialog.getOpenFileNames(self, "请选择要添加的文件", "./", "Text Files (*.txt);;All Files (*)")
            self.file = list(self.file)[0][0]
            fp = open(self.file, 'r', encoding="utf-8")
            x = fp.read()
            fp.close()
            fp1 = open("tiku.txt", 'w', encoding="utf-8")
            fp1.write(x)
            fp1.close()
            self.init()
            self.UI_tiku()
        except:
            pass

    def line_function(self):
        if self.now_falg == 2:
            len1 = len(self.ti[self.key[self.num]])
            print(len1)
            if len1 == 1:
                self.tian_panduan1111()
                self.num += 1
                self.total()
            else:
                self.lineEdit_2.setFocus()
        else:
            len1 = len(self.tian[self.item_tian[self.num]])
            x = self.tian[self.item_tian[self.num]]
            if len1 != 1:
                if self.lineEdit.text() in x:
                    self.lineEdit_2.setFocus()
                else:
                    self.lineEdit.selectAll()
            else:
                if self.lineEdit.text() == x[0]:
                    self.num += 1
                    self.clearline()
                else:
                    self.lineEdit.setText('×')
                    self.lineEdit.selectAll()

    def line1_function(self):

        if self.now_falg == 2:
            len1 = len(self.ti[self.key[self.num]])
            if len1 == 2:
                self.tian_panduan1111()
                self.num += 1
                self.total()
            else:
                self.lineEdit_3.setFocus()
        else:
            len1 = len(self.tian[self.item_tian[self.num]])
            x = self.tian[self.item_tian[self.num]]

            if len1 != 2:
                if self.lineEdit_2.text() in x:
                    self.lineEdit_3.setFocus()
                else:
                    self.lineEdit_2.selectAll()
            else:
                self.tian_panduan()
                self.lineEdit.setFocus()

    def line2_function(self):

        if self.now_falg == 2:
            len1 = len(self.ti[self.key[self.num]])
            if len1 == 3:
                self.tian_panduan1111()
                self.num += 1
                self.total()
            else:
                self.lineEdit_4.setFocus()
        else:
            len1 = len(self.tian[self.item_tian[self.num]])
            x = self.tian[self.item_tian[self.num]]

            if len1 != 3:
                if self.lineEdit_3.text() in x:
                    self.lineEdit_4.setFocus()
                else:
                    self.lineEdit_3.selectAll()
            else:
                self.tian_panduan()
                self.lineEdit.setFocus()

    def tian_panduan1111(self):
        print(1)
        answers = [self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text()]
        print(answers)
        answers_1 = answers[:]
        answers_a = self.value[self.num][:]
        print(1)
        while '' in answers:
            answers.remove('')
        if answers == []:
            return
        for answer in answers_a:
            if answer in answers:
                answers.remove(answer)
        print(1)
        if self.num in self.result:
            del self.result[self.num]
        if self.num in self.result_1:
            del self.result_1[self.num]
        print(1)
        self.result_1[self.num] = [answers_1, self.soc['tian'] * (1 - len(answers) / len(answers_a)), self.soc['tian']]
        if answers == []:
            self.result[self.num] = ['yes', self.key[self.num][:]] + [
                "<font color=\"#55ff7f\">{}</font>".format('回答正确: {}'.format([i for i in self.value[self.num]])), '\n']
        else:
            self.result[self.num] = ['no', self.key[self.num][:]] + ["<font color=\"#ff0000\">{}</font>".format(
                '回答错误: {} 你的回答：{} \n 正确答案：{}'.format('\n', [j for j in answers_1], [i for i in self.value[self.num]])), '\n']

    def line3_function(self):
        if self.now_falg == 2:
            len1 = len(self.ti[self.key[self.num]])
            if len1 == 4:
                self.tian_panduan1111()
                self.num += 1
                self.total()
            else:
                self.num += 1
                self.clearline()
                self.lineEdit.setFocus()
        else:
            self.tian_panduan()
            self.lineEdit.setFocus()

    def tian_panduan1(self):
        x = []
        x.append(self.lineEdit.text())
        x.append(self.lineEdit_2.text())
        x.append(self.lineEdit_3.text())
        x.append(self.lineEdit_4.text())
        # 动态创建变量
        createVar = locals()
        listTemp = range(len(self.ti[self.key[self.num]]))
        for i in listTemp:
            createVar['x' + str(i)] = self.ti[self.key[self.num]][i]

        while '' in x:
            x.remove('')
        if set(x) == set(self.ti[self.key[self.num]]):
            self.num += 1
            self.clearline()
        else:
            len1 = len(self.ti[self.key[self.num]])
            # 当所有空都没填时，显示答案
            if x == []:
                self.lineEdit.setText(x0)
                if len1 > 1:
                    self.lineEdit_2.setText(x1)
                if len1 > 2:
                    self.lineEdit_3.setText(x2)
                if len1 > 3:
                    self.lineEdit_4.setText(x3)
            # 没有答案的时候下一题
            elif len1 == 0:
                self.num += 1
                self.clearline()
            # 当只有一个答案时
            elif len1 == 1:
                if self.lineEdit.text() == x0:
                    self.num += 1
                    self.clearline()
                else:
                    self.lineEdit.setText('×')
                if self.lineEdit_3.text() != "":
                    self.lineEdit_3.setText('×')
                if self.lineEdit_2.text() != "":
                    self.lineEdit_2.setText('×')
            elif len1 == 2:
                if self.lineEdit.text() == x0:
                    if self.lineEdit_2.text() == x1:
                        self.num += 1
                        self.clearline()
                    else:
                        self.lineEdit_2.setText('×')
                else:
                    self.lineEdit.setText('×')
                    if self.lineEdit_2.text() != x1:
                        self.lineEdit_2.setText('×')
                if self.lineEdit_3.text() != "":
                    self.lineEdit_3.setText('×')
            elif len1 == 3:
                if self.lineEdit.text() == x0:
                    if self.lineEdit_2.text() == x1:
                        if self.lineEdit_3.text() == x2:
                            self.num += 1
                            self.clearline()
                        else:
                            self.lineEdit_3.setText('×')
                    else:
                        self.lineEdit_2.setText('×')
                        if self.lineEdit_3.text() != x2:
                            self.lineEdit_3.setText('×')
                else:
                    self.lineEdit.setText('×')
                    if self.lineEdit_2.text() != x1:
                        self.lineEdit_2.setText('×')
                    if self.lineEdit_3.text() != x2:
                        self.lineEdit_3.setText('×')
            elif len1 >= 4:
                if self.lineEdit.text() == x0:
                    if self.lineEdit_2.text() == x1:
                        if self.lineEdit_3.text() == x2:
                            if self.lineEdit_4.text() == x3:
                                self.num += 1
                                self.clearline()
                            else:
                                self.lineEdit_4.setText('×')
                        else:
                            self.lineEdit_3.setText('×')
                            if self.lineEdit_4.text() != x3:
                                self.lineEdit_4.setText('×')
                    else:
                        self.lineEdit_2.setText('×')
                        if self.lineEdit_3.text() != x2:
                            self.lineEdit_3.setText('×')
                        if self.lineEdit_4.text() != x3:
                            self.lineEdit_4.setText('×')
                else:
                    self.lineEdit.setText('×')
                    if self.lineEdit_2.text() != x1:
                        self.lineEdit_2.setText('×')
                    if self.lineEdit_3.text() != x2:
                        self.lineEdit_3.setText('×')
                    if self.lineEdit_4.text() != x3:
                        self.lineEdit_4.setText('×')

    def tian_panduan(self):
        if self.now_falg == 2:
            self.tian_panduan1()
            return
        x = []
        x.append(self.lineEdit.text())
        x.append(self.lineEdit_2.text())
        x.append(self.lineEdit_3.text())
        x.append(self.lineEdit_4.text())
        while '' in x:
            x.remove('')
        if set(x) == set(self.tian[self.item_tian[self.num]]):
            self.num += 1
            self.clearline()
        else:
            len1 = len(self.tian[self.item_tian[self.num]])
            # 当所有空都没填时，显示答案
            if x == []:
                self.lineEdit.setText(self.tian[self.item_tian[self.num]][0])
                if len1 > 1:
                    self.lineEdit_2.setText(self.tian[self.item_tian[self.num]][1])
                if len1 > 2:
                    self.lineEdit_3.setText(self.tian[self.item_tian[self.num]][2])
                if len1 > 3:
                    self.lineEdit_4.setText(self.tian[self.item_tian[self.num]][3])
            # 没有答案的时候下一题
            elif len1 == 0:
                self.num += 1
                self.clearline()
            # 当只有一个答案时
            elif len1 == 1:
                if self.lineEdit.text() == self.tian[self.item_tian[self.num]][0]:
                    self.num += 1
                    self.clearline()
                else:
                    self.lineEdit.setText('×')
                if self.lineEdit_3.text() != "":
                    self.lineEdit_3.setText('×')
                if self.lineEdit_2.text() != "":
                    self.lineEdit_2.setText('×')
            elif len1 == 2:
                if self.lineEdit.text() == self.tian[self.item_tian[self.num]][0]:
                    if self.lineEdit_2.text() == self.tian[self.item_tian[self.num]][1]:
                        self.num += 1
                        self.clearline()
                    else:
                        self.lineEdit_2.setText('×')
                else:
                    self.lineEdit.setText('×')
                    if self.lineEdit_2.text() != self.tian[self.item_tian[self.num]][1]:
                        self.lineEdit_2.setText('×')
                if self.lineEdit_3.text() != "":
                    self.lineEdit_3.setText('×')
            elif len1 == 3:
                if self.lineEdit.text() == self.tian[self.item_tian[self.num]][0]:
                    if self.lineEdit_2.text() == self.tian[self.item_tian[self.num]][1]:
                        if self.lineEdit_3.text() == self.tian[self.item_tian[self.num]][2]:
                            self.num += 1
                            self.clearline()
                        else:
                            self.lineEdit_3.setText('×')
                    else:
                        self.lineEdit_2.setText('×')
                        if self.lineEdit_3.text() != self.tian[self.item_tian[self.num]][2]:
                            self.lineEdit_3.setText('×')
                else:
                    self.lineEdit.setText('×')
                    if self.lineEdit_2.text() != self.tian[self.item_tian[self.num]][1]:
                        self.lineEdit_2.setText('×')
                    if self.lineEdit_3.text() != self.tian[self.item_tian[self.num]][2]:
                        self.lineEdit_3.setText('×')
            elif len1 >= 4:
                if self.lineEdit.text() == self.tian[self.item_tian[self.num]][0]:
                    if self.lineEdit_2.text() == self.tian[self.item_tian[self.num]][1]:
                        if self.lineEdit_3.text() == self.tian[self.item_tian[self.num]][2]:
                            if self.lineEdit_4.text() == self.tian[self.item_tian[self.num]][3]:
                                self.num += 1
                                self.clearline()
                            else:
                                self.lineEdit_4.setText('×')
                        else:
                            self.lineEdit_3.setText('×')
                            if self.lineEdit_4.text() != self.tian[self.item_tian[self.num]][3]:
                                self.lineEdit_4.setText('×')
                    else:
                        self.lineEdit_2.setText('×')
                        if self.lineEdit_3.text() != self.tian[self.item_tian[self.num]][2]:
                            self.lineEdit_3.setText('×')
                        if self.lineEdit_4.text() != self.tian[self.item_tian[self.num]][3]:
                            self.lineEdit_4.setText('×')
                else:
                    self.lineEdit.setText('×')
                    if self.lineEdit_2.text() != self.tian[self.item_tian[self.num]][1]:
                        self.lineEdit_2.setText('×')
                    if self.lineEdit_3.text() != self.tian[self.item_tian[self.num]][2]:
                        self.lineEdit_3.setText('×')
                    if self.lineEdit_4.text() != self.tian[self.item_tian[self.num]][3]:
                        self.lineEdit_4.setText('×')

    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        try:
            self.chile_Win = help.ChildWindow()
            text = """
            <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
    <html><head><meta name="qrichtext" content="1" /><style type="text/css">
    p, li { white-space: pre-wrap; }
    </style></head><body style=" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;">
    <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">大家好</span></p>
    <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">由于软件没有设计联网功能</span></p>
    <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">为了统计有多少人使用这个垃圾软件</span></p>
    <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">大家在空闲时间可以发送数字1</span></p>
    <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">到邮箱178005807@qq.com</span></p>
    <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">以便统计使用人数</span></p>
    <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">如果垃圾开发者收到了100个数字1</span></p>
    <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">垃圾程序员将会</span></p>
    <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">升级维护软件</span></p>
    <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">提高工具的使用体验。</span></p>
    <p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;"><br /></p>
    <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">如果您想关注工具的更新</span></p>
    <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">欢迎加入QQ群</span></p>
    <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">977786070</span></p>
    <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">加入群也可以更方便的</span></p>
    <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">找到大家分享的题库</span></p>
    <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">哦</span></p>
    <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:11pt;">作者：邹永佳</span></p>
    <p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;"><br /></p>
    <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt; color:#ff007f;">感谢大家使用这个垃圾软件</span></p></body></html>
            """
            self.chile_Win.textBrowser1.setHtml(text)
            self.chile_Win.show()
            self.chile_Win.exec_()
        except:
            self.box("运行出错，请联系开发者！错误编码：005")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

# 开启乱序
# 只支持4个填空题
# 进度条

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chile_Win1 = Dialog()
    chile_Win1.show()
    chile_Win1.exec_()
    Fo = Form()
    ui = Ui_Form()
    Fo.show()
    sys.exit(app.exec_())


# append() 只能用字符串，不能用其他类型的变量