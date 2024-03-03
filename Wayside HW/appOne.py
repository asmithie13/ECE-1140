from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtCore import (Qt, pyqtSignal)
from Block import Block
from otherFunctions import *
import sys
import serial
import time

#Set-up serial communication
#Testing w/o Arduino connection

#ser = serial.Serial('COM5', 9600, timeout=0)
#time.sleep(2)

#Initialization of UI:
class TrackController_UI(QMainWindow):

    #Signals:
    blockStates = pyqtSignal(list)

    def __init__(self):
        #Load-in UI from the TrackControllerHW_UI file:
        super(TrackController_UI, self).__init__()
        uic.loadUi("Wayside HW/TrackControllerHW_UI.ui", self)
        
        #Read all blocks and their attributes (Crossings, switches, etc.)
        self.waysideBlue = readTrackFile("blueLine.csv")
        self.allGreenBlocks = readTrackFile("greenLine.csv")
        self.allRedBlocks = readTrackFile("redLine.csv")
    
        #Divide the red and green line sections into four separate waysides:
        self.waysideOne, self.waysideTwo = splitGreenBlocks(self.allGreenBlocks)
        self.waysideThree, self.waysideFour = splitRedBlocks(self.allRedBlocks)
    
        #Disable automatic mode button until a PLC file is uploaded:
        self.modeFlag = 0 #Determines if system is in initial manual or post-automatic manual
        self.checkAuto.setEnabled(False)
        self.checkManual.setChecked(True)
        self.manualMode()

        #Set wayside and block selections as disabled before a line is selected:
        self.comboBoxWayside.setEnabled(False)
        self.comboBoxSection.setEnabled(False)
        self.comboBoxBlock.setEnabled(False)

        self.buttonCrossing.setEnabled(False)
        self.buttonSwitch.setEnabled(False)
        self.buttonLight.setEnabled(False)

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

        #Section selection signal:
        self.comboBoxSection.activated.connect(self.sectionSelect)

        #Block selection signal:
        self.comboBoxBlock.activated.connect(self.setBlockConditions)

        #Signals for attribute buttons:
        self.buttonCrossing.clicked.connect(self.setCrossing)
        self.buttonSwitch.clicked.connect(self.setSwitch)
        self.buttonLight.clicked.connect(self.setLight)
    
    #Function to change the position of the crossing:
    def setCrossing(self):
        #Assign the temporary list to be altered by the wayside programmer:
        if(self.comboBoxWayside.currentText() == "Blue"):
            tempBlockList = self.waysideBlue
        elif(self.comboBoxWayside.currentText() == "1"):
            tempBlockList = self.waysideOne
        elif(self.comboBoxWayside.currentText() == "2"):
            tempBlockList = self.waysideTwo
        elif(self.comboBoxWayside.currentText() == "3"):
            tempBlockList = self.waysideThree
        elif(self.comboBoxWayside.currentText() == "4"):
            tempBlockList = self.waysideFour

        for block in tempBlockList:
            if(block.blockSection == self.comboBoxSection.currentText() and block.blockNum == self.comboBoxBlock.currentText()):
                if(block.crossingState == False):
                    block.crossingState = True
                    self.lineEditCrossingState.setText("DOWN")
                    self.buttonCrossing.setText("UP")
                else:
                    block.crossingState = False
                    self.lineEditCrossingState.setText("UP")
                    self.buttonCrossing.setText("DOWN")

        if(self.comboBoxWayside.currentText() == "Blue"):
            self.waysideBlue = tempBlockList
            self.blockStates.emit(self.waysideBlue)
        elif(self.comboBoxWayside.currentText() == "1"):
            self.waysideOne = tempBlockList
            self.blockStates.emit(self.waysideOne)
        elif(self.comboBoxWayside.currentText() == "2"):
            self.waysideTwo = tempBlockList
            self.blockStates.emit(self.waysideTwo)
        elif(self.comboBoxWayside.currentText() == "3"):
            self.waysideThree = tempBlockList
            self.blockStates.emit(self.waysideThree)
        elif(self.comboBoxWayside.currentText() == "4"):
            self.waysideFour = tempBlockList
            self.blockStates.emit(self.waysideFour)
    
    #Function to change the position of the switch:
    def setSwitch(self):
        #Assign the temporary list to be altered by the wayside programmer:
        if(self.comboBoxWayside.currentText() == "Blue"):
            tempBlockList = self.waysideBlue
        elif(self.comboBoxWayside.currentText() == "1"):
            tempBlockList = self.waysideOne
        elif(self.comboBoxWayside.currentText() == "2"):
            tempBlockList = self.waysideTwo
        elif(self.comboBoxWayside.currentText() == "3"):
            tempBlockList = self.waysideThree
        elif(self.comboBoxWayside.currentText() == "4"):
            tempBlockList = self.waysideFour

        for block in tempBlockList:
            if(block.blockSection == self.comboBoxSection.currentText() and block.blockNum == self.comboBoxBlock.currentText()):
                if(block.switchState == False):
                    block.switchState = True
                    self.lineEditSwitchState.setText("RIGHT")
                    self.buttonSwitch.setText("LEFT")
                else:
                    block.switchState = False
                    self.lineEditSwitchState.setText("LEFT")
                    self.buttonSwitch.setText("RIGHT")
       
        if(self.comboBoxWayside.currentText() == "Blue"):
            self.waysideBlue = tempBlockList
            self.blockStates.emit(self.waysideBlue)
        elif(self.comboBoxWayside.currentText() == "1"):
            self.waysideOne = tempBlockList
            self.blockStates.emit(self.waysideOne)
        elif(self.comboBoxWayside.currentText() == "2"):
            self.waysideTwo = tempBlockList
            self.blockStates.emit(self.waysideTwo)
        elif(self.comboBoxWayside.currentText() == "3"):
            self.waysideThree = tempBlockList
            self.blockStates.emit(self.waysideThree)
        elif(self.comboBoxWayside.currentText() == "4"):
            self.waysideFour = tempBlockList
            self.blockStates.emit(self.waysideFour)

    #Function to change the color of the light:
    def setLight(self):
        #Assign the temporary list to be altered by the wayside programmer:
        if(self.comboBoxWayside.currentText() == "Blue"):
            tempBlockList = self.waysideBlue
        elif(self.comboBoxWayside.currentText() == "1"):
            tempBlockList = self.waysideOne
        elif(self.comboBoxWayside.currentText() == "2"):
            tempBlockList = self.waysideTwo
        elif(self.comboBoxWayside.currentText() == "3"):
            tempBlockList = self.waysideThree
        elif(self.comboBoxWayside.currentText() == "4"):
            tempBlockList = self.waysideFour

        for block in self.waysideBlue:
            if(block.blockSection == self.comboBoxSection.currentText() and block.blockNum == self.comboBoxBlock.currentText()):
                if(block.lightState == False):
                    block.lightState = True
                    self.lineEditLightState.setText("GREEN")
                    self.buttonLight.setText("RED")
                else:
                    block.lightState = False
                    self.lineEditLightState.setText("RED")
                    self.buttonLight.setText("GREEN")
                    
        if(self.comboBoxWayside.currentText() == "Blue"):
            self.waysideBlue = tempBlockList
            self.blockStates.emit(self.waysideBlue)
        elif(self.comboBoxWayside.currentText() == "1"):
            self.waysideOne = tempBlockList
            self.blockStates.emit(self.waysideOne)
        elif(self.comboBoxWayside.currentText() == "2"):
            self.waysideTwo = tempBlockList
            self.blockStates.emit(self.waysideTwo)
        elif(self.comboBoxWayside.currentText() == "3"):
            self.waysideThree = tempBlockList
            self.blockStates.emit(self.waysideThree)
        elif(self.comboBoxWayside.currentText() == "4"):
            self.waysideFour = tempBlockList
            self.blockStates.emit(self.waysideFour)
    
    #Function to upload the PLC file and display the file path:
    def uploadPLCFile(self):
        fileName = QFileDialog.getOpenFileName(self, "Select PLC File", "C:")
        fileName = fileName[0] #Returns path of the selected PLC file

        self.lineEditBrowse.setText(fileName)
        self.buttonBrowse.setEnabled(False) #Cannot upload another PLC file if one is already uploaded
        #Only option is to switch to manual operation from this point

        self.checkManual.setChecked(False)
        self.checkAuto.setEnabled(True)
        self.checkAuto.setChecked(True)
        self.automaticMode()
    
    #Occurs if the blue line is selected:
    def blueLineButton(self): #FUNCTION IS GOOD
        self.comboBoxWayside.setEnabled(True)
        self.buttonBrowse.setEnabled(True)

        self.comboBoxWayside.clear()
        self.comboBoxSection.clear()
        self.comboBoxBlock.clear()

        self.comboBoxWayside.addItem("Blue") #Number of waysides will be hard-coded

    #Occurs if the red line is selected:
    def redLineButton(self): #FUNCTION IS GOOD
        self.comboBoxWayside.setEnabled(True)
        self.buttonBrowse.setEnabled(True)

        self.comboBoxWayside.clear()
        self.comboBoxSection.clear()
        self.comboBoxBlock.clear()

        self.comboBoxWayside.addItem("3")
        self.comboBoxWayside.addItem("4")

    #Occurs if the green line is selected:
    def greenLineButton(self): #FUNCTION IS GOOD
        self.comboBoxWayside.setEnabled(True)
        self.buttonBrowse.setEnabled(True)
        
        self.comboBoxWayside.clear()
        self.comboBoxSection.clear()
        self.comboBoxBlock.clear()

        self.comboBoxWayside.addItem("1")
        self.comboBoxWayside.addItem("2")

    #Occurs if the system is in automatic operation:
    def automaticMode(self):
        self.modeFlag = 1
        self.comboBoxWayside.setEnabled(False)
        self.comboBoxBlock.setEnabled(False)

        self.buttonSwitch.setEnabled(False)
        self.buttonLight.setEnabled(False)
        self.buttonCrossing.setEnabled(False)

        self.lineEditSwitchState.setText("-")
        self.lineEditLightState.setText("-")
        self.lineEditCrossingState.setText("-")
        #Here, there should be a connection to a function that interprets the PLC file,
        #and adjusts block attributes accordingly
    
    #Occcurs if the user selects manual operation:
    def manualMode(self):
        if(self.modeFlag == 1): #Indicates that this is not initial manual mode, but manual-from-automatic
            self.buttonBrowse.setEnabled(False) #Unable to move back to automatic operation if currently in manual
            self.checkAuto.setChecked(False)
            self.checkAuto.setEnabled(False) 
            self.lineEditBrowse.setText("")

        self.comboBoxWayside.setEnabled(True)
        self.comboBoxSection.setEnabled(True)
        self.comboBoxBlock.setEnabled(True)
    
    #Function to enable and fill the block section drop-down menu when a wayside is selected:
    def waysideSelect(self):
        self.comboBoxSection.setEnabled(True)
        if(self.comboBoxWayside.currentText() == "Blue"): #If the "Blue" wayside is selected (Temporary wayside for the blue line):
            pixmap = QPixmap("Wayside HW/blueline.png")
            self.labelPhoto.setPixmap(pixmap)

            self.comboBoxSection.clear()
            self.comboBoxBlock.clear()

            listBlockSec = []
            for blockNum in self.waysideBlue:
                if blockNum.blockSection in listBlockSec:
                    continue
                listBlockSec.append(blockNum.blockSection)
            self.comboBoxSection.addItems(listBlockSec)

        elif(self.comboBoxWayside.currentText() == "1"): #If the "Blue" wayside is selected (Temporary wayside for the blue line):
            #pixmap = QPixmap("Wayside HW/blueline.png") #Add photo later
            #self.labelPhoto.setPixmap(pixmap)

            self.comboBoxSection.clear()
            self.comboBoxBlock.clear()

            listBlockSec = []
            for blockNum in self.waysideOne:
                if blockNum.blockSection in listBlockSec:
                    continue
                listBlockSec.append(blockNum.blockSection)
            self.comboBoxSection.addItems(listBlockSec)
        
        elif(self.comboBoxWayside.currentText() == "2"): #If the "Blue" wayside is selected (Temporary wayside for the blue line):
            #pixmap = QPixmap("Wayside HW/blueline.png") #Add photo later
            #self.labelPhoto.setPixmap(pixmap)

            self.comboBoxSection.clear()
            self.comboBoxBlock.clear()

            listBlockSec = []
            for blockNum in self.waysideTwo:
                if blockNum.blockSection in listBlockSec:
                    continue
                listBlockSec.append(blockNum.blockSection)
            self.comboBoxSection.addItems(listBlockSec)
        
        elif(self.comboBoxWayside.currentText() == "3"): #If the "Blue" wayside is selected (Temporary wayside for the blue line):
            #pixmap = QPixmap("Wayside HW/blueline.png") #Add photo later
            #self.labelPhoto.setPixmap(pixmap)

            self.comboBoxSection.clear()
            self.comboBoxBlock.clear()

            listBlockSec = []
            for blockNum in self.waysideThree:
                if blockNum.blockSection in listBlockSec:
                    continue
                listBlockSec.append(blockNum.blockSection)
            self.comboBoxSection.addItems(listBlockSec)
        
        elif(self.comboBoxWayside.currentText() == "4"): #If the "Blue" wayside is selected (Temporary wayside for the blue line):
            #pixmap = QPixmap("Wayside HW/blueline.png") #Add photo later
            #self.labelPhoto.setPixmap(pixmap)

            self.comboBoxSection.clear()
            self.comboBoxBlock.clear()

            listBlockSec = []
            for blockNum in self.waysideFour:
                if blockNum.blockSection in listBlockSec:
                    continue
                listBlockSec.append(blockNum.blockSection)
            self.comboBoxSection.addItems(listBlockSec)
    
    #Function to enable and fill the block number drop-down menu when a block section is selected:
    def sectionSelect(self):
        self.comboBoxBlock.clear()
        self.comboBoxBlock.setEnabled(True)

        if(self.comboBoxWayside.currentText() == "Blue"):
            for blockNum in self.waysideBlue:
                if(blockNum.blockSection == self.comboBoxSection.currentText()):
                    self.comboBoxBlock.addItem(blockNum.blockNum)
        
        elif(self.comboBoxWayside.currentText() == "1"):
            for blockNum in self.waysideOne:
                if(blockNum.blockSection == self.comboBoxSection.currentText()):
                    self.comboBoxBlock.addItem(blockNum.blockNum)
        
        elif(self.comboBoxWayside.currentText() == "2"):
            for blockNum in self.waysideTwo:
                if(blockNum.blockSection == self.comboBoxSection.currentText()):
                    self.comboBoxBlock.addItem(blockNum.blockNum)
        
        elif(self.comboBoxWayside.currentText() == "3"):
            for blockNum in self.waysideThree:
                if(blockNum.blockSection == self.comboBoxSection.currentText()):
                    self.comboBoxBlock.addItem(blockNum.blockNum)
        
        elif(self.comboBoxWayside.currentText() == "4"):
            for blockNum in self.waysideFour:
                if(blockNum.blockSection == self.comboBoxSection.currentText()):
                    self.comboBoxBlock.addItem(blockNum.blockNum)

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

    #Function to set a selected block - Enables programmer to edit block states:
    def setBlockConditions(self):

        #Assign the temporary list to be altered by the wayside programmer:
        if(self.comboBoxWayside.currentText() == "Blue"):
            tempBlockList = self.waysideBlue
        elif(self.comboBoxWayside.currentText() == "1"):
            tempBlockList = self.waysideOne
        elif(self.comboBoxWayside.currentText() == "2"):
            tempBlockList = self.waysideTwo
        elif(self.comboBoxWayside.currentText() == "3"):
            tempBlockList = self.waysideThree
        elif(self.comboBoxWayside.currentText() == "4"):
            tempBlockList = self.waysideFour

        #Scan all blocks in the temporary list, and find the selected one:
        for block in tempBlockList:
            if(block.blockSection == self.comboBoxSection.currentText() and block.blockNum == self.comboBoxBlock.currentText()):
                if(block.hasSwitch == True):
                    self.buttonSwitch.setEnabled(True)
                    self.buttonLight.setEnabled(True)

                    if(block.switchState == False):
                        self.lineEditSwitchState.setText("LEFT")
                        self.buttonSwitch.setText("RIGHT")
                    else:
                        self.lineEditSwitchState.setText("RIGHT")
                        self.buttonSwitch.setText("LEFT")
                    
                    if(block.lightState ==  False):
                        self.lineEditLightState.setText("RED")
                        self.buttonLight.setText("GREEN")
                    else:
                        self.lineEditLightState.setText("GREEN")
                        self.buttonLight.setText("RED")
                
                elif(block.hasSwitch == False):
                    self.buttonSwitch.setEnabled(False)
                    self.buttonLight.setEnabled(False)

                    self.lineEditSwitchState.setText("-")
                    self.lineEditLightState.setText("-")

                if(block.hasCrossing == True):
                    self.buttonCrossing.setEnabled(True)
                    
                    if(block.crossingState ==  False):
                        self.lineEditCrossingState.setText("UP")
                        self.buttonCrossing.setText("DOWN")
                    else:
                        self.lineEditCrossingState.setText("DOWN")
                        self.buttonCrossing.setText("UP")

                elif(block.hasCrossing == False):
                    self.buttonCrossing.setEnabled(False)
                    self.lineEditCrossingState.setText("-")
        
        if(self.comboBoxWayside.currentText() == "Blue"):
            self.waysideBlue = tempBlockList
            self.blockStates.emit(self.waysideBlue)
        elif(self.comboBoxWayside.currentText() == "1"):
            self.waysideOne = tempBlockList
            self.blockStates.emit(self.waysideOne)
        elif(self.comboBoxWayside.currentText() == "2"):
            self.waysideTwo = tempBlockList
            self.blockStates.emit(self.waysideTwo)
        elif(self.comboBoxWayside.currentText() == "3"):
            self.waysideThree = tempBlockList
            self.blockStates.emit(self.waysideThree)
        elif(self.comboBoxWayside.currentText() == "4"):
            self.waysideFour = tempBlockList
            self.blockStates.emit(self.waysideFour)

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

        self.totalBlueBlock = readTrackFile("blueLine.csv")
        for block in self.totalBlueBlock:
            self.comboBoxOccIn.addItem(block.blockSection + block.blockNum)
            self.comboBoxFailedIn.addItem(block.blockSection + block.blockNum)
            self.comboBoxCheckBlock.addItem(block.blockSection + block.blockNum)
        
        #Clear block fields:
        self.buttonClearOcc.clicked.connect(self.clearOccupied)
        self.buttonClearFailed.clicked.connect(self.clearFailed)

        #Temporary blocks - Block being displayed at one time
        self.tempBlockList = []

        self.comboBoxCheckBlock.activated.connect(self.displayBlockStates)
    
    #Send input speed to output (Wayside does not change):
    def sendSpeed(self):
        inputSpeed = self.lineEditSpeedInput.text()
        self.lineEditSpeedOut.setText(inputSpeed)
    
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
        #currentText = self.lineEditFailedOut.text()
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

#Intialize Wayside object
class Wayside():
    def __init__(self):
        #Create instance of window:
        app = QApplication(sys.argv)
        windowOne = TrackController_UI()
        windowTwo = TrackController_TestBench()

        windowOne.blockStates.connect(windowTwo.getUpdatedBlockList)

        windowTwo.occBlocksChanged.connect(windowOne.displayOccupancies)
        windowTwo.failedBlocksChanged.connect(windowOne.displayFailures)

        windowOne.show()
        windowTwo.show()
        sys.exit(app.exec_())

waysideOne = Wayside()