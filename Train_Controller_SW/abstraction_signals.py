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
        self.underground_sig = pyqtSignal(bool)


        #connecting UI buttons to functions
        self.ui.Ebrake.clicked.connect(self.Control_Emergency_Brake())
        self.ui.buttonMan.clicked.connect(self.Control_Manual)
        self.ui.buttonAuto.clicked.connect(self.Control_Automatic())
        self.ui.temp.valueChanged.connect(self.Control_Temperature())
        self.ui.lineEditAnn.editingFinished.connect(self.Control_Annoucement(self.ui.lineEditAnn.text()))




    #connecting internal UI signals to interal fucntion



   



    # def Control_KI(self):
    #     self.lcdKi.display(self.inputKi.value())
    #     self.Control_Power()
    #     #self.curr_KI_sig.emit(self.inputKi.value())

    # def Control_KP(self):
    #     self.lcdKp.display(self.inputKp.value())
    #     #self.curr_KI_sig.emit(self.inputKi.value())
    #     self.Control_Power()

    # def Control_Power(self):
    #     # at this point in development, since we do not have time integration, dt will be static
    #     self.dt = 1
    #     self.power = (self.ui.inputKp.value() * self.ui.inputKp.value() / self.dt) * (self.ui.vertSliderPow.value()/100)
    #     self.ui.lcdAcel.display(self.power)
    #     self.curr_power_sig.emit(self.power)
        

        ##I think this is the correct way to do it
        






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


    # def Control_Automatic(self):
    #   self.buttonMan.toggle()
    #   self.buttonDoorL.setDisabled(True)
    #   self.buttonDoorR.setDisabled(True)
    #   self.temp.setDisabled(True)
    #   self.buttonHDoff.setDisabled(True)
    #   self.buttonHDon.setDisabled(True)
    #   self.IntLightSld.setDisabled(True)
    #   self.lineEditAnn.setDisabled(True)
    #   self.inputKi.setDisabled(True)
    #   self.inputKp.setDisabled(True)
    #   self.Speed_Montior()


    # def Control_Manual(self):
    #     self.ui.buttonAuto.toggle()
    #     self.ui.buttonDoorL.setDisabled(False)
    #     self.ui.buttonDoorR.setDisabled(False)
    #     self.ui.temp.setDisabled(False)
    #     self.ui.buttonHDon.setDisabled(False)
    #     self.ui.buttonHDoff.setDisabled(False)
    #     self.ui.IntLightSld.setDisabled(False)
    #     self.ui.lineEditAnn.setDisabled(False)
    #     self.ui.inputKi.setDisabled(False)
    #     self.ui.inputKp.setDisabled(False)





            self.ui.Ebrake.setChecked(False)

    def Control_Annoucement(self,announcement):
        self.ui.SpkrOut.setText(announcement)
        self.announcement_sig.emit(announcement)

    def Control_Underground(self,underground):
        if (underground == True):
            self.ui.underground_disp.setStyleSheet("color: red;\n"
                                          "background-color: rgb(255, 255, 255);")
            # DISABLE
        else:
            self.ui.underground_disp.setStyleSheet("color: rgb(225, 225, 225);\n"
                                          "background-color: rgb(255, 255, 255);")
    def Control_Beacon_Informattion(self,beacon_information):
        ## need to add stuff here
        ### THIS IS NOT RIGHT
        self.ui.CurrentStation.setText(beacon_information)



      
