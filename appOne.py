from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, uic, QtGui
import sys
from Block import Block
import csv

#Function to confirm whether or not the selected PLC file valid:
def PLCvalid(fileName): #Reads based-on heading - Different text can be specified
        fileOpen = open(fileName, 'r')
        headLine = fileOpen.readline()
        if(headLine != "PLC File"):
            return False
        return True

#Function that reads all blocks from a *.csv file:
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
    def __init__(self):
        #Load-in UI from the TrackControllerHW_UI file:
        super(TrackController_UI, self).__init__()
        uic.loadUi("TrackControllerHW_UI.ui", self)

        #Block that is being acted upon at any one time
        self.selectedBlock = Block("Blue", "A", 1, False, False)

        #Read all blocks and their attributes (Crossings, switches, etc.)
        self.allBlueBlocks = readTrackFile("blueLine.csv")
        self.allRedBlocks = readTrackFile("redLine.csv")
        self.allGreenBlocks = readTrackFile("greenLine.csv")

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
    
    #Function to upload the PLC file and display the file location:
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

        print("Selected: Blue Line") #Remove later after adding actual functionality

    #Occurs if the red line is selected:
    def redLineButton(self):
        self.comboBoxWayside.setEnabled(True)
        self.comboBoxWayside.clear()
        self.comboBoxWayside.addItem("1")
        self.comboBoxWayside.addItem("2")

        print("Selected: Red Line")

    #Occurs if the green line is selected:
    def greenLineButton(self):
        self.comboBoxWayside.setEnabled(True)
        self.comboBoxWayside.clear()
        self.comboBoxWayside.addItem("3")
        self.comboBoxWayside.addItem("4")

        print("Selected: Green Line")

    #Occurs if the system is in automatic operation:
    def automaticMode(self):
        self.modeFlag = 1
        self.comboBoxWayside.setEnabled(False)
        self.comboBoxBlock.clear()
        self.comboBoxBlock.setEnabled(False)
        print("Mode: Automatic")
    
    #Occcurs if the user selects manual operation:
    def manualMode(self):
        if(self.modeFlag == 1):
            self.buttonBrowse.setEnabled(False) #Unable to move back to automatic operation if currently in manual
            self.checkAuto.setChecked(False)
            self.checkAuto.setEnabled(False) 
            self.lineEditBrowse.setText("")

        self.comboBoxWayside.setEnabled(True)
        self.comboBoxBlock.setEnabled(True)
        print("Mode: Manual")
    
    def waysideSelect(self):
        #self.buttonBrowse.setEnabled(True) #Automatic not yet implemented, so function is commented-out
        if(self.comboBoxWayside.currentText() == "Blue"): #If the "Blue" wayside is selected (Temporary wayside for the blue line):
            pixmap = QPixmap("blueline.png")
            self.labelPhoto.setPixmap(pixmap)
            self.comboBoxBlock.setEnabled(True)
            for blockNum in self.allBlueBlocks:
                self.comboBoxBlock.addItem(blockNum.returnBlockID())
    
    #Function to handle selected block:
    def blockSelect(self):
        selectedBlockText = self.comboBoxBlock.currentText()
        for block in self.allBlueBlocks:
            if(block.returnBlockID() == selectedBlockText):
                self.selectedBlock = block
                break

    #NEXT:
        #Write functions that allow the Arduino to serially change the switch state,
        #light state, and crossing state of a self.selectedBlock, and then return the edited block
        #to the main block index (here, self.allBlueBlocks)
            
        #SEND FROM TESTBENCH TO UI/UI TO TESTBENCH

#Initialization of test bench:
class TrackController_TestBench(QMainWindow):
    def __init__(self):
        super(TrackController_TestBench, self).__init__()
        uic.loadUi("TrackControllerHW_TestBench.ui", self)

        #Receive the text from the type inputs:
        self.lineEditSpeedInput.returnPressed.connect(self.sendSpeed)
        self.lineEditAuthorityInput.returnPressed.connect(self.sendAuthority)

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
    def sendAuthority(self):
        inputAuthority = self.lineEditAuthorityInput.text()
        #Send the input authority to the UI to be displayed, and receive the
        #user-entered commanded authority from the UI to display on the testbench
    
    #Handle occupancy input:
    def sendOccupied(self):
        selectedBlock = self.comboBoxOccIn.currentText()
        currentText = self.lineEditOccupiedOut.text()
        tempStr = currentText + " " + selectedBlock
        self.lineEditOccupiedOut.setText(tempStr)
        #Send this string to the UI to be displayed
    
    #Handle failure input:
    def sendFailed(self):
        selectedBlock = self.comboBoxFailedIn.currentText()
        currentText = self.lineEditFailedOut.text()
        tempStr = currentText + " " + selectedBlock
        self.lineEditFailedOut.setText(tempStr)
        #Send this string to the UI to be displayed
    
    #Handle clear buttons:
    def clearOccupied(self):
        self.lineEditOccupiedOut.clear()
    
    def clearFailed(self):
        self.lineEditFailedOut.clear()

    #Function to check block states:
    def checkBlockStates(self):
        selectedBlock = self.comboBoxCheckBlock.currentText()
        #Find the block object with the corresponding ID from the UI, and display the states here

#Intialize Wayside object
class Wayside():
    def __init__(self):
        #Create instance of window:
        app = QApplication(sys.argv)
        windowOne = TrackController_UI()
        windowOne.show()

        windowTwo = TrackController_TestBench()
        windowTwo.show()

        if __name__ == "__main__":
            sys.exit(app.exec_())

waysideOne = Wayside()


