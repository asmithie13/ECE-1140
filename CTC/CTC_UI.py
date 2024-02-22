#File to run the UI for the CTC Module
#Abby Magistro

#pyqt imports
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
#My class import
from Schedule import *
from OccupiedBlocks import *
from CTC_Maintenance import *
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
        self.AutoModeButton.clicked.connect(self.selectAutoMode_button)
            #TestBench Buttons
        self.UpdateBlocksButton.clicked.connect(self.updateBlocks_button)

        #Changing Button Colors
        self.AddTrainButton.setStyleSheet("background-color : rgb(38, 207, 4)")
        self.UploadButton.setStyleSheet("background-color : rgb(38, 207, 4)")
        self.UpdateBlocksButton.setStyleSheet("background-color : rgb(38, 207, 4)")
        self.CloseBlockButton.setStyleSheet("background-color: rgb(195, 16, 40)")

        #Changing Background colors to section off UI
        self.MaualDispatchBox.setStyleSheet("background-color : rgb(233, 247, 255);")
        self.OccupiedBlocksBox.setStyleSheet("background-color : rgb(233, 247, 255);")
        self.MaintenceBox.setStyleSheet("background-color : rgb(233, 247, 255);")

        #Manual Dispatch Formatting
        self.ArrivalTimeEdit.setDisplayFormat("hh:mm")
        self.DepartureTimeEdit.setDisplayFormat("hh:mm")

        #Add the clock
        #self.Clock = QtCore.QTimer(self)
        #self.Clock.timeout.connect(self.showTime(time))
        #self.Clock.display(ourClock.time)

        #Initializing Schedule
        self.trainSchedule = Schedule()
        self.ScheduleTable.setModel(ScheduleTableModel(self.trainSchedule.Scheduledata))

        #Initializing Occupied Blocks Table
        self.occupiedBlocks = OccupiedBlocks()
        self.OccupiedBlockTable.setModel(BlocksTableModel(self.occupiedBlocks.BlockData))

        #Initializing Maintance Table
        self.Maintence = CTC_Maintenance()
        self.MaintenanceTable.setModel(MaintenanceTableModel(self.Maintence.BlocksClosed))    
        

        
    #defining manual mode add train button functionality
    def addTrain_button(self):
        #Indicating manual mode is selected if it's not selected beforehand
        self.ManualModeButton.setEnabled(False)
        self.ManualModeButton.setStyleSheet("background-color : blue; color: black;")

        TrainID = self.TrainNameField.text()
        Departure = self.DepartureSationSelect.currentText()
        DepartureTime = self.DepartureTimeEdit.time()
        DepartureTime = DepartureTime.toString("hh:mm")
        Destination = self.DestinationSelect.currentText()
        ArrivalTime = self.ArrivalTimeEdit.time()
        ArrivalTime = ArrivalTime.toString("hh:mm")

        self.trainSchedule.addTrain(TrainID, Destination, ArrivalTime, Departure, DepartureTime)
        self.ScheduleTable.setModel(ScheduleTableModel(self.trainSchedule.Scheduledata))


    #Define mutually exclisive auto/manual mode when manual mode is selected
    def selectManualMode_button(self):
        #Disable Manual Mode button because there's no need to select it twice
        self.ManualModeButton.setEnabled(False)
        self.ManualModeButton.setStyleSheet("background-color : blue; color: black;")

    #Define mutually exclusive auto/manual mode when automatic mode is selected.
    #Same behavior will occur when a schedule is uploaded, even if the mode was not explicitly selected. 
    def selectAutoMode_button(self):
        #Disable The train name box
        self.TrainNameField.clear()
        self.TrainNameField.setEnabled(False)
        #Disable the Departure Station and Destination Drop Downs
        self.DepartureSationSelect.setEnabled(False)
        self.DestinationSelect.setEnabled(False)
        #Disable the time edits
        self.DepartureTimeEdit.setEnabled(False)
        self.ArrivalTimeEdit.setEnabled(False)
        #Disable the add train button
        self.AddTrainButton.setEnabled(False)


        #Highlight Auto selected and disable manual select button
        self.AutoModeButton.setEnabled(False)
        self.AutoModeButton.setStyleSheet("background-color : blue; color: black;")
        self.ManualModeButton.setEnabled(False)
        self.ManualModeButton.setStyleSheet("background-color : rgb(240, 240, 240); color: rgb(120, 120, 120);")

        #Changing label text to gray
        self.TrainNameLabel.setStyleSheet("color: rgb(120, 120, 120);")
        self.DepartureStationLabel.setStyleSheet("color: rgb(120, 120, 120);")
        self.DestinationLabel.setStyleSheet("color: rgb(120, 120, 120);")
        self.DepartureTimeLabel.setStyleSheet("color: rgb(120, 120, 120);")
        self.ArrivalTimeLabel.setStyleSheet("color: rgb(120, 120, 120);")


    #Define functionality for Upload File Button
    def open_files(self):
        # Open a file dialog to select a Excel File
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Schedule File", "", "CSV FIle (*.csv);;All Files (*)")

        #Parse File
        self.trainSchedule.parseScheduleFile(file_path)
        #Update Table
        self.ScheduleTable.setModel(ScheduleTableModel(self.trainSchedule.Scheduledata))

        #Disable Manual Mode and upload button
        self.selectAutoMode_button()
        self.UploadButton.setEnabled(False)
        self.UploadButton.setStyleSheet("background-color : rgb(240, 240, 240); color: rgb(120, 120, 120);")

    

    """TEST BENCH FUNCTIONS"""
    def updateBlocks_button(self):
        BlockText = self.OccupiedBlocksField.text()
        UpdatedBlocks = list(map(str.strip, BlockText.split(',')))

        UpdatedBlocksWithTrain = []
        for i in UpdatedBlocks:
            UpdatedBlocksWithTrain.append(['X', i])

        self.occupiedBlocks.BlockData = UpdatedBlocksWithTrain
        self.OccupiedBlockTable.setModel(BlocksTableModel(self.occupiedBlocks.BlockData))


"""
UI_window = QtWidgets.QApplication(sys.argv)
window = UI()
window.show()
UI_window.exec_()
"""