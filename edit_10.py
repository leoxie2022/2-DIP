# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(291, 389)
        Form.setMinimumSize(QtCore.QSize(291, 389))
        Form.setMaximumSize(QtCore.QSize(291, 389))
        Form.setStyleSheet("background-color:white\n"
"")
        self.productname_display = QtWidgets.QLabel(Form)
        self.productname_display.setGeometry(QtCore.QRect(40, 240, 191, 21))
        self.productname_display.setText("")
        self.productname_display.setObjectName("productname_display")
        self.quantity_spinbox = QtWidgets.QSpinBox(Form)
        self.quantity_spinbox.setGeometry(QtCore.QRect(40, 330, 51, 22))
        self.quantity_spinbox.setObjectName("quantity_spinbox")
        self.size_comboBox = QtWidgets.QComboBox(Form)
        self.size_comboBox.setGeometry(QtCore.QRect(80, 300, 41, 21))
        self.size_comboBox.setObjectName("size_comboBox")
        self.botany_logo = QtWidgets.QLabel(Form)
        self.botany_logo.setGeometry(QtCore.QRect(10, 10, 121, 51))
        self.botany_logo.setText("")
        self.botany_logo.setScaledContents(True)
        self.botany_logo.setObjectName("botany_logo")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 300, 41, 21))
        self.label_3.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(40, 70, 191, 161))
        self.image.setText("")
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.ok_button = QtWidgets.QPushButton(Form)
        self.ok_button.setGeometry(QtCore.QRect(100, 330, 51, 21))
        self.ok_button.setStyleSheet("background-color:rgb(240,240,240)\n"
"")
        self.ok_button.setObjectName("ok_button")
        self.price_display = QtWidgets.QLabel(Form)
        self.price_display.setGeometry(QtCore.QRect(130, 300, 121, 21))
        self.price_display.setStyleSheet("font: 11pt \"Times New Roman\";")
        self.price_display.setText("")
        self.price_display.setObjectName("price_display")
        self.back_button = QtWidgets.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(160, 330, 51, 21))
        self.back_button.setStyleSheet("background-color:rgb(240,240,240)\n"
"")
        self.back_button.setObjectName("back_button")
        self.desciption = QtWidgets.QLabel(Form)
        self.desciption.setGeometry(QtCore.QRect(40, 270, 191, 21))
        self.desciption.setText("")
        self.desciption.setObjectName("desciption")
        self.delete_button = QtWidgets.QPushButton(Form)
        self.delete_button.setGeometry(QtCore.QRect(220, 330, 56, 21))
        self.delete_button.setStyleSheet("background-color:rgb(240,240,240)\n"
"")
        self.delete_button.setObjectName("delete_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Size:"))
        self.ok_button.setText(_translate("Form", "OK"))
        self.back_button.setText(_translate("Form", "Back"))
        self.delete_button.setText(_translate("Form", "Delete"))
