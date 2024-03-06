from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import uic
from PyQt5.QtCore import (Qt, pyqtSignal)
from Block import *
from otherFunctions import *
import sys

#Initialization of test bench:
class TrackController_TestBench(QMainWindow):

    #Signals:
    occBlocksChanged = pyqtSignal(list) #Sending block occupancies to UI
    failedBlocksChanged = pyqtSignal(list) #Sending failed blocks to UI
    authoritySent = pyqtSignal(str) #Sending suggested authority to UI

    def __init__(self):
        super(TrackController_TestBench, self).__init__()
        uic.loadUi("Wayside HW/TrackControllerHW_TestBench.ui", self)

        #List to hold occupied and failed blocks:
        self.occupiedBlocks = []
        self.failedBlocks = []

        #Receive the text from the type inputs:
        self.lineEditSpeedInput.returnPressed.connect(self.sendSpeed)

        #Receive blocks from combo box:
        self.comboBoxOccIn.activated.connect(self.sendOccupied)
        self.comboBoxFailedIn.activated.connect(self.sendFailed)

        self.blueTriplesIDs = []
        self.redTriplesIDs = []
        self.greenTriplesIDs = []

        self.waysideBlue = readTrackFile("blueLine.csv", self.blueTriplesIDs)
        self.waysideOne, self.waysideTwo = splitGreenBlocks(readTrackFile("greenLine.csv", self.greenTriplesIDs))
        self.waysideThree, self.waysideFour = splitRedBlocks(readTrackFile("redLine.csv", self.redTriplesIDs))

        self.allBlocks = []
        self.allBlocks.append(self.waysideBlue)
        self.allBlocks.append(self.waysideOne)
        self.allBlocks.append(self.waysideTwo)
        self.allBlocks.append(self.waysideThree)
        self.allBlocks.append(self.waysideFour)

        for wayside in self.allBlocks:
            for block in wayside:
                self.comboBoxOccIn.addItem(block.blockSection + block.blockNum)
                self.comboBoxFailedIn.addItem(block.blockSection + block.blockNum)
                self.comboBoxCheckBlock.addItem(block.blockSection + block.blockNum)
        
        #Clear block fields:
        self.buttonClearOcc.clicked.connect(self.clearOccupied)
        self.buttonClearFailed.clicked.connect(self.clearFailed)

        #Temporary blocks - Block being displayed at one time
        self.tempBlockList = []

        self.comboBoxCheckBlock.activated.connect(self.displayBlockStates)
    
    #Send input speed to output:
    def sendSpeed(self):
        inputSpeed = self.lineEditSpeedInput.text()
        self.lineEditSpeedOut.setText(inputSpeed)
    
    #Send input authority to output:
    def sendSpeed(self):
        inputSpeed = self.lineEditSpeedInput.text()
        self.lineEditSpeedOut.setText(inputSpeed)
    
    #Handle occupancy input:
    def sendOccupied(self):
        selectedBlock = self.comboBoxOccIn.currentText()
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
        if selectedBlock in self.failedBlocks:
            pass
        else:
            self.failedBlocks.append(selectedBlock)
            self.failedBlocks.sort()
        
        self.failedBlockObjects = []
        for wayside in self.allBlocks:
            for block in wayside:
                if block.ID in self.failedBlocks:
                    self.failedBlockObjects.append(block)

        self.failedBlocksChanged.emit(self.failedBlockObjects)
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
    
    #Function to display block states:
    def getUpdatedBlockList(self, allBlock):
        self.tempBlockList = allBlock
    
    def displayBlockStates(self):
        for block in self.tempBlockList:
            if((block.blockSection + block.blockNum) == self.comboBoxCheckBlock.currentText()):
                if(block.hasCrossing == False):
                    self.lineEditCrossingOut.setText("-")
                else:
                    if(block.crossingState == False):
                        self.lineEditCrossingOut.setText("UP")
                    else:
                        self.lineEditCrossingOut.setText("DOWN")
                
                if(block.hasSwitch == False):
                    self.lineEditSwitchOut.setText("-")
                else:
                    if(block.switchState == False):
                        self.lineEditSwitchOut.setText("LEFT")
                    else:
                        self.lineEditSwitchOut.setText("RIGHT")
                
                if(block.hasLight == False):
                    self.lineEditLightOut.setText("-")
                else:
                    if(block.lightState == False):
                        self.lineEditLightOut.setText("RED")
                    else:
                        self.lineEditLightOut.setText("GREEN")