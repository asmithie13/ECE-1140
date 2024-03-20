from TrainController import *

class Vital_Speed(TrainController):
    def Speed_Monitor(self):
        #check current speed every time speed is updated or speed limit is updated
        #if speed is greater than speed limit, send command to brake
        #if speed is less than speed limit, send command to accelerate

        #our train is frictionless so it will maintain speed unless we tell it to do something else

        current_speed = TrainController.ui.lcdCurSpd.value()
        speed_limit = TrainController.ui.lcdSpdLim.value()
        cmd_speed = TrainController.ui.lcdCmdSpd.value()

        #this case is vital, will override driver input
        if current_speed > speed_limit:
            TrainController.ui.vertSliderBrk.setValue(1)
            TrainController.ui.vertSliderPow.setValue(0)
        
        #this case only is used in automatic mode, if we are in manual mode the train driver can drive how they please
        elif current_speed < ((speed_limit | cmd_speed) & (TrainController.ui.buttonAuto.isChecked() == True)):
            TrainController.ui.vertSliderPow.setValue(1)
            TrainController.ui.vertSliderBrk.setValue(0)
        
        #this case only is used in automatic mode, if we are in manual mode the train driver can drive how they please
        elif current_speed == (speed_limit | cmd_speed):
            TrainController.ui.vertSliderPow.setValue(0)
            TrainController.ui.vertSliderBrk.setValue(0) 
    
    def service_brake(self):
        #send signal to brake
        if TrainController.ui.vertSliderBrk.value() == 1:
            #emit(1)
            print("Service Brake On")
        if TrainController.ui.vertSliderBrk.value() == 0:
            #emit(0)
            print("Service Brake Off")
        
    ## i kinda have these both done in TC but we can put them in here so its not a class with two function but these will have literally one line in them
    #def Control_Speed_Limit():
        #update speed limit for current block

    #def Control_Commanded_Speed(self):
        #update commanded speed for from signal