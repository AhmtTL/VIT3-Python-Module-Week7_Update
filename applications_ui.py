# Form implementation generated from reading ui file 'applications_ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FormApplications(object):
    def setupUi(self, FormApplications):
        FormApplications.setObjectName("FormApplications")
        FormApplications.resize(1080, 680)
        FormApplications.setMinimumSize(QtCore.QSize(1080, 680))
        FormApplications.setMaximumSize(QtCore.QSize(1080, 680))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pictures/wehere_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        FormApplications.setWindowIcon(icon)
        FormApplications.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.489, y1:1, x2:0.494, y2:0, stop:0 rgba(71, 71, 71, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_app_all_app = QtWidgets.QPushButton(parent=FormApplications)
        self.pushButton_app_all_app.setGeometry(QtCore.QRect(40, 210, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_app_all_app.setFont(font)
        self.pushButton_app_all_app.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"    border: 2px solid rgb(162, 0, 0);\n"
"}")
        self.pushButton_app_all_app.setObjectName("pushButton_app_all_app")
        self.label = QtWidgets.QLabel(parent=FormApplications)
        self.label.setGeometry(QtCore.QRect(270, 22, 261, 101))
        self.label.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pictures/werhere_logo.ico"))
        self.label.setObjectName("label")
        self.pushButton_app_planned_mentor = QtWidgets.QPushButton(parent=FormApplications)
        self.pushButton_app_planned_mentor.setGeometry(QtCore.QRect(40, 260, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_app_planned_mentor.setFont(font)
        self.pushButton_app_planned_mentor.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"    border: 2px solid rgb(162, 0, 0);\n"
"}")
        self.pushButton_app_planned_mentor.setObjectName("pushButton_app_planned_mentor")
        self.pushButton_app_unscheduled_meeting = QtWidgets.QPushButton(parent=FormApplications)
        self.pushButton_app_unscheduled_meeting.setGeometry(QtCore.QRect(40, 310, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_app_unscheduled_meeting.setFont(font)
        self.pushButton_app_unscheduled_meeting.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"    border: 2px solid rgb(162, 0, 0);\n"
"}")
        self.pushButton_app_unscheduled_meeting.setObjectName("pushButton_app_unscheduled_meeting")
        self.pushButton_app_pre_vit_control = QtWidgets.QPushButton(parent=FormApplications)
        self.pushButton_app_pre_vit_control.setGeometry(QtCore.QRect(40, 360, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_app_pre_vit_control.setFont(font)
        self.pushButton_app_pre_vit_control.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
" border: 2px solid rgb(162, 0, 0);\n"
"}")
        self.pushButton_app_pre_vit_control.setObjectName("pushButton_app_pre_vit_control")
        self.pushButton_app_rep_registrations = QtWidgets.QPushButton(parent=FormApplications)
        self.pushButton_app_rep_registrations.setGeometry(QtCore.QRect(40, 410, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_app_rep_registrations.setFont(font)
        self.pushButton_app_rep_registrations.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
" border: 2px solid rgb(162, 0, 0);\n"
"}")
        self.pushButton_app_rep_registrations.setObjectName("pushButton_app_rep_registrations")
        self.pushButton_diff_registration = QtWidgets.QPushButton(parent=FormApplications)
        self.pushButton_diff_registration.setGeometry(QtCore.QRect(40, 460, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_diff_registration.setFont(font)
        self.pushButton_diff_registration.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
" border: 2px solid rgb(162, 0, 0);\n"
"}")
        self.pushButton_diff_registration.setObjectName("pushButton_diff_registration")
        self.pushButton_app_back_menu = QtWidgets.QPushButton(parent=FormApplications)
        self.pushButton_app_back_menu.setGeometry(QtCore.QRect(40, 560, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_app_back_menu.setFont(font)
        self.pushButton_app_back_menu.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
" border: 2px solid rgb(162, 0, 0);\n"
"}")
        self.pushButton_app_back_menu.setObjectName("pushButton_app_back_menu")
        self.pushButton_app_filter_app = QtWidgets.QPushButton(parent=FormApplications)
        self.pushButton_app_filter_app.setGeometry(QtCore.QRect(40, 510, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_app_filter_app.setFont(font)
        self.pushButton_app_filter_app.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
" border: 2px solid rgb(162, 0, 0);\n"
"}")
        self.pushButton_app_filter_app.setObjectName("pushButton_app_filter_app")
        self.pushButton_app_exit = QtWidgets.QPushButton(parent=FormApplications)
        self.pushButton_app_exit.setGeometry(QtCore.QRect(40, 610, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_app_exit.setFont(font)
        self.pushButton_app_exit.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"    border: 2px solid rgb(162, 0, 0);\n"
"}")
        self.pushButton_app_exit.setObjectName("pushButton_app_exit")
        self.pushButton_app_search = QtWidgets.QPushButton(parent=FormApplications)
        self.pushButton_app_search.setGeometry(QtCore.QRect(40, 170, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_app_search.setFont(font)
        self.pushButton_app_search.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"    border: 2px solid rgb(162, 0, 0);\n"
"}")
        self.pushButton_app_search.setObjectName("pushButton_app_search")
        self.tableWidget_app = QtWidgets.QTableWidget(parent=FormApplications)
        self.tableWidget_app.setGeometry(QtCore.QRect(250, 130, 801, 521))
        self.tableWidget_app.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.tableWidget_app.setObjectName("tableWidget_app")
        self.tableWidget_app.setColumnCount(8)
        self.tableWidget_app.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(7, item)
        self.lineEdit_app_username = QtWidgets.QLineEdit(parent=FormApplications)
        self.lineEdit_app_username.setEnabled(True)
        self.lineEdit_app_username.setGeometry(QtCore.QRect(40, 130, 171, 31))
        self.lineEdit_app_username.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.lineEdit_app_username.setStyleSheet("QLineEdit {\n"
"  border: 2px solid rgb(38, 38, 48);\n"
"  border-radius: 15px;\n"
"  color: #FFF;\n"
"  padding-left: 15px;\n"
"  background-color: rgba(0, 0, 0,55%);\n"
" \n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"\n"
" QLineEdit:focus  {\n"
"  border: 2px solid rgb(35, 218, 233);\n"
"  background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"   \n"
"\n"
"\n"
"\n"
"")
        self.lineEdit_app_username.setText("")
        self.lineEdit_app_username.setObjectName("lineEdit_app_username")
        self.label_2 = QtWidgets.QLabel(parent=FormApplications)
        self.label_2.setGeometry(QtCore.QRect(530, 50, 491, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"color: rgb(71, 84, 88);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=FormApplications)
        self.label_3.setGeometry(QtCore.QRect(8, 10, 231, 121))
        self.label_3.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("pictures/project_app.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(FormApplications)
        QtCore.QMetaObject.connectSlotsByName(FormApplications)
        FormApplications.setTabOrder(self.lineEdit_app_username, self.pushButton_app_search)
        FormApplications.setTabOrder(self.pushButton_app_search, self.pushButton_app_all_app)
        FormApplications.setTabOrder(self.pushButton_app_all_app, self.pushButton_app_planned_mentor)
        FormApplications.setTabOrder(self.pushButton_app_planned_mentor, self.pushButton_app_unscheduled_meeting)
        FormApplications.setTabOrder(self.pushButton_app_unscheduled_meeting, self.pushButton_app_pre_vit_control)
        FormApplications.setTabOrder(self.pushButton_app_pre_vit_control, self.pushButton_app_rep_registrations)
        FormApplications.setTabOrder(self.pushButton_app_rep_registrations, self.pushButton_diff_registration)
        FormApplications.setTabOrder(self.pushButton_diff_registration, self.pushButton_app_filter_app)
        FormApplications.setTabOrder(self.pushButton_app_filter_app, self.tableWidget_app)
        FormApplications.setTabOrder(self.tableWidget_app, self.pushButton_app_back_menu)
        FormApplications.setTabOrder(self.pushButton_app_back_menu, self.pushButton_app_exit)

    def retranslateUi(self, FormApplications):
        _translate = QtCore.QCoreApplication.translate
        FormApplications.setWindowTitle(_translate("FormApplications", "APPLICATION"))
        self.pushButton_app_all_app.setText(_translate("FormApplications", "All Applications"))
        self.pushButton_app_planned_mentor.setText(_translate("FormApplications", "Planned Mentor Meetings"))
        self.pushButton_app_unscheduled_meeting.setText(_translate("FormApplications", "Unscheduled M. Meetings"))
        self.pushButton_app_pre_vit_control.setText(_translate("FormApplications", "Previous VIT Control"))
        self.pushButton_app_rep_registrations.setText(_translate("FormApplications", "Repeated Registration"))
        self.pushButton_diff_registration.setText(_translate("FormApplications", "Different Registration"))
        self.pushButton_app_back_menu.setText(_translate("FormApplications", "Back Menu"))
        self.pushButton_app_filter_app.setText(_translate("FormApplications", "Filter Application"))
        self.pushButton_app_exit.setText(_translate("FormApplications", "Exit"))
        self.pushButton_app_search.setText(_translate("FormApplications", "Search"))
        item = self.tableWidget_app.horizontalHeaderItem(0)
        item.setText(_translate("FormApplications", "Date"))
        item = self.tableWidget_app.horizontalHeaderItem(1)
        item.setText(_translate("FormApplications", "Name Surname"))
        item = self.tableWidget_app.horizontalHeaderItem(2)
        item.setText(_translate("FormApplications", "Mail"))
        item = self.tableWidget_app.horizontalHeaderItem(3)
        item.setText(_translate("FormApplications", "Telephone"))
        item = self.tableWidget_app.horizontalHeaderItem(4)
        item.setText(_translate("FormApplications", "Post Code"))
        item = self.tableWidget_app.horizontalHeaderItem(5)
        item.setText(_translate("FormApplications", "State"))
        item = self.tableWidget_app.horizontalHeaderItem(6)
        item.setText(_translate("FormApplications", "Status"))
        item = self.tableWidget_app.horizontalHeaderItem(7)
        item.setText(_translate("FormApplications", "Economical \n"
"Situation"))
        self.lineEdit_app_username.setPlaceholderText(_translate("FormApplications", "      Name or Surname"))
        self.label_2.setText(_translate("FormApplications", "PROJECT APPLICATIONS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormApplications = QtWidgets.QWidget()
    ui = Ui_FormApplications()
    ui.setupUi(FormApplications)
    FormApplications.show()
    sys.exit(app.exec())
