from mainControl import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

class TrainController :
    def __init__(self):
        #signals that we take as inputs # I dont think we need these, I think this is on Tanvis side
        self.curr_spd_sig =pyqtSignal(int)
        self.curr_spd_sig.connect(self.Control_Current_Speed())
        self.curr_auth_sig=pyqtSignal(int)

        self.curr_spd_lim_sig = pyqtSignal(int)

        self.curr_temp_sig = pyqtSignal(int)
        self.curr_temp_sig.connect(self.Control_Temperature())

        self.ebrake_sig = pyqtSignal(bool)
        self.ebrake_sig.connect(self.Control_Emergency_Brake())

        self.pwr_fail_sig = pyqtSignal(bool)
        self.pwr_fail_sig.connect(self.Control_Power_Failure())

        self.brk_fail_sig = pyqtSignal(bool)
        self.brk_fail_sig.connect(self.Control_Brake_Failure())

        self.sig_fail_sig = pyqtSignal(bool)
        self.bsig_fail_sig.connect(self.Control_Signal_Failure())

        self.underground_sig = pyqtSignal(bool)
        #need to add

        self.next_station_sig = pyqtSignal(str)
        self.next_station_sig.connect(self.Control_Next_Station())

        self.dist_to_next_station_sig = pyqtSignal(int)
        self.dist_to_next_station_sig.connect(self.Control_Next_Station())

        self.block_passed_sig = pyqtSignal(bool)
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
        self.ui.Ebrake.clicked.connect(self.Control_Emergency_Brake())
        self.ui.buttonMan.clicked.connect(self.Control_Manual)
        self.ui.buttonAuto.clicked.connect(self.Control_Automatic())
        self.ui.temp.valueChanged.connect(self.Control_Temperature())
        self.ui.lineEditAnn.editingFinished.connect(self.Control_Annoucement(self.ui.lineEditAnn.text()))

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

    