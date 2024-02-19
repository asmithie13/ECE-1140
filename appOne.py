from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, uic, QtGui
import sys
from Block import Block
import csv

#Function to confirm whether or not the selected PLC file valid
def PLCvalid(fileName):
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
    
    return totalBlocks

#Initialization of UI
class TrackController_UI(QMainWindow):
    def __init__(self):
        #Load-in UI from the TrackControllerHW_UI file:
        super(TrackController_UI, self).__init__()
        uic.loadUi("TrackControllerHW_UI.ui", self)

        #Read all blocks and their attributes:
        self.allBlueBlocks = readTrackFile("blueLine.csv")
        self.allRedBlocks = readTrackFile("redLine.csv")
        self.allGreenBlocks = readTrackFile("greenLine.csv")

        #Disable the "Browse" button until a line is selected:
        self.buttonBrowse.setEnabled(False)

        #Disable red and green line selections - Not yet implemented:
        #Before implementing - Must determine which wayside stations cover which blocks:
        self.radioButtonRed.setEnabled(False) #TO BE REMOVED LATER
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
        #self.buttonSave.clicked.connect(self.savePLCFile)

        #Signals for line selection:
        self.radioButtonBlue.clicked.connect(self.blueLineButton)
        self.radioButtonRed.clicked.connect(self.redLineButton)
        self.radioButtonGreen.clicked.connect(self.greenLineButton)

        #Signals for mode selection:
        self.checkAuto.clicked.connect(self.automaticMode)
        self.checkManual.clicked.connect(self.manualMode)

        #Wayside selection signal:
        self.comboBoxWayside.activated.connect(self.waysideSelect) #Any selection will trigger this
    
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

        self.comboBoxWayside.setEnabled(True)
        self.comboBoxBlock.setEnabled(True)

        self.buttonBrowse.setEnabled(False)
        self.lineEditBrowse.setText("")

        print("Mode: Manual")
    
    #Need to make function for each wayside station
    def waysideSelect(self):
        self.buttonBrowse.setEnabled(True)
        if(self.comboBoxWayside.currentText() == "Blue"): #If the "Blue" wayside is selected (Temporary wayside for the blue line):
            pixmap = QPixmap("blueline.png")
            self.labelPhoto.setPixmap(pixmap)
            self.comboBoxBlock.setEnabled(True)
            for blockNum in self.allBlueBlocks:
                self.comboBoxBlock.addItem(blockNum.returnBlockID())

#Initialization of test bench:
class TrackController_TestBench(QMainWindow):
    def __init__(self):
        super(TrackController_TestBench, self).__init__()
        uic.loadUi("TrackControllerHW_TestBench.ui", self)

        #Receive the text from the type inputs:
        self.lineEditSpeedInput.returnPressed.connect(self.sendSpeed)
        self.lineEditAuthorityInput.returnPressed.connect(self.sendAuthority)
        self.lineEditOccupiedInput.returnPressed.connect(self.sendOccupied)
        self.lineEditFailedInput.returnPressed.connect(self.sendFailed)
    
    def sendSpeed(self):
        inputSpeed = self.lineEditSpeedInput.text()
        print(inputSpeed)
    
    def sendAuthority(self):
        inputAuthority = self.lineEditAuthorityInput.text()
        
        print(inputAuthority)
    
    def sendOccupied(self):
        inputBlock = self.lineEditOccupiedInput.text()
        print(inputBlock)
    
    def sendFailed(self):
        inputBlock = self.lineEditFailedInput.text()
        print(inputBlock)

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


