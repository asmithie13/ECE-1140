import sys
from PyQt5 import QtCore
from CTC_UI import *
from CTC_Testbench import *


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

#CTC Input Signals
CTC_tb.sendOccupiedBlocks.connect(CTCwindow.updateOccupiedBlocks)
CTC_tb.sendTicketSales.connect(CTCwindow.updateTicketSales)
#CTC Output Signals
CTCwindow.sendDispatchInfo.connect(CTC_tb.showDispatchInfo)




"""Clock"""
#Initializing Qtimer for clock
timer0 = QtCore.QTimer()
time = QtCore.QTime(0, 0, 0)    #Hours, Minutes, Second
timer0.setInterval(100)         #Interval in ms
timer0.timeout.connect(clock)
timer0.start()



sys.exit(UI_window.exec_())