import sys

from PyQt5 import QtCore
from CTC_UI import *


def clock():
    global time
    time = time.addSecs(60)

    current_time = time.toString("hh:mm")
    CTCwindow.displayClock(current_time)

#app = QtCore.QCoreApplication(sys.argv)
UI_window = QtWidgets.QApplication(sys.argv)

#CTC UI connection
global CTCwindow
CTCwindow = UI()
CTCwindow.show()

#Initializing Qtimer for clock
timer0 = QtCore.QTimer()
time = QtCore.QTime(0, 0, 0)    #Hours, Minutes, Second
timer0.setInterval(1000)
timer0.timeout.connect(clock)
timer0.start()



sys.exit(UI_window.exec_())