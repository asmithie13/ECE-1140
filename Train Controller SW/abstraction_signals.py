from mainControl import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, QTSignals


#functions we need to make


class Train_Controller_Signals :

    def __init__(self) : 
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

        # Add PyQT signal declarations
        signals.curr_spd =pyqSignal(int)
        signals.curr_spd.connect(Control_Speed)

   


    def Control_Service_Brake(self):
        self.lcdBrk.display(self.vertSliderBrk.value())

        if(self.lcdBrk.value() != 0):
            testvalue = self.lcdCurSpd.value() - 2.68433022233

            if (testvalue <= 0):
                self.lcdCurSpd.display(0)
            else:
                self.lcdCurSpd.display(int(testvalue))
            #value = (6 * 81000) * (self.vertSliderBrk.value() / 100)
            #self.brakePower = value
            # print(f"brake value changed to: {value}")
            self.vertSliderPow.setValue(0);
        #if self.lastSliderMoved != 'brk':
         #   self.lcdPow_2.display(0)
          #  self.vertSliderPow.setValue(0)
           # self.lastSliderMoved = 'brk'

    def Control_Acceleration(self):
        # if authority is zero, the power stays at zero
        if self.lcdAuth.value() == 0:
            self.vertSliderPow.setValue(0)
            self.lcdPowOut.display(0)

        self.lcdPow_2.display(self.vertSliderPow.value())

        self.CalcPower()
        if self.vertSliderPow.value() > 1:
            self.vertSliderBrk.setValue(0)
        self.lcdCurSpd.display(self.lcdCurSpd.value() + 20 * self.vertSliderPow.value()/100)

    def Control_KI(self):
        self.lcdKi.display(self.inputKi.value())
        self.Ki = self.inputKi.value()
        self.CalcPower()


    def Control_KP(self):
        self.lcdKp.display(self.inputKp.value())
        self.Kp = self.inputKp.value()
        self.CalcPower()
        # print(f"Kp set to: {self.Kp}")


    def Control_Power(self):
        # at this point in development, since we do not have time integration, dt will be static
        self.dt = 1
        self.power = (self.inputKp.value() * self.inputKp.value() / self.dt) * (self.vertSliderPow.value()/100)
        self.lcdPwrOut.display(self.power)

    def Control_Temperature(self):
        ##set temp



        # if self.buttonMan.setChecked() == False:
        #     self.v_error = self.v_cmd - self.v_current
        #     self.integral_error += self.v_error * self.dt
        #     self.control_output = self.Kp * self.v_error + self.Ki * self.integral_error
        #     if self.control_output > 120000:
        #         self.control_output = 120000
        #     elif self.control_output < 0:
        #         self.control_output = 0
        #
        #     self.lcdPwrOut.display(self.control_output)
        #     print(f"Control output set to: {self.control_output}")

    ################################################################################ vital stff

    # called when speed changes
    def Control_Current_Speed(self):


        # over speed limit

        #if (self.lcdCmdSpd.value() > self.lcdSpdLim.value()) & (self.lcdCurSpd.value() < self.lcdCmdSpd.value()):
            #self.lcdCmdSpd.display(self.lcdSpdLim.value())
            #self.lcdCurSpd.display(self.lcdCurSpd.value() + 1)
        # if cmd is less than current speed and speed limit
        #elif (self.lcdCmdSpd.value() > self.lcdCurSpd.value()) & (self.lcdCmdSpd.value() < self.lcdSpdLim.value()):
            #self.lcdCurSpd.display(self.lcdCurSpd.value() - 1)
        #self.calcAuth()
        if(self.lcdCurSpd.value() == 0 and self.lcdAuth.value() == 0):
            self.speedTimer.stop()
        elif(self.lcdCurSpd.value() > self.lcdCmdSpd.value() or self.lcdCurSpd.value() > self.lcdSpdLim.value() and self.vertSliderBrk == 0):
            self.vertSliderPow.setValue(0)
            self.vertSliderBrk.setValue(1)
            self.calBrakeOutput()
            self.vertSliderPow.setDisabled(True)
        elif (self.lcdCurSpd.value() < self.lcdCmdSpd.value() and self.lcdCurSpd.value() < self.lcdSpdLim.value()):
            self.vertSliderBrk.setValue(0)
            self.vertSliderPow.setValue(50)
            self.lcdCurSpd.display(self.lcdCurSpd.value() + 1)
        else:
            self.speedTimer.stop()
            self.vertSliderPow.setDisabled(False)
            self.vertSliderPow.setValue(0)

    def Control_Doors(self,enable):
        self.buttonDoorL.setEnabled(enable)
        self.buttonDoorR.setEnabled(enable)
    ## we need to call this when auth is entered from TB and we have a speed
    def calcAuth(self):
        # update auth every second
        self.calSpeed()
        if not self.authTimer.isActive():
            self.authTimer.start()


    def updateAuth(self):
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


    def Control_Manual(self):
        self.buttonAuto.toggle()
        self.buttonDoorL.setDisabled(False)
        self.buttonDoorR.setDisabled(False)
        self.temp.setDisabled(False)
        self.buttonHDon.setDisabled(False)
        self.buttonHDoff.setDisabled(False)
        self.IntLightSld.setDisabled(False)
        self.lineEditAnn.setDisabled(False)
        self.inputKi.setDisabled(False)
        self.inputKp.setDisabled(False)

    def Control_Emergency_Brake(self):
        if self.Ebrake.isChecked() == True:
            enable = True
        else :
            enable = False

        self.buttonMan.setDisabled(enable)
        self.buttonMan.setDisabled(enable)
        self.buttonDoorL.setDisabled(enable)
        self.buttonDoorR.setDisabled(enable)
        self.temp.setDisabled(enable)
        self.buttonHDoff.setDisabled(enable)
        self.buttonHDon.setDisabled(enable)
        self.IntLightSld.setDisabled(enable)
        self.lineEditAnn.setDisabled(enable)
        self.vertSliderPow.setValue(0)
        self.vertSliderBrk.setValue(0)
        self.vertSliderBrk.setDisabled(enable)
        self.vertSliderPow.setDisabled(enable)
        self.inputKi.setDisabled(enable)
        self.inputKp.setDisabled(enable)


    def Control_Signal_Failure(self):

        self.SigFail.setStyleSheet("color: red;\n"
                                      "background-color: rgb(255, 255, 255);")
        self.vertSliderPow.setValue(0)
        self.vertSliderBrk.setValue(1)
        self.vertSliderPow.setDisabled(True)
        self.vertSliderBrk.setDisabled(True)

        self.SigFail.setStyleSheet("color: rgb(225, 225, 225);\n"
                                   "background-color: rgb(255, 255, 255);")
        self.vertSliderPow.setDisabled(False)
        self.vertSliderBrk.setDisabled(False)



    
       

    def Control_Power_Failure(self):
        self.PwrFail.setStyleSheet("color: red;\n"
                                      "background-color: rgb(255, 255, 255);")
        self.vertSliderPow.setValue(0)
        self.vertSliderBrk.setValue(1)
        self.vertSliderPow.setDisabled(True)
        self.vertSliderBrk.setDisabled(True)
        //else
        self.PwrFail.setStyleSheet("color: rgb(225, 225, 225);\n"
                                   "background-color: rgb(255, 255, 255);")
        self.vertSliderPow.setDisabled(False)
        self.vertSliderBrk.setDisabled(False)


    def Control_Brake_Failure(self):
        self.BrkFail.setStyleSheet("color: red;\n"
                                   "background-color: rgb(255, 255, 255);")

        self.Ebrake.setChecked(True)
        self.ebrake_enable()

        #DISABLE
        self.BrkFail.setStyleSheet("color: rgb(225, 225, 225);\n"
                                   "background-color: rgb(255, 255, 255);")
        self.Ebrake.setChecked(False)
        self.ebrake_enable()



      
