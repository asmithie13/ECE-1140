import sys
from PyQt5 import QtCore


#Fixing file hierarchy issues
import os
import re
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

import CTC
from CTC.CTC_UI import *
from CTC.CTC_Testbench import *

class Clock(QtCore.QObject):
    # Define a signal to emit the current time
    current_time_changed = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_time)
        self.time = QtCore.QTime(0, 0, 0)
        self.timer.start(1000)  # Update time every second

    def update_time(self):
        self.time = self.time.addSecs(1)
        current_time = self.time.toString("hh:mm:ss")
        self.current_time_changed.emit(current_time)

if __name__ == "__main__":
    clock = Clock()
    app = QtWidgets.QApplication(sys.argv)

    # Start the main event loop
    sys.exit(app.exec_())


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