
from PyQt5 import QtCore, QtGui, QtWidgets
from mainControl import *

class Ui_TestBench(object):
    def set_automatic_manual(self):
       self.ui.buttonAuto.toggle()
       self.ui.buttonMan.toggle()
    def set_annoucement(self):
        text_output = self.Announcement.text()
        self.ui.SpkrOut.setText(text_output)

    def set_station(self):
        text_output = self.Station.text()
        self.ui.CurStatOut.setText(text_output)

    def set_left_door(self):
        self.ui.buttonDoorL.toggle()
    def set_right_door(self):
        self.ui.buttonDoorR.toggle()
    def set_headlights(self):
        self.ui.buttonHDon.toggle()
        self.ui.buttonHDoff.toggle()
    def set_power_failure(self):
        if(not(self.PowerFailure.isChecked())):
            self.ui.Power_Failure_Disable()
        else:
            self.ui.Power_Failure_Enable()
    def set_brake_failure(self):
        if(not(self.BrakeFailure.isChecked())):
            self.ui.Brake_Failure_Disable()
        else:
            self.ui.Brake_Failure_Enable()
    def set_signal_failure(self):
        if(not(self.SignalFailure.isChecked())):
            self.ui.Signal_Failure_Disable()
        else:
            self.ui.Signal_Failure_Enable()

    def set_interior_lights(self):
        if self.CabinLights.value() == 2:
            self.ui.IntLightSld.setValue(2)
        elif self.CabinLights.value() == 0:
            self.ui.IntLightSld.setValue(0)
        elif self.CabinLights.value() == 1:
            self.ui.IntLightSld.setValue(1)

    def set_KI(self):
        value = self.KI.value()
        self.ui.inputKi.setValue(value)

    def set_KP(self):
        value = self.KP.value()
        self.ui.inputKp.setValue(value)

    def set_accelleration(self):
        value = int(self.Power.value())
        self.ui.vertSliderPow.setValue(value)

    def set_brake(self):
        value = int(self.Brake.value())
        self.ui.vertSliderBrk.setValue(value)

    def set_commanded_spped(self):
        value = int(self.CSpeed.value())
        self.ui.lcdCmdSpd.display(value)

    def set_speed_limit(self):
        value = int(self.SpeedLimit.value())
        self.ui.lcdSpdLim.display(value)

    def set_current_speed(self):
        value = int(self.CurSpeed.value())
        self.ui.lcdCurSpd.display(value)

    def set_authority(self):
        value = int(self.Authority.value())
        self.ui.lcdAuth.display(value)

    def set_cabin_temp(self):
        value = int(self.CabinTemp.value())
        self.ui.temp.setValue(value)

    def set_ebrake(self):
        if((self.PassengerBrake.isChecked() or self.Ebrake.isChecked()) and not(self.ui.Ebrake.isChecked())):
            self.ui.Ebrake.setChecked(True)
        elif(not((self.PassengerBrake.isChecked() or self.Ebrake.isChecked()))):
            self.ui.Ebrake.setChecked(False)

    def setupUi(self, TestBench):
        TestBench.setObjectName("TestBench")
        TestBench.resize(571, 665)
        self.centralwidget = QtWidgets.QWidget(TestBench)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.KI = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.KI.setObjectName("KI")
        self.KI.editingFinished.connect(lambda : self.set_KI())
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.KI)
        self.SpeedLimit = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.SpeedLimit.setObjectName("SpeedLimit")
        self.SpeedLimit.editingFinished.connect( lambda : self.set_speed_limit())
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.SpeedLimit)
        self.CurSpeed = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.CurSpeed.setObjectName("CurSpeed")
        self.CurSpeed.editingFinished.connect( lambda : self.set_current_speed())
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.CurSpeed)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.Authority = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Authority.setRange(0,9999)
        self.Authority.setObjectName("Authority")
        self.Authority.editingFinished.connect( lambda : self.set_authority())
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.Authority)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.CabinTemp = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.CabinTemp.setMinimum(60.0)
        self.CabinTemp.setMaximum(90.0)
        self.CabinTemp.setObjectName("CabinTemp")
        self.CabinTemp.editingFinished.connect(lambda : self.set_cabin_temp())
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.CabinTemp)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.OpenLeft = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.set_left_door())
        self.OpenLeft.setCheckable(True)
        self.OpenLeft.setChecked(True)
        self.OpenLeft.setObjectName("OpenLeft")
        self.horizontalLayout.addWidget(self.OpenLeft)
        self.CloseLeft = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.set_left_door())
        self.CloseLeft.setCheckable(True)
        self.CloseLeft.setObjectName("CloseLeft")
        self.horizontalLayout.addWidget(self.CloseLeft)
        self.OpenRight = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.set_right_door())
        self.OpenRight.setCheckable(True)
        self.OpenRight.setChecked(True)
        self.OpenRight.setObjectName("OpenRight")
        self.horizontalLayout.addWidget(self.OpenRight)
        self.CloseRight = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.set_right_door())
        self.CloseRight.setCheckable(True)
        self.CloseRight.setObjectName("CloseRight")
        self.horizontalLayout.addWidget(self.CloseRight)
        self.formLayout.setLayout(12, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.HLightOn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.set_headlights())
        self.HLightOn.setCheckable(True)
        self.HLightOn.setChecked(True)
        self.HLightOn.setObjectName("HLightOn")
        self.horizontalLayout_3.addWidget(self.HLightOn)
        self.HLightOff = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.set_headlights())
        self.HLightOff.setCheckable(True)
        self.HLightOff.setObjectName("HLightOff")
        self.horizontalLayout_3.addWidget(self.HLightOff)
        self.formLayout.setLayout(15, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.KP = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.KP.setObjectName("KP")
        self.KP.editingFinished.connect( lambda : self.set_KP())
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.KP)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.Power = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Power.setObjectName("Power")
        self.Power.editingFinished.connect(lambda : self.set_accelleration())
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Power)
        self.Brake = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Brake.setObjectName("Brake")
        self.Brake.editingFinished.connect( lambda : self.set_brake())
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Brake)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.CSpeed = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.CSpeed.setObjectName("CSpeed")
        self.CSpeed.editingFinished.connect( lambda : self.set_commanded_spped())
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.CSpeed)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.Station = QtWidgets.QLineEdit(self.centralwidget)
        self.Station.setObjectName("Station")
        self.Station.returnPressed.connect(lambda: self.set_station())
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.Station)
        self.Announcement = QtWidgets.QLineEdit(self.centralwidget)
        self.Announcement.returnPressed.connect(lambda : self.set_annoucement())
        self.Announcement.setObjectName("Announcement")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.Announcement)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.PowerFailure = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.set_power_failure())
        self.PowerFailure.setCheckable(True)
        self.PowerFailure.setObjectName("PowerFailure")
        self.horizontalLayout_4.addWidget(self.PowerFailure)
        self.BrakeFailure = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.set_brake_failure())
        self.BrakeFailure.setCheckable(True)
        self.BrakeFailure.setObjectName("BrakeFailure")
        self.horizontalLayout_4.addWidget(self.BrakeFailure)
        self.SignalFailure = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.set_signal_failure())
        self.SignalFailure.setCheckable(True)
        self.SignalFailure.setObjectName("SignalFailure")
        self.horizontalLayout_4.addWidget(self.SignalFailure)
        self.formLayout.setLayout(20, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Auto = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.set_automatic_manual())
        self.Auto.setCheckable(True)
        self.Auto.setChecked(True)
        self.Auto.setObjectName("Auto")
        self.horizontalLayout_5.addWidget(self.Auto)
        self.Manual = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.set_automatic_manual())
        self.Manual.setCheckable(True)
        self.Manual.setObjectName("Manual")
        self.horizontalLayout_5.addWidget(self.Manual)
        self.formLayout.setLayout(21, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.CabinLights = QtWidgets.QSlider(self.centralwidget)
        self.CabinLights.setMaximum(2)
        self.CabinLights.setSingleStep(1)
        self.CabinLights.setPageStep(2)
        self.CabinLights.setSliderPosition(0)
        self.CabinLights.setTracking(False)
        self.CabinLights.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.CabinLights.setTickInterval(1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CabinLights.sizePolicy().hasHeightForWidth())
        self.CabinLights.setSizePolicy(sizePolicy)
        self.CabinLights.setOrientation(QtCore.Qt.Horizontal)

        self.Ebrake = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.set_ebrake())
        self.Ebrake.setCheckable(True)
        self.Ebrake.setObjectName("EBrake")
        self.horizontalLayout_4.addWidget(self.Ebrake)
        self.Ebrake.setText("Ebrake")

        self.PassengerBrake= QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.set_ebrake())
        self.PassengerBrake.setCheckable(True)
        self.PassengerBrake.setObjectName("Passenger EBrake")
        self.horizontalLayout_4.addWidget(self.PassengerBrake)
        self.PassengerBrake.setText("Passenger Ebrake")

        ##link to signal
        self.CabinLights.valueChanged.connect(lambda : self.set_interior_lights())
        self.CabinLights.setObjectName("CabinLights")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.CabinLights)
        TestBench.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TestBench)
        self.statusbar.setObjectName("statusbar")
        TestBench.setStatusBar(self.statusbar)

        self.retranslateUi(TestBench)
        self.Auto.clicked['bool'].connect(self.Manual.toggle) # type: ignore
        self.Manual.clicked['bool'].connect(self.Auto.toggle) # type: ignore
        self.HLightOff.clicked['bool'].connect(self.HLightOn.toggle) # type: ignore
        self.HLightOn.clicked['bool'].connect(self.HLightOff.toggle) # type: ignore
        self.OpenLeft.clicked['bool'].connect(self.CloseLeft.toggle) # type: ignore
        self.OpenRight.clicked['bool'].connect(self.CloseRight.toggle) # type: ignore
        self.CloseLeft.clicked['bool'].connect(self.OpenLeft.toggle) # type: ignore
        self.CloseRight.clicked['bool'].connect(self.OpenRight.toggle) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(TestBench)

    def retranslateUi(self, TestBench):
        _translate = QtCore.QCoreApplication.translate
        TestBench.setWindowTitle(_translate("TestBench", "MainWindow"))
        self.label.setText(_translate("TestBench", "Ki"))
        self.label_7.setText(_translate("TestBench", "Authority"))
        self.label_10.setText(_translate("TestBench", "Cabin Temp"))
        self.label_9.setText(_translate("TestBench", "Doors"))
        self.OpenLeft.setText(_translate("TestBench", "Open Left"))
        self.CloseLeft.setText(_translate("TestBench", "Close Left"))
        self.OpenRight.setText(_translate("TestBench", "Open Right"))
        self.CloseRight.setText(_translate("TestBench", "Close Right"))
        self.label_5.setText(_translate("TestBench", "Cabin Lights"))
        self.label_8.setText(_translate("TestBench", "Headlights"))
        self.HLightOn.setText(_translate("TestBench", "On"))
        self.HLightOff.setText(_translate("TestBench", "Off"))
        self.label_2.setText(_translate("TestBench", "Kp"))
        self.label_11.setText(_translate("TestBench", "Power"))
        self.label_6.setText(_translate("TestBench", "Speed Limit"))
        self.label_4.setText(_translate("TestBench", "Current Speed"))
        self.label_12.setText(_translate("TestBench", "Brake"))
        self.label_3.setText(_translate("TestBench", "Commanded speed"))
        self.label_13.setText(_translate("TestBench", "Announce"))
        self.label_14.setText(_translate("TestBench", "Station"))
        self.label_15.setText(_translate("TestBench", "Failures"))
        self.PowerFailure.setText(_translate("TestBench", "Power"))
        self.BrakeFailure.setText(_translate("TestBench", "Brake"))
        self.SignalFailure.setText(_translate("TestBench", "Signal"))
        self.label_16.setText(_translate("TestBench", "Mode"))
        self.Auto.setText(_translate("TestBench", "Auto"))
        self.Manual.setText(_translate("TestBench", "Manual"))

        self.Authority.valueChanged.connect(lambda : self.Trigger_Authoirty_Countdown())
        self.CurSpeed.valueChanged.connect(lambda : self.ui.speedControl())

    def Trigger_Authoirty_Countdown(self):
        self.ui.calcAuth()
    def Open_Main_UI(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TestBench = QtWidgets.QMainWindow()
    ui = Ui_TestBench()
    ui.setupUi(TestBench)
    TestBench.show()
    sys.exit(app.exec_())
