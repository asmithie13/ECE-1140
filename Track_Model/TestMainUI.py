import sys
from PyQt5 import QtCore
#Add CTC Imports
import CTC
from CTC.CTC_UI import *
from CTC.CTC_Testbench import *

#Add Wayside SW Imports
import Wayside_SW
from Wayside_SW.app import *



def clock():
    global time
    time = time.addSecs(60)

    current_time = time.toString("hh:mm")
    CTCwindow.displayClock(current_time)

UI_window = QtWidgets.QApplication(sys.argv)

"""CTC"""
#CTC UI connection
global CTCwindow
CTCwindow = CTC_UI()
CTCwindow.show()
#CTC Testbench connection
global CTC_tb
CTC_tb = CTC_Testbench()
CTC_tb.show()

#Wayside SW
window = MyApp()
window2 = TestBench()

#CTC Input Signals
CTC_tb.sendOccupiedBlocks.connect(CTCwindow.updateOccupiedBlocks)
window2.OccBlocksChanged.connect(CTCwindow.updateOccupiedBlocks)
CTC_tb.sendTicketSales.connect(CTCwindow.updateTicketSales)
#CTC Output Signals
CTCwindow.sendDispatchInfo.connect(CTC_tb.showDispatchInfo)


"""Wayside SW"""
#Signal: Window
window.sendSpecialBlocks.connect(window2.updateBlockStates)
window.changeModeSend.connect(window2.receiveMode)

#Signal: Window 2
window2.OccBlocksChanged.connect(window.updateBlocks)
window2.tbChangeMode.connect(window.changeMode)

window.show()
window2.show()




"""Clock"""
#Initializing Qtimer for clock
timer0 = QtCore.QTimer()
time = QtCore.QTime(0, 0, 0)    #Hours, Minutes, Second
timer0.setInterval(100)
timer0.timeout.connect(clock)
timer0.start()



sys.exit(UI_window.exec_())