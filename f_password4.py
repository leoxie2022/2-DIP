# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F_password.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(321, 370)
        Form.setMinimumSize(QtCore.QSize(321, 370))
        Form.setMaximumSize(QtCore.QSize(321, 370))
        Form.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Forget_password = QtWidgets.QLabel(Form)
        self.Forget_password.setGeometry(QtCore.QRect(40, 40, 291, 41))
        self.Forget_password.setStyleSheet("font: 20pt \"Nirmala UI Semilight\";\n"
"font: 75 20pt \"Nirmala UI\";\n"
"font-weight:100px")
        self.Forget_password.setObjectName("Forget_password")
        self.username_label = QtWidgets.QLabel(Form)
        self.username_label.setGeometry(QtCore.QRect(40, 110, 81, 16))
        self.username_label.setObjectName("username_label")
        self.username_2 = QtWidgets.QLineEdit(Form)
        self.username_2.setGeometry(QtCore.QRect(40, 130, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.username_2.setFont(font)
        self.username_2.setAutoFillBackground(False)
        self.username_2.setStyleSheet("border: 1px solid gray; \n"
"selection-background-color: darkgray; \n"
" font-size: 16px;\n"
"")
        self.username_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.username_2.setText("")
        self.username_2.setMaxLength(32767)
        self.username_2.setObjectName("username_2")
        self.passwordcode_label = QtWidgets.QLabel(Form)
        self.passwordcode_label.setGeometry(QtCore.QRect(40, 190, 111, 16))
        self.passwordcode_label.setObjectName("passwordcode_label")
        self.password_code_2 = QtWidgets.QLineEdit(Form)
        self.password_code_2.setGeometry(QtCore.QRect(40, 210, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.password_code_2.setFont(font)
        self.password_code_2.setAutoFillBackground(False)
        self.password_code_2.setStyleSheet("border: 1px solid gray; \n"
"selection-background-color: darkgray; \n"
" font-size: 16px;\n"
"")
        self.password_code_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.password_code_2.setText("")
        self.password_code_2.setMaxLength(32767)
        self.password_code_2.setObjectName("password_code_2")
        self.username_tips = QtWidgets.QLabel(Form)
        self.username_tips.setGeometry(QtCore.QRect(40, 170, 191, 16))
        self.username_tips.setStyleSheet("color:rgb(255, 0, 0)")
        self.username_tips.setText("")
        self.username_tips.setObjectName("username_tips")
        self.passwordcode_tips = QtWidgets.QLabel(Form)
        self.passwordcode_tips.setGeometry(QtCore.QRect(40, 250, 191, 16))
        self.passwordcode_tips.setStyleSheet("color:rgb(255, 0, 0)")
        self.passwordcode_tips.setText("")
        self.passwordcode_tips.setObjectName("passwordcode_tips")
        self.confirm_1 = QtWidgets.QPushButton(Form)
        self.confirm_1.setGeometry(QtCore.QRect(140, 280, 91, 31))
        self.confirm_1.setStyleSheet("font: 13pt \"MS Reference Sans Serif\";\n"
"background-color:rgb(240, 240, 240)")
        self.confirm_1.setObjectName("confirm_1")
        self.back_1 = QtWidgets.QPushButton(Form)
        self.back_1.setGeometry(QtCore.QRect(40, 280, 91, 31))
        self.back_1.setStyleSheet("font: 13pt \"MS Reference Sans Serif\";\n"
"background-color:rgb(240, 240, 240)")
        self.back_1.setObjectName("back_1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Forget_password.setText(_translate("Form", "Forget password"))
        self.username_label.setText(_translate("Form", "Username"))
        self.passwordcode_label.setText(_translate("Form", "Password code:4 digit"))
        self.confirm_1.setText(_translate("Form", "Confirm"))
        self.back_1.setText(_translate("Form", "Return"))
