# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TC_TestBench_TM_Only.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 705)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 0, 129, 634))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.currspdin = QtWidgets.QSpinBox(self.layoutWidget)
        self.currspdin.setObjectName("currspdin")
        self.verticalLayout_2.addWidget(self.currspdin)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.cmdspdin = QtWidgets.QSpinBox(self.layoutWidget)
        self.cmdspdin.setObjectName("cmdspdin")
        self.verticalLayout_2.addWidget(self.cmdspdin)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.spdlimin = QtWidgets.QSpinBox(self.layoutWidget)
        self.spdlimin.setObjectName("spdlimin")
        self.verticalLayout_2.addWidget(self.spdlimin)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.spinBox_3 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_3.setObjectName("spinBox_3")
        self.verticalLayout_2.addWidget(self.spinBox_3)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox.setMaximum(9999)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_2.addWidget(self.spinBox)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.ebrakein = QtWidgets.QRadioButton(self.layoutWidget)
        self.ebrakein.setObjectName("ebrakein")
        self.verticalLayout_2.addWidget(self.ebrakein)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.beaconin = QtWidgets.QLineEdit(self.layoutWidget)
        self.beaconin.setObjectName("beaconin")
        self.verticalLayout_2.addWidget(self.beaconin)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.currtempin = QtWidgets.QSpinBox(self.layoutWidget)
        self.currtempin.setObjectName("currtempin")
        self.verticalLayout_2.addWidget(self.currtempin)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.underground = QtWidgets.QRadioButton(self.layoutWidget)
        self.underground.setObjectName("underground")
        self.verticalLayout_2.addWidget(self.underground)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.pwrfailin = QtWidgets.QRadioButton(self.layoutWidget)
        self.pwrfailin.setObjectName("pwrfailin")
        self.verticalLayout_2.addWidget(self.pwrfailin)
        self.brkfail = QtWidgets.QRadioButton(self.layoutWidget)
        self.brkfail.setObjectName("brkfail")
        self.verticalLayout_2.addWidget(self.brkfail)
        self.sigfail = QtWidgets.QRadioButton(self.layoutWidget)
        self.sigfail.setObjectName("sigfail")
        self.verticalLayout_2.addWidget(self.sigfail)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(490, 60, 111, 449))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pow_out = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.pow_out.setObjectName("pow_out")
        self.verticalLayout.addWidget(self.pow_out)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.door_out = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.door_out.setObjectName("door_out")
        self.verticalLayout.addWidget(self.door_out)
        self.ExtLight = QtWidgets.QLabel(self.layoutWidget1)
        self.ExtLight.setObjectName("ExtLight")
        self.verticalLayout.addWidget(self.ExtLight)
        self.lcdNumber = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)
        self.InteriorLight = QtWidgets.QLabel(self.layoutWidget1)
        self.InteriorLight.setObjectName("InteriorLight")
        self.verticalLayout.addWidget(self.InteriorLight)
        self.int_light = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.int_light.setObjectName("int_light")
        self.verticalLayout.addWidget(self.int_light)
        self.Desired_Temp = QtWidgets.QLabel(self.layoutWidget1)
        self.Desired_Temp.setObjectName("Desired_Temp")
        self.verticalLayout.addWidget(self.Desired_Temp)
        self.des_temp = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.des_temp.setObjectName("des_temp")
        self.verticalLayout.addWidget(self.des_temp)
        self.DisableEbrake = QtWidgets.QLabel(self.layoutWidget1)
        self.DisableEbrake.setObjectName("DisableEbrake")
        self.verticalLayout.addWidget(self.DisableEbrake)
        self.EbrakeStat = QtWidgets.QCheckBox(self.layoutWidget1)
        self.EbrakeStat.setCheckable(True)
        self.EbrakeStat.setObjectName("EbrakeStat")
        self.verticalLayout.addWidget(self.EbrakeStat)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.Anon_Out = QtWidgets.QLabel(self.layoutWidget1)
        self.Anon_Out.setObjectName("Anon_Out")
        self.verticalLayout.addWidget(self.Anon_Out)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.brakeen = QtWidgets.QRadioButton(self.layoutWidget1)
        self.brakeen.setObjectName("brakeen")
        self.verticalLayout.addWidget(self.brakeen)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "From Train Controller"))
        self.label_17.setText(_translate("MainWindow", "Curr Spd"))
        self.label_4.setText(_translate("MainWindow", "CMD SPEED"))
        self.label_5.setText(_translate("MainWindow", "SPEED LIM"))
        self.label_7.setText(_translate("MainWindow", "SPEED LIM"))
        self.label_15.setText(_translate("MainWindow", "Authority"))
        self.label_8.setText(_translate("MainWindow", "Pass Ebrake"))
        self.ebrakein.setText(_translate("MainWindow", "RadioButton"))
        self.label_9.setText(_translate("MainWindow", "Beacon"))
        self.label_14.setText(_translate("MainWindow", "Curr Temp"))
        self.label_10.setText(_translate("MainWindow", "Underground"))
        self.underground.setText(_translate("MainWindow", "underground"))
        self.label_11.setText(_translate("MainWindow", "Failures "))
        self.pwrfailin.setText(_translate("MainWindow", "pwrfail"))
        self.brkfail.setText(_translate("MainWindow", "brkfail"))
        self.sigfail.setText(_translate("MainWindow", "sigfail"))
        self.label_12.setText(_translate("MainWindow", "Block Passed"))
        self.radioButton_3.setText(_translate("MainWindow", "blockpassed"))
        self.label_2.setText(_translate("MainWindow", "To Train Controller"))
        self.label.setText(_translate("MainWindow", "Power"))
        self.label_13.setText(_translate("MainWindow", "Door"))
        self.ExtLight.setText(_translate("MainWindow", "Ext Light"))
        self.InteriorLight.setText(_translate("MainWindow", "Interior Light"))
        self.Desired_Temp.setText(_translate("MainWindow", "Desired Temp"))
        self.DisableEbrake.setText(_translate("MainWindow", "Disable Ebrake"))
        self.EbrakeStat.setText(_translate("MainWindow", "Ebrake On"))
        self.label_6.setText(_translate("MainWindow", "Annoucement "))
        self.Anon_Out.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "Service Brake"))
        self.brakeen.setText(_translate("MainWindow", "enabled"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
