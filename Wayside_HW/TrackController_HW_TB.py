from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys
import os
import re

#Using Block Class as a seperate file
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from Track_Resources.Block import Block
from Wayside_HW.readTrackFile import *

class TrackController_HW_TB(QMainWindow):
    #Signals:
    occupiedBlocksSignal = pyqtSignal(list)
    closedBlocksSignal = pyqtSignal(list)
    speedSignal = pyqtSignal(int)
    authoritySignal = pyqtSignal(int)

    def __init__(self):
        #Upload UI file:
        super(TrackController_HW_TB, self).__init__()
        uic.loadUi("Wayside HW/TrackController_HW_TB.ui", self)

        #Initialize an empty list to hold all blocks:
        self.allTripleIDs = [] #Don't need for TB
        self.allBlocks = readTrackFile("Wayside HW/greenLine.csv", self.allTripleIDs)

        self.listBlockIDs = []
        for block in self.allBlocks:
            self.listBlockIDs.append(block.ID)
        
        self.comboBoxOccupancies.addItems(self.listBlockIDs)
        self.comboBoxClosures.addItems(self.listBlockIDs)
        self.comboBoxBlockStates.addItems(self.listBlockIDs)

        #Initialize a list to hold block occupancies and closures:
        self.occupiedBlocks = []
        self.closedBlocks = []

        #Signals:
        self.comboBoxOccupancies.activated.connect(self.selectOccupiedBlocks)
        self.comboBoxClosures.activated.connect(self.selectClosedBlocks)
        self.comboBoxBlockStates.activated.connect(self.displayBlockStates)
        self.pushButtonClearOcc.clicked.connect(self.clearOccupiedBlocks)
        self.pushButtonClearClose.clicked.connect(self.clearClosedBlocks)
        self.lineEditAuthIn.returnPressed.connect(self.sendAuth)
        self.lineEditSpeedIn.returnPressed.connect(self.sendSpeed)

    def selectOccupiedBlocks(self):
        currentBlockStr = self.comboBoxOccupancies.currentText()
        for block in self.allBlocks:
            if block.ID == currentBlockStr:
                self.occupiedBlocks.append(block)
                break
        self.occupiedBlocksSignal.emit(self.occupiedBlocks)
    
    def selectClosedBlocks(self):
        currentBlockStr = self.comboBoxClosures.currentText()
        for block in self.allBlocks:
            if block.ID == currentBlockStr:
                self.closedBlocks.append(block)
                break
        self.closedBlocksSignal.emit(self.closedBlocks)
    
    def clearOccupiedBlocks(self):
        self.occupiedBlocks.clear()
        self.occupiedBlocksSignal.emit(self.occupiedBlocks)
    
    def clearClosedBlocks(self):
        self.closedBlocks.clear()
        self.closedBlocksSignal.emit(self.closedBlocks)

    def sendSpeed(self):
        tempSpeed = int(self.lineEditSpeedIn.text())
        self.speedSignal.emit(tempSpeed)
        #Add signal here to main UI
    
    def sendAuth(self):
        tempAuth = int(self.lineEditAuthIn.text())
        self.authoritySignal.emit(tempAuth)
        #Add signal here to main UI
    
    def receiveSpeed(self, receivedSpeed):
        self.lineEditSpeedOut.setText(str(receivedSpeed))

    def receiveAuthority(self, receivedAuthority):
        self.lineEditAuthOut.setText(str(receivedAuthority))
    
    def receiveOccupiedBlocks(self, occupiedBlocks):
        blockOccupancyStr = ""
        for block in occupiedBlocks:
            blockOccupancyStr = blockOccupancyStr + block.ID + " "
        self.lineEditOccupancies.setText(blockOccupancyStr)
    
    def receiveUpdatedBlocks(self, updatedBlocks):
        self.allBlocks = updatedBlocks

    def displayBlockStates(self):
        for block in self.allBlocks:
            if block.ID == self.comboBoxBlockStates.currentText():
                tempBlock = block
                break
        
        if tempBlock.LIGHT == False:
            self.lineEditLight.setText("-")
        else:
            if tempBlock.lightState == False:
                self.lineEditLight.setText("RED")
            else:
                self.lineEditLight.setText("GREEN")
        
        if tempBlock.SWITCH == False:
            self.lineEditSwitch.setText("-")
        else:
            if tempBlock.switchState == False:
                self.lineEditSwitch.setText("RIGHT")
            else:
                self.lineEditSwitch.setText("LIGHT")
        
        if tempBlock.CROSSING == False:
            self.lineEditCrossing.setText("-")
        else:
            if tempBlock.crossingState == False:
                self.lineEditCrossing.setText("DOWN")
            else:
                self.lineEditCrossing.setText("UP")

   
