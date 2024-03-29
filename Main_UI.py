#pyqt imports
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import subprocess

#CTC Imports
import CTC
from CTC.CTC_UI import *
from CTC.CTC_Testbench import *

#Wayside SW imports
import Wayside_SW
from Wayside_SW.WaysideSWandTB import *

#Wayside HW imports
import Wayside_HW
from Wayside_HW.TrackController_HW import *
from Wayside_HW.TrackController_HW_TB import *

#Track Model Imports
import Track_Model
from Track_Model.TrackModel import *

#Train Model Imports
import Train_Model
from Train_Model.app_trainmodel_ui import *
from Train_Model.app_trainmodel_tb import *


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
        self.WaysideHWwindow = TrackController_HW()
        self.WaysideHW_tb = TrackController_HW_TB()
        self.WaysideHW_Button.clicked.connect(self.open_waysideHW_UI)

        #Track Model Window
        self.TrackModelWindow = TrackModelMain()
        self.TrackModel_tb = TrackModel_tb()
        self.TrackModelButton.clicked.connect(self.open_track_model_UI)

        #Train Model (Might need initialized per train)
        self.currentTrains = []
        #self.TrainModelWindow = TrainModel_mainwindow()
        #self.TrackModel_tb = trainmodel_testbench()
        #self.TrainModelWindow.show()
        self.TrainModelButton.clicked.connect(self.create_new_train)

        #Train Controller SW (Might need initialized per train)


        #Train Controller HW (Might need initialized per train)



    def open_CTC_UI(self):
        self.CTCwindow.show()
        self.CTC_tb.show()

    def open_waysideSW_UI(self):
        self.WaysideSWwindow.show()
        self.WaysideSW_tb.show() 
    
    def open_waysideHW_UI(self):
        self.WaysideHWwindow.show()
        self.WaysideHW_tb.show()

    def open_track_model_UI(self):
        # Define the path to the mainControl.py file
        #track_model_path = "Track_Model/TrackModel.py"

        # Run mainControl.py as a separate process
        #subprocess.Popen(["python", track_model_path])
        self.TrackModelWindow.show()
        self.TrackModel_tb.show()

    def create_new_train(self, TrainID):
        #Add new train UI to list
        self.currentTrains.append(TrainModel_mainwindow())
        self.currentTrains[-1].show()

        #Track Model to Train Model
        # [Train ID, commanded speed, authority]
        self.TrackModelWindow.sendSpeedAuth.connect(self.currentTrains[-1].receiveSpeedAuth_tm)

        #Train Model to Track Model
        # Actual Velocity
        #self.currentTrains[-1].function.connect(self.TrackModelWindow.receiveSendVelocity)

        #Connect Signals to Track Model
        #self.currentTrains[-1].sendSignalToTrack.(self.TrackModelWindow.recieveSignalFromTrain)



"""
UI_window = QtWidgets.QApplication(sys.argv)
window = MainUI()
window.show()
UI_window.exec_()
"""