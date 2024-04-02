from Train_Controller_SW.mainControl import Ui_MainWindow
from Train_Controller_SW.Power import Vital_Power
from Train_Controller_SW.Speed import Vital_Speed
from Train_Controller_SW.Authority import Vital_Authority
from Train_Controller_SW.Failure import Vital_Failure
from Train_Controller_SW.NonVital import NonVital
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
#from PyQt5 import uic

class TrainController(QMainWindow):
    #signals declaered here

    #vital signals we recieve
    curr_spd_sig = pyqtSignal(int)
    curr_auth_sig = pyqtSignal(float)
    curr_bool_auth_sig  = pyqtSignal(bool)
    curr_cmd_spd_sig = pyqtSignal(int)
    curr_temp_sig = pyqtSignal(int)
    curr_spd_lim_sig = pyqtSignal(int)
    ebrake_sig = pyqtSignal(bool)
    pwr_fail_sig = pyqtSignal(bool)
    brk_fail_sig = pyqtSignal(bool)
    sig_fail_sig = pyqtSignal(bool)
    beacon_info_sig = pyqtSignal(str)
    #non vital we recieve
    #underground_sig = pyqtSignal(bool)
    block_passed_sig = pyqtSignal(bool)
    time_sig = pyqtSignal(str)
    # signals we use as outputs

    #signals we send
    service_brake_sig = pyqtSignal(bool)
    curr_power_sig = pyqtSignal(int)
    # connect all of these to power calc function
    door_control_sig = pyqtSignal(int)
    announcement_sig = pyqtSignal(str)
    temp_control_sig = pyqtSignal(int)
    int_light_sig = pyqtSignal(int)
    ext_light_sig = pyqtSignal(int)
    ebrake_disable_sig = pyqtSignal(bool)


    def __init__(self):
        super(TrainController, self).__init__()
        #self.ui = ui
        #opening UI

        self.globalClock = 0

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        #creating subclasses
        self.Vital_Power = Vital_Power(self.ui, self.curr_power_sig)
        self.Vital_Speed = Vital_Speed(self.ui, self.service_brake_sig)
        self.Vital_Authority = Vital_Authority(self.ui,self.curr_auth_sig)
        self.Vital_Failure = Vital_Failure(self.ui, self.ebrake_sig, self.ebrake_disable_sig)
        self.NonVital = NonVital(self.ui,self.door_control_sig,self.announcement_sig,
        self.temp_control_sig,self.int_light_sig,self.ext_light_sig)

        #slotting siganls
        self.curr_spd_sig.connect(self.Vital_Speed.Control_Current_Speed)
        self.curr_cmd_spd_sig.connect(self.Vital_Speed.Control_Commanded_Speed)
        self.curr_spd_lim_sig.connect(self.Vital_Speed.Control_Speed_Limit)
        self.curr_auth_sig.connect(self.Vital_Authority.Control_Authority)
        self.curr_temp_sig.connect(self.NonVital.Cabin_Temperature)
        self.ebrake_sig.connect(self.Vital_Failure.Control_Emergency_Brake)
        self.pwr_fail_sig.connect(self.Vital_Failure.Control_Power_Failure)
        self.brk_fail_sig.connect(self.Vital_Failure.Control_Brake_Failure)
        self.sig_fail_sig.connect(self.Vital_Failure.Control_Signal_Failure)
        self.beacon_info_sig.connect(self.NonVital.Read_Beacon)    
        self.curr_bool_auth_sig.connect(self.Vital_Authority.Authority_Monitor_Bool)
        self.block_passed_sig.connect(self.NonVital.BlockCounter)
        self.curr_bool_auth_sig.connect(self.Vital_Authority.Authority_Monitor_Bool)
        self.time_sig.connect(self.Timer)

        #connecting UI buttons to functions
        self.ui.Ebrake.clicked.connect(lambda : self.Vital_Failure.Control_Emergency_Brake(self.ui.Ebrake.isChecked()))
        self.ui.buttonMan.clicked.connect(lambda : self.Control_Manual())
        self.ui.buttonAuto.clicked.connect(lambda : self.Control_Automatic())
        #self.ui.temp.valueChanged.connect(lambda : self.NonVital.Cabin_Temperature())
        self.ui.buttonHDoff.clicked.connect(lambda : self.NonVital.Control_Headlights_Off())
        self.ui.buttonHDon.clicked.connect(lambda : self.NonVital.Control_Headlights_On())
        self.ui.lineEditAnn.textChanged['QString'].connect(self.ui.SpkrOut.setText)  # type: ignore

        self.ui.inputKp.valueChanged.connect(lambda : self.Vital_Power.Control_Kp())
        self.ui.inputKi.valueChanged.connect(lambda : self.Vital_Power.Control_Ki())
        self.ui.vertSliderPow.valueChanged.connect(lambda : self.Vital_Power.calculate_power())
        #self.ui.lcdCurSpd.connect(self.Vital_Speed.Speed_Monitor)
        self.ui.vertSliderBrk.valueChanged.connect(lambda : self.Vital_Speed.service_brake())
        #self.ui.lcdAuth.valueChanged.connect(lambda :self.Vital_Authority.authTimerStart())

        #sending off signals in manual mode
        self.ui.buttonDoorL.clicked.connect(lambda : self.NonVital.Door())
        self.ui.buttonDoorR.clicked.connect(lambda : self.NonVital.Door())
        self.ui.IntLightSld.valueChanged.connect(lambda : self.int_light_sig.emit(self.ui.IntLightSld.value()))


        #these may conflict with the one above
        self.ui.lineEditAnn.editingFinished.connect(lambda : self.announcement_sig.emit(self.ui.lineEditAnn.text()))

        #these probably don't work
        #self.ui.BrkFail.stateChanged.connect(self.Vital_Failure.Control_Brake_Failure())
        #self.ui.PwrFail.stateChanged.connect(self.Vital_Failure.Control_Power_Failure())
        #self.ui.SigFail.stateChanged.connect(self.Vital_Failure.Control_Signal_Failure())
        #self.ui.Ebrake.stateChanged.connect(self.Vital_Failure.Control_Emergency_Brake())

        #temporary ADD SPEED LIM
        self.curr_spd_lim_sig.emit(30)

        ## add for doors
        self.window.show()

    def Control_Automatic(self):
      self.ui.buttonMan.toggle()
      self.ui.buttonDoorL.setDisabled(True)
      self.ui.buttonDoorR.setDisabled(True)
      self.ui.temp.setDisabled(True)
      self.ui.buttonHDoff.setDisabled(True)
      self.ui.buttonHDon.setDisabled(True)
      self.ui.IntLightSld.setDisabled(True)
      self.ui.lineEditAnn.setDisabled(True)
      self.ui.inputKi.setDisabled(True)
      self.ui.inputKp.setDisabled(True)

      #self.Vital_Speed.Speed_Monitor()
      #self.ui.vertSliderPow.setDisabled(True)
      #self.ui.vertSliderBrk.setDisabled(True)

    def Control_Manual(self):
        self.ui.buttonAuto.toggle()
        self.ui.buttonDoorL.setDisabled(False)
        self.ui.buttonDoorR.setDisabled(False)
        self.ui.temp.setDisabled(False)
        self.ui.buttonHDon.setDisabled(False)
        self.ui.buttonHDoff.setDisabled(False)
        self.ui.IntLightSld.setDisabled(False)
        self.ui.lineEditAnn.setDisabled(False)
        self.ui.inputKi.setDisabled(False)
        self.ui.inputKp.setDisabled(False)
        
        if(self.ui.lcdAuth.value() == 0):
            self.ui.vertSliderPow.setDisabled(True)
        else:
            self.ui.vertSliderPow.setDisabled(False)
            self.ui.vertSliderBrk.setDisabled(False)

    def Timer(self, time):

        hours, minutes, seconds = [int(part) for part in time.split(':')]
        total_seconds = (hours * 3600) + (minutes * 60) + seconds
        #if things go wrong, try changing the order of speed, authority, power
        self.Vital_Power.Set_Clock(total_seconds)
        self.Vital_Speed.Speed_Monitor()
        self.Vital_Authority.Authority_Monitor()
        self.globalClock = total_seconds
        self.Vital_Power.calculate_power()
        #print(total_seconds)

    def Open_Main_UI(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

#if __name__ == "__main__":
 #   import sys
 #   app = QtWidgets.QApplication(sys.argv)
 #   MainWindow = QtWidgets.QMainWindow()
 #   ui = Ui_MainWindow()
 #   ui.setupUi(MainWindow)
 #   TrainController(ui)
 #   MainWindow.show()
 #   sys.exit(app.exec_())


