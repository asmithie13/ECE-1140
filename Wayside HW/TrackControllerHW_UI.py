from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from PyQt5.QtCore import (Qt, pyqtSignal)
from Block import *
from otherFunctions import *

#Initialization of UI:
class TrackController_UI(QMainWindow):
    
    #Signals:
    blockStates = pyqtSignal(list)

    def __init__(self):
        #Load-in UI from the TrackControllerHW_UI file:
        super(TrackController_UI, self).__init__()
        uic.loadUi("Wayside HW/TrackControllerHW_UI.ui", self)

        #Set triples involved in crossings for each wayside station:
        self.blueTriplesIDs = []
        self.redTriplesIDs = []
        self.greenTriplesIDs = []

        #Read all blocks and their attributes (Crossings, switches, etc.)
        self.waysideBlue = readTrackFile("blueLine.csv", self.blueTriplesIDs)
        self.waysideOne, self.waysideTwo = splitGreenBlocks(readTrackFile("greenLine.csv", self.greenTriplesIDs))
        self.waysideThree, self.waysideFour = splitRedBlocks(readTrackFile("redLine.csv", self.redTriplesIDs))

        #Occupied and failed blocks for each line:
        self.occupiedBlue = []
        #self.failedBlue = []

        self.occupiedGreen = []
        #self.failedGreen = []

        self.occupiedRed = []
        #self.failedRed = []

        #Set wayside and block selections as disabled before a line is selected:
        self.comboBoxWayside.setEnabled(False)
        self.comboBoxSection.setEnabled(False)
        self.comboBoxBlock.setEnabled(False)

        self.buttonCrossing.setEnabled(False)
        self.buttonSwitch.setEnabled(False)
        self.buttonLight.setEnabled(False)

        #Initialize wayside in manual mode before a PLC file is uploaded:
        self.modeFlag = 0
        self.checkManual.setChecked(True)
        self.checkAuto.setEnabled(False)
        self.manualMode()

        #Disable combo boxes until a line is selected:
        self.comboBoxWayside.setEnabled(False)
        self.comboBoxSection.setEnabled(False)
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
                    self.lineEditCrossingState.setText("UP")
                    self.buttonCrossing.setText("DOWN")
                else:
                    block.crossingState = False
                    self.lineEditCrossingState.setText("DOWN")
                    self.buttonCrossing.setText("UP")

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
                    self.lineEditSwitchState.setText("LEFT")
                    self.buttonSwitch.setText("RIGHT")
                else:
                    block.switchState = False
                    self.lineEditSwitchState.setText("RIGHT")
                    self.buttonSwitch.setText("LEFT")
       
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

        for block in tempBlockList:
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
        self.lineEditOccupiedBlocks.setText("")
        self.lineEditClosedBlocks.setText("")

        tempStr = ""
        for block in self.occupiedBlue:
            tempStr = tempStr + block.ID + " "
        self.lineEditOccupiedBlocks.setText(tempStr)
        tempStr = ""
        for block in self.failedBlue:
            tempStr = tempStr + block.ID + " "
        self.lineEditClosedBlocks.setText(tempStr)

        self.comboBoxWayside.setEnabled(True)
        self.buttonBrowse.setEnabled(True)

        self.comboBoxWayside.clear()
        self.comboBoxSection.clear()
        self.comboBoxBlock.clear()

        self.lineEditCrossingState.setText("-")
        self.lineEditSwitchState.setText("-")
        self.lineEditLightState.setText("-")

        #self.displayOccupancies()
        #self.displayFailures()

        self.comboBoxWayside.addItem("Blue") #Number of waysides will be hard-coded

    #Occurs if the red line is selected:
    def redLineButton(self): #FUNCTION IS GOOD
        self.lineEditOccupiedBlocks.setText("")
        self.lineEditClosedBlocks.setText("")

        tempStr = ""
        for block in self.occupiedRed:
            tempStr = tempStr + block.ID + " "
        self.lineEditOccupiedBlocks.setText(tempStr)
        tempStr = ""
        for block in self.failedRed:
            tempStr = tempStr + block.ID + " "
        self.lineEditClosedBlocks.setText(tempStr)

        self.comboBoxWayside.setEnabled(True)
        self.buttonBrowse.setEnabled(True)

        self.comboBoxWayside.clear()
        self.comboBoxSection.clear()
        self.comboBoxBlock.clear()

        self.lineEditCrossingState.setText("-")
        self.lineEditSwitchState.setText("-")
        self.lineEditLightState.setText("-")

        #self.displayOccupancies()
        #self.displayFailures()

        self.comboBoxWayside.addItem("3")
        self.comboBoxWayside.addItem("4")

    #Occurs if the green line is selected:
    def greenLineButton(self): #FUNCTION IS GOOD
        self.lineEditOccupiedBlocks.setText("")
        self.lineEditClosedBlocks.setText("")

        tempStr = ""
        for block in self.occupiedGreen:
            tempStr = tempStr + block.ID + " "
        self.lineEditOccupiedBlocks.setText(tempStr)
        tempStr = ""
        for block in self.failedGreen:
            tempStr = tempStr + block.ID + " "
        self.lineEditClosedBlocks.setText(tempStr)

        self.comboBoxWayside.setEnabled(True)
        self.buttonBrowse.setEnabled(True)
        
        self.comboBoxWayside.clear()
        self.comboBoxSection.clear()
        self.comboBoxBlock.clear()

        self.lineEditCrossingState.setText("-")
        self.lineEditSwitchState.setText("-")
        self.lineEditLightState.setText("-")

        #self.displayOccupancies()
        #self.displayFailures()

        self.comboBoxWayside.addItem("1")
        self.comboBoxWayside.addItem("2")

    #Occurs if the system is in automatic operation:
    def automaticMode(self):
        self.modeFlag = 1

        self.comboBoxWayside.clear()
        self.comboBoxSection.clear()
        self.comboBoxBlock.clear()

        self.comboBoxWayside.setEnabled(False)
        self.comboBoxSection.setEnabled(False)
        self.comboBoxBlock.setEnabled(False)

        self.radioButtonBlue.setCheckable(False)
        self.radioButtonGreen.setCheckable(False)
        self.radioButtonRed.setCheckable(False)

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
        if(self.modeFlag == 1):
            self.buttonBrowse.setEnabled(False) #Unable to move back to automatic operation if currently in manual
            self.checkAuto.setChecked(False)
            self.checkAuto.setEnabled(False) 
            self.lineEditBrowse.setText("")

        self.radioButtonBlue.setCheckable(True)
        self.radioButtonGreen.setCheckable(True)
        self.radioButtonRed.setCheckable(True)

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
        
        self.lineEditCrossingState.setText("-")
        self.lineEditSwitchState.setText("-")
        self.lineEditLightState.setText("-")
    
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
        
        self.lineEditCrossingState.setText("-")
        self.lineEditSwitchState.setText("-")
        self.lineEditLightState.setText("-")

    #Function to receive and display block occupancies:
    def displayOccupancies(self, occBlock):
        self.occupiedBlue = []
        self.occupiedGreen = []
        self.occupiedRed = []
       
        blueOcc = ""
        redOcc = ""
        greenOcc = ""
        for block in occBlock:
            if block.lineColor == "Blue":
                blueOcc = blueOcc + block.ID + " "
                self.occupiedBlue.append(block)
            elif block.lineColor == "Green":
                greenOcc = greenOcc + block.ID + " "
                self.occupiedGreen.append(block)
            if block.lineColor == "Red":
                redOcc = redOcc + block.ID + " "
                self.occupiedRed.append(block)
        
        if self.radioButtonBlue.isChecked():
            self.lineEditOccupiedBlocks.setText(blueOcc)
        elif self.radioButtonGreen.isChecked():
            self.lineEditOccupiedBlocks.setText(greenOcc)
        elif self.radioButtonRed.isChecked():
            self.lineEditOccupiedBlocks.setText(redOcc)
    
    #Function to receive and display block failures:
    def displayFailures(self, failBlock):
        self.failedBlue = []
        self.failedGreen = []
        self.failedRed = []

        blueFail = ""
        redFail = ""
        greenFail = ""
    
        for block in failBlock:
            if block.lineColor == "Blue":
                blueFail = blueFail + block.ID + " "
                self.failedBlue.append(block)
            elif block.lineColor == "Green":
                greenFail = greenFail + block.ID + " "
                self.failedGreen.append(block)
            if block.lineColor == "Red":
                redFail = redFail + block.ID + " "
                self.failedRed.append(block)
        
        if self.radioButtonBlue.isChecked():
            self.lineEditClosedBlocks.setText(blueFail)
        elif self.radioButtonGreen.isChecked():
            self.lineEditClosedBlocks.setText(greenFail)
        elif self.radioButtonRed.isChecked():
            self.lineEditClosedBlocks.setText(redFail)

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
                if(block.SWITCH == True):
                    self.buttonSwitch.setEnabled(True)
                    if(block.switchState == False):
                        self.lineEditSwitchState.setText("RIGHT")
                        self.buttonSwitch.setText("LEFT")
                    else:
                        self.lineEditSwitchState.setText("LEFT")
                        self.buttonSwitch.setText("RIGHT")
                elif(block.SWITCH == False):
                    self.buttonSwitch.setEnabled(False)
                    self.lineEditSwitchState.setText("-")
                
                if(block.LIGHT == True):
                    self.buttonLight.setEnabled(True)
                    if(block.lightState == False):
                        self.lineEditLightState.setText("RED")
                        self.buttonLight.setText("GREEN")
                    else:
                        self.lineEditLightState.setText("GREEN")
                        self.buttonLight.setText("RED")
                elif(block.LIGHT == False):
                    self.buttonLight.setEnabled(False)
                    self.lineEditLightState.setText("-")

                if(block.CROSSING == True):
                    self.buttonCrossing.setEnabled(True)
                    if(block.crossingState ==  False):
                        self.lineEditCrossingState.setText("DOWN")
                        self.buttonCrossing.setText("UP")
                    else:
                        self.lineEditCrossingState.setText("UP")
                        self.buttonCrossing.setText("DOWN")
                elif(block.CROSSING == False):
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