import sys

from PyQt5 import QtCore
from CTC_UI import *

class Clock:
    def __init__(self):
        self.time = ""


def calculo():
    global time
    time = time.addSecs(60)

    ourClock.time = time.toString("hh:mm")
    window.displayClock(ourClock.time)
    #print(ourClock.time)

#app = QtCore.QCoreApplication(sys.argv)
UI_window = QtWidgets.QApplication(sys.argv)
    #Test#
global window
window = UI()
window.show()

global ourClock
ourClock = Clock()

timer0 = QtCore.QTimer()
time = QtCore.QTime(11, 0, 0)
timer0.setInterval(100)
timer0.timeout.connect(calculo)
timer0.start()



sys.exit(UI_window.exec_())