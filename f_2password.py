# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F_password2.ui'
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
        Form.setStyleSheet("background-color:white\n"
"")
        self.newpassword_tip = QtWidgets.QLabel(Form)
        self.newpassword_tip.setGeometry(QtCore.QRect(40, 170, 191, 16))
        self.newpassword_tip.setStyleSheet("color:rgb(255, 0, 0)")
        self.newpassword_tip.setText("")
        self.newpassword_tip.setObjectName("newpassword_tip")
        self.cnew_password = QtWidgets.QLineEdit(Form)
        self.cnew_password.setGeometry(QtCore.QRect(40, 210, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.cnew_password.setFont(font)
        self.cnew_password.setAutoFillBackground(False)
        self.cnew_password.setStyleSheet("border: 1px solid gray; \n"
"selection-background-color: darkgray; \n"
" font-size: 16px;\n"
"")
        self.cnew_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.cnew_password.setText("")
        self.cnew_password.setMaxLength(32767)
        self.cnew_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cnew_password.setObjectName("cnew_password")
        self.new_password = QtWidgets.QLineEdit(Form)
        self.new_password.setGeometry(QtCore.QRect(40, 130, 191, 31))
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
        self.newpassword_label = QtWidgets.QLabel(Form)
        self.newpassword_label.setGeometry(QtCore.QRect(40, 110, 191, 16))
        self.newpassword_label.setObjectName("newpassword_label")
        self.cnewpassword_label = QtWidgets.QLabel(Form)
        self.cnewpassword_label.setGeometry(QtCore.QRect(40, 190, 191, 16))
        self.cnewpassword_label.setObjectName("cnewpassword_label")
        self.Forget_password = QtWidgets.QLabel(Form)
        self.Forget_password.setGeometry(QtCore.QRect(40, 40, 291, 41))
        self.Forget_password.setStyleSheet("font: 20pt \"Nirmala UI Semilight\";\n"
"font: 75 20pt \"Nirmala UI\";\n"
"font-weight:100px")
        self.Forget_password.setObjectName("Forget_password")
        self.cnewpassowrd_tip = QtWidgets.QLabel(Form)
        self.cnewpassowrd_tip.setGeometry(QtCore.QRect(40, 250, 191, 16))
        self.cnewpassowrd_tip.setStyleSheet("color:rgb(255, 0, 0)")
        self.cnewpassowrd_tip.setText("")
        self.cnewpassowrd_tip.setObjectName("cnewpassowrd_tip")
        self.return_2 = QtWidgets.QPushButton(Form)
        self.return_2.setGeometry(QtCore.QRect(40, 280, 91, 31))
        self.return_2.setStyleSheet("font: 13pt \"MS Reference Sans Serif\";\n"
"background-color:rgb(240, 240, 240)")
        self.return_2.setObjectName("return_2")
        self.confirm_2 = QtWidgets.QPushButton(Form)
        self.confirm_2.setGeometry(QtCore.QRect(140, 280, 91, 31))
        self.confirm_2.setStyleSheet("font: 13pt \"MS Reference Sans Serif\";\n"
"background-color:rgb(240, 240, 240)")
        self.confirm_2.setObjectName("confirm_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.newpassword_label.setText(_translate("Form", "New password"))
        self.cnewpassword_label.setText(_translate("Form", "Confirm new password"))
        self.Forget_password.setText(_translate("Form", "Forget password"))
        self.return_2.setText(_translate("Form", "Return"))
        self.confirm_2.setText(_translate("Form", "Confirm"))