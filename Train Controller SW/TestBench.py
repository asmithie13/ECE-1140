
from PyQt5 import QtCore, QtGui, QtWidgets
from TrainController import TrainController
from Test_Bench_UI import TC_TestBench_UI

class TC_TestBench(object):
    def __init__(self):
        #where all the connections will go
        #where we will initalizw the TestBenchUI varible
        self.window = QtWidgets.QMainWindow()
        self.tb_ui = TC_TestBench_UI()
        self.tb_ui.setupUi(self.window)
        self.window.show()
        self.TC = TrainController()
        #also need the Train Controller object to access it

    def Set_Automatic_Manual(self):
       self.tb_ui.buttonAuto.toggle()
       self.tb_ui.buttonMan.toggle()
    
    def Set_Annoucement(self):
        text_output = self.tb_ui.Announcement.text()
        self.TC.ui.lineEditAnn.setText(text_output)

    def Set_Beacon_Information(self):
        text_output = self.Station.text()
        self.TC.beacon_info_sig.emit(self.Station.text())

    def Set_Left_Door(self):
        self.ui.buttonDoorL.toggle()
        #should autocall in main file
    def Set_Right_Door(self):
        self.ui.buttonDoorR.toggle()
    def Set_Headlights(self):
        self.ui.buttonHDon.toggle()
        self.ui.buttonHDoff.toggle()
    
    def Set_Power_Failure(self):
        if(not(self.PowerFailure.isChecked())):
            self.TC.pwr_fail_sig.emit(0)
        else:
            self.TC.pwr_fail_sig.emit(1)
    
    def Set_Brake_Failure(self):
        if(not(self.BrakeFailure.isChecked())):
            self.TC.brk_fail_sig.emit(0)
        else:
            self.TC.brk_fail_sig.emit(1)
   
    def Set_Signal_Failure(self):
        if(not(self.SignalFailure.isChecked())):
            self.TC.sig_fail_sig.emit(0)
        else:
            self.TC.sig_fail_sig.emit(1)

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

    def Set_Accelleration(self):
        value = int(self.Power.value())
        self.ui.vertSliderPow.setValue(value)

    def Set_Service_Brake(self):
        value = int(self.Brake.value())
        self.ui.vertSliderBrk.setValue(value)

    def Set_Commanded_Speed(self):
        value = int(self.CSpeed.value())
        self.TC.curr_cmd_spd_sig.emit(value)

    def Set_Speed_Limit(self):
        value = int(self.SpeedLimit.value())
        self.TC.curr_spd_lim_sig.emit(value)

    def Set_Current_Speed(self):
        # in future iterations, move this to the UI function
        value = int(self.CurSpeed.value())
        self.TC.curr_spd_sig.emit(value)

    def Set_Authority(self):
        value = int(self.Authority.value())
        self.ui.lcdAuth.display(value)

    def Set_Cabin_Temperature(self): 
        value = int(self.CabinTemp.value())
        self.ui.temp.setValue(value)

    def Set_Emergency_Brake(self):
        if((self.PassengerBrake.isChecked() or self.Ebrake.isChecked()) and not(self.ui.Ebrake.isChecked())):
            self.ui.Ebrake.setChecked(True)
        elif(not((self.PassengerBrake.isChecked() or self.Ebrake.isChecked()))):
            self.ui.Ebrake.setChecked(False)

    #def Trigger_Authoirty_Countdown(self):
      #  self.ui.calcAuth()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TestBench = QtWidgets.QMainWindow()
    ui = TC_TestBench_UI
    ui.setupUi(TestBench)
    TestBench.show()
    sys.exit(app.exec_())
