from Train_Controller_SW.mainControl import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
#from PyQt5 import Timer

class Vital_Speed_Auth():

    #def __init__(self,ui):
    def __init__(self,ui,curr_auth_signal, service_brake_sig):
        self.ui = ui
        self.curr_auth_signal = curr_auth_signal
        self.service_brake_sig = service_brake_sig
        self.stopcal = 0

    def Control_Current_Speed(self,newSpeed):
        print("Curr Spd Tanvi :", newSpeed)
        self.ui.lcdCurSpd.display(newSpeed)
        #self.Speed_Monitor()
    
    def service_brake(self):
        #send signal to brake
        #turn down acceltor
        if self.ui.vertSliderBrk.value() > 0:
            self.ui.vertSliderPow.setValue(0)
            self.service_brake_sig.emit(True)
        if self.ui.vertSliderBrk.value() == 0:
            self.service_brake_sig.emit(False)
        self.ui.lcdBrk.display(self.ui.vertSliderBrk.value())
        
    def Control_Speed_Limit(self,spdLim):
        #update speed limit for current block
        self.ui.lcdSpdLim.display(spdLim)
        #self.Speed_Monitor()
        
    def Control_Commanded_Speed(self,cmdSpd):
        #update commanded speed for from signal
        self.ui.lcdCmdSpd.display(cmdSpd)
        #self.Speed_Monitor()


        #make sure we can stop in time for authority in ft
    #Put this on a timer every sec based on global
    def Speed_Authority_Monitor(self):

        #calculate authority using d=r*t
        self.rate = self.ui.lcdCurSpd.value()*1.46667 #mph to fps
        self.rate_metric = self.ui.lcdCurSpd.value()*0.44704
        self.time = 1

        current_speed = self.ui.lcdCurSpd.value()
        speed_limit = self.ui.lcdSpdLim.value()
        cmd_speed = self.ui.lcdCmdSpd.value()
        
        if(not(self.ui.lcdAuth.value() <= 0) and not(self.ui.lcdCurSpd.value == 0)):
            self.ui.lcdAuth.display(self.ui.lcdAuth.value() - int(self.rate*self.time)) #auth = auth - rate*time
            
            
            self.decimal_m_auth = self.decimal_m_auth - float(self.rate_metric*self.time)


            
            # if self.ui.lcdAuth.value() > 0:

            #authority in m from ft
            
            # in order to get most accurate stopping distance we use this
            #self.AuthM = self.ui.lcdAuth.value()*0.3048

            self.AuthM = self.decimal_m_auth
        
            #current speed in m/s from mph
            self.V_i = self.ui.lcdCurSpd.value()*0.44704

            #from top speed (70kph) it takes 157.535288067 m to stop with the service brake
            #from top speed (70kph) it takes 70.0156835852 m to stop with the emergency brake

            #if self.stopcal == True:
            self.stoppingdistanceService = (self.V_i**2)/(2*1.2)
            self.stoppubgdistanceEmergency = (self.V_i**2)/(2*2.73)
                

            if self.AuthM <= self.stoppubgdistanceEmergency:
                self.ui.vertSliderBrk.setValue(0)
                self.ui.Ebrake.setChecked(True)

            elif self.AuthM <= self.stoppingdistanceService:
                self.ui.vertSliderBrk.setValue(1)
                self.ui.vertSliderPow.setValue(0)
                self.ui.vertSliderPow.setDisabled(True)
                #self.stopcal = True

                #self.stopcal = True


            #check current speed every time speed is updated or speed limit is updated
            #if speed is greater than speed limit, send command to brake
            #if speed is less than speed limit, send command to accelerate

            #our train is frictionless so it will maintain speed unless we tell it to do something else

            #this case is vital, will override driver input
            elif current_speed > speed_limit:
                self.ui.vertSliderBrk.setValue(1)
                self.ui.vertSliderPow.setValue(0)
            
            #this case only is used in automatic mode, if we are in manual mode the train driver can drive how they please
            elif current_speed < ((speed_limit or cmd_speed) and (self.ui.buttonAuto.isChecked() == True)):
                self.ui.vertSliderPow.setValue(100)
                self.ui.vertSliderBrk.setValue(0)
            
            #this case only is used in automatic mode, if we are in manual mode the train driver can drive how they please
            elif current_speed == (speed_limit or cmd_speed):
                self.ui.vertSliderPow.setValue(0)
                self.ui.vertSliderBrk.setValue(0)

        # elif self.stopcal == 1:
        #     self.ui.lcdAuth.display(self.ui.lcdAuth.value() - int(self.rate*self.time))
        


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
        self.authft = round(auth * 3.28084)
        self.ui.lcdAuth.display(self.authft)
        print(self.authft)
        self.ui.vertSliderPow.setEnabled(True)