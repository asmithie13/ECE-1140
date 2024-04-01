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
        self.MaintenanceModeButton.clicked.connect(self.maintenanceMode_button)
        self.CloseBlockButton.clicked.connect(self.closeBlock_button)
        self.ReopenBlockButton.clicked.connect(self.reopenBlock_button)
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
        self.MaintenanceBox.setStyleSheet("background-color : rgb(233, 247, 255);")

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
        #ScheduleHeader.setSectionResizeMode(QHeaderView.Fixed)

        #Initializing Manual Mode Functions before Manual Mode has been selected
        self.TrainNameSelect.clear()
        self.TrainNameSelect.setEnabled(False)
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
        self.inMaintenance = False
        self.CloseBlockSelect.setEnabled(False)
        self.CloseBlockButton.setEnabled(False)
        self.ChooseSwitchSelect.setEnabled(False)
        self.SwitchPositionSelect.setEnabled(False)
        self.ReopenBlockButton.setEnabled(False)
        self.SetSwitchPositionButton.setEnabled(False)
        self.ReleaseSwitchButton.setEnabled(False)
        #Setting text to gray
        self.CloseBlockPromptLabel.setStyleSheet("color: rgb(120, 120, 120);")
        self.ChooseSwitchLabel.setStyleSheet("color: rgb(120, 120, 120);")
        self.SwitchPositionLabel.setStyleSheet("color: rgb(120, 120, 120);")
        self.MaintenanceBox.setStyleSheet("color: rgb(120, 120, 120);")
        #Seting the Swith Position Drop Down
        self.ChooseSwitchSelect.currentIndexChanged.connect(self.newSwitchSelected)
        
        #Initializing Occupied Blocks Table
        self.occupiedBlocks = OccupiedBlocks()
        self.OccupiedBlockTable.setModel(BlocksTableModel(self.occupiedBlocks.BlockDataCurrent))
        OBHeader = self.OccupiedBlockTable.horizontalHeader()
        OBHeader.setSectionResizeMode(QHeaderView.Stretch)

        #Initializing Maintance Tables
        self.Maintenance = CTC_Maintenance()
        self.BlockClosureTable.setModel(ClosedBlocksTableModel(self.Maintenance.BlocksClosed))
        BCHeader = self.BlockClosureTable.horizontalHeader()
        BCHeader.setSectionResizeMode(QHeaderView.Stretch)
        
        self.SwitchPositionTable.setModel(SwitchPositionTableModel(self.Maintenance.SwitchText))
        SPHeader = self.SwitchPositionTable.horizontalHeader()
        SPHeader.setSectionResizeMode(QHeaderView.Stretch)

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
    #Define mutually exclisive auto/manual mode when manual mode is selected
    def selectManualMode_button(self):
        #Disable Manual Mode button because there's no need to select it twice
        self.ManualModeButton.setEnabled(False)
        self.ManualModeButton.setStyleSheet("background-color : blue; color: black;")

        self.TrainNameSelect.setEnabled(True)
        self.TrainNameSelect.clear()
        self.TrainNameSelect.addItems(self.trainSchedule.TrainNames)
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
        self.TrainNameSelect.clear()
        self.TrainNameSelect.setEnabled(False)
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
        self.currentLine = 'Green'
        
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
        self.currentLine = 'Red'
        
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
                self.sendDispatchInfo.emit([i[1], 40, self.trainSchedule.AuthorityInfo[int(i[1][1:]) - 1]])
                print(i[1], "Dispatched")

                #Initializing where the train starts
                if i[0] == 'Green':
                    self.occupiedBlocks.currentTrains.append(['K63'])
                elif i[0] == 'Red':
                    self.occupiedBlocks.currentTrains.append(['D10'])


    #Define functionality for Upload File Button
    def selectScheduleFile(self):
        # Open a file dialog to select a Excel File
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Schedule File", "", "CSV FIle (*.csv);;All Files (*)")

        #Validate user has choosen a file
        if file_path == "":
            #Popup a message if the user enters a block that isn't closed
            error_msg = QMessageBox()
            error_msg.setWindowTitle("Selection Error")
            error_msg.setText("No Schedule File Selected")
            error_msg.setIcon(QMessageBox.Critical)

            error_msg.exec_() 

            return

        #Parse File
        self.trainSchedule.parseScheduleFile(file_path)
        #Update Table
        self.ScheduleTable.setModel(ScheduleTableModel(self.trainSchedule.Scheduledata))

        #Disable Manual Mode and upload button
        self.UploadButton.setEnabled(False)
        self.UploadButton.setStyleSheet("background-color : rgb(240, 240, 240); color: rgb(120, 120, 120);")
    
    #Function to determine if the system is entering or exitting maintenance mode
    def maintenanceMode_button(self):
        if self.inMaintenance == False:
            self.enterMaintenanceMode()
        else:
            self.exitMaintenanceMode()

    #Indication that the system is in maintenance mode
    #Same behavior will occur if a block is closed or a switch is sets
    def enterMaintenanceMode(self):
        self.inMaintenance = True
        
        #Set button color to blue to indicate selection
        self.MaintenanceModeButton.setStyleSheet("background-color : blue; color: black;")

        #Enable Maintenance Mode functions
        self.CloseBlockSelect.setEnabled(True)
        self.CloseBlockButton.setEnabled(True)
        self.ReopenBlockButton.setEnabled(True)
        self.ChooseSwitchSelect.setEnabled(True)
        self.SwitchPositionSelect.setEnabled(True)
        self.SetSwitchPositionButton.setEnabled(True)
        self.ReleaseSwitchButton.setEnabled(True)
        #Setting text to black
        self.CloseBlockPromptLabel.setStyleSheet("color: black;")
        self.ChooseSwitchLabel.setStyleSheet("color: black;")
        self.SwitchPositionLabel.setStyleSheet("color: black;")
        self.MaintenanceBox.setStyleSheet("color: black;")


    #Will indicate that the system is no longer in maintenance mode
    #Should work on the double press of the button
    #or if the block closures/switch position are empty
    def exitMaintenanceMode(self):
        #If there are closures/switches set ask the user if they want to reopen all of them
        if (len(self.Maintenance.BlocksClosed) > 0) or (len(self.Maintenance.SwitchesSet) > 0):
            #Popup a message if the user enters a block that isn't closed
            error_msg = QMessageBox()
            error_msg.setWindowTitle("Confirmation")
            error_msg.setText("Exiting Maintenance Mode will reopen all blocks and release all switches")
            error_msg.setIcon(QMessageBox.Warning)
            error_msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            #error_msg.buttonClicked.connect(self.msgbtn)

            exitMode = error_msg.exec_()
        else:
            exitMode = QMessageBox.Ok

        #If we are exiting Maintenance Mode
        if exitMode == QMessageBox.Ok:
            #Set button color
            self.inMaintenance = False
            self.MaintenanceModeButton.setStyleSheet("background-color : white")
            #Disable all button/maintenace functions
            self.CloseBlockSelect.setEnabled(False)
            self.CloseBlockButton.setEnabled(False)
            self.ChooseSwitchSelect.setEnabled(False)
            self.SwitchPositionSelect.setEnabled(False)
            self.ReopenBlockButton.setEnabled(False)
            self.SetSwitchPositionButton.setEnabled(False)
            self.ReleaseSwitchButton.setEnabled(False)
            #Setting text to gray
            self.CloseBlockPromptLabel.setStyleSheet("color: rgb(120, 120, 120);")
            self.ChooseSwitchLabel.setStyleSheet("color: rgb(120, 120, 120);")
            self.SwitchPositionLabel.setStyleSheet("color: rgb(120, 120, 120);")
            self.MaintenanceBox.setStyleSheet("color: rgb(120, 120, 120);")

            #Reopen all blocks if there are any
            if len(self.Maintenance.BlocksClosed) > 0:
                for block in range(len(self.Maintenance.BlocksClosed)):
                    #Reset block
                    self.Maintenance.BlocksClosed[block].occupied = 0
                    self.Maintenance.BlocksClosed[block].maintenance = 0

                    
                #Send to wayside
                self.sendBlockClosures.emit(self.Maintenance.BlocksClosed)

                #Update Table
                self.Maintenance.BlocksClosed.clear()
                self.Maintenance.BlocksClosedIDs.clear()
                self.BlockClosureTable.setModel(ClosedBlocksTableModel(self.Maintenance.BlocksClosedIDs))

            #Release all switches if any are set
            if len(self.Maintenance.SwitchesSet) > 0:
                for switch in range(len(self.Maintenance.SwitchesSet)):
                    #Reset block
                    self.Maintenance.SwitchesSet[switch].maintenance = 0

                #Send to wayside
                self.sendSwitchPositions.emit(self.Maintenance.SwitchesSet)

                #Update Table
                self.Maintenance.SwitchesSet.clear()
                self.Maintenance.SwitchText.clear()
                self.SwitchPositionTable.setModel(SwitchPositionTableModel(self.Maintenance.SwitchText))


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
        TrainID = self.TrainNameSelect.currentText() 
        Destination = self.DestinationSelect.currentText()
        ArrivalTime = self.ArrivalTimeEdit.time()

        #Add a new train name option if required
        if TrainID == self.trainSchedule.TrainNames[0]:
            TrainID = self.trainSchedule.TrainNames[0][1:]
            self.trainSchedule.TrainNames[0] = TrainID
            newID = "*T" + str(int(self.trainSchedule.TrainNames[0][1:]) + 1)
            self.trainSchedule.TrainNames.insert(0,newID)
            
            #reset train name options
            self.TrainNameSelect.clear()
            self.TrainNameSelect.addItems(self.trainSchedule.TrainNames)

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
        if self.currentLine == 'Green':
            for i in self.TrackData.GreenBlocks:
                if i.ID == BlockToClose:
                    temp = i
        else:   #line selection is red, find corresponding red line block
            for i in self.TrackData.RedBlocks:
                if i.ID == BlockToClose:
                    temp = i

        #Add to list of strings for diplaying on CTC UI
        self.Maintenance.BlocksClosedIDs.append([BlockToClose, temp.lineColor])
        self.BlockClosureTable.setModel(ClosedBlocksTableModel(self.Maintenance.BlocksClosedIDs))
        #Add to list of block objects for sending to wayside
        temp.occupied = 1
        temp.maintenance = 1
        self.Maintenance.BlocksClosed.append(temp)

        #Send to wayside
        self.sendBlockClosures.emit(self.Maintenance.BlocksClosed)

    #Function to reopen a block closure when in maintence mode
    def reopenBlock_button(self):
        #Read block selection from UI drop down
        BlockToOpen = []
        BlockToOpen.append(self.CloseBlockSelect.currentText())
        BlockToOpen.append(self.currentLine)

        for i in range(len(self.Maintenance.BlocksClosedIDs)):
            if BlockToOpen == self.Maintenance.BlocksClosedIDs[i]:
                #Reset block
                self.Maintenance.BlocksClosed[i].occupied = 0
                self.Maintenance.BlocksClosed[i].maintenance = 0

                #Send to wayside
                self.sendBlockClosures.emit(self.Maintenance.BlocksClosed)

                #Remove from maintenence list and update table
                self.Maintenance.BlocksClosed.pop(i)
                self.Maintenance.BlocksClosedIDs.pop(i)
                self.BlockClosureTable.setModel(ClosedBlocksTableModel(self.Maintenance.BlocksClosedIDs))

                return

        #Popup a message if the user enters a block that isn't closed
        error_msg = QMessageBox()
        error_msg.setWindowTitle("Selection Error")
        error_msg.setText("Selected block was not closed")
        error_msg.setIcon(QMessageBox.Critical)

        error_msg.exec_() 
        
    #Function to set switch positons when in maintenance mode
    def setSwitch_button(self):
        #Read the current switch and position selected
        switchToSet = self.ChooseSwitchSelect.currentText()
        positionToSet = self.SwitchPositionSelect.currentText()
        positionIndex = self.SwitchPositionSelect.currentIndex()

        #if green line blocks are being shown, find corresponding green line block
        if self.currentLine == 'Green':
            for i in self.TrackData.GreenBlocks:
                if i.blockNum == switchToSet:
                    temp = i
        else:   #line selection is red, find corresponding red line block
            for i in self.TrackData.RedBlocks:
                if i.blockNum == switchToSet:
                    temp = i

        #Add to list of strings for displaying on CTC UI
        self.Maintenance.SwitchText.append([switchToSet, positionToSet, temp.lineColor])
        self.SwitchPositionTable.setModel(SwitchPositionTableModel(self.Maintenance.SwitchText))
        #Add to list of block objects for sending to wayside
        #If the position is the first one, switch state is left = true
        if positionIndex == 0:
            temp.switchState = True
        else:   #Else the position is the second one, switch state is right = false
            temp.switchState = False

        temp.maintenance = 1

        self.Maintenance.SwitchesSet.append(temp)
    
    #Function to release a set switch positons when in maintenance mode
    def releaseSwitch_button(self):
        #Read the current switch selected
        switchToRelease = self.ChooseSwitchSelect.currentText()

        for i in range(len(self.Maintenance.SwitchText)):
            if (switchToRelease == self.Maintenance.SwitchText[i][0]) and (self.currentLine == self.Maintenance.SwitchText[i][2]):
                #Reset block
                self.Maintenance.SwitchesSet[i].maintenance = 0

                #Send to wayside
                self.sendSwitchPositions.emit(self.Maintenance.SwitchesSet)

                #Remove from maintenence list and update table
                self.Maintenance.SwitchText.pop(i)
                self.Maintenance.SwitchesSet.pop(i)
                self.SwitchPositionTable.setModel(SwitchPositionTableModel(self.Maintenance.SwitchText))

                return
            
        #Popup a message if the user enters a block that isn't closed
        error_msg = QMessageBox()
        error_msg.setWindowTitle("Selection Error")
        error_msg.setText("Selected switch was not under maintenance")
        error_msg.setIcon(QMessageBox.Critical)

        error_msg.exec_() 


    #Funciton to sync switch position options to current selected switch
    def newSwitchSelected(self, index):
        self.SwitchPositionSelect.clear()

        if self.currentLine == 'Green':
            self.SwitchPositionSelect.addItem(self.TrackData.GreenSwitches[index][1])
            self.SwitchPositionSelect.addItem(self.TrackData.GreenSwitches[index][2])
        if self.currentLine == 'Red':
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