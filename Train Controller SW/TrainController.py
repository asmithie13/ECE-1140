from mainControl import Ui_MainWindow
from Power import Vital_Power
from Speed import Vital_Speed
from Authority import Vital_Authority
from Failure import Vital_Failure
from NonVital import NonVital
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

class TrainController :
    def __init__(self):

        #update displays
        #signals that we take as inputs # I dont think we need these, I think this is on Tanvis side
        self.curr_spd_sig = pyqtSignal(int)
        self.curr_spd_sig.connect(self.ui.lcdCurSpd.display(self.curr_spd_sig))
        
        self.curr_auth_sig = pyqtSignal(int)
        self.curr_auth_sig.connect(self.ui.lcdAuth.display(self.curr_auth_sig))

        self.curr_spd_lim_sig = pyqtSignal(int)
        self.curr_spd_lim_sig.connect(self.ui.lcdSpdLim.display(self.curr_spd_lim_sig))

        self.curr_temp_sig = pyqtSignal(int)
        self.curr_temp_sig.connect(self.ui.lcdCurTemp.display(self.curr_temp_sig))

        self.ebrake_sig = pyqtSignal(bool)
        self.ebrak_sig.connect(self.Ebrake.setChecked(self.ebrake_sig))

        self.pwr_fail_sig = pyqtSignal(bool)
        self.pwr_fail_sig.connect(self.PwrFail.setChecked(self.pwr_fail_sig))

        self.brk_fail_sig = pyqtSignal(bool)
        self.brk_fail_sig.connect(self.BrkFail.setChecked(self.brk_fail_sig))

        self.sig_fail_sig = pyqtSignal(bool)
        self.sig_fail_sig.connect(self.SigFail.setChecked(self.sig_fail_sig))

        self.underground_sig = pyqtSignal(bool)
        #self.underground_sig.connect(self.underground_sig.setChecked(self.underground_sig))
        #DNE in UI
        
        self.next_station_sig = pyqtSignal(str)
        self.next_station_sig.connect(self.Control_Next_Station())

        self.dist_to_next_station_sig = pyqtSignal(int)
        self.dist_to_next_station_sig.connect(self.Control_Next_Station())

        #block 
        self.block_passed_sig = pyqtSignal(bool)
        self.block_passed_sig.connect(NonVital.BlockCounter())

        self.block_length_sig = pyqtSignal(int)

        #signals we use as outputs
        self.service_brake_sig = pyqtSignal(bool)
        self.curr_power_sig = pyqtSignal(int)
        #connect all of these to power calc function
        
        self.door_control_sig = pyqtSignal(int)
        self.announcement_sig = pyqtSignal(str)
        self.temp_control_sig = pyqtSignal(int)
        self.underground_sig = pyqtSignal(bool)


        #connecting UI buttons to functions
        self.ui.Ebrake.clicked.connect(Vital_Failure.Control_Emergency_Brake())
        
        self.ui.buttonMan.clicked.connect(self.Control_Manual())
        self.ui.buttonAuto.clicked.connect(self.Control_Automatic())
        
        self.ui.temp.valueChanged.connect(NonVital.Control_Temperature(self.ui.temp.value()))

        self.ui.buttonHDoff.clicked.connect(NonVital.Control_Headlights())
        self.ui.buttonHDon.clicked.connect(NonVital.Control_Headlights())
        
        self.ui.lineEditAnn.editingFinished.connect(self.Control_Annoucement(self.ui.lineEditAnn.text()))
        
        #power
        self.ui.inputKp.valueChanged.connect(Vital_Power.Control_Ki())
        self.ui.inputKi.valueChanged.connect(Vital_Power.Control_Kp())
        self.ui.vertSliderPow.valueChanged.connect(Vital_Power.calculate_power())

        #speed
        self.ui.lcdCurSpd.valueChanged.connect(Vital_Speed.Speed_Monitor())
        self.ui.vertSliderBrk.valueChanged.connect(Vital_Speed.Control_Brake())
        #tanvi sends the control speed limit signal
        #tanvi sends control commanded speed signal

        #authority
        self.ui.lcdAuth.valueChanged.connect(Vital_Authority.Authority_Monitor())
        #tanvi sends the control authority signal

        #failure convert to indicator possibly
        self.ui.BrkFail.stateChanged.connect(Vital_Failure.Control_Brake_Failure())
        self.ui.PwrFail.stateChanged.connect(Vital_Failure.Control_Power_Failure())
        self.ui.SigFail.stateChanged.connect(Vital_Failure.Control_Signal_Failure())
        self.ui.Ebrake.stateChanged.connect(Vital_Failure.Control_Emergency_Brake())

    def openUI(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def Control_Automatic(self):
      self.buttonMan.toggle()
      self.buttonDoorL.setDisabled(True)
      self.buttonDoorR.setDisabled(True)
      self.temp.setDisabled(True)
      self.buttonHDoff.setDisabled(True)
      self.buttonHDon.setDisabled(True)
      self.IntLightSld.setDisabled(True)
      self.lineEditAnn.setDisabled(True)
      self.inputKi.setDisabled(True)
      self.inputKp.setDisabled(True)
      self.Speed_Montior()


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

    