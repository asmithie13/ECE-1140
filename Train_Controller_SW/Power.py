from Train_Controller_SW.mainControl import Ui_MainWindow

class Vital_Power():
    def __init__(self,ui, curr_power_sig):
        self.ui = ui

        self.local_clock = 0

        self.Ki = 0
        self.Kp = 0
        self.power = 0
        self.power0 = 0
        self.power1 = 0
        self.power2 = 0
        self.time = 0
        self.dt = 0
        self.error = 0
        self.uk = 0
        self.prevError = 0
        self.prevUk = 0
        self.prevTime = 0
        
        self.curr_power_sig = curr_power_sig

    def Control_Ki(self):
            self.ui.lcdKi.display(self.ui.inputKi.value())
            self.Ki = self.ui.inputKi.value()

    def Control_Kp(self):
            self.ui.lcdKp.display(self.ui.inputKp.value())
            self.Kp = self.ui.inputKp.value()

    def Set_Clock(self, time):
         self.local_clock = time

    
    def calculate_power(self):
        if self.ui.Ebrake.isChecked():
           self.power = 0
        
        elif self.ui.vertSliderBrk.value() == 1:
            self.power = 0
        
        elif self.ui.vertSliderPow.value() == 0:
            self.power = 0

        else:
            self.time = self.local_clock
            print("Curr Time", self.time)
            self.dt = self.time - self.prevTime
            self.prevTime = self.time
            self.error = float(self.ui.lcdCmdSpd.value()) * 0.44704 - float(self.ui.lcdCurSpd.value()) * 0.44704
            self.uk = self.prevUk + (self.error + self.prevError) * self.dt / 2
            self.prevError = self.error
            self.prevUk = self.uk

            self.power0 = (float(self.ui.lcdKp.value()) * self.error + float(self.ui.lcdKi.value()) * self.uk) * (float(self.ui.lcdPowOut.value()) / 100.0)
            self.power1 = (float(self.ui.lcdKp.value()) * self.error + float(self.ui.lcdKi.value()) * self.uk) * (float(self.ui.lcdPowOut.value()) / 100.0)  
            self.power2 = (float(self.ui.lcdKp.value()) * self.error + float(self.ui.lcdKi.value()) * self.uk) * (float(self.ui.lcdPowOut.value()) / 100.0)

            if(self.power0 == self.power1 or self.power1 == self.power2 or self.power0 == self.power2):
                if(self.power0 == self.power1):
                    self.power = self.power0
                elif(self.power1 == self.power2):
                    self.power = self.power1
                elif(self.power0 == self.power2):
                    self.power = self.power0
            else: 
                self.power = 0
            
            if self.power > 120000:
                self.power = 120000
            elif self.power < 0:
                self.power = 0
        
        self.ui.lcdPowOut.display(self.ui.vertSliderPow.value())
        self.ui.lcdBrk.display(self.ui.vertSliderBrk.value())
        self.ui.lcdAcel.display(self.power)
        self.curr_power_sig.emit(int(self.power))

    def Control_Accelleration(self):
        if(self.ui.vertSliderPow.value() > 0):
            self.ui.vertSliderBrk.setValue(0)
            self.ui.lcdBrk.display(self.ui.vertSliderBrk.value())   