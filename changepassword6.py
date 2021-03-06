# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_password.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(363, 527)
        Form.setMinimumSize(QtCore.QSize(363, 527))
        Form.setMaximumSize(QtCore.QSize(363, 527))
        Form.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Change_password = QtWidgets.QLabel(Form)
        self.Change_password.setGeometry(QtCore.QRect(40, 40, 291, 41))
        self.Change_password.setStyleSheet("font: 20pt \"Nirmala UI Semilight\";\n"
"font: 75 20pt \"Nirmala UI\";\n"
"font-weight:100px")
        self.Change_password.setObjectName("Change_password")
        self.username = QtWidgets.QLineEdit(Form)
        self.username.setGeometry(QtCore.QRect(40, 130, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.username.setFont(font)
        self.username.setAutoFillBackground(False)
        self.username.setStyleSheet("border: 1px solid gray; \n"
"selection-background-color: darkgray; \n"
" font-size: 16px;\n"
"")
        self.username.setInputMethodHints(QtCore.Qt.ImhNone)
        self.username.setText("")
        self.username.setMaxLength(32767)
        self.username.setObjectName("username")
        self.Username_label = QtWidgets.QLabel(Form)
        self.Username_label.setGeometry(QtCore.QRect(40, 110, 121, 16))
        self.Username_label.setObjectName("Username_label")
        self.oldpassword_label = QtWidgets.QLabel(Form)
        self.oldpassword_label.setGeometry(QtCore.QRect(40, 190, 111, 16))
        self.oldpassword_label.setObjectName("oldpassword_label")
        self.old_password = QtWidgets.QLineEdit(Form)
        self.old_password.setGeometry(QtCore.QRect(40, 210, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.old_password.setFont(font)
        self.old_password.setAutoFillBackground(False)
        self.old_password.setStyleSheet("border: 1px solid gray; \n"
"selection-background-color: darkgray; \n"
" font-size: 16px;\n"
"")
        self.old_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.old_password.setText("")
        self.old_password.setMaxLength(32767)
        self.old_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.old_password.setObjectName("old_password")
        self.new_password = QtWidgets.QLineEdit(Form)
        self.new_password.setGeometry(QtCore.QRect(40, 290, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.new_password.setFont(font)
        self.new_password.setAutoFillBackground(False)
        self.new_password.setStyleSheet("border: 1px solid gray; \n"
"selection-background-color: darkgray; \n"
" font-size: 16px;\n"
"")
        self.new_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.new_password.setText("")
        self.new_password.setMaxLength(32767)
        self.new_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password.setObjectName("new_password")
        self.newpassword = QtWidgets.QLabel(Form)
        self.newpassword.setGeometry(QtCore.QRect(40, 270, 141, 16))
        self.newpassword.setObjectName("newpassword")
        self.c_npassword = QtWidgets.QLineEdit(Form)
        self.c_npassword.setGeometry(QtCore.QRect(40, 370, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.c_npassword.setFont(font)
        self.c_npassword.setAutoFillBackground(False)
        self.c_npassword.setStyleSheet("border: 1px solid gray; \n"
"selection-background-color: darkgray; \n"
" font-size: 16px;\n"
"")
        self.c_npassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.c_npassword.setText("")
        self.c_npassword.setMaxLength(32767)
        self.c_npassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.c_npassword.setObjectName("c_npassword")
        self.confirm_npassword = QtWidgets.QLabel(Form)
        self.confirm_npassword.setGeometry(QtCore.QRect(40, 350, 151, 16))
        self.confirm_npassword.setObjectName("confirm_npassword")
        self.username_tip = QtWidgets.QLabel(Form)
        self.username_tip.setGeometry(QtCore.QRect(40, 170, 191, 16))
        self.username_tip.setStyleSheet("color:rgb(255, 0, 0)")
        self.username_tip.setText("")
        self.username_tip.setObjectName("username_tip")
        self.oldpassword_tip = QtWidgets.QLabel(Form)
        self.oldpassword_tip.setGeometry(QtCore.QRect(40, 250, 191, 16))
        self.oldpassword_tip.setStyleSheet("color:rgb(255, 0, 0)")
        self.oldpassword_tip.setText("")
        self.oldpassword_tip.setObjectName("oldpassword_tip")
        self.newpassword_tip = QtWidgets.QLabel(Form)
        self.newpassword_tip.setGeometry(QtCore.QRect(40, 330, 191, 16))
        self.newpassword_tip.setStyleSheet("color:rgb(255, 0, 0)")
        self.newpassword_tip.setText("")
        self.newpassword_tip.setObjectName("newpassword_tip")
        self.cnpassword_tip = QtWidgets.QLabel(Form)
        self.cnpassword_tip.setGeometry(QtCore.QRect(40, 410, 191, 16))
        self.cnpassword_tip.setStyleSheet("color:rgb(255, 0, 0)")
        self.cnpassword_tip.setText("")
        self.cnpassword_tip.setObjectName("cnpassword_tip")
        self.confirm_1 = QtWidgets.QPushButton(Form)
        self.confirm_1.setGeometry(QtCore.QRect(40, 430, 91, 31))
        self.confirm_1.setStyleSheet("font: 13pt \"MS Reference Sans Serif\";\n"
"background-color:rgb(240, 240, 240)")
        self.confirm_1.setObjectName("confirm_1")
        self.return_2 = QtWidgets.QPushButton(Form)
        self.return_2.setGeometry(QtCore.QRect(140, 430, 91, 31))
        self.return_2.setStyleSheet("font: 13pt \"MS Reference Sans Serif\";\n"
"background-color:rgb(240, 240, 240)")
        self.return_2.setObjectName("return_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Change_password.setText(_translate("Form", "Change Password"))
        self.Username_label.setText(_translate("Form", "Username"))
        self.oldpassword_label.setText(_translate("Form", "Old password"))
        self.newpassword.setText(_translate("Form", "New password"))
        self.confirm_npassword.setText(_translate("Form", "Confirm new password"))
        self.confirm_1.setText(_translate("Form", "Confirm"))
        self.return_2.setText(_translate("Form", "Return"))
