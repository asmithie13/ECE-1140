from mainControl import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import Timer

class Vital_Authority():

    def __init__(self,ui):
        self.ui = ui
        # self.authTimer = QTimer()
        # self.authTimer.setInterval(1000)
        # self.authTimer.timeout.connect(self.Authority_Monitor)


    def authTimerStart(self):
        if not self.authTimer.isActive():
            self.authTimer.start()

    
    #make sure we can stop in time for authority in ft
    #Put this on a timer every sec based on global
    def Authority_Monitor(self):

        if self.ui.lcdAuth.value() != 0:

            #authority in m from ft
            self.AuthM = self.ui.lcdAuth.value()*0.3048

            #current speed in m/s from mph
            self.V_i = self.ui.lcdCurSpd.value()*0.44704

            #from top speed (70kph) it takes 157.535288067 m to stop with the service brake
            #from top speed (70kph) it takes 70.0156835852 m to stop with the emergency brake

            self.stoppingdistanceService = (self.V_i**2)/(2*1.2)
            self.stoppubgdistanceEmergency = (self.V_i**2)/(2*2.73)

            if self.AuthM < self.stoppingdistanceService:
                self.ui.vertSliderBrk.setValue(1)
                self.ui.vertSliderPow.setValue(0)
                self.ui.vertSliderPow.setDisabled(True)
                if self.AuthM < self.stoppubgdistanceEmergency:
                    self.ui.Ebrake.setChecked(True)
            else:
                self.authTimer.stop()

    #we need to deal with whatever this is
    def Authority_Monitor_Bool(self, bool_auth):
        if(bool_auth):
            self.ui.vertSliderBrk.setValue(1)
            self.ui.vertSliderPow.setDisabled(True)
        else:
            self.ui.vertSliderPow.setDisabled(False)

    #I want to move this to nonvital
    def Control_Doors(self,door):
        if self.ui.lcdCurSpd.valu() == 0:
            if door == "Left":
                self.ui.buttonDoorL.toggle()
            elif door == "Right":
                self.ui.buttonDoorR.toggle()
            elif door == "Both":
                self.ui.buttonDoorL.toggle()
                self.ui.buttonDoorR.toggle()

    def Control_Authority(self,auth):
        self.ui.lcdAuth.display(auth)