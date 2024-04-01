from Train_Controller_SW.mainControl import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
#from PyQt5 import Timer

class Vital_Authority():

    #def __init__(self,ui):
    def __init__(self,ui,curr_auth_signal):
        self.ui = ui
        self.curr_auth_signal = curr_auth_signal

    
    #make sure we can stop in time for authority in ft
    #Put this on a timer every sec based on global
    def Authority_Monitor(self):

        #calculate authority using d=r*t
        self.rate = self.ui.lcdCurSpd.value()*1.46667 #mph to fps
        self.time = 1
        if(not(self.ui.lcdAuth.value() == 0) and not(self.ui.lcdCurSpd.value)):
            self.ui.lcdAuth.display(self.ui.lcdAuth.value() - int(self.rate*self.time)) #auth = auth - rate*time


        if self.ui.lcdAuth.value() != 0:

            #authority in m from ft
            
            # in order to get most accurate stopping distance we use this
            #self.AuthM = self.ui.lcdAuth.value()*0.3048

            self.AuthM = self.decimal_m_auth
        
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
        self.decimal_m_auth = auth
        print(auth)
        self.ui.lcdAuth.display(int(auth * 3.28084))
        self.ui.vertSliderPow.setEnabled(True)