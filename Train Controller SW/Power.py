from mainControl import Ui_MainWindow

class Vital_Power():
    def __init__(self,ui, curr_power_sig):
        self.ui = ui
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
    
    def calculate_power(self):

        if self.ui.vertSliderPow.value() == 0:
            self.ui.vertSliderBrk.setValue(1)
            self.power = 0

        else:
            #self.time = self.globalClock
            self.dt = self.time - self.prevTime
            self.prevTime = self.time
            self.error = self.lcdCmdSpd.value() - self.lcdCurSpd.value()
            self.uk = self.prevUk + (self.error + self.prevError) * self.dt / 2
            self.prevError = self.error
            self.prevUk = self.uk
            
            self.power0 = (self.ui.lcdKp.value() * self.error + self.ui.lcdKi.value() * self.uk) * (self.ui.lcdPwrOut.value() / 100)
            self.power1 = (self.ui.lcdKp.value() * self.error + self.ui.lcdKi.value() * self.uk) * (self.ui.lcdPwrOut.value() / 100)
            self.power2 = (self.ui.lcdKp.value() * self.error + self.ui.lcdKi.value() * self.uk) * (self.ui.lcdPwrOut.value() / 100)

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
        
        self.ui.lcdPwrOut.display(self.power)
        self.curr_power_sig.emit(self.power)
        