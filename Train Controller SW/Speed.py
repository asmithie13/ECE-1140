from mainControl import Ui_MainWindow

class Vital_Speed():
    
    def __init__(self,ui):
        self.ui = ui

    def Control_Current_Speed(self,newSpeed):
        self.ui.lcdCurSpd.setValue(newSpeed)
        self.Speed_Monitor()
    
    def Speed_Monitor(self):
        #check current speed every time speed is updated or speed limit is updated
        #if speed is greater than speed limit, send command to brake
        #if speed is less than speed limit, send command to accelerate

        #our train is frictionless so it will maintain speed unless we tell it to do something else

        current_speed = self.ui.lcdCurSpd.value()
        speed_limit = self.ui.lcdSpdLim.value()
        cmd_speed = self.ui.lcdCmdSpd.value()

        #this case is vital, will override driver input
        if current_speed > speed_limit:
            self.ui.vertSliderBrk.setValue(1)
            self.ui.vertSliderPow.setValue(0)
        
        #this case only is used in automatic mode, if we are in manual mode the train driver can drive how they please
        elif current_speed < ((speed_limit | cmd_speed) & (self.ui.buttonAuto.isChecked() == True)):
            self.ui.vertSliderPow.setValue(1)
            self.ui.vertSliderBrk.setValue(0)
        
        #this case only is used in automatic mode, if we are in manual mode the train driver can drive how they please
        elif current_speed == (speed_limit | cmd_speed):
            self.ui.vertSliderPow.setValue(0)
            self.ui.vertSliderBrk.setValue(0) 
    
    def service_brake(self):
        #send signal to brake
        #turn down acceltor
        if self.ui.vertSliderBrk.value() == 1:
            self.ui.vertSliderPow.setValue(0)
            #emit(1)
            print("Service Brake On")
        if self.ui.vertSliderBrk.value() == 0:
            #emit(0)
            print("Service Brake Off")
        
    def Control_Speed_Limit(self,spdLim):
        #update speed limit for current block
        self.ui.lcdSpdLim.setValue(spdLim)
        self.Speed_Monitor()
        
    def Control_Commanded_Speed(self,cmdSpd):
        #update commanded speed for from signal
        self.ui.lcdCmdSpd.setValue(cmdSpd)
        self.Speed_Monitor()