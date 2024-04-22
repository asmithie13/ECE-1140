from Train_Controller_SW.mainControl import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
#from PyQt5 import Timer

class Vital_Speed_Auth():

    #def __init__(self,ui):
    def __init__(self,ui,curr_auth_signal, service_brake_sig,ebrake_internal_sig,stop_at_station_sig,NonVital):
        self.ui = ui
        self.curr_auth_signal = curr_auth_signal
        self.service_brake_sig = service_brake_sig
        self.stopcal = 0
        self.local_clock = 0,
        self.time = 0
        self.prev_time = 0
        self.ebrake_sig = ebrake_internal_sig
        self.decimal_m_auth = 0
        self.stop_at_station_sig = stop_at_station_sig
        self.NonVital = NonVital
        self.bool_auth_enabled = False

    def Control_Current_Speed(self,newSpeed):
        self.ui.lcdCurSpd.display(newSpeed)
    
    def Set_Clock(self, time):
         self.local_clock = time
    
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
        self.rate = self.ui.lcdCurSpd.value()*0.00146667 #mph to fpms
        self.rate_metric = self.ui.lcdCurSpd.value()*0.00044704 #mph to m/,ms,
        self.time = self.local_clock - self.prev_time
        self.prev_time = self.local_clock 

        current_speed = self.ui.lcdCurSpd.value()
        speed_limit = float(self.ui.lcdSpdLim.value())
        cmd_speed = self.ui.lcdCmdSpd.value()
        
        if(not(self.ui.lcdCurSpd.value == 0)):
            self.decimal_m_auth = self.decimal_m_auth - float(self.rate_metric*self.time)
            self.ui.lcdAuth.display(round(self.decimal_m_auth* 3.28084))
            # if self.ui.lcdAuth.value() > 0:

            #authority in m from ft
            
            # in order to get most accurate stopping distance we use this
            self.AuthM = self.decimal_m_auth
    
            #current speed in m/ms from mph
            self.V_i = (self.ui.lcdCurSpd.value()*0.00044704)

            #from top speed (70kph) it takes 157.535288067 m to stop with the service brake
            #from top speed (70kph) it takes 70.0156835852 m to stop with the emergency brake

        
            #if self.stopcal == True:
            self.stoppingdistanceService = (self.V_i**2)/(2*0.000012)   
            print("Stopping Distance :",self.stoppingdistanceService)
            print(self.stoppingdistanceService)
            #print("Dist Service : ", self.stoppingdistanceService)
            self.stoppubgdistanceEmergency = (self.V_i**2)/(2*0.0000273) 
            #print("E Stop: ", self.stoppubgdistanceEmergency)

            if self.bool_auth_enabled == 1:
                self.ui.vertSliderBrk.setValue(1)
                self.ui.vertSliderPow.setEnabled(False)

            elif self.AuthM <= self.stoppubgdistanceEmergency and self.AuthM >= 5:
                self.ui.vertSliderBrk.setValue(0)
                self.ui.vertSliderPow.setValue(0)
                self.ui.vertSliderPow.setEnabled(False)
                self.ui.Ebrake.setChecked(True)
                self.ebrake_sig.emit(1)
            
            elif (self.AuthM <= self.stoppingdistanceService) or (self.AuthM < 0 and self.ui.lcdCurSpd.value > 0) :
                self.ui.vertSliderBrk.setValue(1)
                self.ui.vertSliderPow.setValue(0)
                self.ui.vertSliderPow.setEnabled(False)

            #check current speed every time speed is updated or speed limit is updated
            #if speed is greater than speed limit, send command to brake
            #if speed is less than speed limit, send command to accelerate
            #our train is frictionless so it will maintain speed unless we tell it to do something else

            #this case is vital, will override driver input
            elif (current_speed > speed_limit):
                self.ui.vertSliderBrk.setValue(1)
                self.ui.vertSliderPow.setValue(0)

            elif (current_speed > cmd_speed):
                self.ui.vertSliderBrk.setValue(1)
                self.ui.vertSliderPow.setValue(0)
            
            #this case only is used in automatic mode, if we are in manual mode the train driver can drive how they please
            elif (((current_speed < speed_limit) or (current_speed < cmd_speed)) and (self.ui.buttonAuto.isChecked())):
                self.ui.vertSliderPow.setEnabled(True)
                if (self.AuthM <= 50):
                    self.ui.vertSliderPow.setValue(25)
                elif self.AuthM > 60:
                    self.ui.vertSliderPow.setValue(100)
                elif 50 < self.AuthM  < 100:
                    self.ui.vertSliderPow.setValue(50)
                self.ui.vertSliderBrk.setValue(0)
            
            #this case only is used in automatic mode, if we are in manual mode the train driver can drive how they please
            elif (current_speed == speed_limit) or (current_speed == cmd_speed) and (self.ui.buttonAuto.isChecked()):
                self.ui.vertSliderPow.setValue(0)
                self.ui.vertSliderBrk.setValue(0)
            
            elif self.ui.buttonMan.isChecked() :
                self.ui.vertSliderPow.setEnabled(True)

        elif self.decimal_m_auth < 1 and self.ui.lcdCurSpd == 0:
            if self.NonVital.arrived == True:
                ## add timer 
                self.stop_at_station_sig.emit(1)
                if self.ui.buttonAuto.isChecked():
                    self.Emit_Doors()

        else :
            self.stop_at_station_sig.emit(0)


    #we need to deal with whatever this is
    def Authority_Monitor_Bool(self, bool_auth):
        self.bool_auth_enabled = bool_auth

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
        if self.decimal_m_auth > 0 :
            self.ui.vertSliderPow.setEnabled(True)
            self.NonVital.doors = 0
            self.NonVital.Emit_Doors()
