#File to run the UI for the CTC Module
#Abby Magistro

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from Schedule import *
from Clock import *
#from UI_temp import MainWindow



class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        #Loading base UI layout from .ui file
        uic.loadUi("CTC/CTC_UI.ui", self)


        #Connect Buttons to signals defining behavior
        self.UploadButton.clicked.connect(self.open_files)
        self.ManualModeButton.clicked.connect(self.selectManualMode_button)
        self.AddTrainButton.clicked.connect(self.addTrain_button)

        #Changing Button Colors
        self.AddTrainButton.setStyleSheet("background-color : rgb(38, 207, 4)")
        self.UploadButton.setStyleSheet("background-color : rgb(38, 207, 4)")

        #Changing Background colors to section off UI
        self.MaualDispatchBox.setStyleSheet("background-color : rgb(233, 247, 255);")

        #Manual Dispatch Formatting
        self.ArrivalTimeEdit.setDisplayFormat("hh:mm")
        self.DepartureTimeEdit.setDisplayFormat("hh:mm")

        #Add the clock
        #self.Clock = QtCore.QTimer(self)
        #self.Clock.timeout.connect(self.showTime(time))
        self.Clock.display(ourClock.time)

        #Initializing Schedule
        self.trainSchedule = Schedule()
        self.ScheduleTable.setModel(TableModel(self.trainSchedule.Scheduledata))
        
        

        


    #Define functionality for Upload File Button
    def open_files(self):
        # Open a file dialog to select a Excel File
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Schedule File", "", "Excel Workbook (*.xlsx);;All Files (*)")

        """
        #TO DO LATER
        if file_path:
            # Implement your logic with the selected file path
            print(f"Selected PLC File: {file_path}")
        """
    

    #Define mutually exclisive auto/manual mode
    def selectManualMode_button(self):
        #When Manual Mode button is pressed

        #Disable AutoMode Button
        self.AutoModeButton.setEnabled(False)
        #And File Upload Button
        self.UploadButton.setEnabled(False)
        self.UploadButton.setStyleSheet("background-color : #ebfae8")

        #Disable Manual Mode button (because it's one use)
        self.ManualModeButton.setEnabled(False)
        self.ManualModeButton.setStyleSheet("background-color : blue; color: black;")
    
    #defining manual mode add train button functionality
    def addTrain_button(self):
        TrainID = self.TrainNameField.text()
        Departure = self.DepartureSationSelect.currentText()
        DepartureTime = self.DepartureTimeEdit.time()
        DepartureTime = DepartureTime.toString("hh:mm")
        Destination = self.DestinationSelect.currentText()
        ArrivalTime = self.ArrivalTimeEdit.time()
        ArrivalTime = ArrivalTime.toString("hh:mm")

        self.trainSchedule.addTrain(TrainID, Destination, ArrivalTime, Departure, DepartureTime)
        self.ScheduleTable.setModel(TableModel(self.trainSchedule.Scheduledata))



test = QtWidgets.QApplication(sys.argv)
window = UI()
window.show()
test.exec_()