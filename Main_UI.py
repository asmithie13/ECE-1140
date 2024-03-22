#pyqt imports
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
#CTC Imports
import CTC
from CTC.CTC_UI import *
from CTC.CTC_Testbench import *
#Wayside SW imports
import Wayside_SW
from Wayside_SW.WaysideSWandTB import *
#Track Model Imports
import Track_Model
from Track_Model.TrackModel import * 

class Main_UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main_UI, self).__init__()
        #Loading base UI layout from .ui file
        uic.loadUi("MainUI.ui", self)

        #CTC UI Window
        self.CTCwindow = CTC_UI()
        self.CTC_tb = CTC_Testbench()
        self.CTC_Button.clicked.connect(self.open_CTC_UI)

        #Wayside SW Window
        self.WaysideSWwindow = WaysideSW()
        self.WaysideSW_tb = TestBench()
        self.WaysideSW_Button.clicked.connect(self.open_waysideSW_UI)

        #Wayside HW Window


        #Track Model Window
        self.TrackModelWindow = TrackModelMain()
        self.TrackModel_tb = TrackModel_tb()
        self.TrackModelButton.clicked.connect(self.open_track_model_UI)

        #Train Model (Might need initialized per train)


        #Train Controller SW (Might need initialized per train)


        #Train Controller HW (Might need initialized per train)



    def open_CTC_UI(self):
        self.CTCwindow.show()
        self.CTC_tb.show()

    def open_waysideSW_UI(self):
        self.WaysideSWwindow.show()
        self.WaysideSW_tb.show() 

    def open_track_model_UI(self):
        self.TrackModelWindow.show()
        self.TrackModel_tb.show()


"""
UI_window = QtWidgets.QApplication(sys.argv)
window = MainUI()
window.show()
UI_window.exec_()
"""