#File that holds the data to run the CTC UI
#Abby Magistro

#pyqt imports
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
#My class imports
from CTC.Schedule import *
from CTC.OccupiedBlocks import *
from CTC.CTC_Maintenance import *
from CTC.Throughput import *
from CTC.TempData import *
#From other folders
from Track_Resources import *


class CTC_UI(QtWidgets.QMainWindow):
    #Signals, for Wayside (and Testbench)
    sendDispatchInfo = pyqtSignal(list)
    sendBlockClosures = pyqtSignal(list)
    sendSwitchPositions = pyqtSignal(list)
    create_a_train = pyqtSignal(str)

    def __init__(self):
        super(CTC_UI, self).__init__()
        #Loading base UI layout from .ui file
        uic.loadUi("CTC/CTC_UI.ui", self)


        #Connect Buttons to signals defining behavior
        self.ManualModeButton.clicked.connect(self.selectManualMode_button)
        self.AutoModeButton.clicked.connect(self.selectAutoMode_button)
        self.GreenLineButton.clicked.connect(self.greenLine_button)
        self.RedLineButton.clicked.connect(self.redLine_button)
        self.UploadButton.clicked.connect(self.selectScheduleFile)
        self.AddTrainButton.clicked.connect(self.addTrain_button)
        self.MaintenanceModeButton.clicked.connect(self.enterMaintenanceMode)
        self.CloseBlockButton.clicked.connect(self.closeBlock_button)
        self.ReopenBlockButto.clicked.connect(self.reopenBlock_button)
        self.SetSwitchPositionButton.clicked.connect(self.setSwitch_button)
        self.ReleaseSwitchButton.clicked.connect(self.releaseSwitch_button)

        #Changing Button Colors
        self.AddTrainButton.setStyleSheet("background-color : rgb(38, 207, 4)")             #Green
        self.UploadButton.setStyleSheet("background-color : rgb(38, 207, 4)")               #Green
        self.CloseBlockButton.setStyleSheet("background-color: rgb(195, 16, 40)")           #Red
        self.ReopenBlockButton.setStyleSheet("background-color : rgb(38, 207, 4)")          #Green
        self.SetSwitchPositionButton.setStyleSheet("background-color: rgb(195, 16, 40)")    #Red
        self.ReleaseSwitchButton.setStyleSheet("background-color : rgb(38, 207, 4)")        #Green

        #Changing Background colors to section off UI, all light blue
        self.MaualDispatchBox.setStyleSheet("background-color : rgb(233, 247, 255);")
        self.ScheduleBox.setStyleSheet("background-color : rgb(233, 247, 255);")
        self.OccupiedBlocksBox.setStyleSheet("background-color : rgb(233, 247, 255);")
        self.MaintenceBox.setStyleSheet("background-color : rgb(233, 247, 255);")

        #Manual Dispatch Formatting
        self.ArrivalTimeEdit.setDisplayFormat("hh:mm")

        #Importing Track Data
        self.TrackData = TempData()

        #Data to hold the current line selected
        self.currentLine = ''

        #Initializing Schedule
        self.trainSchedule = Schedule() 
        self.ScheduleTable.setModel(ScheduleTableModel(self.trainSchedule.Scheduledata))
        ScheduleHeader = self.ScheduleTable.horizontalHeader()
        ScheduleHeader.setSectionResizeMode(QHeaderView.ResizeToContents)

        #Initializing Manual Mode Functions before Manual Mode has been selected
        self.TrainNameField.clear()
        self.TrainNameField.setEnabled(False)
        self.DestinationSelect.setEnabled(False)
        self.ArrivalTimeEdit.setEnabled(False)
        #Disable the add train button
        self.AddTrainButton.setEnabled(False)
        #Changing label text to gray
        self.TrainNameLabel.setStyleSheet("color: rgb(120, 120, 120);")
        self.DestinationLabel.setStyleSheet("color: rgb(120, 120, 120);")
        self.ArrivalTimeLabel.setStyleSheet("color: rgb(120, 120, 120);")
        self.MaualDispatchBox.setStyleSheet("color: rgb(120, 120, 120);")

        #Disabling Auto Mode select schedule button until auto mode is selected
        self.UploadButton.setEnabled(False)
        self.UploadButton.setStyleSheet("background-color : rgb(240, 240, 240); color: rgb(120, 120, 120);")
        
        #Initializing Maintenance Mode functions before Mainenance Mode has been selected
        self.CloseBlockSelect.setEnabled(False)
        self.CloseBlockButton.setEnabled(False)
        self.ChooseSwitchSelect.setEnabled(False)
        self.SwitchPositionSelect.setEnabled(False)
        self.ReopenBlockButton.setEnables(False)
        self.SetSwitchPositionButton.setEnabled(False)
        self.ReleaseSwitchButton.setEnable(False)
        #Setting text to gray
        self.CloseBlockPromptLabel.setStyleSheet("color: rgb(120, 120, 120);")
        self.ChooseSwitchLabel.setStyleSheet("color: rgb(120, 120, 120);")
        self.SwitchPositionLabel.setStyleSheet("color: rgb(120, 120, 120);")
        self.MaintenceBox.setStyleSheet("color: rgb(120, 120, 120);")
        #Seting the Swith Position Drop Down
        self.ChooseSwitchSelect.currentIndexChanged.connect(self.newSwitchSelected)
        
        #Initializing Occupied Blocks Table
        self.occupiedBlocks = OccupiedBlocks()
        self.OccupiedBlockTable.setModel(BlocksTableModel(self.occupiedBlocks.BlockDataCurrent))

        #Initializing Maintance Tables
        self.Maintence = CTC_Maintenance()
        self.BlockClosureTable.setModel(ClosedBlocksTableModel(self.Maintence.BlocksClosed))
        BCHeader = self.BlockClosureTable.horizontalHeader()
        BCHeader.setSectionResizeMode(QHeaderView.ResizeToContents)
        
        self.SwitchPositionTable.setModel(SwitchPositionTableModel(self.Maintence.BlocksClosed))
        SPHeader = self.SwitchPositionTable.horizontalHeader()
        SPHeader.setSectionResizeMode(QHeaderView.ResizeToContents)

        #Initializing Throughput    
        self.ThroughputGraph = Throughput()
        resolution = QtCore.QSize(250, 200)
        pixmap = QPixmap('CTC/ThroughputGraph.png')
        pixmap = pixmap.scaled(resolution, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.ThroughputGraphLabel.setPixmap(pixmap)
        
        #Connecting signals for testbench
        #self.sendAuthority.emit(0)

    """Slots to recieve Signals"""
    #BlockList will be a list of occupied block objects from wayside controllers
    def recieveOccupiedBlocksG1(self, BlockList):
        #Parsign through block objects to pull out ID and lineColor
        TempBlockList = []
        for i in BlockList:
            TempBlockList.append([i.ID, i.lineColor])

        #Add to list that holds occupancies by block
        self.occupiedBlocks.recievedFromWayside[0] = TempBlockList

        #Compile all occupied blocks into full list to update list
        FullBlockList = []
        for i in self.occupiedBlocks.recievedFromWayside:
            for j in i:
                FullBlockList.append(j)

        self.updateOccupiedBlocks(FullBlockList)

    def recieveOccupiedBlocksG2(self, BlockList):
        #Parsign through block objects to pull out ID and lineColor
        TempBlockList = []
        for i in BlockList:
            TempBlockList.append([i.ID, i.lineColor])

        #Add to list that holds occupancies by block
        self.occupiedBlocks.recievedFromWayside[1] = TempBlockList

        #Compile all occupied blocks into full list to update list
        FullBlockList = []
        for i in self.occupiedBlocks.recievedFromWayside:
            for j in i:
                FullBlockList.append(j)

        self.updateOccupiedBlocks(FullBlockList)

    def recieveOccupiedBlocksR1(self, BlockList):
        #Parsign through block objects to pull out ID and lineColor
        TempBlockList = []
        for i in BlockList:
            TempBlockList.append([i.ID, i.lineColor])

        #Add to list that holds occupancies by block
        self.occupiedBlocks.recievedFromWayside[2] = TempBlockList

        #Compile all occupied blocks into full list to update list
        FullBlockList = []
        for i in self.occupiedBlocks.recievedFromWayside:
            for j in i:
                FullBlockList.append(j)

        self.updateOccupiedBlocks(FullBlockList)

    def recieveOccupiedBlocksR2(self, BlockList):
        #Parsign through block objects to pull out ID and lineColor
        TempBlockList = []
        for i in BlockList:
            TempBlockList.append([i.ID, i.lineColor])

        #Add to list that holds occupancies by block
        self.occupiedBlocks.recievedFromWayside[3] = TempBlockList

        #Compile all occupied blocks into full list to update list
        FullBlockList = []
        for i in self.occupiedBlocks.recievedFromWayside:
            for j in i:
                FullBlockList.append(j)

        self.updateOccupiedBlocks(FullBlockList)

    #TicketSales will be a list of two lists of ints, representing the sales at each station in 
    #green line and red line respectively, from Track Model
    def recieveTicketSales(self, TicketSales):
        print("Hello")
        
        AverageSales = [0, 0]
        print(TicketSales)

        AverageSales[0] = sum(TicketSales[0])/len(TicketSales[0])
        AverageSales[1] = sum(TicketSales[1])/len(TicketSales[1])

        self.updateTicketSales(AverageSales)

    """Function to Define Behavior of CTC UI"""    
    #defining manual mode add train button functionality
    def addTrain_button(self):
        #Grabbing values from the UI
        TrainID = self.TrainNameField.text()
        Destination = self.DestinationSelect.currentText()
        ArrivalTime = self.ArrivalTimeEdit.time()

        #Calculatig the Departure Station and time
        Departure = []
        self.trainSchedule.calculateDeparture(Destination, ArrivalTime, Departure)

        #Adding the train to the schedule
        self.trainSchedule.addTrain(TrainID, Destination, ArrivalTime, Departure[0], Departure[1])
        self.ScheduleTable.setModel(ScheduleTableModel(self.trainSchedule.Scheduledata))


    #Define mutually exclisive auto/manual mode when manual mode is selected
    def selectManualMode_button(self):
        #Disable Manual Mode button because there's no need to select it twice
        self.ManualModeButton.setEnabled(False)
        self.ManualModeButton.setStyleSheet("background-color : blue; color: black;")

        self.TrainNameField.setEnabled(True)
        self.DestinationSelect.setEnabled(True)
        self.ArrivalTimeEdit.setEnabled(True)
        #Disable the add train button
        self.AddTrainButton.setEnabled(True)
        #Changing label text to gray
        self.TrainNameLabel.setStyleSheet("color: black;")
        self.DestinationLabel.setStyleSheet("color: black;")
        self.ArrivalTimeLabel.setStyleSheet("color: black;")
        self.MaualDispatchBox.setStyleSheet("color: black;")

    #Define mutually exclusive auto/manual mode when automatic mode is selected.
    def selectAutoMode_button(self):
        #Enable Schedule Upload Button
        self.UploadButton.setEnabled(True)
        self.UploadButton.setStyleSheet("background-color : rgb(38, 207, 4)")       #Green
        
        #Disable Manual Mode Functions
        self.TrainNameField.clear()
        self.TrainNameField.setEnabled(False)
        self.DestinationSelect.setEnabled(False)
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
        self.DestinationLabel.setStyleSheet("color: rgb(120, 120, 120);")
        self.ArrivalTimeLabel.setStyleSheet("color: rgb(120, 120, 120);")
        self.MaualDispatchBox.setStyleSheet("color: rgb(120, 120, 120);")

    #Sets drop down options if green line is selected
    def greenLine_button(self):
        self.currentLine = 'green'
        
        #Highlight green line button
        self.GreenLineButton.setStyleSheet("background-color : rgb(38, 207, 4)")     #Green
        self.RedLineButton.setStyleSheet("background-color : white")

        #Set stations selctions to green line
        self.DestinationSelect.clear()
        self.DestinationSelect.addItems(self.TrackData.GreenStations)
        #Setting Block selections to green line
        self.CloseBlockSelect.clear()
        self.CloseBlockSelect.addItems(self.TrackData.GreenBlockIDs)
        #Setting Switch selctions to green line
        self.ChooseSwitchSelect.clear()
        for i in self.TrackData.GreenSwitches:
            self.ChooseSwitchSelect.addItem(i[0])
        self.newSwitchSelected(0)
    
    def redLine_button(self):
        self.currentLine = 'red'
        
        #Highlight red line button
        self.RedLineButton.setStyleSheet("background-color: rgb(195, 16, 40)")     #Red
        self.GreenLineButton.setStyleSheet("background-color : white")

        #Set stations selctions to red line
        self.DestinationSelect.clear()
        self.DestinationSelect.addItems(self.TrackData.RedStations)
        #Setting Block selections to red line
        self.CloseBlockSelect.clear()
        self.CloseBlockSelect.addItems(self.TrackData.RedBlockIDs)
        #Setting Switch selctions to red line
        self.ChooseSwitchSelect.clear()
        for i in self.TrackData.RedSwitches:
            self.ChooseSwitchSelect.addItem(i[0])
        self.newSwitchSelected(0)

    #function to update the clock display on the layout
    def displayClock(self, time):
        self.CTC_clock.display(time)
        
        for i in self.trainSchedule.Scheduledata:
            if (time == i[5]) and (int(i[1][1:]) > len(self.occupiedBlocks.currentTrains)):
                self.create_a_train.emit(i[1])

                #Train ID, speed, Authority
                self.sendDispatchInfo.emit([i[1], 70, self.trainSchedule.AuthorityInfo[int(i[1][1:]) - 1]])
                print(i[1], "Dispatched")

                #Initializing where the train starts
                if i[0] == 'green':
                    self.occupiedBlocks.currentTrains.append(['K63'])
                elif i[0] == 'red':
                    self.occupiedBlocks.currentTrains.append(['D10'])


    #Define functionality for Upload File Button
    def selectScheduleFile(self):
        # Open a file dialog to select a Excel File
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Schedule File", "", "CSV FIle (*.csv);;All Files (*)")

        #Parse File
        self.trainSchedule.parseScheduleFile(file_path)
        #Update Table
        self.ScheduleTable.setModel(ScheduleTableModel(self.trainSchedule.Scheduledata))

        #Disable Manual Mode and upload button
        self.UploadButton.setEnabled(False)
        self.UploadButton.setStyleSheet("background-color : rgb(240, 240, 240); color: rgb(120, 120, 120);")


    #Indication that the system is in maintenance mode
    #Same behavior will occur if a block is closed or a switch is sets
    def enterMaintenanceMode(self):
        #Set button color to blue to indicate selection
        self.MaintenanceModeButton.setStyleSheet("background-color : blue; color: black;")

        #Enable Maintenance Mode functions
        self.CloseBlockSelect.setEnabled(True)
        self.CloseBlockButton.setEnabled(True)
        self.ChooseSwitchSelect.setEnabled(True)
        self.SwitchPositionSelect.setEnabled(True)
        self.SetSwitchPositionButton.setEnabled(True)
        #Setting text to gray
        self.CloseBlockPromptLabel.setStyleSheet("color: black;")
        self.ChooseSwitchLabel.setStyleSheet("color: black;")
        self.SwitchPositionLabel.setStyleSheet("color: black;")
        self.MaintenceBox.setStyleSheet("color: black;")


    #Will indicate that the system is no longer in maintenance mode
    #Should work on the double press of the button
    #or if the block closures/switch position are empty
    def exitMaintenanceMode(self):
        print("You still need to write this")


    #function to update block occupied table based on input from Wayside
    def updateOccupiedBlocks(self, arr):
        #Clear temp new block layout array
        self.occupiedBlocks.BlockDataNew = []
        #clear new train matrix, and initialize the correct number of row
        self.occupiedBlocks.newTrains = []
        for i in range(len(self.occupiedBlocks.currentTrains)):
            self.occupiedBlocks.newTrains.append([])

        #Adding TrainID, Block ID, and line color to an array
        for block in arr:
            #Getting train ID
            TrainID = self.occupiedBlocks.matchOccupanciesToTrains(block[0], block[1])
            self.occupiedBlocks.BlockDataNew.append([TrainID, block[0], block[1]])

            #If it's a train, add to updated train list
            if TrainID != 'X':
                self.occupiedBlocks.newTrains[int(TrainID[1:]) - 1].append(block[0])

        #update the current variable to be the newly calculated ones
        self.occupiedBlocks.currentTrains = self.occupiedBlocks.newTrains
        self.occupiedBlocks.BlockDataCurrent = self.occupiedBlocks.BlockDataNew

        self.OccupiedBlockTable.setModel(BlocksTableModel(self.occupiedBlocks.BlockDataCurrent))


    #defining manual mode add train button functionality
    def addTrain_button(self):
        #Getting User entered Info
        TrainID = self.TrainNameField.text()
        Destination = self.DestinationSelect.currentText()
        ArrivalTime = self.ArrivalTimeEdit.time()

        #Calculating Departure Info
        Departure = []
        self.trainSchedule.calculateDeparture(Destination, ArrivalTime, Departure, self.currentLine)

        #Adding all schedule info to the schedule
        ArrivalTime = ArrivalTime.toString("hh:mm")
        #Line, TrainID, Destination, Arrival Time, Departure Station, Departure Time
        self.trainSchedule.addTrain(self.currentLine, TrainID, Destination, ArrivalTime, Departure[0], Departure[1])

        self.ScheduleTable.setModel(ScheduleTableModel(self.trainSchedule.Scheduledata))


    #Function to add a block closure when in maintence mode, sets block object as occupied
    def closeBlock_button(self):
        #Read block selection from UI drop down
        BlockToClose = self.CloseBlockSelect.currentText()
        
        #if green line blocks are being shown, find corresponding green line block
        if self.currentLine == 'green':
            for i in self.TrackData.GreenBlocks:
                if i.ID == BlockToClose:
                    temp = i
        else:   #line selection is red, find corresponding red line block
            for i in self.TrackData.RedBlocks:
                if i.ID == BlockToClose:
                    temp = i

        #Add to list of strings for diplaying on CTC UI
        self.Maintence.BlocksClosedIDs.append([BlockToClose, temp.lineColor])
        self.BlockClosureTable.setModel(ClosedBlocksTableModel(self.Maintence.BlocksClosedIDs))
        #Add to list of block objects for sending to wayside
        temp.occupied = 1
        temp.maintenance = 1
        self.Maintence.BlocksClosed.append(temp)

        #Send to wayside
        self.sendBlockClosures.emit(self.Maintence.BlocksClosed)

    #Function to reopen a block closure when in maintence mode
    def reopenBlock_button(self):
        print("to be written")
        
    #Function to set switch positons when in maintenance mode
    def setSwitch_button(self):
        #Read the current switch and position selected
        switchToSet = self.ChooseSwitchSelect.currentText()
        positionToSet = self.SwitchPositionSelect.currentText()
        positionIndex = self.SwitchPositionSelect.currentIndex()

        #if green line blocks are being shown, find corresponding green line block
        if self.currentLine == 'green':
            for i in self.TrackData.GreenBlocks:
                if i.blockNum == switchToSet:
                    temp = i
        else:   #line selection is red, find corresponding red line block
            for i in self.TrackData.RedBlocks:
                if i.blockNum == switchToSet:
                    temp = i

        #Add to list of strings for displaying on CTC UI
        self.Maintence.SwitchText.append([switchToSet, positionToSet, temp.lineColor])
        self.SwitchPositionTable.setModel(SwitchPositionTableModel(self.Maintence.SwitchText))
        #Add to list of block objects for sending to wayside
        #If the position is the first one, switch state is left = true
        if positionIndex == 0:
            temp.switchState = True
        else:   #Else the position is the second one, switch state is right = false
            temp.switchState = False

        temp.maintenance = 1

        self.Maintence.SwitchesSet.append(temp)
    
    #Function to release a set switch positons when in maintenance mode
    def releaseSwitch_button(self):
        print("TBD")

    #Funciton to sync switch position options to current selected switch
    def newSwitchSelected(self, index):
        self.SwitchPositionSelect.clear()

        if self.currentLine == 'green':
            self.SwitchPositionSelect.addItem(self.TrackData.GreenSwitches[index][1])
            self.SwitchPositionSelect.addItem(self.TrackData.GreenSwitches[index][2])
        if self.currentLine == 'red':
            self.SwitchPositionSelect.addItem(self.TrackData.RedSwitches[index][1])
            self.SwitchPositionSelect.addItem(self.TrackData.RedSwitches[index][2])

    #Function to update the ticket sales based on information from Track Model
    def updateTicketSales(self, Sales):
        self.ThroughputGraph.heights = Sales
        
        self.ThroughputGraph.updateThroughputGraph()
        resolution = QtCore.QSize(250, 200)
        pixmap = QPixmap('CTC/ThroughputGraph.png')
        pixmap = pixmap.scaled(resolution, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.ThroughputGraphLabel.setPixmap(pixmap)




"""
UI_window = QtWidgets.QApplication(sys.argv)
window = UI()
window.show()
UI_window.exec_()
"""