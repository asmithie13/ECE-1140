from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, uic, QtGui
import sys
from Block import Block
import csv
from PyQt5.QtCore import (Qt, pyqtSignal)

#Function to confirm whether or not the selected PLC file is valid:
def PLCvalid(fileName): #Reads based-on heading - Include heading in PLC files
        fileOpen = open(fileName, 'r')
        headLine = fileOpen.readline()
        if(headLine != "PLC File"): #Here, heading is set to "PLC File"
            return False
        return True

#Function that reads all blocks from a *.csv file and assigns block attributes:
def readTrackFile(fileName):
    totalBlocks = []
    with open(fileName, "r") as fileObject:
        readObj = csv.reader(fileObject, delimiter=",")
        for i, line in enumerate(readObj):
            hasCrossingTemp = False
            hasSwitchTemp = False
            if(i == 0):
                continue
            else:
                if(line[6] == "RAILWAY CROSSING"):
                    hasCrossingTemp = True
                elif(line[6][0:6] == "Switch"):
                    hasSwitchTemp = True
            tempBlock = Block(line[0], line[1], line[2], hasSwitchTemp, hasCrossingTemp)
            totalBlocks.append(tempBlock)
    
    return totalBlocks #Return a list of all blocks within the file

#Initialization of UI:
class TrackController_UI(QMainWindow):

    #Signals:
    commandedAuth = pyqtSignal(str) #Signal to output the commanded authority to the testbench

    def __init__(self):
        #Load-in UI from the TrackControllerHW_UI file:
        super(TrackController_UI, self).__init__()
        uic.loadUi("TrackControllerHW_UI.ui", self)

        #Read all blocks and their attributes (Crossings, switches, etc.)
        self.allBlueBlocks = readTrackFile("blueLine.csv")
        self.allRedBlocks = readTrackFile("redLine.csv")
        self.allGreenBlocks = readTrackFile("greenLine.csv")

        #Block that is selected at any one time:
        self.selectedBlock = Block("", "", 0, False, False)

        #Disable the "Browse" button until a line is selected:
        self.buttonBrowse.setEnabled(False) #Leave disabled until automatic mode is fully implemented

        #Disable red and green line selections - Not yet implemented:
        #Before implementing - Must determine which wayside stations cover which blocks:
        self.radioButtonRed.setEnabled(False)
        self.radioButtonGreen.setEnabled(False)

        #Disable automatic mode button until a PLC file is uploaded:
        self.modeFlag = 0 #Determines if system is in initial manual or post-automatic manual
        self.checkAuto.setEnabled(False)
        self.checkManual.setChecked(True)
        self.manualMode()

        #Set wayside and block selections are disabled before a line is selected:
        self.comboBoxWayside.setEnabled(False)
        self.comboBoxBlock.setEnabled(False)

        self.buttonSwitchLeft.setEnabled(False)
        self.buttonSwitchRight.setEnabled(False)
        self.buttonLightRed.setEnabled(False)
        self.buttonLightGreen.setEnabled(False)
        self.buttonCrossingUp.setEnabled(False)
        self.buttonCrossingDown.setEnabled(False)

        #Signals for PLC upload menu:
        self.buttonBrowse.clicked.connect(self.uploadPLCFile)

        #Signals for line selection:
        self.radioButtonBlue.clicked.connect(self.blueLineButton)
        self.radioButtonRed.clicked.connect(self.redLineButton)
        self.radioButtonGreen.clicked.connect(self.greenLineButton)

        #Signals for mode selection:
        self.checkAuto.clicked.connect(self.automaticMode)
        self.checkManual.clicked.connect(self.manualMode)

        #Wayside selection signal:
        self.comboBoxWayside.activated.connect(self.waysideSelect) #Any selection will trigger this

        #Block selection signal:
        self.comboBoxBlock.activated.connect(self.blockSelect)
        self.comboBoxBlock.activated.connect(self.setSelectedBlock)

        #Commanded authority signal:
        self.lineEditCommandedAuth.returnPressed.connect(self.sendCommandedAuth)
    
    #Function to upload the PLC file and display the file path:
    def uploadPLCFile(self):
        fileName = QFileDialog.getOpenFileName(self, "Select PLC File", "C:")
        fileName = fileName[0]

        if(PLCvalid(fileName) == True):
            self.lineEditBrowse.setText(fileName)
            self.buttonBrowse.setEnabled(False) #Cannot upload another PLC file if one is already uploaded
            #Only option is to switch to manual operation from this point

            self.checkManual.setChecked(False)
            self.checkAuto.setEnabled(True)
            self.checkAuto.setChecked(True)
            self.automaticMode()
        else:
            self.lineEditBrowse.setText("")
    
    #Occurs if the blue line is selected:
    def blueLineButton(self):
        self.comboBoxWayside.setEnabled(True)
        self.comboBoxWayside.clear()
        self.comboBoxWayside.addItem("Blue") #Number of waysides will be hard-coded

    #Occurs if the red line is selected:
    def redLineButton(self):
        self.comboBoxWayside.setEnabled(True)
        self.comboBoxWayside.clear()
        self.comboBoxWayside.addItem("1")
        self.comboBoxWayside.addItem("2") #Number of waysides will be hard-coded

    #Occurs if the green line is selected:
    def greenLineButton(self):
        self.comboBoxWayside.setEnabled(True)
        self.comboBoxWayside.clear()
        self.comboBoxWayside.addItem("3") #Number of waysides will be hard-coded
        self.comboBoxWayside.addItem("4")

    #Occurs if the system is in automatic operation:
    def automaticMode(self):
        self.modeFlag = 1
        self.comboBoxBlock.clear() #Specific blocks are not controlled in automatic operation
        self.comboBoxWayside.setEnabled(False)
        self.comboBoxBlock.setEnabled(False)
    
    #Occcurs if the user selects manual operation:
    def manualMode(self):
        if(self.modeFlag == 1): #Indicates that this is not initial manual mode, but manual-from-automatic
            self.buttonBrowse.setEnabled(False) #Unable to move back to automatic operation if currently in manual
            self.checkAuto.setChecked(False)
            self.checkAuto.setEnabled(False) 
            self.lineEditBrowse.setText("")

        self.comboBoxWayside.setEnabled(True)
        self.comboBoxBlock.setEnabled(True)
    
    def waysideSelect(self):
        #self.buttonBrowse.setEnabled(True) #Automatic not yet implemented, so function is commented-out
        if(self.comboBoxWayside.currentText() == "Blue"): #If the "Blue" wayside is selected (Temporary wayside for the blue line):
            pixmap = QPixmap("blueline.png")
            self.labelPhoto.setPixmap(pixmap)
            self.comboBoxBlock.setEnabled(True)
            for blockNum in self.allBlueBlocks:
                self.comboBoxBlock.addItem(blockNum.returnBlockID())
    
    #Function to find a specific block given the block ID, and assign the block to the specifi
    def blockSelect(self):
        selectedBlockText = self.comboBoxBlock.currentText()
        for block in self.allBlueBlocks:
            if(block.returnBlockID() == selectedBlockText):
                self.selectedBlock = block
                break
    
    #Function to receive and display block occupancies:
    def displayOccupancies(self, occBlock):
        tempStr = ""
        for block in occBlock:
            tempStr = tempStr + block + " "
        
        self.lineEditOccupiedBlocks.setText(tempStr)
    
    #Function to receive and display block failures:
    def displayFailures(self, failBlock):
        tempStr = ""
        for block in failBlock:
            tempStr = tempStr + block + " "
    
        self.lineEditClosedBlocks.setText(tempStr)
    
    #Function to display the received suggested authority (from CTC):
    def displaySuggestedAuth(self, tempStr):
        self.lineEditReceivedAuth.setText(tempStr)
    
    #Function to send the commanded authority to the testbench:
    def sendCommandedAuth(self):
        commandedAuth = self.lineEditCommandedAuth.text()
        self.commandedAuth.emit(commandedAuth)

    #Function to set a selected block - Enables programmer to edit block states:
    def setSelectedBlock(self):
        currentBlock = self.comboBoxBlock.currentText()
        for block in self.allBlueBlocks:
            if(block.returnBlockID() == currentBlock):
                self.selectedBlock = block
                break
        
        if(self.selectedBlock.hasSwitch == True):
            self.buttonSwitchLeft.setEnabled(True)
            self.buttonSwitchRight.setEnabled(True)
            self.buttonLightRed.setEnabled(True)
            self.buttonLightGreen.setEnabled(True)
        elif(self.selectedBlock.hasSwitch == False):
            self.buttonSwitchLeft.setEnabled(False)
            self.buttonSwitchRight.setEnabled(False)
            self.buttonLightRed.setEnabled(False)
            self.buttonLightGreen.setEnabled(False)

        if(self.selectedBlock.hasCrossing == True):
            self.buttonCrossingUp.setEnabled(True)
            self.buttonCrossingDown.setEnabled(True)
        elif(self.selectedBlock.hasCrossing == False):
            self.buttonCrossingUp.setEnabled(False)
            self.buttonCrossingDown.setEnabled(False)

    #NEXT:
        #Write functions that allow the Arduino to serially change the switch state,
        #light state, and crossing state of a self.selectedBlock, and then return the edited block
        #to the main block index (here, self.allBlueBlocks)
            
        #SEND FROM TESTBENCH TO UI/UI TO TESTBENCH

#Initialization of test bench:
class TrackController_TestBench(QMainWindow):

    #Signals:
    occBlocksChanged = pyqtSignal(list) #Sending block occupancies to UI
    failedBlocksChanged = pyqtSignal(list) #Sending failed blocks to UI
    authoritySent = pyqtSignal(str) #Sending suggested authority to UI

    def __init__(self):
        super(TrackController_TestBench, self).__init__()
        uic.loadUi("TrackControllerHW_TestBench.ui", self)

        #List to hold occupied and failed blocks:
        self.occupiedBlocks = []
        self.failedBlocks = []

        #Receive the text from the type inputs:
        self.lineEditSpeedInput.returnPressed.connect(self.sendSpeed)
        self.lineEditAuthorityInput.returnPressed.connect(self.sendSuggestedAuth)

        #Receive blocks from combo box:
        self.comboBoxOccIn.activated.connect(self.sendOccupied)
        self.comboBoxFailedIn.activated.connect(self.sendFailed)

        self.totalBlueBlock = readTrackFile("blueLine.csv")
        for block in self.totalBlueBlock:
            self.comboBoxOccIn.addItem(block.returnBlockID())
            self.comboBoxFailedIn.addItem(block.returnBlockID())
            self.comboBoxCheckBlock.addItem(block.returnBlockID())
        
        #Clear block fields:
        self.buttonClearOcc.clicked.connect(self.clearOccupied)
        self.buttonClearFailed.clicked.connect(self.clearFailed)
    
    #Send input speed to output (Wayside does not change):
    def sendSpeed(self):
        inputSpeed = self.lineEditSpeedInput.text()
        self.lineEditSpeedOut.setText(inputSpeed)
    
    #Handle authority input:
    def sendSuggestedAuth(self):
        inputAuthority = self.lineEditAuthorityInput.text()
        self.authoritySent.emit(inputAuthority)

        #Send the input authority to the UI to be displayed, and receive the
        #user-entered commanded authority from the UI to display on the testbench
    
    #Display received commanded authority:
    def displayCommandedAuth(self, commandedAuth):
        self.lineEditAuthOut.setText(commandedAuth)
    
    #Handle occupancy input:
    def sendOccupied(self):
        selectedBlock = self.comboBoxOccIn.currentText()
        currentText = self.lineEditOccupiedOut.text()
        if selectedBlock in self.occupiedBlocks:
            pass
        else:
            self.occupiedBlocks.append(selectedBlock)
            self.occupiedBlocks.sort()
        
        tempStr = ""
        for block in self.occupiedBlocks:
            tempStr = tempStr + block + " "
        self.lineEditOccupiedOut.setText(tempStr)

        self.occBlocksChanged.emit(self.occupiedBlocks)
        #Send this string to the UI to be displayed
    
    #Handle failure input:
    def sendFailed(self):
        selectedBlock = self.comboBoxFailedIn.currentText()
        currentText = self.lineEditFailedOut.text()
        if selectedBlock in self.failedBlocks:
            pass
        else:
            self.failedBlocks.append(selectedBlock)
            self.failedBlocks.sort()
        
        tempStr = ""
        for block in self.failedBlocks:
            tempStr = tempStr + block + " "
        self.lineEditFailedOut.setText(tempStr)

        self.failedBlocksChanged.emit(self.failedBlocks)
        #Send this string to the UI to be displayed
    
    #Handle clear buttons:
    def clearOccupied(self):
        self.occupiedBlocks = []
        self.occBlocksChanged.emit(self.occupiedBlocks)
        self.lineEditOccupiedOut.clear()
    
    def clearFailed(self):
        self.failedBlocks = []
        self.failedBlocksChanged.emit(self.failedBlocks)
        self.lineEditFailedOut.clear()


#Intialize Wayside object
class Wayside():
    def __init__(self):
        #Create instance of window:
        app = QApplication(sys.argv)
        windowOne = TrackController_UI()
        windowTwo = TrackController_TestBench()

        windowOne.commandedAuth.connect(windowTwo.displayCommandedAuth)

        windowTwo.occBlocksChanged.connect(windowOne.displayOccupancies)
        windowTwo.failedBlocksChanged.connect(windowOne.displayFailures)
        windowTwo.authoritySent.connect(windowOne.displaySuggestedAuth)

        windowOne.show()
        windowTwo.show()
        sys.exit(app.exec_())

waysideOne = Wayside()


