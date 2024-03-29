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

from Wayside_HW.TrackController_HW_TB import *
from Wayside_HW.readTrackFile import *
from Track_Resources.Block import Block

#Main train controller class:
class TrackController_HW(QMainWindow):
    #Signals:
    sendSpeedAuthority = pyqtSignal(list)
    sendUpdatedBlocks = pyqtSignal(list)
    sendOccupiedBlocks = pyqtSignal(list)
    
    def __init__(self):
        #Upload UI file:
        super(TrackController_HW, self).__init__()
        uic.loadUi("Wayside_HW/TrackController_HW.ui", self)

        #Disable manual mode operations, as program begins in automatic operation:
        self.groupBoxManual.setEnabled(False)

        #Initialize an empty list to hold all blocks:
        self.allTripleIDs = []
        self.allBlocks = readTrackFile("Wayside_HW/greenLine.csv", self.allTripleIDs)

        #Initialize a flag integer to determine which mode the system is currently in:
        self.modeFlag = 0 #0 = Automatic, 1 = Manual, 2 = Maintenance

        #Lists to hold blocks that are currently occupied or closed by CTC:
        self.occupiedBlocks = []
        self.closedBlocks = []

        #Signals (Manual mode-related):
        self.checkBoxManual.clicked.connect(self.manualMode)
        self.comboBoxSection.activated.connect(self.selectBlock)
        self.comboBoxBlock.activated.connect(self.initialBlockConditions)
        self.pushButtonRed.clicked.connect(self.setLightRed)
        self.pushButtonGreen.clicked.connect(self.setLightGreen)
        self.pushButtonLeft.clicked.connect(self.setSwitchLeft)
        self.pushButtonRight.clicked.connect(self.setSwitchRight)
        self.pushButtonUp.clicked.connect(self.setCrossingUp)
        self.pushButtonDown.clicked.connect(self.setCrossingDown)
    
    def modeHandler(self, occupiedBlocks):
        self.occupiedBlocks = occupiedBlocks
        listBlockIDOccupied = []
        listBlockStrOccupied = ""
        self.sendOccupiedBlocks.emit(self.occupiedBlocks)

        for block in self.occupiedBlocks:
            listBlockIDOccupied.append(block.ID)
        listBlockIDOccupied.sort()
        for ID in listBlockIDOccupied:
            listBlockStrOccupied = listBlockStrOccupied + ID + " "
        self.lineEditOccupied.setText(listBlockStrOccupied)

        #If a block is closed by CTC, it is recognized as "occupied" by the PLC parser:
        for block in self.closedBlocks:
            if block not in self.occupiedBlocks:
                self.occupiedBlocks.append(block)

        if self.modeFlag == 0:
            self.automaticMode()
        
    def getClosedBlocks(self, closedBlocks):
        self.closedBlocks = closedBlocks
        listBlockIDClosed = []
        listBlockStrClosed = ""

        for block in closedBlocks:
            listBlockIDClosed.append(block.ID)
        listBlockIDClosed.sort()
        for ID in listBlockIDClosed:
            listBlockStrClosed = listBlockStrClosed + ID + " "
        self.lineEditClosed.setText(listBlockStrClosed)

    def manualMode(self):
        self.modeFlag = 1
        self.frameLight.setEnabled(False)
        self.frameSwitch.setEnabled(False)
        self.frameCrossing.setEnabled(False)

        #Automatic mode cannot be re-entered upon operating in manual mode
        self.checkBoxAutomatic.setChecked(False)
        self.checkBoxAutomatic.setEnabled(False)
    
        self.groupBoxManual.setEnabled(True)
        self.comboBoxSection.setEnabled(True)
        
        listSecIDs = []
        for block in self.allBlocks:
            if block.blockSection in listSecIDs:
                continue
            listSecIDs.append(block.blockSection)
        self.comboBoxSection.addItems(listSecIDs)
    
    def automaticMode(self):
        #Add the IDs of all occupanices to a list to be communicated serially
        occupiedBlockIDs = []
        for block in self.occupiedBlocks:
            occupiedBlockIDs.append(block.ID)
        occupiedBlockIDs.sort()
        
        #Initialize serial communication with Raspberry Pi here
        #Produce a list of changed block states to emit to Track Model, as conducted in manual operation
    
    def selectBlock(self):
        self.frameLight.setEnabled(False)
        self.frameSwitch.setEnabled(False)
        self.frameCrossing.setEnabled(False)

        self.pushButtonRed.setStyleSheet("background-color: white")
        self.pushButtonGreen.setStyleSheet("background-color: white")
        self.pushButtonLeft.setStyleSheet("background-color: white")
        self.pushButtonRight.setStyleSheet("background-color: white")
        self.pushButtonUp.setStyleSheet("background-color: white")
        self.pushButtonDown.setStyleSheet("background-color: white")

        self.pushButtonRed.setFont(QFont("Times New Roman", 12))
        self.pushButtonGreen.setFont(QFont("Times New Roman", 12))
        self.pushButtonLeft.setFont(QFont("Times New Roman", 12))
        self.pushButtonRight.setFont(QFont("Times New Roman", 12))
        self.pushButtonUp.setFont(QFont("Times New Roman", 12))
        self.pushButtonDown.setFont(QFont("Times New Roman", 12))

        self.comboBoxBlock.clear()
        listBlockNum = []
        for block in self.allBlocks:
            if block.blockSection == self.comboBoxSection.currentText():
                listBlockNum.append(block.blockNum)
        self.comboBoxBlock.addItems(listBlockNum)

    def initialBlockConditions(self):
        for block in self.allBlocks:
            if block.ID == self.comboBoxSection.currentText() + self.comboBoxBlock.currentText():
                selectedBlock = block
                break
        
        if selectedBlock.LIGHT == False:
            self.frameLight.setEnabled(False)
        else:
            self.frameLight.setEnabled(True)
            if selectedBlock.lightState == False:
                self.setLightRed()
            else:
                self.setLightGreen()
        
        if selectedBlock.SWITCH == False:
            self.frameSwitch.setEnabled(False)
        else:
            self.frameSwitch.setEnabled(True)
            if selectedBlock.switchState == False:
                self.setSwitchRight()
            else:
                self.setSwitchLeft()
        
        if selectedBlock.CROSSING == False:
            self.frameCrossing.setEnabled(False)
        else:
            self.frameCrossing.setEnabled(True)
            if selectedBlock.crossingState == False:
                self.setCrossingDown()
            else:
                self.setCrossingUp()
        
    def setLightRed(self):
        for block in self.allBlocks:
            if block.ID == self.comboBoxSection.currentText() + self.comboBoxBlock.currentText():
                block.lightState = False
                break
        self.sendUpdatedBlocks.emit(self.allBlocks)

        self.pushButtonGreen.setEnabled(True)
        self.pushButtonGreen.setStyleSheet("background-color : white")
        self.pushButtonGreen.setFont(QFont("Times New Roman", 12))
        self.pushButtonRed.setEnabled(False)
        self.pushButtonRed.setStyleSheet("background-color : #f06363")
        self.pushButtonRed.setFont(QFont("Times New Roman", 12))
    
    def setLightGreen(self):
        for block in self.allBlocks:
            if block.ID == self.comboBoxSection.currentText() + self.comboBoxBlock.currentText():
                block.lightState = True
                break
        self.sendUpdatedBlocks.emit(self.allBlocks)

        self.pushButtonRed.setEnabled(True)
        self.pushButtonRed.setStyleSheet("background-color : white")
        self.pushButtonRed.setFont(QFont("Times New Roman", 12))
        self.pushButtonGreen.setEnabled(False)
        self.pushButtonGreen.setStyleSheet("background-color : #99f7a4")
        self.pushButtonGreen.setFont(QFont("Times New Roman", 12))
    
    def setSwitchLeft(self):
        for block in self.allBlocks:
            if block.ID == self.comboBoxSection.currentText() + self.comboBoxBlock.currentText():
                block.switchState = True
                break
        self.sendUpdatedBlocks.emit(self.allBlocks)

        self.pushButtonRight.setEnabled(True)
        self.pushButtonRight.setStyleSheet("background-color: white")
        self.pushButtonRight.setFont(QFont("Times New Roman", 12))
        self.pushButtonLeft.setEnabled(False)
        self.pushButtonLeft.setStyleSheet("background-color: #9bc0f0")
        self.pushButtonLeft.setFont(QFont("Times New Roman", 12))
    
    def setSwitchRight(self):
        for block in self.allBlocks:
            if block.ID == self.comboBoxSection.currentText() + self.comboBoxBlock.currentText():
                block.switchState = False
                break
        self.sendUpdatedBlocks.emit(self.allBlocks)

        self.pushButtonLeft.setEnabled(True)
        self.pushButtonLeft.setStyleSheet("background-color: white")
        self.pushButtonLeft.setFont(QFont("Times New Roman", 12))
        self.pushButtonRight.setEnabled(False)
        self.pushButtonRight.setStyleSheet("background-color: #9bc0f0")
        self.pushButtonRight.setFont(QFont("Times New Roman", 12))
    
    def setCrossingUp(self):
        for block in self.allBlocks:
            if block.ID == self.comboBoxSection.currentText() + self.comboBoxBlock.currentText():
                block.crossingState = True
                break
        self.sendUpdatedBlocks.emit(self.allBlocks)

        self.pushButtonDown.setEnabled(True)
        self.pushButtonDown.setStyleSheet("background-color : white")
        self.pushButtonDown.setFont(QFont("Times New Roman", 12))
        self.pushButtonUp.setEnabled(False)
        self.pushButtonUp.setStyleSheet("background-color : #f0ecb1")
        self.pushButtonUp.setFont(QFont("Times New Roman", 12))

    def setCrossingDown(self):
        for block in self.allBlocks:
            if block.ID == self.comboBoxSection.currentText() + self.comboBoxBlock.currentText():
                block.crossingState = False
                break
        self.sendUpdatedBlocks.emit(self.allBlocks)

        self.pushButtonUp.setEnabled(True)
        self.pushButtonUp.setStyleSheet("background-color : white")
        self.pushButtonUp.setFont(QFont("Times New Roman", 12))
        self.pushButtonDown.setEnabled(False)
        self.pushButtonDown.setStyleSheet("background-color : #f0ecb1")
        self.pushButtonDown.setFont(QFont("Times New Roman", 12))
    
    def handleSpeedAuthority(self, receivedSpeedAuthority):
        self.sendSpeedAuthority.emit(receivedSpeedAuthority) #Pass-on distance-wise authority straight to train controller without changing