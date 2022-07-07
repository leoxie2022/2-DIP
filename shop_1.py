# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(533, 505)
        Form.setMinimumSize(QtCore.QSize(533, 505))
        Form.setMaximumSize(QtCore.QSize(533, 505))
        Form.setStyleSheet("background-color:white")
        self.botany_logo = QtWidgets.QLabel(Form)
        self.botany_logo.setGeometry(QtCore.QRect(10, 10, 121, 51))
        self.botany_logo.setStyleSheet("")
        self.botany_logo.setText("")
        self.botany_logo.setScaledContents(True)
        self.botany_logo.setObjectName("botany_logo")
        self.search_button = QtWidgets.QPushButton(Form)
        self.search_button.setGeometry(QtCore.QRect(430, 30, 81, 21))
        self.search_button.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(240, 240, 240)")
        self.search_button.setObjectName("search_button")
        self.serach_1 = QtWidgets.QLineEdit(Form)
        self.serach_1.setGeometry(QtCore.QRect(140, 30, 271, 20))
        self.serach_1.setObjectName("serach_1")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 80, 141, 171))
        self.frame.setStyleSheet("border:1px solid grey")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.description_1 = QtWidgets.QLabel(self.frame)
        self.description_1.setGeometry(QtCore.QRect(10, 110, 111, 21))
        self.description_1.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";")
        self.description_1.setText("")
        self.description_1.setScaledContents(False)
        self.description_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description_1.setWordWrap(True)
        self.description_1.setObjectName("description_1")
        self.image_1 = QtWidgets.QLabel(self.frame)
        self.image_1.setGeometry(QtCore.QRect(10, 0, 111, 101))
        self.image_1.setStyleSheet("")
        self.image_1.setText("")
        self.image_1.setScaledContents(True)
        self.image_1.setObjectName("image_1")
        self.price_1 = QtWidgets.QLabel(self.frame)
        self.price_1.setGeometry(QtCore.QRect(10, 130, 101, 16))
        self.price_1.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.price_1.setText("")
        self.price_1.setObjectName("price_1")
        self.view_1 = QtWidgets.QPushButton(self.frame)
        self.view_1.setGeometry(QtCore.QRect(80, 130, 41, 17))
        self.view_1.setStyleSheet("background-color:rgb(240, 240, 240)")
        self.view_1.setObjectName("view_1")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(200, 80, 141, 171))
        self.frame_2.setStyleSheet("border:1px solid grey")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.description_2 = QtWidgets.QLabel(self.frame_2)
        self.description_2.setGeometry(QtCore.QRect(10, 110, 111, 21))
        self.description_2.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";")
        self.description_2.setText("")
        self.description_2.setScaledContents(False)
        self.description_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description_2.setWordWrap(True)
        self.description_2.setObjectName("description_2")
        self.image_2 = QtWidgets.QLabel(self.frame_2)
        self.image_2.setGeometry(QtCore.QRect(10, 0, 111, 101))
        self.image_2.setStyleSheet("")
        self.image_2.setText("")
        self.image_2.setScaledContents(True)
        self.image_2.setObjectName("image_2")
        self.price_2 = QtWidgets.QLabel(self.frame_2)
        self.price_2.setGeometry(QtCore.QRect(10, 130, 101, 16))
        self.price_2.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.price_2.setText("")
        self.price_2.setObjectName("price_2")
        self.view_2 = QtWidgets.QPushButton(self.frame_2)
        self.view_2.setGeometry(QtCore.QRect(80, 130, 41, 17))
        self.view_2.setStyleSheet("background-color:rgb(240, 240, 240)")
        self.view_2.setObjectName("view_2")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(30, 270, 141, 171))
        self.frame_4.setStyleSheet("border:1px solid grey")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.description_4 = QtWidgets.QLabel(self.frame_4)
        self.description_4.setGeometry(QtCore.QRect(10, 110, 111, 21))
        self.description_4.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";")
        self.description_4.setText("")
        self.description_4.setScaledContents(False)
        self.description_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description_4.setWordWrap(True)
        self.description_4.setObjectName("description_4")
        self.image_4 = QtWidgets.QLabel(self.frame_4)
        self.image_4.setGeometry(QtCore.QRect(10, 0, 111, 101))
        self.image_4.setStyleSheet("")
        self.image_4.setText("")
        self.image_4.setScaledContents(True)
        self.image_4.setObjectName("image_4")
        self.price_4 = QtWidgets.QLabel(self.frame_4)
        self.price_4.setGeometry(QtCore.QRect(10, 130, 101, 16))
        self.price_4.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.price_4.setText("")
        self.price_4.setObjectName("price_4")
        self.view_4 = QtWidgets.QPushButton(self.frame_4)
        self.view_4.setGeometry(QtCore.QRect(80, 130, 41, 17))
        self.view_4.setStyleSheet("background-color:rgb(240, 240, 240)")
        self.view_4.setObjectName("view_4")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(370, 80, 141, 171))
        self.frame_3.setStyleSheet("border:1px solid grey")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.description_3 = QtWidgets.QLabel(self.frame_3)
        self.description_3.setGeometry(QtCore.QRect(10, 110, 111, 21))
        self.description_3.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";")
        self.description_3.setText("")
        self.description_3.setScaledContents(False)
        self.description_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description_3.setWordWrap(True)
        self.description_3.setObjectName("description_3")
        self.image_3 = QtWidgets.QLabel(self.frame_3)
        self.image_3.setGeometry(QtCore.QRect(10, 0, 111, 101))
        self.image_3.setStyleSheet("")
        self.image_3.setText("")
        self.image_3.setScaledContents(True)
        self.image_3.setObjectName("image_3")
        self.price_3 = QtWidgets.QLabel(self.frame_3)
        self.price_3.setGeometry(QtCore.QRect(10, 130, 101, 16))
        self.price_3.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.price_3.setText("")
        self.price_3.setObjectName("price_3")
        self.view_3 = QtWidgets.QPushButton(self.frame_3)
        self.view_3.setGeometry(QtCore.QRect(80, 130, 41, 17))
        self.view_3.setStyleSheet("background-color:rgb(240, 240, 240)")
        self.view_3.setObjectName("view_3")
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(200, 270, 141, 171))
        self.frame_5.setStyleSheet("border:1px solid grey")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.description_5 = QtWidgets.QLabel(self.frame_5)
        self.description_5.setGeometry(QtCore.QRect(10, 110, 111, 21))
        self.description_5.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";")
        self.description_5.setText("")
        self.description_5.setScaledContents(False)
        self.description_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description_5.setWordWrap(True)
        self.description_5.setObjectName("description_5")
        self.image_5 = QtWidgets.QLabel(self.frame_5)
        self.image_5.setGeometry(QtCore.QRect(10, 0, 111, 101))
        self.image_5.setStyleSheet("")
        self.image_5.setText("")
        self.image_5.setScaledContents(True)
        self.image_5.setObjectName("image_5")
        self.price_5 = QtWidgets.QLabel(self.frame_5)
        self.price_5.setGeometry(QtCore.QRect(10, 130, 101, 16))
        self.price_5.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.price_5.setText("")
        self.price_5.setObjectName("price_5")
        self.view_5 = QtWidgets.QPushButton(self.frame_5)
        self.view_5.setGeometry(QtCore.QRect(80, 130, 41, 17))
        self.view_5.setStyleSheet("background-color:rgb(240, 240, 240)")
        self.view_5.setObjectName("view_5")
        self.frame_6 = QtWidgets.QFrame(Form)
        self.frame_6.setGeometry(QtCore.QRect(370, 270, 141, 171))
        self.frame_6.setStyleSheet("border:1px solid grey")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.description_6 = QtWidgets.QLabel(self.frame_6)
        self.description_6.setGeometry(QtCore.QRect(10, 110, 111, 21))
        self.description_6.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";")
        self.description_6.setText("")
        self.description_6.setScaledContents(False)
        self.description_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description_6.setWordWrap(True)
        self.description_6.setObjectName("description_6")
        self.image_6 = QtWidgets.QLabel(self.frame_6)
        self.image_6.setGeometry(QtCore.QRect(10, 0, 111, 101))
        self.image_6.setStyleSheet("")
        self.image_6.setText("")
        self.image_6.setScaledContents(True)
        self.image_6.setObjectName("image_6")
        self.price_6 = QtWidgets.QLabel(self.frame_6)
        self.price_6.setGeometry(QtCore.QRect(10, 130, 101, 16))
        self.price_6.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.price_6.setText("")
        self.price_6.setObjectName("price_6")
        self.view_6 = QtWidgets.QPushButton(self.frame_6)
        self.view_6.setGeometry(QtCore.QRect(80, 130, 41, 17))
        self.view_6.setStyleSheet("background-color:rgb(240, 240, 240)")
        self.view_6.setObjectName("view_6")
        self.next_page = QtWidgets.QPushButton(Form)
        self.next_page.setGeometry(QtCore.QRect(310, 450, 31, 21))
        self.next_page.setStyleSheet("background-color:rgb(240,240,240)")
        self.next_page.setText("")
        self.next_page.setIconSize(QtCore.QSize(20, 20))
        self.next_page.setObjectName("next_page")
        self.page_1 = QtWidgets.QLabel(Form)
        self.page_1.setGeometry(QtCore.QRect(250, 450, 51, 20))
        self.page_1.setStyleSheet("border: 1px solid gray; \n"
"font: 12pt \"PMingLiU-ExtB\";")
        self.page_1.setAlignment(QtCore.Qt.AlignCenter)
        self.page_1.setObjectName("page_1")
        self.last_page = QtWidgets.QPushButton(Form)
        self.last_page.setGeometry(QtCore.QRect(210, 450, 31, 21))
        self.last_page.setStyleSheet("background-color:rgb(240,240,240)")
        self.last_page.setText("")
        self.last_page.setIconSize(QtCore.QSize(20, 20))
        self.last_page.setObjectName("last_page")
        self.back_profile = QtWidgets.QPushButton(Form)
        self.back_profile.setGeometry(QtCore.QRect(30, 450, 141, 21))
        self.back_profile.setStyleSheet("background-color:rgb(240,240,240)")
        self.back_profile.setObjectName("back_profile")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.search_button.setText(_translate("Form", "Search"))
        self.view_1.setText(_translate("Form", "view"))
        self.view_2.setText(_translate("Form", "view"))
        self.view_4.setText(_translate("Form", "view"))
        self.view_3.setText(_translate("Form", "view"))
        self.view_5.setText(_translate("Form", "view"))
        self.view_6.setText(_translate("Form", "view"))
        self.page_1.setText(_translate("Form", "1"))
        self.back_profile.setText(_translate("Form", "Back to profile"))
