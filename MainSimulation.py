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


#Utility function to initialize clock
def clock():
    global time
    time = time.addSecs(60)

    current_time = time.toString("hh:mm")
    #Pulling clock data for CTC UI
    MainWindow.CTCwindow.displayClock(current_time)

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


"""Track Model Signals"""
MainWindow.TrackModelWindow.send_com_speed_tb.connect(MainWindow.TrackModel_tb.update_commanded_speed)
MainWindow.TrackModelWindow.send_authority_tb.connect(MainWindow.TrackModel_tb.update_authority)

#Track Model to CTC
MainWindow.TrackModelWindow.SendTicketsales.connect(MainWindow.CTCwindow.recieveTicketSales)

"""Clock Initialization"""
#Initializing Qtimer for clock
timer0 = QtCore.QTimer()
time = QtCore.QTime(0, 0, 0)    #Hours, Minutes, Second
timer0.setInterval(100)         #Interval in ms
timer0.timeout.connect(clock)
timer0.start()
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)


sys.exit(UI_window.exec_())
