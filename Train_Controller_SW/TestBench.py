
from PyQt5 import QtCore, QtGui, QtWidgets
from TrainController import *
from TC_TestBench_TM_Only import *

class Ui_TestBench(object):

    def __init__(self):
        self.TC = TrainController()

    def sig_connect(self):
        #signals we send out
        self.TC.announcement_sig.connect(self.Anon_Out.setText)
        self.TC.temp_control_sig.connect(self.des_temp.display)
        self.TC.int_light_sig.connect(self.int_light.display)
        self.TC.door_control_sig.connect(self.door_out.display)
        self.TC.ext_light_sig.connect(self.lcdNumber.display)
        self.TC.curr_power_sig.connect(self.pow_out.display)
        #this needs some work
        self.TC.ebrake_disable_sig.connect(self.EbrakeStat.setDown)
        self.TC.service_brake_sig.connect(self.brakeen.setDown)

        #signals we recieve
        self.currspdin.editingFinished.connect(lambda : self.Cur_Spd_Emit())
        self.cmdspdin.editingFinished.connect(lambda : self.Com_Spd_Emit())
        self.spdlimin.editingFinished.connect(lambda : self.Spd_Lim_Emit())
        self.spinBox.editingFinished.connect(lambda : self.Auth_Emit())
        self.ebrakein.toggled.connect(lambda : self.Pass_E_Emit())
        self.beaconin.editingFinished.connect(lambda : self.Beacon_Emit())
        self.underground.toggled.connect(lambda : self.Underground_Emit())
        self.pwrfailin.toggled.connect(lambda : self.Pwr_Fail_Emit())
        self.brkfail.toggled.connect(lambda : self.Brk_Fail_Emit())
        self.sigfail.toggled.connect(lambda : self.Sig_Fail_Emit())
        self.blockpass.toggled.connect(lambda : self.Block_Paseed_Emit())
        self.currtempin.valueChanged.connect(lambda : self.Temp_Emit())
        self.boolauth.toggled.connect(lambda : self.Bool_Auth_Emit())

    def Bool_Auth_Emit(self):
        if self.boolauth.isChecked() :
            self.TC.curr_bool_auth_sig.emit(1)
        else :
            self.TC.curr_bool_auth_sig.emit(0)
    def Cur_Spd_Emit(self):
        self.TC.curr_spd_sig.emit(self.currspdin.value())
    def Com_Spd_Emit(self):
        self.TC.curr_cmd_spd_sig.emit(self.cmdspdin.value())
    def Spd_Lim_Emit(self):
        self.TC.curr_spd_lim_sig.emit(self.spdlimin.value())
    def Auth_Emit(self):
        self.TC.curr_auth_sig.emit(self.spinBox.value())
    def Pass_E_Emit(self):
        if(self.ebrakein.isChecked()):
            self.TC.ebrake_sig.emit(1)
        else:
            self.TC.ebrake_sig.emit(0)
    #need to fix
    def Beacon_Emit(self):
       print("beacon emit")

    def Underground_Emit(self):
        if(self.underground.isChecked()):
            self.TC.underground_sig.emit(1)
        else:
            self.TC.underground_sig.emit(0)

    def Pwr_Fail_Emit(self):
        if(self.pwrfailin.isChecked()):
            self.TC.pwr_fail_sig.emit(1)
        else:
            self.TC.pwr_fail_sig.emit(0)

    def Brk_Fail_Emit(self):
        if (self.brkfail.isChecked()):
            self.TC.brk_fail_sig.emit(1)
        else:
            self.TC.brk_fail_sig.emit(0)

    def Sig_Fail_Emit(self):
        if (self.sigfail.isChecked()):
            self.TC.sig_fail_sig.emit(1)
        else:
            self.TC.sig_fail_sig.emit(0)

    def Block_Paseed_Emit(self):
        if(self.blockpass.isChecked()):
            self.TC.block_passed_sig.emit(1)
        else:
            self.TC.block_passed_sig.emit(0)
    def Temp_Emit(self):
        self.TC.curr_temp_sig.emit(self.currtempin)



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


        ####Timer added
        self.label_17.setObjectName("label_17")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.verticalLayout_2.addWidget(self.label_17)
        self.timer = QtWidgets.QSpinBox(self.layoutWidget)
        self.timer.setMaximum(9999)
        self.timer.setObjectName("spinBox")
        self.verticalLayout_2.addWidget(self.timer)

        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_18)
        self.boolauth = QtWidgets.QCheckBox(self.layoutWidget)
        self.boolauth.setObjectName("boolauth")
        self.verticalLayout_2.addWidget(self.boolauth)
        
        


        ###
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.ebrakein = QtWidgets.QCheckBox(self.layoutWidget)
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
        self.underground = QtWidgets.QCheckBox(self.layoutWidget)
        self.underground.setObjectName("underground")
        self.verticalLayout_2.addWidget(self.underground)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.pwrfailin = QtWidgets.QCheckBox(self.layoutWidget)
        self.pwrfailin.setObjectName("pwrfailin")
        self.verticalLayout_2.addWidget(self.pwrfailin)
        self.brkfail = QtWidgets.QCheckBox(self.layoutWidget)
        self.brkfail.setObjectName("brkfail")
        self.verticalLayout_2.addWidget(self.brkfail)
        self.sigfail = QtWidgets.QCheckBox(self.layoutWidget)
        self.sigfail.setObjectName("sigfail")
        self.verticalLayout_2.addWidget(self.sigfail)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.blockpass = QtWidgets.QCheckBox(self.layoutWidget)
        self.blockpass.setObjectName("blockpass")
        self.verticalLayout_2.addWidget(self.blockpass)
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

        self.brakeen = QtWidgets.QCheckBox(self.layoutWidget1)
        
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
        self.ebrakein.setText(_translate("MainWindow", "Pass Ebrak toggle"))
        self.label_9.setText(_translate("MainWindow", "Beacon"))
        self.label_14.setText(_translate("MainWindow", "Curr Temp"))
        self.label_10.setText(_translate("MainWindow", "Underground"))
        self.underground.setText(_translate("MainWindow", "underground"))
        self.label_11.setText(_translate("MainWindow", "Failures "))
        self.pwrfailin.setText(_translate("MainWindow", "pwrfail"))
        self.brkfail.setText(_translate("MainWindow", "brkfail"))
        self.sigfail.setText(_translate("MainWindow", "sigfail"))
        self.label_12.setText(_translate("MainWindow", "Block Passed"))
        self.blockpass.setText(_translate("MainWindow", "blockpassed"))
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
        self.label_17.setText(_translate("MainWindow", "Timer"))
        self.label_18.setText(_translate("MainWindow", "boolauth"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TestBench = QtWidgets.QMainWindow()
    TB_ui = Ui_TestBench()
    TB_ui.setupUi(TestBench)
    TB_ui.sig_connect()
    TestBench.show()
    sys.exit(app.exec_())

