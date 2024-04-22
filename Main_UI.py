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
        self.CTCwindow.resize(850, 600)     #width, height
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
        self.TrainModelButton.clicked.connect(self.open_train_model_UI)
        #self.TrainModelWindow = TrainModel_mainwindow()
        #self.TrackModel_tb = trainmodel_testbench()
        #self.TrainModelWindow.show()
        #self.TrainModelButton.clicked.connect(self.create_new_train)

        #Train Controller SW (Might need initialized per train)
        self.TrainController_Button.clicked.connect(self.open_train_controller_UI)

        #Train Controller HW (Might need initialized per train)


    def open_CTC_UI(self):
        self.CTCwindow.show()
        #self.CTC_tb.show()

    def open_waysideSW_UI(self):
        self.WaysideSWwindow.show()
        #self.WaysideSW_tb.show() 
    
    def open_waysideHW_UI(self):
        self.WaysideHWwindow.show()
        #self.WaysideHW_tb.show()

    def open_track_model_UI(self):
        # Define the path to the mainControl.py file
        #track_model_path = "Track_Model/TrackModel.py"

        # Run mainControl.py as a separate process
        #subprocess.Popen(["python", track_model_path])
        self.TrackModelWindow.show()
        #self.TrackModel_tb.show()

    def create_new_train(self, TrainID, line):
        #Add new train UI to list
        self.currentTrains.append(TrainModel_mainwindow(TrainID))
        self.currentTrains[-1].show()

        #Track Model Dispatch Train Function
        self.TrackModelWindow.get_train_id(TrainID, line)

        #Track Model to Train Model
        # [Train ID, commanded speed, authority]
        self.TrackModelWindow.sendSpeedAuth.connect(self.currentTrains[-1].receiveSpeedAuth_tm)
        
        # Grade for the next block
        self.TrackModelWindow.grade_signal_tm.connect(self.currentTrains[-1].set_grade)

        #Beacon info
        self.TrackModelWindow.send_beacon.connect(self.currentTrains[-1].receive_beacon_info)


        #Ticket sales
        #self.TrackModelWindow.people_boarding_sig.connect(self.currentTrains[-1].set_pcount)

        #Polarity
        self.TrackModelWindow.send_polarity.connect(self.currentTrains[-1].receive_polarity)
        
        #Train Model to Track Model
        # Actual Velocity
        self.currentTrains[-1].track_model_acc_velo.connect(self.TrackModelWindow.receiveSendVelocity)

        #Train stops
        #self. currentTrains[-1].stop_at_station_sig.connect(self.TrackModelWindow.train_stop)

        #People disembarking
        self.currentTrains[-1].people_disemb_sig.connect(self.TrackModelWindow.people_disem)

        #Connect Signals to Track Model
        #self.currentTrains[-1].sendSignalToTrack.(self.TrackModelWindow.recieveSignalFromTrain)

        self.TrainSelect.addItem(TrainID)
    
    #destroy a train object when it goes off the track, based on the TrainID string
    def destroy_train(self, TrainID):
        #Get train num
        TrainNum = int(TrainID[1:]) - 1
        
        if TrainNum < len(self.currentTrains): 
            if self.currentTrains[TrainNum] != 0:
                #Close UIs if open
                self.currentTrains[TrainNum].TC.Close_UI()
                self.currentTrains[TrainNum].close()
                
                #Delete train instance (Will also delete the train controller)
                del self.currentTrains[TrainNum]
                self.currentTrains.insert(TrainNum, 0)


    def open_train_model_UI(self):
        #Error checking that a train actually exists
        if len(self.currentTrains) == 0:
            #Popup a message if the user enters a block that isn't closed
            error_msg = QMessageBox()
            error_msg.setWindowTitle("Selection Error")
            error_msg.setText("No trains currently exist. Please dispatch a train to open the Trian Model UI.")
            error_msg.setIcon(QMessageBox.Critical)

            error_msg.exec_() 

            return
        
        TrainID = self.TrainSelect.currentText() 
        TrainNum = int(TrainID[1:])

        self.currentTrains[TrainNum - 1].show()

    def open_train_controller_UI(self):
        #Error checking that a train actually exists
        if len(self.currentTrains) == 0:
            #Popup a message if the user enters a block that isn't closed
            error_msg = QMessageBox()
            error_msg.setWindowTitle("Selection Error")
            error_msg.setText("No trains currently exist. Please dispatch a train to open the Trian Model UI.")
            error_msg.setIcon(QMessageBox.Critical)

            error_msg.exec_() 

            return
        
        TrainID = self.TrainSelect.currentText() 
        TrainNum = int(TrainID[1:])

        #Pull train controller UI
        self.currentTrains[TrainNum - 1].TC.Open_Main_UI()


"""
UI_window = QtWidgets.QApplication(sys.argv)
window = MainUI()
window.show()
UI_window.exec_()
"""