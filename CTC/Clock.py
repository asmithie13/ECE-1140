import sys

from PyQt5 import QtCore

class Clock:
    def __init__(self):
        self.time = ""


def calculo():
    global time
    time = time.addSecs(60)

    ourClock.time = time.toString("dd hh:mm:ss")
    print(ourClock.time)

app = QtCore.QCoreApplication(sys.argv)

global ourClock
ourClock = Clock()

timer0 = QtCore.QTimer()
time = QtCore.QTime(0, 0, 0)
timer0.setInterval(1000)
timer0.timeout.connect(calculo)
timer0.start()

app.exec_()
#sys.exit(app.exec_())