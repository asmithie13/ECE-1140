# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TrainModel_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1541, 471)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color: rgb(255, 219, 156);\n"
"background-color: rgb(255, 220, 149);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 350, 711, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setStyleSheet("background-color: rgb(195, 16, 40);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(400, 0, 311, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(560, 40, 151, 191))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Lengthofvehicle_lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget_3)
        self.Lengthofvehicle_lcd.setObjectName("Lengthofvehicle_lcd")
        self.verticalLayout_3.addWidget(self.Lengthofvehicle_lcd)
        self.Height_lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget_3)
        self.Height_lcd.setObjectName("Height_lcd")
        self.verticalLayout_3.addWidget(self.Height_lcd)
        self.Width_lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget_3)
        self.Width_lcd.setObjectName("Width_lcd")
        self.verticalLayout_3.addWidget(self.Width_lcd)
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.verticalLayoutWidget_3)
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.verticalLayout_3.addWidget(self.lcdNumber_6)
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.verticalLayoutWidget_3)
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.verticalLayout_3.addWidget(self.lcdNumber_7)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.verticalLayoutWidget_3)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.verticalLayout_3.addWidget(self.lcdNumber_3)
        self.lcdNumber = QtWidgets.QLCDNumber(self.verticalLayoutWidget_3)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_3.addWidget(self.lcdNumber)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(400, 40, 161, 191))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 161, 191))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.verticalLayoutWidget_4.setFont(font)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.LengthVehicle_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.LengthVehicle_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.LengthVehicle_label.setFont(font)
        self.LengthVehicle_label.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.LengthVehicle_label.setFrameShape(QtWidgets.QFrame.Box)
        self.LengthVehicle_label.setAlignment(QtCore.Qt.AlignCenter)
        self.LengthVehicle_label.setObjectName("LengthVehicle_label")
        self.verticalLayout_4.addWidget(self.LengthVehicle_label)
        self.LengthVehicle_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.LengthVehicle_label_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.LengthVehicle_label_2.setFont(font)
        self.LengthVehicle_label_2.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.LengthVehicle_label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.LengthVehicle_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.LengthVehicle_label_2.setObjectName("LengthVehicle_label_2")
        self.verticalLayout_4.addWidget(self.LengthVehicle_label_2)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(0, 0, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 50, 271, 181))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.label_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.label_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.label_10.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(270, 50, 121, 181))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.verticalLayoutWidget_5)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.verticalLayout_6.addWidget(self.lcdNumber_4)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.verticalLayoutWidget_5)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout_6.addWidget(self.lcdNumber_2)
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.verticalLayoutWidget_5)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.verticalLayout_6.addWidget(self.lcdNumber_5)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 230, 711, 56))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(195, 16, 40);\n"
"")
        self.label_11.setFrameShape(QtWidgets.QFrame.Box)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.buttonBox_3 = QtWidgets.QDialogButtonBox(self.horizontalLayoutWidget)
        self.buttonBox_3.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_3.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox_3.setCenterButtons(True)
        self.buttonBox_3.setObjectName("buttonBox_3")
        self.horizontalLayout.addWidget(self.buttonBox_3)
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(195, 16, 40);\n"
"")
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.buttonBox_4 = QtWidgets.QDialogButtonBox(self.horizontalLayoutWidget)
        self.buttonBox_4.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox_4.setCenterButtons(True)
        self.buttonBox_4.setObjectName("buttonBox_4")
        self.horizontalLayout.addWidget(self.buttonBox_4)
        self.line_3 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(195, 16, 40);")
        self.label_13.setFrameShape(QtWidgets.QFrame.Box)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.label_13)
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.horizontalLayoutWidget)
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox_2.setCenterButtons(True)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.horizontalLayout.addWidget(self.buttonBox_2)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 290, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.verticalLayoutWidget_6.setFont(font)
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setFrameShape(QtWidgets.QFrame.Box)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_7.addWidget(self.label_15)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setFrameShape(QtWidgets.QFrame.Box)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_7.addWidget(self.label_14)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(110, 290, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.verticalLayoutWidget_7.setFont(font)
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.label_18.setFrameShape(QtWidgets.QFrame.Box)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_8.addWidget(self.label_18)
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.label_26.setFrameShape(QtWidgets.QFrame.Box)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_8.addWidget(self.label_26)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(240, 290, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.verticalLayoutWidget_8.setFont(font)
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setFrameShape(QtWidgets.QFrame.Box)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_9.addWidget(self.label_21)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setFrameShape(QtWidgets.QFrame.Box)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_9.addWidget(self.label_20)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(370, 290, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.verticalLayoutWidget_9.setFont(font)
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.label_19.setFrameShape(QtWidgets.QFrame.Box)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_10.addWidget(self.label_19)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.label_22.setFrameShape(QtWidgets.QFrame.Box)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_10.addWidget(self.label_22)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(490, 290, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.horizontalLayoutWidget_2.setFont(font)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_25 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setFrameShape(QtWidgets.QFrame.Box)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_2.addWidget(self.label_25)
        self.label_24 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.label_24.setFrameShape(QtWidgets.QFrame.Box)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_2.addWidget(self.label_24)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(212, 290, 21, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.line_4.setFont(font)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(480, 290, 3, 54))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.line_5.setFont(font)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(150, 30, 251, 21))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_3.addWidget(self.label_17)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 30, 141, 21))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_23 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_4.addWidget(self.label_23)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(719, -1, 181, 391))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_16.setStyleSheet("background-color: rgb(162, 162, 162);")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("bk_ad.png"))
        self.label_16.setObjectName("label_16")
        self.verticalLayout_11.addWidget(self.label_16)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#141414;\">EMERGENCY STOP</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Live Train Statistics"))
        self.groupBox.setStyleSheet(_translate("MainWindow", "background-color: rgb(197, 197, 197);"))
        self.verticalLayoutWidget_4.setStyleSheet(_translate("MainWindow", "background-color: rgb(197, 197, 197);"))
        self.LengthVehicle_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Length of Vehicle (feet)</span></p></body></html>"))
        self.LengthVehicle_label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Height (feet)</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Width (feet)</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Grade (%)</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Car Weight Loaded (lbs)</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Passenger Count</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Crew Count</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Train 1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Train 2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Train 3"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Power (Watts)</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Acceleration (mph</span><span style=\" font-size:11pt; vertical-align:super;\">2</span><span style=\" font-size:11pt;\">)</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Actual Velocity (mph)</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Brake Failure</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt;\">Signal Pickup </span></p><p><span style=\" font-size:8pt; color:#c11028;\">abc</span><span style=\" font-size:8pt;\">Failure</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt;\">Engine Failure</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:6pt;\">Interior Lights</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:6pt;\">Exterior Lights</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#464646;\">ON</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#464646;\">ON</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt;\">Right Door</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt;\">Left Door</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#3f3f3f;\">CLOSE</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#464646;\">CLOSE</span></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "Cabin Temperature"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">68 F</p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "blah blah blah blah blah blah blah blah blah blah"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:6pt; font-weight:600;\">Announcements:</span></p></body></html>"))
