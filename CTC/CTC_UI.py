import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
#from UI_temp import MainWindow

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("CTC/CTC_UI.ui", self)
        self.show()


test = QtWidgets.QApplication(sys.argv)
window = UI()
test.exec_()