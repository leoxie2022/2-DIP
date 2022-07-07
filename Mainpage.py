from genericpath import exists
import math
from re import search
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets,QtGui
import openpyxl as op
import os
#import the login ui 
from login_menu1 import Ui_Form as login_ui
from signup_11 import Ui_Form as signup_ui
from changepassword6 import Ui_Form as changepassword_ui
from f_password4 import Ui_Form as Fpassword_ui
from f_2password import Ui_Form as Fpassword2_ui
from personal_profile import Ui_Form as profile_ui
from shop_1 import Ui_Form as interface_ui
from product_detail import Ui_Form as view_ui
from product_pay_1 import Ui_Form as pay_ui   
from product_paid import Ui_Form as paid_ui
from history_3 import Ui_Form as history_ui
from cart_16 import Ui_Form as cart_ui
from error_5 import Ui_Form as error_ui
from edit_10 import Ui_Form as edit_ui
from confirm_1 import Ui_Form as confirm_ui
from csign import Ui_Form as csign_ui
from cart_paid_2 import Ui_Form as cpay_ui
from sign6 import Ui_Form as sign_ui
from sign_2 import Ui_Form as sign_2ui
from no_result_2 import Ui_Form as no_result_ui
#access the file address of this python file
file_address=os.path.dirname(os.path.realpath(sys.argv[0]))
#access the address of the excel file
new_file_address=file_address.replace('\\','/')
data_address=new_file_address+"/"+"data"+"/"+"shop.xlsx"

#create the login window use the login_ui
class Login_window(QMainWindow, login_ui):
    def __init__(self,parent=None):
        super(Login_window, self).__init__(parent)
        self.setupUi(self)
        # add the botany logo 
        self.botany_logo.setPixmap(QtGui.QPixmap(file_address+"\\image\\botany_logo.png"))
        # once the user click the login button, connect to the gologin function
        
        self.login.clicked.connect(self.gologin)
        self.create_account.clicked.connect(self.gosignup)
        self.change_password.clicked.connect(self.gochangepassword)
        self.forget_password.clicked.connect(self.gofpassword)

    def gofpassword(self):
        #go to the forget password window and close login window
        self.fpassword=fpassword_window()
        self.fpassword.show()
        self.close()
    def gologin(self):
        # access the username from the username lineedit
        username = self.username.text()
        password = self.password.text()
        # open the excel workbook
        workbook=op.open(data_address)
        # choose the student worksheet
        student_worksheet=workbook["student"]
        # get the max row of the column A
        max_row=len(student_worksheet["A"])
        # to find if the username or the password exist and do they match?
        for i in range(2,max_row):
            if str(username)==str(student_worksheet["B"+str(i)].value) and str(password)==str(student_worksheet["C"+str(i)].value):
                    # global the row variable it will be used in the following code
                    global row
                    row=i
                    # open the profile window and close login window
                    self.profile=profile_window()
                    self.profile.show()
                    self.close()
                    break
            else:
                    #set the text of the error_tips label
                    self.error_tips.setText("Invalid username or password")
    def gosignup(self):
        self.signup=signup_window()
        self.signup.show()
        self.close()
    def gochangepassword(self):
        self.changepassword=changepassword_window()
        self.changepassword.show()
        self.close()
        
#create the login window use the login_ui
class signup_window(QMainWindow, signup_ui):

    def __init__(self,parent=None):
        super(signup_window, self).__init__(parent)
        self.setupUi(self)
        #once the user click sign up button, connect to the sign up function
        self.signup_B.clicked.connect(self.sign_up)
        self.return_B.clicked.connect(self.back)
        self.center()
    def center(self):
        #this function is used to set the window in the middle of the computer screen
        screen =  QtWidgets.QDesktopWidget().screenGeometry()
        size  =  self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
    def back(self):
        #open the login_window and close the sign up window
        self.login=Login_window()
        self.login.show()
        self.close()
    def sign_up(self):
        # access the student_id from the student_id lineedit
        student_id=self.student_id.text()
        Password=self.password.text()
        Confirm_password=self.confirm_password.text()
        Username=self.username.text()
        First_name=self.first_name.text()
        age=self.age.text()
        Last_name=self.lastname.text()
        Password_code=self.password_code.text()
        #open the excel workbook
        workbook=op.open(data_address)
        #open the student worksheet
        student_worksheet=workbook["student"]
        #gain the max_row of the column A
        max_row=len(student_worksheet["A"])
        #set the variable 'test' to detect if there is any error
        test=0
        #if the user enter nothing, the tip will appear
        if age=="":
            self.age_tips.setText("please enter your age")
            test=1
        #if the user enter the number less than 13 or more than 18, the tip will appear
        elif int(age)<13 or int(age)>18:
            self.age_tips.setText("This app is only suitable for users aged 13 to 18 years old")
            test=1
        #if there is no error, the tip will appear nothing
        else:
            self.age_tips.setText("")
            
        #if the user enter nothing, the tip will appear
        if First_name=="":
            self.firstname_tips.setText("please enter your first name")
            test=1
        else:
            self.firstname_tips.setText("")
            
        #if the user enter nothing, the tip will appear
        if Last_name=="":
            self.lastname_tips.setText("please enter your last name")
            test=1
        else:
            self.lastname_tips.setText("")
            
        #if the user enter nothing, the tip will appear
        if student_id=="":
            self.studentid_tips.setText("please enter your student ID")
            test=1
        elif student_id!="":
            #if the length of the student id not equal to 5, the tip will appear
            if len(student_id)!=5:
                self.studentid_tips.setText("student_id should be 5 digits")
                test=1
            else:
                #the for loop is used to detect if the student id have already existed.
                for i in range(2,max_row):
                    if student_id==student_worksheet["A"+str(i)].value:
                        self.studentid_tips.setText("student_id have already existed")
                        test=1
                        break
                    else:
                        self.studentid_tips.setText("")
            
            
        #if the user enter nothing, the tip will appear
        if Username=="":
            self.usernmae_tips.setText("please enter username")
            test=1
        elif Username!="":
            #the for loop is used to detect if the username have already existed.
            for i in range(2,max_row):
                if Username==student_worksheet["B"+str(i)].value:
                    self.usernmae_tips.setText("username have already existed")
                    test=1
                    break
                else:
                    self.usernmae_tips.setText("")
                    
        #if the user enter nothing, the tip will appear
        if Password=="":
            self.password_tips.setText("please enter password")
            test=1
        #if the length of the password less than 6, the tip will appear
        elif len(Password)<6:
            self.password_tips.setText("at least 6 digits password")
            test=1
        else:
            self.password_tips.setText("")
        
        #if the user enter nothing, the tip will appear
        if Confirm_password=="":
            self.cpassword_tips.setText("please confirm your password")
            test=1
        else:
            self.cpassword_tips.setText("")
            
        #if the user enter nothing, the tip will appear
        if Password_code=="":
            self.passwordcode_tips.setText("please enter password code")
            test=1
        #if the password code more than 4 digit, the tip will appear
        elif len(Password_code)>4:
            self.passwordcode_tips.setText("please enter 4 digit number")
            test=1
        #if the password code less than 4 digit, the tip will appear
        elif len(Password_code)<4:
            self.passwordcode_tips.setText("please enter 4 digit number")
            test=1
        else:
            self.passwordcode_tips.setText("")
        #only if the test equal to 0, the data the user input will be recorded to the excel table
        if test==0:
            #this is used to find the actual max_row
            for i in range(2,max_row):
                if student_worksheet["A"+str(i)].value==None:
                    global real_maxrow
                    real_maxrow=i
                    break
            real_maxrow=i
            print(real_maxrow)
            #this is used to record the data to the excel table
            student_worksheet["A"+str(real_maxrow)].value=student_id
            student_worksheet["B"+str(real_maxrow)].value=Username
            student_worksheet["C"+str(real_maxrow)].value=Password
            student_worksheet["D"+str(real_maxrow)].value=Last_name
            student_worksheet["E"+str(real_maxrow)].value=First_name
            student_worksheet["F"+str(real_maxrow)].value=Password_code
            student_worksheet["G"+str(real_maxrow)].value=1000
            workbook.save(data_address)
            self.goback=sign_window()
            self.goback.show()
            self.close()    
#create the changepassword window use the changepassword_ui
class changepassword_window(QMainWindow, changepassword_ui):
    def __init__(self,parent=None):
        super(changepassword_window, self).__init__(parent)
        
        self.setupUi(self)
        #once the user click confirm button, connect to the confirm function
        self.confirm_1.clicked.connect(self.confirm)
        self.return_2.clicked.connect(self.back)
        #call the center function
        self.center()
    def center(self):
        #this function is used to set the window in the middle of the computer screen
        screen =  QtWidgets.QDesktopWidget().screenGeometry()
        size  =  self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
    def back(self):
        #jump to the login window and close changepassword window
        self.login=Login_window()
        self.login.show()
        self.close()
    def confirm(self):
        #access the username from the username line edit
        username = self.username.text()
        password = self.old_password.text()
        New_password=self.new_password.text()
        confirm_password=self.c_npassword.text()
        #open excel workbook
        workbook=op.open(data_address)
        #open the student worksheet
        student_worksheet=workbook["student"]
        #gain the max row of the column A
        max_row=len(student_worksheet["A"])
        # set the test variable to detect if there is any error
        test=0
        #if the user enter nothing, the tip will appear
        if username=="":
            self.username_tip.setText("please enter your username")
            test=1
        else:
            self.username_tip.setText("")
        #if the user enter nothing, the tip will appear
        if password=="":
            self.oldpassword_tip.setText("please enter your password")
            test=1
        else:
            self.oldpassword_tip.setText("")
        #if the user enter nothing, the tip will appear
        if New_password=="":
            self.newpassword_tip.setText("please enter your new password")
            test=1
        #if the length of password less than 6, the tip will appear
        elif len(New_password)<6:
            self.newpassword_tip.setText("at least 6 digits password")
            test=1
        else:
            self.newpassword_tip.setText("")
        #if the user enter nothing, the tip will appear
        if confirm_password=="":
            self.cnpassword_tip.setText("please confirm your password")
            test=1
        else:
            self.cnpassword_tip.setText("")
        #only if the test equal to 0, the data the user enter will be recorded to the excel table
        if test==0:
            #set the switch variable to detect which error occur
            switch=1
            # this for loop is used to find if the username and the password match
            for i in range(2,max_row):
                if str(username)==str(student_worksheet["B"+str(i)].value) and str(password)==str(student_worksheet["C"+str(i)].value):
                    if New_password==confirm_password:
                        student_worksheet["C"+str(i)].value=New_password
                        workbook.save(data_address)
                        self.goback=sign_window()
                        self.goback.show()
                        self.close() 
                        break
                    else:
                        self.cnpassword_tip.setText("Those password didn't match")
                        switch=0
                        break
            # if switch equal to 1, it only has 2 conditions, first the password and username don't match, second no error occur. if there is no error occur, it will jump to another window and this window will close, the user won't see the tips.
            if switch==1:
                self.oldpassword_tip.setText("invalid password and username")
class fpassword_window(QMainWindow, Fpassword_ui):
    def __init__(self,parent=None):
        super(fpassword_window, self).__init__(parent)
        self.setupUi(self)
        #once the user click confirm, it will connect to the gonpage function
        self.confirm_1.clicked.connect(self.gonpage)
        self.back_1.clicked.connect(self.back)
    def back(self):
        #back to login window
        self.login=Login_window()
        self.login.show()
        self.close()
    def gonpage(self):
        #gain the username from the lineedit
        username = self.username_2.text()
        password_code = self.password_code_2.text()
        #open excel workbook
        workbook=op.open(data_address)
        #open student_worksheet
        student_worksheet=workbook["student"]
        max_row=len(student_worksheet["A"])
        test=1
        #if user enter nothing, the tip will appear
        if username=="":
            self.username_tips.setText("please enter your username")
            test=0
        else:
            self.username_tips.setText("")
        if password_code=="":
            self.passwordcode_tips.setText("please enter your password code")
            test=0
        else:
            self.passwordcode_tips.setText("")
        #if the test equal to 1, （it also means there are no errors,） the program will jump to next window
        if test==1:
            for i in range(2,max_row):
                if str(username)==str(student_worksheet["B"+str(i)].value) and str(password_code)==str(student_worksheet["F"+str(i)].value):
                        global row
                        row=i
                        self.fpassword=fpassword2_window()
                        self.fpassword.show()
                        self.close()
                        break
                else:
                    self.passwordcode_tips.setText("invalid username and password code")
class fpassword2_window(QMainWindow, Fpassword2_ui):
    def __init__(self,parent=None):
        super(fpassword2_window, self).__init__(parent)
        self.setupUi(self)
        #once the user click confirm, it will connect to the confirm function
        self.confirm_2.clicked.connect(self.confirm)
        self.return_2.clicked.connect(self.back)
    def back(self):
        #the first window show if the user click back
        self.fpassword=fpassword_window()
        self.fpassword.show()
        self.close()
    def confirm(self):
        #gain the new password from the correspond line edit
        New_password=self.new_password.text()
        confirm_password=self.cnew_password.text()
        # open excel workbook
        workbook=op.open(data_address)
        # open the student worksheet
        student_worksheet=workbook["student"]
        test=1
        # if the user enter nothing, the tip will appear
        if New_password=="":
            self.newpassword_tip.setText("please create a new password")
            test=0
        elif len(New_password)<6:
            self.newpassword_tip.setText("at least 6 digits password")
            test=0
        else:
            self.newpassword_tip.setText("")
        if confirm_password=="":
            self.cnewpassowrd_tip.setText("please confirm your password")
            test=0
        else:
            self.cnewpassowrd_tip.setText("")
        #if the test equal to 1, （it also means there are no errors,） the program will jump to next window
        if test==1:
            if New_password==confirm_password:
                student_worksheet["C"+str(row)].value=New_password
                workbook.save(data_address)
                self.goback=sign_window()
                self.goback.show()
                self.close() 
            else:
                self.cnewpassowrd_tip.setText("Those password didn't match")
#create the profile window use profile_ui
class profile_window(QMainWindow, profile_ui):
    def __init__(self,parent=None):
        super(profile_window, self).__init__(parent)
        self.setupUi(self)
        #set the botany log
        self.botany_logo.setPixmap(QtGui.QPixmap(file_address+"/image/a03.png"))
        #open the workbook
        workbook=op.open(data_address)
        #choose the student worksheet
        student_worksheet=workbook["student"]
        #display the name, student_id and account balance
        self.display_name.setText(student_worksheet["E"+str(row)].value.capitalize()+" "+student_worksheet["D"+str(row)].value.capitalize())
        self.display_studentid.setText(student_worksheet["A"+str(row)].value)
        self.display_accountbalance.setText("${}".format(student_worksheet["G"+str(row)].value))
        #once the user click shop button, it will connect the shop function
        self.shop_1.clicked.connect(self.shop)
        self.logout.clicked.connect(self.backlogin)
        self.cart_1.clicked.connect(self.gocart)
        self.history.clicked.connect(self.gohistory)
    #the user will go to the purchase history window
    def gohistory(self):
        self.history=history_window()
        self.history.show()
        self.close()
    def gocart(self):
        self.buy=cart_window()
        self.buy.show()
        self.close()
    def backlogin(self):
        self.login=Login_window()
        self.login.show()
        self.close()
    def shop(self):
        self.interface=interface_window()
        self.interface.show()
        self.close()
# create cart_window use Cart_ui
class cart_window(QMainWindow, cart_ui):
    def __init__(self,parent=None):
        super(cart_window, self).__init__(parent)
        self.setupUi(self)
        #set the botany logo
        self.botany_logo.setPixmap(QtGui.QPixmap(file_address+"/image/a03.png"))
        #open the work book
        workbook=op.open(data_address)
        #choose the orderdetail worksheet
        orderdetail_worksheet=workbook["orderdetail"]
        #gain the max row of column C
        max_page=len(orderdetail_worksheet["C"])
        #choose the student worksheet
        student_worksheet=workbook["student"]
        student_id=student_worksheet["A"+str(row)].value
        #gain the cart item for current account
        global list_4
        list_4=[]
        for i in range(2,max_page):
            if orderdetail_worksheet["B"+str(i)].value==student_id and orderdetail_worksheet["H"+str(i)].value=="Cart":
                
                list_4.append(i)
        #if the cart don't have item, the user can't use pay
        if len(list_4)==0:
            self.pay_1.setEnabled(False)
        #Insert the item to the cart_list
        self.cart_list.insertItem(1,"Name        Quantity        Price       Size")
        for a in range(0,len(list_4)):
            self.cart_list.insertItem(a+2,"{}          {}          ${}         {}".format(orderdetail_worksheet["C"+str(list_4[a])].value,orderdetail_worksheet["E"+str(list_4[a])].value,orderdetail_worksheet["D"+str(list_4[a])].value,orderdetail_worksheet["F"+str(list_4[a])].value))
        total=0
        max_row=len(orderdetail_worksheet["C"])
        #gain the actual max row
        for b in range(2,max_row):
            if orderdetail_worksheet["C"+str(b)].value==None:
                break
        real_maxrow_1=b
        #calculate the total price
        for a in range(2,real_maxrow_1):
            if orderdetail_worksheet["B"+str(a)].value==student_id and orderdetail_worksheet["H"+str(a)].value=="Cart":
                total=total+int(orderdetail_worksheet["D"+str(a)].value)*int(orderdetail_worksheet["E"+str(a)].value)
        self.cart_list.insertItem(2+len(list_4),"Total Price: ${}".format(total))
        #once the user click the cart item, it will connect the edit
        self.cart_list.clicked.connect(self.edit)
        self.back_1.clicked.connect(self.back)
        self.pay_1.clicked.connect(self.pay)
    #open the confirm window
    def pay(self):
        global confirm
        confirm="Cart"
        self.confirm=confirm_window()
        self.confirm.show()
        self.close()
    def back(self):
        self.profile=profile_window()
        self.profile.show()
        self.close()

    def edit(self):
        #the first row and last row can't be clicked
        if self.cart_list.row(self.cart_list.currentItem())==0:
            None
        elif self.cart_list.row(self.cart_list.currentItem())==len(list_4)+1:
            None
        else:
            global view
            view=self.cart_list.row(self.cart_list.currentItem())
            self.edit=edit_window()
            self.edit.show()
            self.close()
#create cart pay window use cpay_ui similar as the product pay window
class cpay_window(QMainWindow, cpay_ui):
    def __init__(self,parent=None):
        super(cpay_window, self).__init__(parent)
        self.setupUi(self)
        workbook=op.open(data_address)
        orderdetail_worksheet=workbook["orderdetail"]
        student_worksheet=workbook["student"]
        max_row=len(orderdetail_worksheet["C"])
        student_id=student_worksheet["A"+str(row)].value
        name=student_worksheet["E"+str(row)].value.capitalize()+" "+student_worksheet["D"+str(row)].value.capitalize()
        self.botany_logo.setPixmap(QtGui.QPixmap(file_address+"/image/a03.png"))
        self.studentid_display.setText("Student ID: {}".format(student_id))
        self.name_display.setText("Name: {}".format(name))
        total=0
        max_row=len(orderdetail_worksheet["C"])
        for i in range(2,max_row):
            if orderdetail_worksheet["C"+str(i)].value==None:
                real_maxrow_2=i
                break
        real_maxrow_2=i
      
        for a in range(2,real_maxrow_2):
            if orderdetail_worksheet["B"+str(a)].value==student_id and orderdetail_worksheet["H"+str(a)].value=="Cart":
                total=total+int(orderdetail_worksheet["D"+str(a)].value)*int(orderdetail_worksheet["E"+str(a)].value)
                orderdetail_worksheet["H"+str(a)].value="Paid"
       
        self.totalprice_display.setText("Total price: ${}".format(str(total)))
        account_balance=int(student_worksheet["G"+str(row)].value)-total
        self.accountbalance_display.setText("Account balance: ${}".format(str(account_balance)))
        student_worksheet["G"+str(row)].value=account_balance      
        self.back_profile_1.clicked.connect(self.back_profile)
        self.go_shop.clicked.connect(self.back_shop)
        workbook.save(data_address)
    def back_profile(self):
        self.profile=profile_window()
        self.profile.show()
        self.close()
    def back_shop(self):
        self.interface=interface_window()
        self.interface.show()
        self.close()
#create the edit_window use edit_ui
class edit_window(QMainWindow, edit_ui):
    def __init__(self,parent=None):
        super(edit_window, self).__init__(parent)
        self.setupUi(self)   
        workbook=op.open(data_address)
        orderdetail_worksheet=workbook["orderdetail"]
        self.botany_logo.setPixmap(QtGui.QPixmap(file_address+"/image/a03.png"))
        self.image.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(orderdetail_worksheet["I"+str(list_4[view-1])].value)))
        self.productname_display.setText(orderdetail_worksheet["C"+str(list_4[view-1])].value)
        self.desciption.setText(orderdetail_worksheet["J"+str(list_4[view-1])].value)
        self.price_display.setText("${}".format(orderdetail_worksheet["D"+str(list_4[view-1])].value))
        self.quantity_spinbox.setValue(int(orderdetail_worksheet["E"+str(list_4[view-1])].value))
        self.quantity_spinbox.setRange(1,9)
        size=orderdetail_worksheet["K"+str(list_4[view-1])].value.split(',')
        self.size_comboBox.addItems(size)
        self.back_button.clicked.connect(self.back)
        self.delete_button.clicked.connect(self.delete)
        self.ok_button.clicked.connect(self.change)
    def change(self):
        workbook=op.open(data_address)
        orderdetail_worksheet=workbook["orderdetail"]
        orderdetail_worksheet["E"+str(list_4[view-1])].value=self.quantity_spinbox.value()
        orderdetail_worksheet["F"+str(list_4[view-1])].value=self.size_comboBox.currentText()
        workbook.save(data_address)
        self.buy=cart_window()
        self.buy.show()
        self.close()
    def back(self):
        self.buy=cart_window()
        self.buy.show()
        self.close()
    def delete(self):
        self.setupUi(self)   
        workbook=op.open(data_address)
        orderdetail_worksheet=workbook["orderdetail"]
        
        orderdetail_worksheet["H"+str(list_4[view-1])].value=str("deleted")
        workbook.save(data_address)
        self.buy=cart_window()
        self.buy.show()
        self.close()
#create history_window use history_ui
class history_window(QMainWindow, history_ui):
    def __init__(self,parent=None):
        
        super(history_window, self).__init__(parent)
        self.setupUi(self)
        #open the workbook
        workbook=op.open(data_address)
        #choose the orderdetail and student
        orderdetail_worksheet=workbook["orderdetail"]
        student_worksheet=workbook["student"]
        student_id=student_worksheet["A"+str(row)].value
      
        max_row=len(orderdetail_worksheet["C"])
        global list_3
        list_3=[]
        self.botany_logo.setPixmap(QtGui.QPixmap(file_address+"/image/a03.png"))
        for i in range(2,max_row):
            if orderdetail_worksheet["B"+str(i)].value==student_id and orderdetail_worksheet["H"+str(i)].value=="Paid":
                    list_3.append(i)
                

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(file_address+"/image/11.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_page_1.setIcon(icon)
        self.next_page_1.setIconSize(QtCore.QSize(20, 20))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(file_address+"/image/b033.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.last_page_1.setIcon(icon)
        self.last_page_1.setIconSize(QtCore.QSize(20, 20))
        global page_2
        page_2=1
        self.label_3.setText(str(page_2))
        #display the product, if there is no item, show nothing
        try:
            self.image_1.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(orderdetail_worksheet["I"+str(list_3[0])].value)))
            self.productname_display.setText("Product name: {}".format(str(orderdetail_worksheet["C"+str(list_3[0])].value)))
            self.price_display.setText("Price: ${}".format(str(orderdetail_worksheet["D"+str(list_3[0])].value)))
            self.size_display.setText("Size: {}".format(str(orderdetail_worksheet["F"+str(list_3[0])].value)))
            self.quantity_display.setText("Quantity: {}".format(str(orderdetail_worksheet["E"+str(list_3[0])].value)))
        except:
            self.image_1.clear()
            self.productname_display.clear()
            self.price_display.clear()
            self.size_display.clear()
            self.quantity_display.clear()
        try:
            self.image_2.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(orderdetail_worksheet["I"+str(list_3[1])].value)))
            self.productname_display_2.setText("Product name: {}".format(str(orderdetail_worksheet["C"+str(list_3[1])].value)))
            self.price_display_2.setText("Price: ${}".format(str(orderdetail_worksheet["D"+str(list_3[1])].value)))
            self.size_display_2.setText("Size: {}".format(str(orderdetail_worksheet["F"+str(list_3[1])].value)))
            self.quantity_display_2.setText("Quantity: {}".format(str(orderdetail_worksheet["E"+str(list_3[1])].value)))
        except:
            self.image_2.clear()
            self.productname_display_2.clear()
            self.price_display_2.clear()
            self.size_display_2.clear()
            self.quantity_display_2.clear()
        try:
            self.image_3.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(orderdetail_worksheet["I"+str(list_3[2])].value)))
            self.productname_display_3.setText("Product name: {}".format(str(orderdetail_worksheet["C"+str(list_3[2])].value)))
            self.price_display_3.setText("Price: ${}".format(str(orderdetail_worksheet["D"+str(list_3[2])].value)))
            self.size_display_3.setText("Size: {}".format(str(orderdetail_worksheet["F"+str(list_3[2])].value)))
            self.quantity_display_3.setText("Quantity: {}".format(str(orderdetail_worksheet["E"+str(list_3[2])].value)))
        except:
            self.image_3.clear()
            self.productname_display_3.clear()
            self.price_display_3.clear()
            self.size_display_3.clear()
            self.quantity_display_3.clear()
        self.last_page_1.clicked.connect(self.lastpage)
        self.next_page_1.clicked.connect(self.nextpage)
        self.back_profile_1.clicked.connect(self.back_profile)
        self.center()
    def center(self):
        screen =  QtWidgets.QDesktopWidget().screenGeometry()
        size  =  self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
    def back_profile(self):
        self.profile=profile_window()
        self.profile.show()
        self.close()
    def lastpage(self):
        workbook=op.open(data_address)
        orderdetail_worksheet=workbook["orderdetail"]
        max_page=len(orderdetail_worksheet["C"])
        global page_2
        page_2=page_2-1
        max_page=math.ceil(len(list_3)/3)
        if page_2<1:
            page_2=max_page
        #click to view last 3 product
        try:
            self.image_1.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(orderdetail_worksheet["I"+str(list_3[0+(page_2-1)*3])].value)))
            self.productname_display.setText("Product name: {}".format((str(orderdetail_worksheet["C"+str(list_3[0+(page_2-1)*3])].value))))
            self.price_display.setText(str("Price: ${}".format(orderdetail_worksheet["D"+str(list_3[0+(page_2-1)*3])].value)))
            self.size_display.setText("Size: {}".format(str(orderdetail_worksheet["F"+str(list_3[0+(page_2-1)*3])].value)))
            self.quantity_display.setText("Quantity: {}".format(str(orderdetail_worksheet["E"+str(list_3[0+(page_2-1)*3])].value)))
        except:
            self.image_1.clear()
            self.productname_display.clear()
            self.price_display.clear()
            self.size_display.clear()
            self.quantity_display.clear()
        try:
            self.image_2.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(orderdetail_worksheet["I"+str(list_3[1+(page_2-1)*3])].value)))
            self.productname_display_2.setText("Product name: {}".format(str(orderdetail_worksheet["C"+str(list_3[1+(page_2-1)*3])].value)))
            self.price_display_2.setText("Price: ${}".format((str(orderdetail_worksheet["D"+str(list_3[1+(page_2-1)*3])].value))))
            self.size_display_2.setText("Size: {}".format(str(orderdetail_worksheet["F"+str(list_3[1+(page_2-1)*3])].value)))
            self.quantity_display_2.setText("Quantity: {}".format(str(orderdetail_worksheet["E"+str(list_3[1+(page_2-1)*3])].value)))
        except:
            self.image_2.clear()
            self.productname_display_2.clear()
            self.price_display_2.clear()
            self.size_display_2.clear()
            self.quantity_display_2.clear()
        try:
            self.image_3.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(orderdetail_worksheet["I"+str(list_3[2+(page_2-1)*3])].value)))
            self.productname_display_3.setText("Product name: {}".format((str(orderdetail_worksheet["C"+str(list_3[2+(page_2-1)*3])].value))))
            self.price_display_3.setText("Price: ${}".format(str(orderdetail_worksheet["D"+str(list_3[2+(page_2-1)*3])].value)))
            self.size_display_3.setText("Size: {}".format(str(orderdetail_worksheet["F"+str(list_3[2+(page_2-1)*3])].value)))
            self.quantity_display_3.setText("Quantity: {}".format(str(orderdetail_worksheet["E"+str(list_3[2+(page_2-1)*3])].value)))
        except:
            self.image_3.clear()
            self.productname_display_3.clear()
            self.price_display_3.clear()
            self.size_display_3.clear()
            self.quantity_display_3.clear()
        self.label_3.setText(str(page_2))
    def nextpage(self):
        workbook=op.open(data_address)
        orderdetail_worksheet=workbook["orderdetail"]
        max_page=len(orderdetail_worksheet["C"])
        global page_2
        page_2=page_2+1
        max_page=math.ceil(len(list_3)/3)
        if page_2>max_page:
            page_2=1
        #click to view next 3 product
        try:
            self.image_1.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(orderdetail_worksheet["I"+str(list_3[0+(page_2-1)*3])].value)))
            self.productname_display.setText("Product name: {}".format((str(orderdetail_worksheet["C"+str(list_3[0+(page_2-1)*3])].value))))
            self.price_display.setText(str("Price: ${}".format(orderdetail_worksheet["D"+str(list_3[0+(page_2-1)*3])].value)))
            self.size_display.setText("Size: {}".format(str(orderdetail_worksheet["F"+str(list_3[0+(page_2-1)*3])].value)))
            self.quantity_display.setText("Quantity: {}".format(str(orderdetail_worksheet["E"+str(list_3[0+(page_2-1)*3])].value)))
        except:
            self.image_1.clear()
            self.productname_display.clear()
            self.price_display.clear()
            self.size_display.clear()
            self.quantity_display.clear()
        try:
            self.image_2.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(orderdetail_worksheet["I"+str(list_3[1+(page_2-1)*3])].value)))
            self.productname_display_2.setText("Product name: {}".format(str(orderdetail_worksheet["C"+str(list_3[1+(page_2-1)*3])].value)))
            self.price_display_2.setText("Price: ${}".format((str(orderdetail_worksheet["D"+str(list_3[1+(page_2-1)*3])].value))))
            self.size_display_2.setText("Size: {}".format(str(orderdetail_worksheet["F"+str(list_3[1+(page_2-1)*3])].value)))
            self.quantity_display_2.setText("Quantity: {}".format(str(orderdetail_worksheet["E"+str(list_3[1+(page_2-1)*3])].value)))
        except:
            self.image_2.clear()
            self.productname_display_2.clear()
            self.price_display_2.clear()
            self.size_display_2.clear()
            self.quantity_display_2.clear()
        try:
            self.image_3.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(orderdetail_worksheet["I"+str(list_3[2+(page_2-1)*3])].value)))
            self.productname_display_3.setText("Product name: {}".format((str(orderdetail_worksheet["C"+str(list_3[2+(page_2-1)*3])].value))))
            self.price_display_3.setText("Price: ${}".format(str(orderdetail_worksheet["D"+str(list_3[2+(page_2-1)*3])].value)))
            self.size_display_3.setText("Size: {}".format(str(orderdetail_worksheet["F"+str(list_3[2+(page_2-1)*3])].value)))
            self.quantity_display_3.setText("Quantity: {}".format(str(orderdetail_worksheet["E"+str(list_3[2+(page_2-1)*3])].value)))
        except:
            self.image_3.clear()
            self.productname_display_3.clear()
            self.price_display_3.clear()
            self.size_display_3.clear()
            self.quantity_display_3.clear()
        self.label_3.setText(str(page_2))



        
#set the variable, all the variable is used in interface window
#page is used to inform user which page they are in
#times is used to calculate how many times the user click 
#value is used to detect if the user use search
#page_1 is used in the search function
page=1  
times=0
value=1
page_1=1

class interface_window(QMainWindow, interface_ui):
    def __init__(self,parent=None):
        
        super(interface_window, self).__init__(parent)
        self.setupUi(self)     
        #open excel workbook
        workbook=op.open(data_address)
        #open product sheet of the excel workbook
        product_worksheet=workbook["product"]
        icon = QtGui.QIcon()
        #add Icon (right arrow)
        icon.addPixmap(QtGui.QPixmap(file_address+"/image/11.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_page.setIcon(icon)
        self.next_page.setIconSize(QtCore.QSize(20, 20))
        icon = QtGui.QIcon()
        #add Icon (left arrow)
        icon.addPixmap(QtGui.QPixmap(file_address+"/image/b033.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.last_page.setIcon(icon)
        self.last_page.setIconSize(QtCore.QSize(20, 20))
        #add the botany logo
        self.botany_logo.setPixmap(QtGui.QPixmap(file_address+"/image/a03.png"))
        
        global page
        page=page
        global times
        times=times
        

        
        #this case is when the user has used search function, then the shop will use list_1 to display product
        if value==0:
            self.page_1.setText(str(page_1))
            self.image_1.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[0+6*(page_1-1)])].value)))
            self.price_1.setText(str(product_worksheet["F"+str(list_1[0+(page_1-1)])].value))
            self.description_1.setText(product_worksheet["C"+str(list_1[0+6*(page_1-1)])].value)
            self.image_2.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[1+6*(page_1-1)])].value)))
            self.price_2.setText(str(product_worksheet["F"+str(list_1[1+6*(page_1-1)])].value))
            self.description_2.setText(product_worksheet["C"+str(list_1[1+6*(page_1-1)])].value)
            self.image_3.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[2+6*(page_1-1)])].value)))
            self.price_3.setText(str(product_worksheet["F"+str(list_1[2+6*(page_1-1)])].value))
            self.description_3.setText(product_worksheet["C"+str(list_1[2+6*(page_1-1)])].value)
            self.image_4.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[3+6*(page_1-1)])].value)))
            self.price_4.setText(str(product_worksheet["F"+str(list_1[3+6*(page_1-1)])].value))
            self.description_4.setText(product_worksheet["C"+str(list_1[3+6*(page_1-1)])].value)
            self.image_5.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[4+6*(page_1-1)])].value)))
            self.price_5.setText(str(product_worksheet["F"+str(list_1[4+6*(page_1-1)])].value))
            self.description_5.setText(product_worksheet["C"+str(list_1[4+6*(page_1-1)])].value)
            self.image_6.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[5+6*(page_1-1)])].value)))
            self.price_6.setText(str(product_worksheet["F"+str(list_1[5+6*(page_1-1)])].value))
            self.description_6.setText(product_worksheet["C"+str(list_1[5+6*(page_1-1)])].value)
            if self.price_1.text()=="None":
                self.frame.hide()
                self.price_1.clear()
                self.view_1.hide()
            else:
                self.frame.show()
                self.view_1.show()
            if self.price_2.text()=="None":
                self.frame_2.hide()
                self.price_2.clear()
                self.view_2.hide()
            else:
                self.frame_2.show()
                self.view_2.show()
            if self.price_3.text()=="None":
                self.frame_3.hide()
                self.price_3.clear()
                self.view_3.hide()
            else:
                self.frame_3.show()
                self.view_3.show()
            if self.price_4.text()=="None":
                self.frame_4.hide()
                self.price_4.clear()
                self.view_4.hide()
            else:
                self.frame_4.show()
                self.view_4.show()
            if self.price_5.text()=="None":
                self.frame_5.hide()
                self.price_5.clear()
                self.view_5.hide()
            else:
                self.frame_5.show()
                self.view_5.show()
            if self.price_6.text()=="None":
                self.frame_6.hide()
                self.price_6.clear()
                self.view_6.hide()
            else:
                self.frame_6.show()
                self.view_6.show()
        #this case is the user didn't use the search, the shop will use times to display the product
        else:
            self.page_1.setText(str(page))
            self.image_1.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(2+6*times)].value)))
            self.price_1.setText(str(product_worksheet["F"+str(2+6*times)].value))
            self.description_1.setText(product_worksheet["C"+str(2+6*times)].value)
            self.image_2.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(3+6*times)].value)))
            self.price_2.setText(str(product_worksheet["F"+str(3+6*times)].value))
            self.description_2.setText(product_worksheet["C"+str(3+6*times)].value)
            self.image_3.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(4+6*times)].value)))
            self.price_3.setText(str(product_worksheet["F"+str(4+6*times)].value))
            self.description_3.setText(product_worksheet["C"+str(4+6*times)].value)
            self.image_4.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(5+6*times)].value)))
            self.price_4.setText(str(product_worksheet["F"+str(5+6*times)].value))
            self.description_4.setText(product_worksheet["C"+str(5+6*times)].value)
            self.image_5.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(6+6*times)].value)))
            self.price_5.setText(str(product_worksheet["F"+str(6+6*times)].value))
            self.description_5.setText(product_worksheet["C"+str(6+6*times)].value)
            self.image_6.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(7+6*times)].value)))
            self.price_6.setText(str(product_worksheet["F"+str(7+6*times)].value))
            self.description_6.setText(product_worksheet["C"+str(7+6*times)].value)
        #if there is nothing, hide the frame and the view button
            if self.price_1.text()=="None":
                self.frame.hide()
                self.price_1.clear()
                self.view_1.hide()
            else:
                self.frame.show()
                self.view_1.show()
            if self.price_2.text()=="None":
                self.frame_2.hide()
                self.price_2.clear()
                self.view_2.hide()
            else:
                self.frame_2.show()
                self.view_2.show()
            if self.price_3.text()=="None":
                self.frame_3.hide()
                self.price_3.clear()
                self.view_3.hide()
            else:
                self.frame_3.show()
                self.view_3.show()
            if self.price_4.text()=="None":
                self.frame_4.hide()
                self.price_4.clear()
                self.view_4.hide()
            else:
                self.frame_4.show()
                self.view_4.show()
            if self.price_5.text()=="None":
                self.frame_5.hide()
                self.price_5.clear()
                self.view_5.hide()
            else:
                self.frame_5.show()
                self.view_5.show()
            if self.price_6.text()=="None":
                self.frame_6.hide()
                self.price_6.clear()
                self.view_6.hide()
            else:
                self.frame_6.show()
                self.view_6.show()
        #once click the back button connect to backprofile
        self.back_profile.clicked.connect(self.backprofile)
        self.next_page.clicked.connect(self.nextpage)
        self.last_page.clicked.connect(self.lastpage)
        self.search_button.clicked.connect(self.search)
        self.view_1.clicked.connect(self.goview_1)
        self.view_2.clicked.connect(self.goview_2)
        self.view_3.clicked.connect(self.goview_3)
        self.view_4.clicked.connect(self.goview_4)
        self.view_5.clicked.connect(self.goview_5)
        self.view_6.clicked.connect(self.goview_6)
        self.center()
    #set the page_1 variable to show the page when user use search function
    page_1=1
    def search(self):
        global value
        #set the value equal to 0, this means the user click the search button
        value=0
        #access the user input from the search line edit
        search_result=self.serach_1.text()
        #open excel workbook
        workbook=op.open(data_address)
        #open product worksheet
        product_worksheet=workbook["product"]
        #gain the max_row of the column A
        max_row=len(product_worksheet["A"])
        global page_1
        page_1=page_1
        # this set of code is used to detect if list_1 exist. 
        #If the user uses the search function more than once, if one of the search results is no_result, 
        # then the previous search_result will remain. The following code is used for this function
        global list_1
        try:
            list_1
        except NameError:
            var_exist=False
        else:
            var_exist=True
        if var_exist==True:
            if list_1!=[]:
                global list_2
                list_2=list_1
        
        global times_1
        times_1=0
        
        list_1=[]
        #this for loop is used to find the actual max row
        for i in range(2,max_row):
                if product_worksheet["A"+str(i)].value==None:
                    global real_maxrow
                    real_maxrow=i
                    break
        #this for loop is used to find the search_result in the excel table, the list 1 will collect all the satisfy result
        for i in range(2,real_maxrow):
            if str(search_result).lower().replace(" ","") in product_worksheet["C"+str(i)].value.lower().replace(" ",""):
                list_1.append(i)
        #if list_1 don't contain anything, then the no result will pop-up.
        if len(list_1)==0:
            self.no_result=no_result_window()
            self.no_result.show()
            try:
                list_1=list_2
            except NameError:
                value=1
                page_1=page
                self.page_1.setText(str(page_1))
        #if the list_1 contain something, then it will display
        else:
            page_1=1
            max_times=int(len(list_1)/6)
            global index
            index=len(list_1)-max_times*6
            add_item=6-index
            if add_item==6:
                None
            else:
                for i in range(0,add_item,1):
                    list_1.append(int(max_row+1))
            self.image_1.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[0])].value)))
            self.price_1.setText(str(product_worksheet["F"+str(list_1[0])].value))
            self.description_1.setText(product_worksheet["C"+str(list_1[0])].value)
            self.image_2.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[1])].value)))
            self.price_2.setText(str(product_worksheet["F"+str(list_1[1])].value))
            self.description_2.setText(product_worksheet["C"+str(list_1[1])].value)
            self.image_3.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[2])].value)))
            self.price_3.setText(str(product_worksheet["F"+str(list_1[2])].value))
            self.description_3.setText(product_worksheet["C"+str(list_1[2])].value)
            self.image_4.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[3])].value)))
            self.price_4.setText(str(product_worksheet["F"+str(list_1[3])].value))
            self.description_4.setText(product_worksheet["C"+str(list_1[3])].value)
            self.image_5.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[4])].value)))
            self.price_5.setText(str(product_worksheet["F"+str(list_1[4])].value))
            self.description_5.setText(product_worksheet["C"+str(list_1[4])].value)
            self.image_6.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[5])].value)))
            self.price_6.setText(str(product_worksheet["F"+str(list_1[5])].value))
            self.description_6.setText(product_worksheet["C"+str(list_1[5])].value)
            self.page_1.setText(str(page_1))
            #if there is nothing, hide the frame and the view button
            if self.price_1.text()=="None":
                self.frame.hide()
                self.price_1.clear()
                self.view_1.hide()
            else:
                self.frame.show()
                self.view_1.show()
            if self.price_2.text()=="None":
                self.frame_2.hide()
                self.price_2.clear()
                self.view_2.hide()
            else:
                self.frame_2.show()
                self.view_2.show()
            if self.price_3.text()=="None":
                self.frame_3.hide()
                self.price_3.clear()
                self.view_3.hide()
            else:
                self.frame_3.show()
                self.view_3.show()
            if self.price_4.text()=="None":
                self.frame_4.hide()
                self.price_4.clear()
                self.view_4.hide()
            else:
                self.frame_4.show()
                self.view_4.show()
            if self.price_5.text()=="None":
                self.frame_5.hide()
                self.price_5.clear()
                self.view_5.hide()
            else:
                self.frame_5.show()
                self.view_5.show()
            if self.price_6.text()=="None":
                self.frame_6.hide()
                self.price_6.clear()
                self.view_6.hide()
            else:
                self.frame_6.show()
                self.view_6.show()
    #this function is used to back profile window
    def backprofile(self):
        self.profile=profile_window()
        self.profile.show()
        self.close()
    #this funtion is used to go to the view window
    def goview_1(self):
    #view variable is used to help the program locate which view button the user click
        global view
        view=1
        self.view=view_window()
        self.view.show()
        self.close()
    def goview_2(self):
        
        global view
        view=2
        self.view=view_window()
        self.view.show()
        self.close()
    def goview_3(self):
        global view
        view=3
        self.view=view_window()
        self.view.show()
        self.close()
    def goview_4(self):
        global view
        view=4
        self.view=view_window()
        self.view.show()
        self.close()
            
    def goview_5(self):
        global view
        view=5
        self.view=view_window()
        self.view.show()
        self.close()
    def goview_6(self):
        global view
        view=6
        self.view=view_window()
        self.view.show()
        self.close()
    def nextpage(self):
        
        #open work book
        workbook=op.open(data_address)
        #open product worksheet
        product_worksheet=workbook["product"]
        #gain the max_row of column A
        max_row=len(product_worksheet["A"])
        #gain the actual max row
        for i in range(2,max_row):
            if product_worksheet["A"+str(i)].value==None:
                break
            global real_maxrow
            real_maxrow=i
        max_page=math.ceil((real_maxrow-1)/6)
        
        
        #this case is used when the user use the search function
        if value==0:
            global page_1
            page_1=page_1+1
            global times_1
            times_1=times_1+1
            #this is used to find the maximum page of the product
            max_page_1=math.ceil(len(list_1)/6)
            #if the page has already been the last page, go back to the first page
            if page_1>max_page_1:
                page_1=1
                times_1=0
            #display the product
            self.page_1.setText(str(page_1))
            self.image_1.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[0+6*(page_1-1)])].value)))
            self.price_1.setText(str(product_worksheet["F"+str(list_1[0+6*(page_1-1)])].value))
            self.description_1.setText(product_worksheet["C"+str(list_1[0+6*(page_1-1)])].value)
            self.image_2.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[1+6*(page_1-1)])].value)))
            self.price_2.setText(str(product_worksheet["F"+str(list_1[1+6*(page_1-1)])].value))
            self.description_2.setText(product_worksheet["C"+str(list_1[1+6*(page_1-1)])].value)
            self.image_3.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[2+6*(page_1-1)])].value)))
            self.price_3.setText(str(product_worksheet["F"+str(list_1[2+6*(page_1-1)])].value))
            self.description_3.setText(product_worksheet["C"+str(list_1[2+6*(page_1-1)])].value)
            self.image_4.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[3+6*(page_1-1)])].value)))
            self.price_4.setText(str(product_worksheet["F"+str(list_1[3+6*(page_1-1)])].value))
            self.description_4.setText(product_worksheet["C"+str(list_1[3+6*(page_1-1)])].value)
            self.image_5.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[4+6*(page_1-1)])].value)))
            self.price_5.setText(str(product_worksheet["F"+str(list_1[4+6*(page_1-1)])].value))
            self.description_5.setText(product_worksheet["C"+str(list_1[4+6*(page_1-1)])].value)
            self.image_6.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[5+6*(page_1-1)])].value)))
            self.price_6.setText(str(product_worksheet["F"+str(list_1[5+6*(page_1-1)])].value))
            self.description_6.setText(product_worksheet["C"+str(list_1[5+6*(page_1-1)])].value)
            #if there is nothing, hide the frame and the view button
            if self.price_1.text()=="None":
                self.frame.hide()
                self.price_1.clear()
                self.view_1.hide()
            else:
                self.frame.show()
                self.view_1.show()
            if self.price_2.text()=="None":
                self.frame_2.hide()
                self.price_2.clear()
                self.view_2.hide()
            else:
                self.frame_2.show()
                self.view_2.show()
            if self.price_3.text()=="None":
                self.frame_3.hide()
                self.price_3.clear()
                self.view_3.hide()
            else:
                self.frame_3.show()
                self.view_3.show()
            if self.price_4.text()=="None":
                self.frame_4.hide()
                self.price_4.clear()
                self.view_4.hide()
            else:
                self.frame_4.show()
                self.view_4.show()
            if self.price_5.text()=="None":
                self.frame_5.hide()
                self.price_5.clear()
                self.view_5.hide()
            else:
                self.frame_5.show()
                self.view_5.show()
            if self.price_6.text()=="None":
                self.frame_6.hide()
                self.price_6.clear()
                self.view_6.hide()
            else:
                self.frame_6.show()
                self.view_6.show()
           
                
        #this case is used when the user didn't use the search function
        else:
            global page
            page=page+1
            global times
            times=times+1
            if page>max_page:
                page=1
                times=0
            self.page_1.setText(str(page))
            self.image_1.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(2+6*times)].value)))
            self.price_1.setText(str(product_worksheet["F"+str(2+6*times)].value))
            self.description_1.setText(product_worksheet["C"+str(2+6*times)].value)
            self.image_2.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(3+6*times)].value)))
            self.price_2.setText(str(product_worksheet["F"+str(3+6*times)].value))
            self.description_2.setText(product_worksheet["C"+str(3+6*times)].value)
            self.image_3.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(4+6*times)].value)))
            self.price_3.setText(str(product_worksheet["F"+str(4+6*times)].value))
            self.description_3.setText(product_worksheet["C"+str(4+6*times)].value)
            self.image_4.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(5+6*times)].value)))
            self.price_4.setText(str(product_worksheet["F"+str(5+6*times)].value))
            self.description_4.setText(product_worksheet["C"+str(5+6*times)].value)
            self.image_5.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(6+6*times)].value)))
            self.price_5.setText(str(product_worksheet["F"+str(6+6*times)].value))
            self.description_5.setText(product_worksheet["C"+str(6+6*times)].value)
            self.image_6.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(7+6*times)].value)))
            self.price_6.setText(str(product_worksheet["F"+str(7+6*times)].value))
            self.description_6.setText(product_worksheet["C"+str(7+6*times)].value)
            if self.price_1.text()=="None":
                self.frame.hide()
                self.price_1.clear()
                self.view_1.hide()
            else:
                self.frame.show()
                self.view_1.show()
            if self.price_2.text()=="None":
                self.frame_2.hide()
                self.price_2.clear()
                self.view_2.hide()
            else:
                self.frame_2.show()
                self.view_2.show()
            if self.price_3.text()=="None":
                self.frame_3.hide()
                self.price_3.clear()
                self.view_3.hide()
            else:
                self.frame_3.show()
                self.view_3.show()
            if self.price_4.text()=="None":
                self.frame_4.hide()
                self.price_4.clear()
                self.view_4.hide()
            else:
                self.frame_4.show()
                self.view_4.show()
            if self.price_5.text()=="None":
                self.frame_5.hide()
                self.price_5.clear()
                self.view_5.hide()
            else:
                self.frame_5.show()
                self.view_5.show()
            if self.price_6.text()=="None":
                self.frame_6.hide()
                self.price_6.clear()
                self.view_6.hide()
            else:
                self.frame_6.show()
                self.view_6.show()
    def lastpage(self):
        workbook=op.open(data_address)
        product_worksheet=workbook["product"]
        max_row=len(product_worksheet["A"])
        for i in range(2,max_row):
            if product_worksheet["A"+str(i)].value==None:
                break
            global real_maxrow
            real_maxrow=i
        max_page=math.ceil((real_maxrow-1)/6)
        
        if value==0:
            max_page_1=math.ceil(len(list_1)/6)
            global times_1
            # if the page has already been the first page, jump to last page
            if times_1==0:
                times_1=max_page_1-1
            else:
                times_1=times_1-1
            global page_1
            if page_1==1:
                page_1=max_page_1
            else:
                page_1=page_1-1
            #display the product
            self.page_1.setText(str(page_1))
            self.image_1.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[0+6*times_1])].value)))
            self.price_1.setText(str(product_worksheet["F"+str(list_1[0+6*times_1])].value))
            self.description_1.setText(product_worksheet["C"+str(list_1[0+6*times_1])].value)
            self.image_2.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[1+6*times_1])].value)))
            self.price_2.setText(str(product_worksheet["F"+str(list_1[1+6*times_1])].value))
            self.description_2.setText(product_worksheet["C"+str(list_1[1+6*times_1])].value)
            self.image_3.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[2+6*times_1])].value)))
            self.price_3.setText(str(product_worksheet["F"+str(list_1[2+6*times_1])].value))
            self.description_3.setText(product_worksheet["C"+str(list_1[2+6*times_1])].value)
            self.image_4.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[3+6*times_1])].value)))
            self.price_4.setText(str(product_worksheet["F"+str(list_1[3+6*times_1])].value))
            self.description_4.setText(product_worksheet["C"+str(list_1[3+6*times_1])].value)
            self.image_5.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[4+6*times_1])].value)))
            self.price_5.setText(str(product_worksheet["F"+str(list_1[4+6*times_1])].value))
            self.description_5.setText(product_worksheet["C"+str(list_1[4+6*times_1])].value)
            self.image_6.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[5+6*times_1])].value)))
            self.price_6.setText(str(product_worksheet["F"+str(list_1[5+6*times_1])].value))
            self.description_6.setText(product_worksheet["C"+str(list_1[5+6*times_1])].value)
            #if there is nothing, hide the frame and the view button
            if self.price_1.text()=="None":
                self.frame.hide()
                self.price_1.clear()
                self.view_1.hide()
            else:
                self.frame.show()
                self.view_1.show()
            if self.price_2.text()=="None":
                self.frame_2.hide()
                self.price_2.clear()
                self.view_2.hide()
            else:
                self.frame_2.show()
                self.view_2.show()
            if self.price_3.text()=="None":
                self.frame_3.hide()
                self.price_3.clear()
                self.view_3.hide()
            else:
                self.frame_3.show()
                self.view_3.show()
            if self.price_4.text()=="None":
                self.frame_4.hide()
                self.price_4.clear()
                self.view_4.hide()
            else:
                self.frame_4.show()
                self.view_4.show()
            if self.price_5.text()=="None":
                self.frame_5.hide()
                self.price_5.clear()
                self.view_5.hide()
            else:
                self.frame_5.show()
                self.view_5.show()
            if self.price_6.text()=="None":
                self.frame_6.hide()
                self.price_6.clear()
                self.view_6.hide()
            else:
                self.frame_6.show()
                self.view_6.show()
        #this case is used when the user didn't use the search function
        else:
            global times
            if times==0:
                times=max_page-1
            else:
                times=times-1
            global page
            if page==1:
                page=max_page
            else:
                page=page-1
            self.page_1.setText(str(page))  
            self.image_1.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(2+6*times)].value)))
            self.price_1.setText(str(product_worksheet["F"+str(2+6*times)].value))
            self.description_1.setText(product_worksheet["C"+str(2+6*times)].value)
            self.image_2.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(3+6*times)].value)))
            self.price_2.setText(str(product_worksheet["F"+str(3+6*times)].value))
            self.description_2.setText(product_worksheet["C"+str(3+6*times)].value)
            self.image_3.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(4+6*times)].value)))
            self.price_3.setText(str(product_worksheet["F"+str(4+6*times)].value))
            self.description_3.setText(product_worksheet["C"+str(4+6*times)].value)
            self.image_4.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(5+6*times)].value)))
            self.price_4.setText(str(product_worksheet["F"+str(5+6*times)].value))
            self.description_4.setText(product_worksheet["C"+str(5+6*times)].value)
            self.image_5.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(6+6*times)].value)))
            self.price_5.setText(str(product_worksheet["F"+str(6+6*times)].value))
            self.description_5.setText(product_worksheet["C"+str(6+6*times)].value)
            self.image_6.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(7+6*times)].value)))
            self.price_6.setText(str(product_worksheet["F"+str(7+6*times)].value))
            self.description_6.setText(product_worksheet["C"+str(7+6*times)].value)
            if self.price_1.text()=="None":
                self.frame.hide()
                self.price_1.clear()
                self.view_1.hide()
            else:
                self.frame.show()
                self.view_1.show()
            if self.price_2.text()=="None":
                self.frame_2.hide()
                self.price_2.clear()
                self.view_2.hide()
            else:
                self.frame_2.show()
                self.view_2.show()
            if self.price_3.text()=="None":
                self.frame_3.hide()
                self.price_3.clear()
                self.view_3.hide()
            else:
                self.frame_3.show()
                self.view_3.show()
            if self.price_4.text()=="None":
                self.frame_4.hide()
                self.price_4.clear()
                self.view_4.hide()
            else:
                self.frame_4.show()
                self.view_4.show()
            if self.price_5.text()=="None":
                self.frame_5.hide()
                self.price_5.clear()
                self.view_5.hide()
            else:
                self.frame_5.show()
                self.view_5.show()
            if self.price_6.text()=="None":
                self.frame_6.hide()
                self.price_6.clear()
                self.view_6.hide()
            else:
                self.frame_6.show()
                self.view_6.show()
    #this function is used to set the window in the middle of computer screen.
    def center(self):
        screen =  QtWidgets.QDesktopWidget().screenGeometry()
        size  =  self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
#create view window use view ui
class view_window(QMainWindow, view_ui):
    def __init__(self,parent=None):
        super(view_window, self).__init__(parent)
        self.setupUi(self)
        #open workbook
        workbook=op.open(data_address)
        #open product worksheet
        product_worksheet=workbook["product"]
        #gain the size from the excel workbook(list form)
        global size
        size=product_worksheet["E"+str(times*6+view+1)].value.split(',')
        #gain the price from the excel work book(list form)
        global price_1
        price_1=product_worksheet["H"+str(times*6+view+1)].value.split(',')
        #add the size to the comboBox
        self.size_comboBox.addItems(size)
        #set the range of spinBox
        self.quantity_spinBox.setRange(1,9)
        #set the botany logo
        self.botany_logo.setPixmap(QtGui.QPixmap(file_address+"/image/a03.png"))
        #this case is that if the user use search function, use list_1 to display the product
        if value==0:
            self.image.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(list_1[view-1+6*times_1])].value)))
            self.price.setText(str(product_worksheet["F"+str(list_1[view-1+6*times_1])].value))
            self.product_name.setText(product_worksheet["C"+str(list_1[view-1+6*times_1])].value)
            self.description.setText(product_worksheet["G"+str(list_1[view-1+6*times_1])].value)
        #this case is that if the user didn't use search function
        else:
            self.image.setPixmap(QtGui.QPixmap(file_address+"/image/"+str(product_worksheet["A"+str(times*6+view+1)].value)))
            self.price.setText(str(product_worksheet["F"+str(times*6+view+1)].value))
            self.product_name.setText(product_worksheet["C"+str(times*6+view+1)].value)
            self.description.setText(product_worksheet["G"+str(times*6+view+1)].value)
        #once the user click back button, it will connect the back function
        self.back_1.clicked.connect(self.back)
        self.next_1.clicked.connect(self.gopay)
    def gopay(self):
        
            
        #gian the current text of the comboBox            
        global size_1
        size_1=self.size_comboBox.currentText()
        #gian the actual price by using the index
        global actual_price
        actual_price=price_1[(size.index(size_1))]
        global quantity
        #gain the spinbox value as the quantity
        quantity=self.quantity_spinBox.value()
        #show the pay window
        self.pay=pay_window()
        self.pay.show()
        self.close()
        
    def back(self):
        #back to the shop window
        self.interface=interface_window()
        self.interface.show()
        self.close()
# create the pay window (use the pay_ui)
class pay_window(QMainWindow, pay_ui):
    def __init__(self,parent=None):
        super(pay_window, self).__init__(parent)
        self.setupUi(self)
        #set the botany logo
        self.botany_logo.setPixmap(QtGui.QPixmap(file_address+"/image/a03.png"))
        #display the unitprice
        self.unitprice_display.setText(actual_price)
        self.size_display.setText(size_1)
        self.quantity_display.setText(str(quantity))
        self.totalprice_display_2.setText(str(int(actual_price)*int(quantity)))
        #open the workbook
        workbook=op.open(data_address)
        #open the student worksheet
        student_worksheet=workbook["student"]
        product_worksheet=workbook["product"]

        # this case is that if the user use search function
        if value==0:
            self.productname_display.setText(product_worksheet["C"+str(list_1[view-1+6*times_1])].value)
        else:
            self.productname_display.setText(product_worksheet["C"+str(times*6+view+1)].value)
        #display the student_id and etc
        self.studentid_display.setText(student_worksheet["A"+str(row)].value)
        self.studentname_display.setText(student_worksheet["E"+str(row)].value.capitalize()+" "+student_worksheet["D"+str(row)].value.capitalize())
        self.add_cart_1.clicked.connect(self.add_cart)
        self.pay_1.clicked.connect(self.pay)
        self.cancel_1.clicked.connect(self.cancel)
    def cancel(self):
        #back to the view window
        self.view=view_window()
        self.view.show()
        self.close()
    def pay(self):
        # take down the student id from the label and open the confirm window
        global student_id_paid
        student_id_paid=self.studentid_display.text()
        global Name_paid
        Name_paid=self.productname_display.text()
        global unit_price_paid
        unit_price_paid=self.unitprice_display.text()
        global Quantity_paid
        Quantity_paid=self.quantity_display.text()
        global size_paid
        size_paid=self.size_display.text()
        global confirm
        confirm="Pay"
        self.confirm=confirm_window()
        self.confirm.show()
        self.close()
    def add_cart(self):
        #open workbook
        workbook=op.open(data_address)
        #choose order detail worksheet
        orderdetail_worksheet=workbook["orderdetail"]
        #choose product worksheet
        product_worksheet=workbook["product"]
        #gain the max row of the column C in orderdetail worksheet
        max_row=len(orderdetail_worksheet["C"])
        for i in range(2,max_row):
            if orderdetail_worksheet["C"+str(i)].value==None:
                global real_maxrow
                real_maxrow=i
                break
        real_maxrow=i
        #store the data in the order detail worksheet
        orderdetail_worksheet["B"+str(real_maxrow)].value=self.studentid_display.text()
        orderdetail_worksheet["C"+str(real_maxrow)].value=self.productname_display.text()
        orderdetail_worksheet["D"+str(real_maxrow)].value=self.unitprice_display.text()
        orderdetail_worksheet["E"+str(real_maxrow)].value=self.quantity_display.text()
        orderdetail_worksheet["F"+str(real_maxrow)].value=self.size_display.text()
        orderdetail_worksheet["H"+str(real_maxrow)].value=str("Cart")
        total_size=""
        for i in range(0,len(size)):
            if i==0:
                total_size=size[i]
            else:
                total_size=size[i]+","+total_size
        orderdetail_worksheet["K"+str(real_maxrow)].value=total_size
        #this case is that the user use search function
        if value==0:
            orderdetail_worksheet["I"+str(real_maxrow)].value=product_worksheet["A"+str(list_1[view-1+6*times_1])].value
            orderdetail_worksheet["J"+str(real_maxrow)].value=product_worksheet["G"+str(list_1[view-1+6*times_1])].value
        else:
            orderdetail_worksheet["I"+str(real_maxrow)].value=product_worksheet["A"+str(times*6+view+1)].value
            orderdetail_worksheet["J"+str(real_maxrow)].value=product_worksheet["G"+str(times*6+view+1)].value
        #save changes to excel
        workbook.save(data_address)
        self.csign=csign_window()
        self.csign.show()
        self.close()
#create paid_window use paid ui
class paid_window(QMainWindow, paid_ui):
    def __init__(self,parent=None):
        super(paid_window, self).__init__(parent)
        self.setupUi(self)
        #open work book
        workbook=op.open(data_address)
        #choose student worksheet
        student_worksheet=workbook["student"]
        #gain the student_id from the worksheet
        student_id=student_worksheet["A"+str(row)].value
        #gain the name from the worksheet
        name=student_worksheet["E"+str(row)].value.capitalize()+" "+student_worksheet["D"+str(row)].value.capitalize()
        #display the student id and name
        self.studentid_display.setText("Student ID: {}".format(student_id))
        self.name_display.setText("Name: {}".format(name))
        #calulate the total price and account_balance
        total_price=int(unit_price_paid)*int(Quantity_paid)
        account_balance=int(student_worksheet["G"+str(row)].value)-int(total_price)
        #store the account balance in the student worksheet
        student_worksheet["G"+str(row)].value=account_balance
        #save changes to workbook
        workbook.save(data_address)
        #set the botany logo
        self.botany_logo.setPixmap(QtGui.QPixmap(file_address+"/image/a03.png"))
        #display the total price and account balance
        self.totalprice_display.setText("Total price: {}".format(str(total_price)))
        self.accountbalance_display.setText("Account_balance: {}".format(str(account_balance)))
        #once the user click shop, it will connect the back_shop function
        self.go_shop.clicked.connect(self.back_shop)
        self.back_profile_1.clicked.connect(self.back_profile)
    #the user will jump to the shop window
    def back_shop(self):
        self.intetface=interface_window()
        self.intetface.show()
        self.close()
    def back_profile(self):
        self.profile=profile_window()
        self.profile.show()
        self.close()
        
        
        
############################################# below is the pop up  #########################################################################        
class no_result_window(QMainWindow, no_result_ui):
    def __init__(self,parent=None):
        super(no_result_window, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.back) 
    def back(self):
        self.close()     

class confirm_window(QMainWindow, confirm_ui):
    def __init__(self,parent=None):
        super(confirm_window, self).__init__(parent)
        self.setupUi(self)    
        if confirm=="Pay":
            self.pushButton_3.clicked.connect(self.pay)
            self.pushButton_2.clicked.connect(self.back)
        elif confirm=="Cart":
            self.pushButton_3.clicked.connect(self.cpay)
            self.pushButton_2.clicked.connect(self.back_2)
        
    def cpay(self):
        wb=op.open(data_address)
        ws1=wb["student"]
        ws2=wb["orderdetail"]
        max_row=len(ws2["A"])
        student_id=ws1["A"+str(row)].value
        account_balance=ws1["G"+str(row)].value
        total=0
        for a in range(2,max_row):
            if ws2["B"+str(a)].value==student_id and ws2["H"+str(a)].value=="Cart":
                total=total+int(ws2["D"+str(a)].value)*int(ws2["E"+str(a)].value)
        if account_balance>=total:
            self.cpay=cpay_window()
            self.cpay.show()
            self.close()
        else: 
            global error
            error="Cart"
            self.error=error_window()
            self.error.show()
            self.close()
    def back(self):
        self.pay=pay_window()
        self.pay.show()
        self.close()
    def back_2(self):
        self.cart=cart_window()
        self.cart.show()
        self.close()
    def pay(self):
        wb=op.open(data_address)
        ws1=wb["orderdetail"]
        ws2=wb["product"]
        ws3=wb["student"]
        student_id=ws3["A"+str(row)].value
        account_balance=ws3["G"+str(row)].value
        total=int(unit_price_paid)*int(Quantity_paid)
        if account_balance>=total:
            max_row=len(ws1["C"])
            for i in range(2,max_row):
                if ws1["C"+str(i)].value==None:
                    global real_maxrow
                    real_maxrow=i
                    break
            real_maxrow=i
            ws1["B"+str(real_maxrow)].value=student_id_paid
            ws1["C"+str(real_maxrow)].value=Name_paid
            ws1["D"+str(real_maxrow)].value=unit_price_paid
            ws1["E"+str(real_maxrow)].value=Quantity_paid
            ws1["F"+str(real_maxrow)].value=size_paid
            ws1["G"+str(real_maxrow)].value=str(int(unit_price_paid)*int(Quantity_paid))
            ws1["H"+str(real_maxrow)].value=str("Paid")
            if value==0:
                ws1["I"+str(real_maxrow)].value=ws2["A"+str(list_1[view-1+6*times_1])].value
                ws1["J"+str(real_maxrow)].value=ws2["G"+str(list_1[view-1+6*times_1])].value
            else:
                ws1["I"+str(real_maxrow)].value=ws2["A"+str(times*6+view+1)].value
                ws1["J"+str(real_maxrow)].value=ws2["G"+str(times*6+view+1)].value
            wb.save(data_address)
            self.paid=paid_window()
            self.paid.show()
            self.close()
        else:
            global error
            error="Paid"
            self.error=error_window()
            self.error.show()
            self.close()

class csign_window(QMainWindow, csign_ui):
    def __init__(self,parent=None):
        super(csign_window, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.back)
    def back(self):
        self.interface=interface_window()
        self.interface.show()
        self.close()
class sign_window(QMainWindow, sign_ui):
    def __init__(self,parent=None):
        super(sign_window, self).__init__(parent)
        
        self.setupUi(self)
        self.pushButton.clicked.connect(self.backlogin)
    def backlogin(self):
        self.loginwindow=Login_window()
        self.loginwindow.show()
        self.close()
class sign2_window(QMainWindow, sign_2ui):
    def __init__(self,parent=None):
        super(sign2_window, self).__init__(parent)
        
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.backlogin)
    def backlogin(self):
        self.loginwindow=Login_window()
        self.loginwindow.show()
        self.close()
class error_window(QMainWindow, error_ui):
    def __init__(self,parent=None):
        super(error_window, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.back)
    def back(self):
        if error=="Paid":
            self.pay=pay_window()
            self.pay.show()
            self.close()
        elif error=="Cart":
            self.buy=cart_window()
            self.buy.show()
            self.close()

if __name__ =="__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    QtGui.QGuiApplication.setAttribute(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app=QApplication(sys.argv)
    myWin= Login_window()
    myWin.show()
    sys.exit(app.exec_())

