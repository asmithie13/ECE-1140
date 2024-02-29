from mainControl import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal


#functions we need to make


class Train_Controller_Signals :

    def __init__(self) : 
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

        # Add PyQT signal declarations

        #signals that we take as inputs # I dont think we need these, I think this is on Tanvis side
        self.curr_spd_sig =pyqtSignal(int)
        self.curr_spd_sig.connect(self.Control_Current_Speed())
        self.curr_auth_sig=pyqtSignal(int)

        self.curr_spd_lim_sig = pyqtSignal(int)

        self.curr_temp_sig = pyqtSignal(int)
        self.curr_temp_sig.connect(self.Control_Temperature())

        self.ebrake_sig = pyqtSignal(bool)
        self.ebrake_sig.connect(self.Control_Emergency_Brake())

        self.pwr_fail_sig = pyqtSignal(bool)
        self.pwr_fail_sig.connect(self.Control_Power_Failure())

        self.brk_fail_sig = pyqtSignal(bool)
        self.brk_fail_sig.connect(self.Control_Brake_Failure())

        self.sig_fail_sig = pyqtSignal(bool)
        self.bsig_fail_sig.connect(self.Control_Signal_Failure())

        self.underground_sig = pyqtSignal(bool)
        #need to add

        self.next_station_sig = pyqtSignal(str)
        self.next_station_sig.connect(self.Control_Next_Station())

        self.dist_to_next_station_sig = pyqtSignal(int)
        self.dist_to_next_station_sig.connect(self.Control_Next_Station())

        self.block_passed_sig = pyqtSignal(bool)
        self.block_length_sig = pyqtSignal(int)

        #signals we use as outputs
        self.service_brake_sig = pyqtSignal(bool)
        self.curr_power_sig = pyqtSignal(int)
        #connect all of these to power calc function
        self.door_control_sig = pyqtSignal(int)
        self.announcement_sig = pyqtSignal(str)
        self.temp_control_sig = pyqtSignal(int)


        #connecting UI buttons to functions
        self.ui.Ebrake.clicked.connect(self.Control_Emergency_Brake())
        self.ui.buttonMan.clicked.connect(self.Control_Manual)
        self.ui.buttonAuto.clicked.connect(self.Control_Automatic())
        self.ui.temp.valueChanged.connect(self.Control_Temperature())
        self.ui.lineEditAnn.editingFinished.connect(self.Control_Annoucement(self.ui.lineEditAnn.text()))




    #connecting internal UI signals to interal fucntion

    def Control_Service_Brake(self):
        #set output display
        self.ui.lcdBrk.display(self.ui.vertSliderBrk.value())
        #send to Train Model
        self.service_brake_sig.emit(1)

    def Control_Acceleration(self):
       #not sure if this part commented out is neccesary
       # if self.curr_auth_sig == 0:
        #    self.vertSliderPow.setValue(0)

       #as long as authority is not equal to zero
       if(self.curr_auth_sig > 0):
            self.ui.lcdPow_2.display(self.ui.vertSliderPow.value())
            self.ui.vertSliderBrk.setValue(0)
            #need to add a signal to change that triggers the power calculation function
            #self.curr_accel_sig.emit(self.ui.vertSliderPow.value())
            #call power function
            self.Control_Power()



    def Control_KI(self):
        self.lcdKi.display(self.inputKi.value())
        self.Control_Power()
        #self.curr_KI_sig.emit(self.inputKi.value())

    def Control_KP(self):

        self.lcdKp.display(self.inputKp.value())
        #self.curr_KI_sig.emit(self.inputKi.value())
        self.Control_Power()

    def Control_Power(self):
        # at this point in development, since we do not have time integration, dt will be static
        self.dt = 1
        self.power = (self.ui.inputKp.value() * self.ui.inputKp.value() / self.dt) * (self.ui.vertSliderPow.value()/100)
        self.ui.lcdPwrOut.display(self.power)
        self.curr_power_sig.emit(self.power)
        

        ##I think this is the correct way to do it
        
        #get current time from global clock called
        #self.time = self.globalClock
        #self.dt = self.time - self.prevTime
        #self.prevTime = self.time
        #self.error = self.lcdCmdSpd.value() - self.lcdCurSpd.value()
        #self.uk = self.prevUk + (self.error + self.prevError) * self.dt / 2
        #self.prevError = self.error
        #self.prevUk = self.uk
        #self.power = self.lcdKp.value() * self.error + self.lcdKi.value() * self.uk
        #if self.power > 120000:
        #    self.power = 120000
        #elif self.power < 0:
        #    self.power = 0
        #self.lcdPwrOut.display(self.power)
        #self.curr_power_sig.emit(self.power)





    def Control_Temperature(self,temp):
        self.ui.lcdCurTemp.display(temp)

    # called when speed changes
    def Control_Current_Speed(self,curr_speed):
        self.ui.lcdCurSpd.display(curr_speed)
        self.Speed_Montior()
        #need an internal function that will adjust other paramters as the current speed adjusts
        # over speed limit

        #if (self.lcdCmdSpd.value() > self.lcdSpdLim.value()) & (self.lcdCurSpd.value() < self.lcdCmdSpd.value()):
            #self.lcdCmdSpd.display(self.lcdSpdLim.value())
            #self.lcdCurSpd.display(self.lcdCurSpd.value() + 1)
        # if cmd is less than current speed and speed limit
        #elif (self.lcdCmdSpd.value() > self.lcdCurSpd.value()) & (self.lcdCmdSpd.value() < self.lcdSpdLim.value()):
            #self.lcdCurSpd.display(self.lcdCurSpd.value() - 1)
        #self.calcAuth(
    def Control_Speed_Limit(self,spd_lim):
        self.ui.lcdSpdLim.display(spd_lim)
        self.Speed_Montior()

    def Control_Commanded_Speed(self,cmd_spd):
        self.ui.lcdCmdSpd.display(cmd_spd)
        self.Speed_Montior()
    def Speed_Montior(self):
        if(self.ui.lcdCurSpd.value() > self.lcdCmdSpd.value() or self.ui.lcdCurSpd.value() > self.ui.lcdSpdLim.value() and self.ui.vertSliderBrk == 0):
            self.ui.vertSliderPow.setValue(0)
            self.ui.vertSliderBrk.setValue(1)
            self.ui.vertSliderPow.setDisabled(True)
        ########AUTOMATIC MODE ONLY ##########
        elif (self.ui.lcdCurSpd.value() < self.ui.lcdCmdSpd.value() and self.ui.lcdCurSpd.value() < self.ui.lcdSpdLim.value()):
            self.vertSliderBrk.setValue(0)
            self.vertSliderPow.setValue(50)
        #######################################
        else:
            self.ui.vertSliderPow.setDisabled(False)
            self.ui.vertSliderPow.setValue(0)

    # I am coming back to you
    # this function I don't get around
    def Control_Doors(self,open):
        if (self.ui.lcdAuth.value == 0):
            self.door_control_sig.emit(open)

    ## we need to call this when auth is entered from TB and we have a speed
    def Control_Authority(self):
        # update auth every second
        self.calSpeed()
        if not self.authTimer.isActive():
            self.authTimer.start()

    def Authority_Montior(self):
        # decrease auth
        # Get current speed every second from train model to calc auth for display
        if ((self.lcdAuth.value() != 0) & (self.lcdCurSpd.value() != 0)):
            self.doorControl(False)
            rate = self.lcdCurSpd.value() * 1.46667
            if self.lcdAuth.value() - rate <= 0:
                self.lcdAuth.display(0)
                self.vertSliderPow.setValue(0)
                self.lcdCurSpd.display(0)
            else:
                self.lcdAuth.display(self.lcdAuth.value() - rate)

        # target auth reached
        else:
            self.authTimer.stop()
            self.doorControl(True)


    def Control_Automatic(self):
      self.buttonMan.toggle()
      self.buttonDoorL.setDisabled(True)
      self.buttonDoorR.setDisabled(True)
      self.temp.setDisabled(True)
      self.buttonHDoff.setDisabled(True)
      self.buttonHDon.setDisabled(True)
      self.IntLightSld.setDisabled(True)
      self.lineEditAnn.setDisabled(True)
      self.inputKi.setDisabled(True)
      self.inputKp.setDisabled(True)
      self.Speed_Montior()


    def Control_Manual(self):
        self.ui.buttonAuto.toggle()
        self.ui.buttonDoorL.setDisabled(False)
        self.ui.buttonDoorR.setDisabled(False)
        self.ui.temp.setDisabled(False)
        self.ui.buttonHDon.setDisabled(False)
        self.ui.buttonHDoff.setDisabled(False)
        self.ui.IntLightSld.setDisabled(False)
        self.ui.lineEditAnn.setDisabled(False)
        self.ui.inputKi.setDisabled(False)
        self.ui.inputKp.setDisabled(False)

    def Control_Emergency_Brake(self):
        if self.ui.Ebrake.isChecked() == True:
            enable = True
        else:
            enable = False
        self.ui.buttonMan.setDisabled(enable)
        self.ui.buttonMan.setDisabled(enable)
        self.ui.buttonDoorL.setDisabled(enable)
        self.ui.buttonDoorR.setDisabled(enable)
        self.ui.temp.setDisabled(enable)
        self.ui.buttonHDoff.setDisabled(enable)
        self.ui.buttonHDon.setDisabled(enable)
        self.ui.IntLightSld.setDisabled(enable)
        self.ui.lineEditAnn.setDisabled(enable)
        self.ui.vertSliderPow.setValue(0)
        self.ui.vertSliderBrk.setValue(0)
        self.ui.vertSliderBrk.setDisabled(enable)
        self.ui.vertSliderPow.setDisabled(enable)
        self.ui.inputKi.setDisabled(enable)
        self.ui.inputKp.setDisabled(enable)


    def Control_Signal_Failure(self,sig_fail):
        if(sig_fail == True):
            self.ui.SigFail.setStyleSheet("color: red;\n"
                                          "background-color: rgb(255, 255, 255);")
            self.ui.vertSliderPow.setValue(0)
            self.ui.vertSliderBrk.setValue(1)
            self.ui.vertSliderPow.setDisabled(True)
            self.ui.vertSliderBrk.setDisabled(True)
        else:
            self.ui.SigFail.setStyleSheet("color: rgb(225, 225, 225);\n"
                                       "background-color: rgb(255, 255, 255);")
            self.ui.vertSliderPow.setDisabled(False)
            self.ui.vertSliderBrk.setDisabled(False)


    def Control_Power_Failure(self,pwr_fail):
        if pwr_fail == True:
            self.ui.PwrFail.setStyleSheet("color: red;\n"
                                          "background-color: rgb(255, 255, 255);")
            self.ui.vertSliderPow.setValue(0)
            self.ui.vertSliderBrk.setValue(1)
            self.ui.vertSliderPow.setDisabled(True)
            self.ui.vertSliderBrk.setDisabled(True)
        else:
            self.ui.PwrFail.setStyleSheet("color: rgb(225, 225, 225);\n"
                                       "background-color: rgb(255, 255, 255);")
            self.ui.vertSliderPow.setDisabled(False)
            self.ui.vertSliderBrk.setDisabled(False)


    def Control_Brake_Failure(self,brk_fail):
        if(brk_fail == True):
            self.ui.BrkFail.setStyleSheet("color: red;\n"
                                       "background-color: rgb(255, 255, 255);")
            self.ui.Ebrake.setChecked(True)
        #DISABLE
        else:
            self.ui.BrkFail.setStyleSheet("color: rgb(225, 225, 225);\n"
                                       "background-color: rgb(255, 255, 255);")
            self.ui.Ebrake.setChecked(False)

    def Control_Annoucement(self,announcement):
        self.ui.SpkrOut.setText(announcement)
        self.announcement_sig.emit(announcement)






      
