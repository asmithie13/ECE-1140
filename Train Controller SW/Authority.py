from mainControl import Ui_MainWindow

class Vital_Authority():

    def __init__(self,ui):
        self.ui = ui
    
    #make sure we can stop in time for authority in ft
    #Put this on a timer every sec based on global
    def Authority_Monitor(self):

        #authority in m from ft
        self.AuthM = self.ui.lcdAuth.value()*0.3048

        #current speed in m/s from mph
        self.V_i = self.ui.lcdCurSpd.value()*0.44704

        #this is wrong, we need to fix this -- units are screwed up 
        #from top speed (70kph) it takes 408.016388267 m to stop with the service brake
        #from top speed (70kph) it takes 179.347862974 m to stop with the emergency brake

        self.stoppingdistanceService = (self.V_i**2)/(2*1.2)
        self.stoppubgdistanceEmergency = (self.V_i**2)/(2*2.73)

        if self.AuthM < self.stoppingdistanceService:
            self.ui.vertSliderBrk.setValue(1)
            self.ui.vertSliderPow.setValue(0)
            self.ui.vertSliderPow.setDisabled(True)
            if self.AuthM < self.stoppubgdistanceEmergency:
                self.ui.Ebrake.setChecked(True)
    
    #we need to deal with whatever this is
    def Authority_Monitor_Bool(self):
        print("Authority Monitor Bool")
        #talk to tanvi about this


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