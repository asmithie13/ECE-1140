from TrainController import *

class Vital_Authority(TrainController):
    
    #make sure we can stop in time for authority in ft
    #Put this on a timer every sec based on global
    def Authority_Monitor(self):

        #authority in m from ft
        self.AuthM = TrainController.ui.lcdAuth.value()*0.3048

        #current speed in m/s from mph
        self.V_i = TrainController.ui.lcdCurSpd.value()*0.44704

        #this is wrong, we need to fix this -- units are screwed up 
        #from top speed (70kph) it takes 408.016388267 m to stop with the service brake
        #from top speed (70kph) it takes 179.347862974 m to stop with the emergency brake

        self.stoppingdistanceService = (self.V_i**2)/(2*1.2)
        self.stoppubgdistanceEmergency = (self.V_i**2)/(2*2.73)

        if self.AuthM < self.stoppingdistanceService:
            TrainController.ui.vertSliderBrk.setValue(1)
            TrainController.ui.vertSliderPow.setValue(0)
            TrainController.ui.vertSliderPow.setDisabled(True)
            if self.AuthM < self.stoppubgdistanceEmergency:
                TrainController.ui.Ebrake.setChecked(True)
    
    #we need to deal with whatever this is
    def Authority_Monitor_Bool(self):
        print("Authority Monitor Bool")
        #talk to tanvi about this


    #I want to move this to nonvital
    def Control_Doors(self,door):
        if TrainController.ui.lcdCurSpd.valu() == 0:
            if door == "Left":
                TrainController.ui.buttonDoorL.toggle()
            elif door == "Right":
                TrainController.ui.buttonDoorR.toggle()
            elif door == "Both":
                TrainController.ui.buttonDoorL.toggle()
                TrainController.ui.buttonDoorR.toggle()