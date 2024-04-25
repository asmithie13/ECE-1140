from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import time
import serial
import sys
import os
import re

#Using Block Class as a seperate file:
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

#Enable serial communication:
serialObject = serial.Serial('COM8', 9600)

from Wayside_HW.TrackController_HW_TB import *
from Wayside_HW.readTrackFile import *
from Wayside_HW.newParse import *
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

        #Constant lists for blocks affected based on light color:
        self.LIGHT_A1 = ['A1', 'A2']
        self.LIGHT_C12 = ['C11', 'C12']
        self.LIGHT_G29 = ['G29', 'G30', 'G31']
        self.LIGHT_Z150 = ['Y148', 'Y149', 'Z150']
        self.ALL_LIGHT = ['A1', 'A2', 'C12', 'D13', 'G29', 'G30', 'G31', 'Y148', 'Y149', 'Z150']

        #Disable manual mode operations, as program begins in automatic operation:
        self.groupBoxManual.setEnabled(False)

        #Initialize an empty list to hold all blocks:
        self.allTripleIDs = [] #This is unused
        self.allBlocks = readTrackFile("Wayside_HW/greenLine.csv", self.allTripleIDs)
        for block in self.allBlocks:
            block.Wayside = "W1"

        #Initialize a flag integer to determine which mode the system is currently in:
        self.modeFlag = 0 #0 = Automatic, 1 = Manual, 2 = Maintenance

        #Lists to hold blocks that are currently occupied or closed by CTC:
        self.previousOccupiedBlock = []
        self.occupiedBlocks = []
        self.occupiedBlockSections = []
        self.listOccIDs = []

        self.closedBlocks = []
        self.listClosedIDs = []

        self.maintenanceSwitches = []

        self.closedFlag = 0
        self.biFlag = 0

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
        occupiedBlocks.sort()
        if occupiedBlocks == self.listOccIDs and self.closedFlag == 0:
            return
        
        if 'F22' in occupiedBlocks:
            self.biFlag += 1
        
        if 'F27' in occupiedBlocks:
            self.biFlag = 0

        self.previousOccupiedBlock = self.occupiedBlocks
        
        self.listOccIDs = occupiedBlocks #Argument received is a string of occupied block IDs
        for block in self.closedBlocks:
            self.listOccIDs.append(block.ID)

        self.occupiedBlocks = [] #Make a list of block objects that are occupied
        for block in self.allBlocks:
            if block.ID in self.listOccIDs:
                self.occupiedBlocks.append(block)
        
        for block in self.allBlocks: #Set occupancy status in the list of all blocks
            if block.ID in self.listOccIDs:
                block.occupied = 1
            else:
                block.occupied = 0
        
        for block in self.occupiedBlocks: #Set occupancy status in the list of all blocks
            block.occupied = 1
        
        self.sendOccupiedBlocks.emit(self.occupiedBlocks)
        listBlockIDOccupied = []
        listBlockStrOccupied = ""

        for block in self.occupiedBlocks:
            listBlockIDOccupied.append(block.ID)
        listBlockIDOccupied.sort()
        for ID in listBlockIDOccupied:
            listBlockStrOccupied = listBlockStrOccupied + ID + " "
        self.lineEditOccupied.setText(listBlockStrOccupied)

        self.setMaintenanceSwitch() #Sets any time that there is a new occupancy
        #Must be called again after automatic mode switch positions are determined

        self.closedFlag = 0
        if self.modeFlag == 0:
            self.automaticMode()
        
    def getClosedBlocks(self, closedBlocks):
        self.closedFlag = 1
        for block in closedBlocks:
            if block.maintenance == 1 and block not in self.closedBlocks:
                self.closedBlocks.append(block)
                self.listClosedIDs.append(block.ID)
        
            elif block.maintenance == 0:
                for blockTwo in self.closedBlocks:
                    if block.ID == blockTwo.ID:
                        self.closedBlocks.remove(block)
                        self.listClosedIDs.remove(block.ID)
                        self.listOccIDs.remove(block.ID)

                for blockTwo in self.occupiedBlocks:
                    if block.ID == blockTwo.ID:
                        self.occupiedBlocks.remove(blockTwo)

        self.modeHandler(self.listOccIDs)

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
        occupiedBlockSections = []
        for block in self.occupiedBlocks:
            if block.blockSection not in occupiedBlockSections:
                occupiedBlockSections.append(block.blockSection)
        occupiedBlockSections.sort()
        self.occupiedBlockSections = occupiedBlockSections

        #Send string with flag at end to send block occupancies serially:
        occupiedBlockString = ""
        for section in self.occupiedBlockSections:
            occupiedBlockString += section
        occupiedBlockString += '1'
        occupiedBlockBytes = occupiedBlockString.encode()

        '''BEGIN SERIAL COMMUNICATION'''
        serialObject.write(occupiedBlockBytes)
        #Receiving serial responses from the Raspberry Pi:
        copyBlocks = self.allBlocks
        attributeList = []
        
        breakFlag = 0
        while True:
           if serialObject.in_waiting > 0:
                myAttribute = serialObject.read(serialObject.in_waiting).decode('utf-8')
                if len(myAttribute) > 1:
                    for char in myAttribute:
                        if char == 'A':
                            breakFlag = 1
                            break
                        else:
                            attributeList.append(char)
                else:
                    if myAttribute == 'A':
                            break
                    else:
                        attributeList.append(myAttribute)
                if breakFlag == 1:
                    break
        
        #Parse PLC file and adjust blocks accordingly:
        self.allBlocks = newParse(occupiedBlockSections, self.allBlocks)
        attributeListSoftware = []
        for block in self.allBlocks:
            if block.LIGHT == True:
                attributeListSoftware.append(str(block.lightState))
            elif block.SWITCH == True:
                attributeListSoftware.append(str(block.switchState))
            elif block.CROSSING == True:
                attributeListSoftware.append(str(block.crossingState))

        if attributeList != attributeListSoftware:
            self.lineEditHardware.setText("ERRORS DETECTED. STOPPING ALL TRAINS.")
            for block in self.allBlocks:
                block.authority = False
                self.sendUpdatedBlocks.emit(self.allBlocks)
        else:
            #Ajust block-wise authority based on active red lights:
            self.setMaintenanceSwitch()
            self.updateBooleanAuth()
            self.preventCollision()
            self.sendUpdatedBlocks.emit(self.allBlocks)
        
        '''self.setMaintenanceSwitch()
        self.updateBooleanAuth() #Uncomment when hardware is not connected
        self.preventCollision() #Function to prevent occupancy collisions
        self.sendUpdatedBlocks.emit(self.allBlocks) #Uncomment when hardware is not connected'''
    
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

        tempBlockID = self.comboBoxSection.currentText() + self.comboBoxBlock.currentText()

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
        
        for block in self.maintenanceSwitches:
            if block.ID == tempBlockID:
                self.frameSwitch.setEnabled(False)
        
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

        #Ajust block-wise authority based on active red lights:
        self.updateBooleanAuth()
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

        #Ajust block-wise authority based on active red lights:
        self.updateBooleanAuth()
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
    
    def updateBooleanAuth(self):
        #Ajust block-wise authority based on active red lights:
        for block in self.allBlocks:
            if block.ID == 'A1':
                tempA1 = block.lightState
            elif block.ID == 'C12':
                tempC12 = block.lightState
            elif block.ID == 'G29':
                tempG29 = block.lightState
            elif block.ID == 'Z150':
                tempZ150 = block.lightState
        
        if tempA1 == 0:
            for block in self.allBlocks:
                if block.ID in self.LIGHT_A1:
                    block.authority = False
        else:
            for block in self.allBlocks:
                if block.ID in self.LIGHT_A1:
                    block.authority = True
        
        if tempC12 == 0:
            for block in self.allBlocks:
                if block.ID in self.LIGHT_C12:
                    block.authority = False
        else:
            for block in self.allBlocks:
                if block.ID in self.LIGHT_C12:
                    block.authority = True
        
        if tempG29 == 0:
            for block in self.allBlocks:
                if block.ID in self.LIGHT_G29:
                    block.authority = False
        else:
            for block in self.allBlocks:
                if block.ID in self.LIGHT_G29:
                    block.authority = True
        
        if tempZ150 == 0:
            for block in self.allBlocks:
                if block.ID in self.LIGHT_Z150:
                    block.authority = False
        else:
            for block in self.allBlocks:
                if block.ID in self.LIGHT_Z150:
                    block.authority = True
    
    def getMaintenanceSwitch(self, switchPos):
        tempBlockID = self.comboBoxSection.currentText() + self.comboBoxBlock.currentText()

        for block in switchPos:
            if block.maintenance == 1:
                self.maintenanceSwitches.append(block)
                if self.modeFlag == 1 and block.ID == tempBlockID:
                    if block.switchState == False:
                        self.pushButtonLeft.setStyleSheet("background-color: white")
                        self.pushButtonLeft.setFont(QFont("Times New Roman", 12))
                        self.pushButtonRight.setStyleSheet("background-color: #9bc0f0")
                        self.pushButtonRight.setFont(QFont("Times New Roman", 12))
                    elif block.switchState == True:
                        self.pushButtonRight.setStyleSheet("background-color: white")
                        self.pushButtonRight.setFont(QFont("Times New Roman", 12))
                        self.pushButtonLeft.setStyleSheet("background-color: #9bc0f0")
                        self.pushButtonLeft.setFont(QFont("Times New Roman", 12))
                    self.frameSwitch.setEnabled(False)
            elif block.maintenance == 0:
                for blockTwo in self.maintenanceSwitches:
                    if block.ID == blockTwo.ID:
                        self.maintenanceSwitches.remove(blockTwo)
                if self.modeFlag == 1 and block.ID == tempBlockID:
                    self.frameSwitch.setEnabled(True)
                    self.pushButtonLeft.setEnabled(True)
                    self.pushButtonRight.setEnabled(True)
    
        self.setMaintenanceSwitch()
    
    def setMaintenanceSwitch(self): #Function to set maintenance mode switch positions from CTC
        flagLightOne = None
        flagLightTwo = None

        for blockOne in self.maintenanceSwitches:
            for blockTwo in self.allBlocks:
                if blockOne.ID == blockTwo.ID:
                    blockTwo.switchState = blockOne.switchState
                    if self.modeFlag == 0:
                        if blockTwo.ID == 'D13' and blockTwo.switchState == True:
                            flagLightOne = True
                        elif blockTwo.ID == 'D13' and blockTwo.switchState == False:
                            flagLightOne = False
                        
                        if blockTwo.ID == 'F28' and blockTwo.switchState == True:
                            flagLightTwo = True
                            
                        elif blockTwo.ID == 'F28' and blockTwo.switchState == False:
                            flagLightTwo = False
    
        if self.modeFlag == 0:
            for block in self.allBlocks:
                if block.ID == 'A1' and flagLightOne == False:
                    block.lightState = True
                elif block.ID == 'A1' and flagLightOne == True:
                    block.lightState = False
                
                if block.ID == 'C12' and flagLightOne == False:
                    block.lightState = False
                elif block.ID == 'C12' and flagLightOne == True:
                    block.lightState = True

                if block.ID == 'Z150' and flagLightTwo == False:
                    block.lightState = True
                elif block.ID == 'Z150' and flagLightTwo == True:
                    block.lightState = False
                
                if block.ID == 'G29' and flagLightTwo == False:
                    block.lightState = False
                elif block.ID == 'G29' and flagLightTwo == True:
                    block.lightState = True
        
        if not self.listOccIDs and self.modeFlag == 0:
            self.updateBooleanAuth()
            self.sendUpdatedBlocks.emit(self.allBlocks)
        
        if self.modeFlag == 1:
            self.sendUpdatedBlocks.emit(self.allBlocks)
        
    def preventCollision(self):
        oneDirectionOne = ['G', 'H', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #Block sections where collisions could occur
        oneDirectionTwo = ['A', 'B', 'C'] 
        biDirection = ['D', 'E', 'F']

        tempSkip = []
        for index, block in enumerate(self.allBlocks):
            if block.blockSection in oneDirectionOne:
                if block.occupied == True:
                    self.allBlocks[index-1].authority = False
                    self.allBlocks[index-2].authority = False
                    tempSkip.append(self.allBlocks[index-1])
                    tempSkip.append(self.allBlocks[index-2])
                elif block.occupied == False and block.ID not in self.ALL_LIGHT:
                    if block not in tempSkip:
                        block.authority = True
                    if self.allBlocks[index-1] not in tempSkip:
                        self.allBlocks[index-1].authority = True
                    if self.allBlocks[index-2] not in tempSkip:
                        self.allBlocks[index-2].authority = True
            if block.blockSection in oneDirectionTwo:
                if block.occupied == True:
                    self.allBlocks[index+1].authority = False
                    self.allBlocks[index+2].authority = False
                    tempSkip.append(self.allBlocks[index+1])
                    tempSkip.append(self.allBlocks[index+2])
                elif block.occupied == False and block.ID not in self.ALL_LIGHT:
                    if block not in tempSkip:
                        block.authority = True
                    if self.allBlocks[index+1] not in tempSkip:
                        self.allBlocks[index+1].authority = True
                    if self.allBlocks[index+2] not in tempSkip:
                        self.allBlocks[index+2].authority = True
            if block.blockSection in biDirection:
                if block.ID == 'D13':
                    continue
                if block.ID == 'F22' and self.biFlag >= 2:
                    if block.occupied == True:
                        self.allBlocks[index-1].authority = False
                        self.allBlocks[index-2].authority = False
                        tempSkip.append(self.allBlocks[index-1])
                        tempSkip.append(self.allBlocks[index-2])
                        continue

                if self.allBlocks[index-1] in self.previousOccupiedBlock:
                    if block.occupied == True:
                        self.allBlocks[index-1].authority = False
                        self.allBlocks[index-2].authority = False
                        tempSkip.append(self.allBlocks[index-1])
                        tempSkip.append(self.allBlocks[index-2])
                    elif block.occupied == False and block.ID not in self.ALL_LIGHT:
                        if block not in tempSkip:
                            block.authority = True
                        if self.allBlocks[index-1] not in tempSkip:
                            self.allBlocks[index-1].authority = True
                        if self.allBlocks[index-2] not in tempSkip:
                            self.allBlocks[index-2].authority = True
                elif self.allBlocks[index+1] in self.previousOccupiedBlock:
                    if block.occupied == True:
                        self.allBlocks[index+1].authority = False
                        self.allBlocks[index+2].authority = False
                        tempSkip.append(self.allBlocks[index+1])
                        tempSkip.append(self.allBlocks[index+2])
                    elif block.occupied == False and block.ID not in self.ALL_LIGHT:
                        if block not in tempSkip:
                            block.authority = True
                        if self.allBlocks[index+1] not in tempSkip:
                            self.allBlocks[index+1].authority = True
                        if self.allBlocks[index+2] not in tempSkip:
                            self.allBlocks[index+2].authority = True
                #The following condition indicates a track failure, since an occupancy is randomly generated...
                #Close blocks on either side as response:
                elif self.allBlocks[index-1] not in self.previousOccupiedBlock and self.allBlocks[index+1] not in self.previousOccupiedBlock:
                    if block.occupied == True:
                        self.allBlocks[index+1].authority = False
                        self.allBlocks[index+2].authority = False
                        tempSkip.append(self.allBlocks[index+1])
                        tempSkip.append(self.allBlocks[index+2])
                        self.allBlocks[index-1].authority = False
                        self.allBlocks[index-2].authority = False
                        tempSkip.append(self.allBlocks[index-1])
                        tempSkip.append(self.allBlocks[index-2])
                    elif block.occupied == False and block.ID not in self.ALL_LIGHT:
                        if block not in tempSkip:
                            block.authority = True
                        if self.allBlocks[index+1] not in tempSkip:
                            self.allBlocks[index+1].authority = True
                        if self.allBlocks[index+2] not in tempSkip:
                            self.allBlocks[index+2].authority = True
                        if self.allBlocks[index-1] not in tempSkip:
                            self.allBlocks[index-1].authority = True
                        if self.allBlocks[index-2] not in tempSkip:
                            self.allBlocks[index-2].authority = True