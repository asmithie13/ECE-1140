#File that holds the data to run the CTC UI
#Abby Magistro

#pyqt imports
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

class CTC_Testbench(QtWidgets.QMainWindow):
    def __init__(self):
        super(CTC_Testbench, self).__init__()
        #Loading base UI layout from .ui file
        uic.loadUi("CTC/CTC_Testbench.ui", self)



UI_Window = QtWidgets.QApplication(sys.argv)
CTC_tb_widow = CTC_Testbench()
CTC_tb_widow.show()
UI_Window.exec_()