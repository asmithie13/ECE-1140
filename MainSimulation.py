#File to run full train control system simulation

import sys
from PyQt5 import QtCore,uic
from Main_UI import *
#CTC Imports
import CTC
from CTC.CTC_UI import *
from CTC.CTC_Testbench import *

#Wayside SW imports
import Wayside_SW
from Wayside_SW.WaysideSWandTB import *

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
#CTC Input Signals
MainWindow.CTC_tb.sendOccupiedBlocks.connect(MainWindow.CTCwindow.updateOccupiedBlocks)
MainWindow.CTC_tb.sendTicketSales.connect(MainWindow.CTCwindow.updateTicketSales)
#CTC Output Signals
MainWindow.CTCwindow.sendDispatchInfo.connect(MainWindow.CTC_tb.showDispatchInfo)


"""Clock Initialization"""
#Initializing Qtimer for clock
timer0 = QtCore.QTimer()
time = QtCore.QTime(0, 0, 0)    #Hours, Minutes, Second
timer0.setInterval(100)         #Interval in ms
timer0.timeout.connect(clock)
timer0.start()


sys.exit(UI_window.exec_())
