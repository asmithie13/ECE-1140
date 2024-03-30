#File to run full train control system simulation
import sys
from PyQt5 import QtCore
from Main_UI import *

#CTC Imports
import CTC
from CTC.CTC_UI import *
from CTC.CTC_Testbench import *

#Wayside SW imports
import Wayside_SW
from Wayside_SW.WaysideSWandTB import *

#Wayside HW imports
import Wayside_HW
from Wayside_HW.TrackController_HW import *
from Wayside_HW.TrackController_HW_TB import *

#Track Model imports
import Track_Model
from Track_Model.TrackModel import *

#Train Model Imports
import Train_Model
from Train_Model.app_trainmodel_ui import *
from Train_Model.app_trainmodel_tb import *

#Utility function to update the clock
def clock():
    global time
    time = time.addSecs(1)
    current_time = time.toString("hh:mm")

    #Pulling clock data for CTC and Track Model
    MainWindow.CTCwindow.displayClock(current_time)
    MainWindow.TrackModelWindow.set_clock(current_time)

    #Pulling clock data for each train in existance
    for train in MainWindow.currentTrains:
        train.update_time(time)

#Modifies speed of simulation based of slider on the main UI    
def updateClockSpeed():
        SliderValue = MainWindow.SpeedSlider.value()
        
        timer.setInterval(int(1000 / SliderValue))   
        timer.timeout.connect(clock)
        timer.start()

        MainWindow.CurrentSpeedLabel.setText("Current Speed: "+str(SliderValue)+"x") 

#Pauses simulation as a toggle function from button on the main UI
def pauseSim():
    if MainWindow.PauseButton.isChecked():
          timer.stop()
          MainWindow.PauseButton.setText("Unpause Simulation")
    else:
         timer.start()
         MainWindow.PauseButton.setText("Pause Simulation")


#Starting PyQt application
UI_window = QtWidgets.QApplication(sys.argv)

#Initializing Main Window
global MainWindow
MainWindow = Main_UI()

MainWindow.show()

"""CTC Signals"""
MainWindow.CTC_tb.sendOccupiedBlocks.connect(MainWindow.CTCwindow.updateOccupiedBlocks)
MainWindow.CTC_tb.sendTicketSales.connect(MainWindow.CTCwindow.updateTicketSales)
MainWindow.CTCwindow.sendDispatchInfo.connect(MainWindow.CTC_tb.showDispatchInfo)

#CTC to Wayside
MainWindow.CTCwindow.sendDispatchInfo.connect(MainWindow.WaysideSWwindow.receiveSpeedAuth)

#CTC to MainWindow
MainWindow.CTCwindow.create_a_train.connect(MainWindow.create_new_train)

"""Wayside SW Signals"""
MainWindow.WaysideSWwindow.sendSpecialBlocks.connect(MainWindow.WaysideSW_tb.updateBlockStates)
MainWindow.WaysideSWwindow.changeModeSend.connect(MainWindow.WaysideSW_tb.receiveMode)
MainWindow.WaysideSWwindow.sendAllBlocks.connect(MainWindow.WaysideSW_tb.receiveBlocks)
MainWindow.WaysideSW_tb.OccBlocksChanged.connect(MainWindow.WaysideSWwindow.updateBlocks)
MainWindow.WaysideSW_tb.tbChangeMode.connect(MainWindow.WaysideSWwindow.changeMode)
MainWindow.WaysideSW_tb.ctcIDSpeedAuthority.connect(MainWindow.WaysideSWwindow.receiveSpeedAuth)

#Wayside to CTC
MainWindow.WaysideSWwindow.sendOccupiedBlocks.connect(MainWindow.CTCwindow.recieveOccupiedBlocks)

#Wayside to Track Model
MainWindow.WaysideSWwindow.sendTrainSpeedAuth.connect(MainWindow.TrackModelWindow.receiveSpeedAuth_tm)
MainWindow.WaysideSWwindow.sendAllBlocks.connect(MainWindow.TrackModelWindow.recieveSpecialBlocks)

"""Wayside HW Signals"""
MainWindow.WaysideHWwindow.sendOccupiedBlocks.connect(MainWindow.WaysideHW_tb.receiveOccupiedBlocks)
MainWindow.WaysideHWwindow.sendSpeedAuthority.connect(MainWindow.WaysideHW_tb.receiveSpeedAuthority)
MainWindow.WaysideHWwindow.sendUpdatedBlocks.connect(MainWindow.WaysideHW_tb.receiveUpdatedBlocks)
MainWindow.WaysideHW_tb.speedAuthoritySignal.connect(MainWindow.WaysideHWwindow.handleSpeedAuthority)
MainWindow.WaysideHW_tb.occupiedBlocksSignal.connect(MainWindow.WaysideHWwindow.modeHandler)
MainWindow.WaysideHW_tb.closedBlocksSignal.connect(MainWindow.WaysideHWwindow.getClosedBlocks)

"""Track Model Signals"""
MainWindow.TrackModelWindow.send_com_speed_tb.connect(MainWindow.TrackModel_tb.update_commanded_speed)
MainWindow.TrackModelWindow.send_authority_tb.connect(MainWindow.TrackModel_tb.update_authority)


#Track Model to CTC
MainWindow.TrackModelWindow.SendTicketsales.connect(MainWindow.CTCwindow.recieveTicketSales)

"""Clock Initialization"""
#Initializing Qtimer for clock
global timer 
timer = QtCore.QTimer()
time = QtCore.QTime(0, 0, 0)    #Hours, Minutes, Second
timer.setInterval(1000)         #Interval in ms
timer.timeout.connect(clock)

#Initializing Time on clock for CTC
MainWindow.CTCwindow.displayClock(time.toString("hh:mm"))
MainWindow.TrackModelWindow.set_clock(time.toString("hh:mm"))


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

#Connecting Main UI functionality signals
MainWindow.SpeedSlider.sliderReleased.connect(updateClockSpeed)
MainWindow.PauseButton.clicked.connect(pauseSim)


sys.exit(UI_window.exec_())
