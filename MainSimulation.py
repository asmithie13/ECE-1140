#File to run full train control system simulation
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject, QDateTime
import threading
import time
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


#Simulation Time
from Simulation_Time import *


def MainWindow_Connect(self,MainWindow):
    "CTC Signals"
    MainWindow.CTC_tb.sendOccupiedBlocks.connect(MainWindow.CTCwindow.updateOccupiedBlocks)
    MainWindow.CTC_tb.sendTicketSales.connect(MainWindow.CTCwindow.updateTicketSales)
    MainWindow.CTCwindow.sendDispatchInfo.connect(MainWindow.CTC_tb.showDispatchInfo)

    #CTC to Wayside SW
    MainWindow.CTCwindow.sendDispatchInfo.connect(MainWindow.WaysideSWwindow.receiveSpeedAuth)

    #CTC to Wayside HW
    MainWindow.CTCwindow.sendBlockClosures.connect(MainWindow.WaysideHWwindow.getClosedBlocks)
    MainWindow.CTCwindow.sendDispatchInfo.connect(MainWindow.WaysideHWwindow.handleSpeedAuthority)

    #CTC to MainWindow
    MainWindow.CTCwindow.create_a_train.connect(MainWindow.create_new_train)

    """Wayside SW Signals"""
    MainWindow.WaysideSWwindow.sendSpecialBlocks.connect(MainWindow.WaysideSW_tb.updateBlockStates)
    MainWindow.WaysideSWwindow.changeModeSend.connect(MainWindow.WaysideSW_tb.receiveMode)
    MainWindow.WaysideSWwindow.sendAllBlocks.connect(MainWindow.WaysideSW_tb.receiveBlocks)
    MainWindow.WaysideSWwindow.sendTrainSpeedAuth.connect(MainWindow.WaysideSW_tb.displaySpeedAuth)
    MainWindow.WaysideSW_tb.OccBlocksChanged.connect(MainWindow.WaysideSWwindow.updateBlocks)
    MainWindow.WaysideSW_tb.tbChangeMode.connect(MainWindow.WaysideSWwindow.changeMode)
    MainWindow.WaysideSW_tb.ctcIDSpeedAuthority.connect(MainWindow.WaysideSWwindow.receiveSpeedAuth)

    #Wayside to CTC
    MainWindow.WaysideSWwindow.sendOccupiedBlocks.connect(MainWindow.CTCwindow.recieveOccupiedBlocksG2)
    #MainWindow.WaysideHWwindow.sendOccupiedBlocks.connect(MainWindow.CTCwindow.recieveOccupiedBlocksR1)
    #MainWindow.WaysideHWwindow.sendOccupiedBlocks.connect(MainWindow.CTCwindow.recieveOccupiedBlocksR2)

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

    #Wayside HW to CTC:
    MainWindow.WaysideHWwindow.sendOccupiedBlocks.connect(MainWindow.CTCwindow.recieveOccupiedBlocksG1)

    #Wayside HW to Track Model:
    MainWindow.WaysideHWwindow.sendSpeedAuthority.connect(MainWindow.TrackModelWindow.receiveSpeedAuth_tm)

    """Track Model Signals"""
    MainWindow.TrackModelWindow.send_com_speed_tb.connect(MainWindow.TrackModel_tb.update_commanded_speed)
    MainWindow.TrackModelWindow.send_authority_tb.connect(MainWindow.TrackModel_tb.update_authority)


def update_time_slot(time_str):
    MainWindow.CTCwindow.displayClock(time_str)
    MainWindow.TrackModelWindow.set_clock(time_str)

def timer_thread(sim_time):
    sim_time.updatetime()

if __name__ == "__main__":
    
    # Starting PyQt application
    UI_window = QtWidgets.QApplication(sys.argv)
    
    # Initializing Main Window
    MainWindow = Main_UI()
    MainWindow_Connect(MainWindow)
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    #Connecting Main UI functionality signals
    MainWindow.SpeedSlider.valueChanged.connect(sim_thread.set_sim_speed)
    MainWindow.PauseButton.clicked.connect(lambda : sim_thread.pause(MainWindow.PauseButton.isChecked()))


    # Connecting signal from SimulationTime to slot in Main_UI
    sim_time = SimulationTime()
    sim_time.timeChanged.connect(update_time_slot)

    # Starting simulation thread
    simulation_thread = threading.Thread(target=timer_thread, args=(sim_time,))
    simulation_thread.start()

   
    MainWindow.show()
    sys.exit(UI_window.exec_())

