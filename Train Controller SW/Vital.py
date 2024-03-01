from TrainController import *

class Vital(TrainController):

    def __init__(self):

        #connecting UI buttons to functions
        #Door Control
        TrainController.ui.buttonDoorL.checked.connect(self.Control_Doors)
        TrainController.ui.buttonDoorR.checked.connect(self.Control_Doors)
        
        #Service Brake
        TrainController.ui.vertSliderBrk.valueChanged.connect(self.Control_Service_Brake)
        #Acceleration
        TrainController.ui.vertSliderPow.valueChanged.connect(self.Control_Acceleration)

        #KI/KP
        TrainController.ui.inputKi.valueChanged.connect(self.Control_KI)
        TrainController.ui.inputKp.valueChanged.connect(self.Control_KP)
        



    def Control_Service_Brake(self):
        #set output display
        TrainController.ui.lcdBrk.display(TrainController.ui.vertSliderBrk.value())
        TrainController.ui.vertSliderPow.setValue(0)
        self.Control_Power()
        #send to Train Model
        TrainController.service_brake_sig.emit(1)


    def Control_Acceleration(self):
        if TrainController.ui.lcdAuth == 0:
            TrainController.vertSliderPow.setValue(0)
            self.Control_Power()
        #as long as authority is not equal to zero
        else if(TrainController.ui.lcdAuth > 0):
            TrainController.ui.lcdPow_2.display(TrainController.ui.vertSliderPow.value())
            TrainController.ui.vertSliderBrk.setValue(0)
            #call power function
            self.Control_Power()

    def Control_KI(self):
        TrainController.lcdKi.display(TrainController.inputKi.value())
        TrainController.Control_Power()
        #TrainController.curr_KI_sig.emit(TrainController.inputKi.value())

    def Control_KP(self):
        TrainController.lcdKp.display(TrainController.inputKp.value())
        #TrainController.curr_KI_sig.emit(TrainController.inputKi.value())
        TrainController.Control_Power()

    def Control_Power(self):
        # at this point in development, since we do not have time integration, dt will be static
        # TrainController.dt = 1
        # TrainController.power = (TrainController.ui.inputKp.value() * TrainController.ui.inputKp.value() / TrainController.dt) * (TrainController.ui.vertSliderPow.value()/100)
        # TrainController.ui.lcdPwrOut.display(TrainController.power)
        # TrainController.curr_power_sig.emit(TrainController.power)

        #get current time from global clock called
        self.time = self.globalClock
        self.dt = self.time - self.prevTime
        self.prevTime = self.time
        self.error = self.lcdCmdSpd.value() - self.lcdCurSpd.value()
        self.uk = self.prevUk + (self.error + self.prevError) * self.dt / 2
        self.prevError = self.error
        self.prevUk = self.uk
        
        self.power0 = self.lcdKp.value() * self.error + self.lcdKi.value() * self.uk
        self.power1 = self.lcdKp.value() * self.error + self.lcdKi.value() * self.uk
        self.power2 = self.lcdKp.value() * self.error + self.lcdKi.value() * self.uk

        if ((self.power0 == self.power1) or (self.power0 == self.power2) or self.power1 == self.power2):
            self.power = self.power0
        else: 
            self.power = 0
        
        if self.power > 120000:
           self.power = 120000
        elif self.power < 0:
           self.power = 0
        self.lcdPwrOut.display(self.power)
        self.curr_power_sig.emit(self.power)

        

     # called when speed changes
    def Control_Current_Speed(self,curr_speed):
        TrainController.ui.lcdCurSpd.display(curr_speed)
        TrainController.Speed_Montior()
        #need an internal function that will adjust other paramters as the current speed adjusts
        # over speed limit

        #if (TrainController.lcdCmdSpd.value() > TrainController.lcdSpdLim.value()) & (TrainController.lcdCurSpd.value() < TrainController.lcdCmdSpd.value()):
            #TrainController.lcdCmdSpd.display(TrainController.lcdSpdLim.value())
            #TrainController.lcdCurSpd.display(TrainController.lcdCurSpd.value() + 1)
        # if cmd is less than current speed and speed limit
        #elif (TrainController.lcdCmdSpd.value() > TrainController.lcdCurSpd.value()) & (TrainController.lcdCmdSpd.value() < TrainController.lcdSpdLim.value()):
            #TrainController.lcdCurSpd.display(TrainController.lcdCurSpd.value() - 1)
        #TrainController.calcAuth(
        
    def Control_Speed_Limit(self,spd_lim):
        TrainController.ui.lcdSpdLim.display(spd_lim)
        TrainController.Speed_Montior()

    def Control_Commanded_Speed(self,cmd_spd):
        TrainController.ui.lcdCmdSpd.display(cmd_spd)
        TrainController.Speed_Montior()
    
    def Speed_Montior(self):
        #add calculate braking speed
        self.dist_to_stop = self.Calc_Dist_To_Stop()
        self.authority_conversion = TrainController.ui.lcdAuth.value * 0.3048
        if(self.authority_conversion == self.dist_to_stop):
            TrainController.ui.vertSliderPow.setValue(0)
            TrainController.ui.vertSliderBrk.setValue(1)
            TrainController.ui.vertSliderPow.setDisabled(True)
        elif(self.authority_conversion < self.dist_to_stop):
            TrainController.ui.Ebrake.setChecked(True)

        ############### AUTOMATIC#################
        if TrainController.ui.buttonAuto.isChecked()
            if(TrainController.ui.lcdCurSpd.value() > TrainController.lcdCmdSpd.value() or TrainController.ui.lcdCurSpd.value() > TrainController.ui.lcdSpdLim.value()):
                TrainController.ui.vertSliderPow.setValue(0)
                TrainController.ui.vertSliderBrk.setValue(1)
                TrainController.ui.vertSliderPow.setDisabled(True)            
            
                 (TrainControlleui.r.ui.lcdCurSpd.valulue(0)
                TrainController.ui.vertSliderPow.setValue(100)
             else:
                TrainController.ui.vertSliderPow.setDisabled(False)
                TrainController.ui.vertSliderPow.setValue(0)
        ###############MANUAL#################
        else():
            if( TrainController.ui.lcdCurSpd.value() > TrainController.ui.lcdSpdLim.value()):
                TrainController.ui.vertSliderPow.setValue(0)
                TrainController.ui.vertSliderBrk.setValue(1)
                TrainController.ui.vertSliderPow.setDisabled(True) 
            else:
                TrainController.ui.vertSliderPow.setDisabled(False)
                TrainController.ui.vertSliderPow.setValue(0)  
            (False)
            TrainController.ui.vertSliderPow.setValue(0)

    def Calc_Dist_To_Stop(self):
        #ADD UNIT CONVERSION
        self.curr_spd_m_p_s = TrainController.ui.lcdCurSpd.value * 0.44704
        self.m_to_stop = pow(self.curr_spd_m_p_s,2)/1.2
        return(self.m_to_stop)

       
    # I am coming back to you
    # this function I don't get around
    def Control_Doors(self,open):
        if (TrainController.ui.lcdAuth.value == 0):
            TrainController.door_control_sig.emit(open)
    
    def Door_Monitor(self):
        if(TrainController.ui.lcdAuth == 0):
            TrainController.ui.buttonDoorL.setEnabled(True)
            TrainController.ui.buttonDoorR.setEnabled(True)
        
        


    ## we need to call this when auth is entered from TB and we have a speed
    def Control_Authority(self):
        # update auth every second
        if not TrainController.authTimer.isActive():
            TrainController.authTimer.start()
        


    def Authority_Montior(self):
        #call speed montior to determine braking
        self.Speed_Montior()
        
        # decrease auth

        # Get current speed every second from train model to calc auth for display
        if ((TrainController.ui.lcdAuth.value() != 0) & (TrainController.ui.lcdCurSpd.value() != 0)):
            TrainController.Control_Doors()
            rate = TrainController.lcdCurSpd.value() * 1.46667
            if TrainController.ui.lcdAuth.value() - rate <= 0:
                TrainController.ui.lcdAuth.display(0)
                TrainController.ui.vertSliderPow.setValue(0)
                TrainController.ui.lcdCurSpd.display(0)
            else:
                TrainController.ui.lcdAuth.display(TrainController.lcdAuth.value() - rate)

        # target auth reached
        else:
            TrainController.ui.authTimer.stop()
            TrainController.Door_Control()
        
    def Control_Emergency_Brake(self):
        if TrainController.ui.Ebrake.isChecked() == True:
            enable = True
        else:
            enable = False
        TrainController.ui.buttonMan.setDisabled(enable)
        TrainController.ui.buttonMan.setDisabled(enable)
        TrainController.ui.buttonDoorL.setDisabled(enable)
        TrainController.ui.buttonDoorR.setDisabled(enable)
        TrainController.ui.temp.setDisabled(enable)
        TrainController.ui.buttonHDoff.setDisabled(enable)
        TrainController.ui.buttonHDon.setDisabled(enable)
        TrainController.ui.IntLightSld.setDisabled(enable)
        TrainController.ui.lineEditAnn.setDisabled(enable)
        TrainController.ui.vertSliderPow.setValue(0)
        TrainController.ui.vertSliderBrk.setValue(0)
        TrainController.ui.vertSliderBrk.setDisabled(enable)
        TrainController.ui.vertSliderPow.setDisabled(enable)
        TrainController.ui.inputKi.setDisabled(enable)
        TrainController.ui.inputKp.setDisabled(enable)


    def Control_Signal_Failure(self,sig_fail):
        if(sig_fail == True):
            TrainController.ui.SigFail.setStyleSheet("color: red;\n"
                                          "background-color: rgb(255, 255, 255);")
            TrainController.ui.vertSliderPow.setValue(0)
            TrainController.ui.vertSliderBrk.setValue(1)
            TrainController.ui.vertSliderPow.setDisabled(True)
            TrainController.ui.vertSliderBrk.setDisabled(True)
        else:
            TrainController.ui.SigFail.setStyleSheet("color: rgb(225, 225, 225);\n"
                                       "background-color: rgb(255, 255, 255);")
            TrainController.ui.vertSliderPow.setDisabled(False)
            TrainController.ui.vertSliderBrk.setDisabled(False)


    def Control_Power_Failure(self,pwr_fail):
        if pwr_fail == True:
            TrainController.ui.PwrFail.setStyleSheet("color: red;\n"
                                          "background-color: rgb(255, 255, 255);")
            TrainController.ui.vertSliderPow.setValue(0)
            TrainController.ui.vertSliderBrk.setValue(1)
            TrainController.ui.vertSliderPow.setDisabled(True)
            TrainController.ui.vertSliderBrk.setDisabled(True)
        else:
            TrainController.ui.PwrFail.setStyleSheet("color: rgb(225, 225, 225);\n"
                                       "background-color: rgb(255, 255, 255);")
            TrainController.ui.vertSliderPow.setDisabled(False)
            TrainController.ui.vertSliderBrk.setDisabled(False)


    def Control_Brake_Failure(self,brk_fail):
        if(brk_fail == True):
            TrainController.ui.BrkFail.setStyleSheet("color: red;\n"
                                       "background-color: rgb(255, 255, 255);")
            TrainController.ui.Ebrake.setChecked(True)
        #DISABLE
        else:
            TrainController.ui.BrkFail.setStyleSheet("color: rgb(225, 225, 225);\n"
                                       "background-color: rgb(255, 255, 255);")
            TrainController.ui.Ebrake.setChecked(False)