#File to run full train control system simulation
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject, QDateTime, QThread
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


# #Train Model Imports
# import Train_Model
# from Train_Model.app_trainmodel_ui import *
# from Train_Model.app_trainmodel_tb import *

#Train Model Imports
import Train_Model
from Train_Model.app_trainmodel_ui import *
from Train_Model.app_trainmodel_tb import *


#Simulation Time
from Simulation_Time import *

#Pauses simulation as a toggle function from button on the main UI
def pauseSim(MainWindow,sim_time):
    if MainWindow.PauseButton.isChecked():
        sim_time.pause(1)
        MainWindow.PauseButton.setText("Unpause Simulation")
    else:
        sim_time.pause(0)
        MainWindow.PauseButton.setText("Pause Simulation")
        

def update_time_slot(time_str):
    MainWindow.CTCwindow.displayClock(time_str)
    MainWindow.TrackModelWindow.set_clock(time_str)
    for train in MainWindow.currentTrains:
        train.update_time(time_str)


def timer_thread(sim_time):
    sim_time.updatetime()

# if __name__ == "__main__":
    
#     # Starting PyQt application
#     UI_window = QtWidgets.QApplication(sys.argv)

#     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    
#     # Initializing Main Window
#     MainWindow = Main_UI()
#     "CTC Signals"
#     MainWindow.CTC_tb.sendOccupiedBlocks.connect(MainWindow.CTCwindow.updateOccupiedBlocks)
#     MainWindow.CTC_tb.sendTicketSales.connect(MainWindow.CTCwindow.updateTicketSales)
#     MainWindow.CTCwindow.sendDispatchInfo.connect(MainWindow.CTC_tb.showDispatchInfo)

#     #CTC to Wayside SW
#     MainWindow.CTCwindow.sendDispatchInfo.connect(MainWindow.WaysideSWwindow.receiveSpeedAuth)

#     #CTC to Wayside HW
#     MainWindow.CTCwindow.sendBlockClosures.connect(MainWindow.WaysideHWwindow.getClosedBlocks)
#     MainWindow.CTCwindow.sendDispatchInfo.connect(MainWindow.WaysideHWwindow.handleSpeedAuthority)

#     #CTC to MainWindow
#     MainWindow.CTCwindow.create_a_train.connect(MainWindow.create_new_train)

#     """Wayside SW Signals"""
#     MainWindow.WaysideSWwindow.sendSpecialBlocks.connect(MainWindow.WaysideSW_tb.updateBlockStates)
#     MainWindow.WaysideSWwindow.changeModeSend.connect(MainWindow.WaysideSW_tb.receiveMode)
#     MainWindow.WaysideSWwindow.sendAllBlocks.connect(MainWindow.WaysideSW_tb.receiveBlocks)
#     MainWindow.WaysideSWwindow.sendTrainSpeedAuth.connect(MainWindow.WaysideSW_tb.displaySpeedAuth)
#     MainWindow.WaysideSW_tb.OccBlocksChanged.connect(MainWindow.WaysideSWwindow.updateBlocks)
#     MainWindow.WaysideSW_tb.tbChangeMode.connect(MainWindow.WaysideSWwindow.changeMode)
#     MainWindow.WaysideSW_tb.ctcIDSpeedAuthority.connect(MainWindow.WaysideSWwindow.receiveSpeedAuth)

#     #Wayside to CTC
#     MainWindow.WaysideSWwindow.sendOccupiedBlocks.connect(MainWindow.CTCwindow.recieveOccupiedBlocksG2)
#     #MainWindow.WaysideHWwindow.sendOccupiedBlocks.connect(MainWindow.CTCwindow.recieveOccupiedBlocksR1)
#     #MainWindow.WaysideHWwindow.sendOccupiedBlocks.connect(MainWindow.CTCwindow.recieveOccupiedBlocksR2)

#     #Wayside to Track Model
#     MainWindow.WaysideSWwindow.sendTrainSpeedAuth.connect(MainWindow.TrackModelWindow.receiveSpeedAuth_tm)
#     MainWindow.WaysideSWwindow.sendAllBlocks.connect(MainWindow.TrackModelWindow.recieveSpecialBlocks)

#     """Wayside HW Signals"""
#     MainWindow.WaysideHWwindow.sendOccupiedBlocks.connect(MainWindow.WaysideHW_tb.receiveOccupiedBlocks)
#     MainWindow.WaysideHWwindow.sendSpeedAuthority.connect(MainWindow.WaysideHW_tb.receiveSpeedAuthority)
#     MainWindow.WaysideHWwindow.sendUpdatedBlocks.connect(MainWindow.WaysideHW_tb.receiveUpdatedBlocks)
#     MainWindow.WaysideHW_tb.speedAuthoritySignal.connect(MainWindow.WaysideHWwindow.handleSpeedAuthority)
#     MainWindow.WaysideHW_tb.occupiedBlocksSignal.connect(MainWindow.WaysideHWwindow.modeHandler)
#     MainWindow.WaysideHW_tb.closedBlocksSignal.connect(MainWindow.WaysideHWwindow.getClosedBlocks)

#     #Wayside HW to CTC:
#     MainWindow.WaysideHWwindow.sendOccupiedBlocks.connect(MainWindow.CTCwindow.recieveOccupiedBlocksG1)

#     #Wayside HW to Track Model:
#     MainWindow.WaysideHWwindow.sendSpeedAuthority.connect(MainWindow.TrackModelWindow.receiveSpeedAuth_tm)

#     """Track Model Signals"""
#     MainWindow.TrackModelWindow.send_com_speed_tb.connect(MainWindow.TrackModel_tb.update_commanded_speed)
#     MainWindow.TrackModelWindow.send_authority_tb.connect(MainWindow.TrackModel_tb.update_authority)


#     # Connecting signal from SimulationTime to slot in Main_UI
#     sim_time = SimulationTime() 
#     # Create QThread
#     sim_thread = QtCore.QThread()
#     # Move worker object to the thread
#     sim_time.moveToThread(sim_thread)
#     sim_time.timeChanged.connect(update_time_slot)


#     #Connecting Main UI functionality signals
#     MainWindow.SpeedSlider.valueChanged.connect(sim_time.set_sim_speed)
#     MainWindow.PauseButton.clicked.connect(lambda : sim_time.pause(MainWindow.PauseButton.isChecked()))


#     # Starting simulation thread
#     #simulation_thread = threading.Thread(target=timer_thread, args=(sim_time,))
#     sim_thread.start()
#     sim_time.start()

   
#     MainWindow.show()
#     exit_code = qApp.exec_()
#     sim_thread.quit()
#     sim_thread.wait()
#     sys.exit(exit_code)

if __name__ == "__main__":
    # Starting PyQt application
    app = QtWidgets.QApplication(sys.argv)
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    # Initializing Main Window
    MainWindow = Main_UI()
    # Setup connections and signals as before
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
    MainWindow.WaysideSW_tb.OccBlocksChanged.connect(MainWindow.WaysideSWwindow.updateBlocks)
    MainWindow.WaysideSW_tb.tbChangeMode.connect(MainWindow.WaysideSWwindow.changeMode)
    MainWindow.WaysideSW_tb.ctcIDSpeedAuthority.connect(MainWindow.WaysideSWwindow.receiveSpeedAuth)

    #Wayside to CTC
    MainWindow.WaysideSWwindow.sendOccupiedBlocks.connect(MainWindow.CTCwindow.recieveOccupiedBlocksG2)
    #MainWindow.WaysideHWwindow.sendOccupiedBlocks.connect(MainWindow.CTCwindow.recieveOccupiedBlocksR1)
    #MainWindow.WaysideHWwindow.sendOccupiedBlocks.connect(MainWindow.CTCwindow.recieveOccupiedBlocksR2)

    #Wayside to Track Model
    MainWindow.WaysideSWwindow.sendTrainSpeedAuth.connect(MainWindow.TrackModelWindow.receiveSpeedAuth_tm)
    MainWindow.WaysideSWwindow.sendAllBlocks.connect(MainWindow.TrackModelWindow.receiveSpecialBlocks_SW)

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
    MainWindow.WaysideHWwindow.sendUpdatedBlocks.connect(MainWindow.TrackModelWindow.receiveSpecialBlocks_HW)

    """Track Model Signals"""
    MainWindow.TrackModelWindow.send_com_speed_tb.connect(MainWindow.TrackModel_tb.update_commanded_speed)
    MainWindow.TrackModelWindow.send_authority_tb.connect(MainWindow.TrackModel_tb.update_authority)

    #Track Model to Wayside_SW
    MainWindow.TrackModelWindow.sendBlockOcc_SW.connect(MainWindow.WaysideSWwindow.updateBlocks)    # Move the sim_time instance to the new thread
    
    #Track Model to Wayside_HW
    MainWindow.TrackModelWindow.sendBlockOcc_HW.connect(MainWindow.WaysideHWwindow.modeHandler)

    # SimulationTime Setup
    sim_time = SimulationTime()  # Ensure this class inherits from QObject
    sim_thread = QtCore.QThread()  # Create a new QThread
    
    sim_time.moveToThread(sim_thread)

    # Connect the sim_time's start method to the thread's started signal
    sim_thread.started.connect(sim_time.updatetime)  # Assuming updatetime starts the simulation loop

    # Connect the timeChanged signal to the update_time_slot function
    sim_time.timeChanged.connect(update_time_slot)

    # Start the thread
    sim_thread.start()

    # UI connections
    MainWindow.SpeedSlider.valueChanged.connect(lambda : sim_time.set_sim_speed(MainWindow.SpeedSlider.value()))
    MainWindow.PauseButton.clicked.connect(lambda : pauseSim(MainWindow, sim_time))

    MainWindow.show()

    sys.exit(app.exec_())

