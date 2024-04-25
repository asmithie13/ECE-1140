import sys
import os
import re

# Using Block Class as a seperate file
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from Track_Resources.Block import Block
from PLC_Files.Parser import Parser
from PyQt5.QtCore import QTimer,pyqtSignal
import csv

def sort_by_number(block):
    return int(block[1:])  # Convert the string to an integer, excluding the 'B' prefix

#Function that reads all blocks from a *.csv file and assigns block attributes:
def readTrackFile(fileName,crossingTriples):
    totalBlocks = []
    lightBlocks = {}
    beaconTriple = [[]]
    #fileName = "Wayside SW/" + fileName
    with open(fileName, "r") as fileObject:
        readObj = csv.reader(fileObject, delimiter=",")
        for i, line in enumerate(readObj):
            hasCrossingTemp = False
            hasSwitchTemp = False
            hasLightTemp = False
            lightState = None
            crossingState = None
            switchState = None
            blockId = line[1] + line[2]
            if(i == 0):
                continue
            else:
                if(line[6] == "RAILWAY CROSSING"):
                    hasCrossingTemp = True
                    crossingState = True

                elif(line[6][0:6] == "SWITCH" and line[6].find("YARD") == -1):
                    hasSwitchTemp = True
                    switchState = True

                    numbers = re.findall(r'\b(\d+)-(\d+)\b', line[6])
                    current = {num: False for pair in numbers for num in pair}

                    #CONFIGURE YARD SWITCH BLOCKS LATER
                    if line[6].find("YARD") == -1: crossingTriples.append(list(current.keys()))
                    lightBlocks.update(current)

            tempBlock = Block(line[0],line[1],line[2],hasLightTemp,hasCrossingTemp,hasSwitchTemp,lightState,crossingState,switchState,blockId)
            tempBlock.blockLength = line[3]
            totalBlocks.append(tempBlock)

            #Assign light values now

        for block in totalBlocks:
            if block.ID[1:] in lightBlocks and (not block.SWITCH or block.lineColor == "Red"):
                block.LIGHT = True
                block.lightState = True

    return totalBlocks #Return a list of all blocks within the file

class WaysideSW(QMainWindow):

    #Signals
    sendSpecialBlocks = pyqtSignal(list)    #Send special blocks to testbench
    changeModeSend = pyqtSignal(bool)
    sendOccupiedBlocks = pyqtSignal(list)   #Send list of occupied blocks to CTC
    sendTrainSpeedAuth = pyqtSignal(list) #Send commanded speed to track model
    sendGreenSwitchPos = pyqtSignal(list)
    sendRedSwitchPos = pyqtSignal(list)

    #signal to send all blocks to testbench
    sendAllBlocks = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        uic.loadUi("Wayside_SW/Wayside_UI_Rough.ui",self)

        self.currentSpecialBlocks = None
        self.currentBlocks = None
        self.currentSwitchBlocks = None

        #Occupied Block list ordered by ID
        self.occupiedBlocks = []

        #List of train ID, inital speed, inital authority sent by CTC
        self.initialTrainSpeedAuthority = []

        #Defines Green Line blocks
        self.greenCrossingTriplesIDS = [] #ids of red crossing blocks
        self.allGreenBlocks = readTrackFile("Wayside_SW/Green_Line.csv",self.greenCrossingTriplesIDS)
        self.specialGreenBlocksW2 = []

        #beacon stuff
        with open('greenBeacon.txt', 'w') as file:
            beac1 = [[]]
            beacblock1 = [x for x in self.allGreenBlocks if int(x.blockNum) >= 63 and int(x.blockNum) <= 100]
            for block in beacblock1:
                info = [block.ID, block.blockLength]
                beac1.append(info)
            file.write("beac1: " + str(beac1) + "\n")

            beac2 = [[]]
            beacblock2 = [x for x in self.allGreenBlocks if x.blockSection == "N"]
            for block in beacblock2:
                info = [block.ID, block.blockLength]
                beac2.append(info)
            file.write("beac2: " + str(beac2) + "\n")

            beac3 = [[]]
            beacblock3 = [x for x in self.allGreenBlocks if int(x.blockNum) >= 101 and int(x.blockNum) <= 150]
            for block in beacblock3:
                info = [block.ID, block.blockLength]
                beac3.append(info)
            file.write("beac3: " + str(beac3) + "\n")

            beac4 = [[]]
            beacblock4 = [x for x in self.allGreenBlocks if int(x.blockNum) >= 12 and int(x.blockNum) <= 27]
            for block in beacblock4:
                info = [block.ID, block.blockLength]
                beac4.append(info)
            file.write("beac4: " + str(beac4) + "\n")

            beac5 = [[]]
            beacblock5 = [x for x in self.allGreenBlocks if int(x.blockNum) >= 12 and int(x.blockNum) <= 57]
            for block in beacblock5:
                info = [block.ID, block.blockLength]
                beac5.append(info)
            file.write("beac5: " + str(beac5) + "\n")


        #SW in charge of W1, HW in charge of W2

        wayside1Chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
        self.greenWayside2Blocks = [x for x in self.allGreenBlocks if x.blockSection not in wayside1Chars]
        self.currentBlocks = self.greenWayside2Blocks

        #for block in self.greenWayside2Blocks: print(block.ID)

        self.sendGreenSwitchPos.emit(self.greenWayside2Blocks)
                                     
        #Defines special greenblocks in wayside 1     
        for block in self.greenWayside2Blocks:
            if block.LIGHT or block.CROSSING or block.SWITCH : self.specialGreenBlocksW2.append(block)
            block.Wayside = "W2"
            
        

        #Defines Red line blocks
        self.redCrossingTriplesIDS = [] #ids of red crossing blocks
        self.allRedBlocks = readTrackFile("Wayside_SW/Red_Line.csv",self.redCrossingTriplesIDS)
        self.specialRedBlocksW1 = []
        self.specialRedBlocksW2 = []

        wayside1Chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.redWayside1Blocks = [x for x in self.allRedBlocks if x.blockSection in wayside1Chars]
        self.redWayside2Blocks = [x for x in self.allRedBlocks if x.blockSection not in wayside1Chars]

        for block in self.redWayside1Blocks:
            if block.LIGHT or block.CROSSING or block.SWITCH : self.specialRedBlocksW1.append(block)
            block.Wayside = "W1"

        for block in self.redWayside2Blocks:
            if block.LIGHT or block.CROSSING or block.SWITCH : self.specialRedBlocksW2.append(block)
            block.Wayside = "W2"

        #Create Parser Object
        self.currentSwitchBlocksNums = [['5','6','11']]

        self.sendRedSwitchPos.emit(self.allRedBlocks)

        #self.FileParser = Parser(None,self.redCrossingTriplesIDS,self.allRedBlocks)  #Currently testing red object
        self.FileParser = Parser(None,self.currentSwitchBlocksNums,self.currentBlocks)

        #holds last blocks
        self.previousOccupiedBlock = []

        # Buttons
        self.fileButton.clicked.connect(self.on_file_button_clicked)
        self.modeButton.clicked.connect(self.changeMode)
        #self.selectLine.stateChanged.connect(self.checkLine)
        self.selectGreenLine.stateChanged.connect(self.checkLine)
        self.selectRedLine.stateChanged.connect(self.checkLine)
        self.blockMenu.currentIndexChanged.connect(self.blockActions)
        self.greenButton.clicked.connect(self.greenButtonPushed)
        self.redButton.clicked.connect(self.redButtonPushed)
        self.upCrossingButton.clicked.connect(self.upButtonPushed)
        self.downCrossingButton.clicked.connect(self.downButtonPushed)
        self.switchButton.clicked.connect(self.switchButtonPushed)
        self.saveButton.clicked.connect(self.onSavePLCFile)
        self.waysideMenu.activated.connect(self.selectWayside)

        #initial signals
        #self.sendSpecialBlocks.emit(self.currentBlocks)
        self.changeModeSend.emit(True)

        #Original Map Image
        pixmap = QPixmap('Wayside_SW\green_red_lines.png')
        width = 400
        height = 400
        pixmap = pixmap.scaled(width, height)
        self.label_17.setPixmap(pixmap)

        #Dropdown menu
        self.blockMenu.addItems(['A3','A5','B6','C11'])
        #self.waysideMenu.addItems(['W1'])

        #Input Initial Conditions
        self.waysideMenu.setDisabled(True)
        self.blockMenu.setDisabled(True)
        self.modeButton.setDisabled(True)
        self.greenButton.setDisabled(True)
        self.redButton.setDisabled(True)
        self.upCrossingButton.setDisabled(True)
        self.downCrossingButton.setDisabled(True)
        self.upCrossingButton.setDisabled(True)
        self.switchButton.setDisabled(True)
        self.saveButton.setDisabled(True)
        self.fileButton.setDisabled(True)
    
    def on_file_button_clicked(self):
        # Open a file dialog to select a PLC file
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select PLC File", "", "Text Files (*.txt);;All Files (*)")

        if file_path:
            file = open(file_path,"r")
            self.FileParser.inputPLC = file.read()
            file.close
            self.modeButton.setEnabled(True) #Can't Change to automatic until PLC is inserted
            self.saveButton.setEnabled(True) #User can svae the PLC file after it is insertted

    def onSavePLCFile(self):
        if self.FileParser.inputPLC:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(self, "Save PLC File", "", "Text Files (*.txt);;All Files (*)")

            if file_path:
                with open(file_path, "w") as file:
                    file.write(self.FileParser.inputPLC)

    def changeMode(self):
        current_text = self.label_7.text()
        if current_text == "MANUAL":   
            self.label_7.setText("AUTOMATIC")

            self.FileParser.parsePLC()  #Update special blocks when automatic mode is set
            check1 = self.currentBlocks.copy #blocks after parsed
            self.FileParser.parsePLC()
            check2 = self.currentBlocks.copy

            if check1 != check2:
                for block in self.currentBlocks: block.authority = False
                print("Redundancy Check Failed")
                return
                
            for block in self.currentBlocks:
                self.handleLights(block)

            self.sendGreenSwitchPos.emit(self.greenWayside2Blocks)
            self.sendRedSwitchPos.emit(self.allRedBlocks)
            self.blockActions()
            self.sendAllBlocks.emit(self.currentBlocks)
            self.changeModeSend.emit(False)

        elif current_text == "AUTOMATIC":
            self.label_7.setText("MANUAL")
            self.blockActions()
            self.sendAllBlocks.emit(self.currentBlocks)
            self.changeModeSend.emit(True)
            self.modeButton.setDisabled(True)
            

    def checkLine(self):
        #checkStatus = self.selectLine.isChecked()
        checkGreen = self.selectGreenLine.isChecked()
        checkRed = self.selectRedLine.isChecked()

        if checkGreen:
            self.selectRedLine.setDisabled(True)
            self.waysideMenu.clear()
            self.waysideMenu.setEnabled(True)
            self.waysideMenu.addItems(['W2'])
            self.selectWayside()

        elif checkRed:
            self.selectGreenLine.setDisabled(True)
            self.waysideMenu.clear()
            self.waysideMenu.setEnabled(True)
            self.waysideMenu.addItems(['W1','W2'])
            self.selectWayside()

        else:
            self.selectGreenLine.setEnabled(True)
            self.selectRedLine.setEnabled(True)
            self.waysideMenu.setEnabled(False)
            self.blockMenu.setDisabled(True)

            self.greenButton.setStyleSheet("")
            self.redButton.setStyleSheet("")
            self.upCrossingButton.setStyleSheet("")
            self.downCrossingButton.setStyleSheet("")

            self.greenButton.setEnabled(False)
            self.redButton.setEnabled(False)
            self.upCrossingButton.setEnabled(False)
            self.downCrossingButton.setEnabled(False)
            self.switchButton.setEnabled(False)

            self.label_11.setText("")

    def selectWayside(self):
        selectedIndex = self.waysideMenu.currentIndex()  
        self.fileButton.setDisabled(False) 

        if selectedIndex == 0 and self.selectGreenLine.isChecked():
            self.currentBlocks = self.greenWayside2Blocks
            self.currentSpecialBlocks = self.specialGreenBlocksW2
            self.blockMenu.setDisabled(False)

            self.blockMenu.clear()
            self.currentSwitchBlocksNums = self.greenCrossingTriplesIDS

            for block in self.currentSpecialBlocks:
                self.blockMenu.addItems([block.ID])

            self.FileParser = Parser(None,self.greenCrossingTriplesIDS,self.greenWayside2Blocks)
            self.sendAllBlocks.emit(self.greenWayside2Blocks)
            

        if selectedIndex == 0 and self.selectRedLine.isChecked():
            self.currentBlocks = self.allRedBlocks
            self.currentSpecialBlocks = self.specialRedBlocksW1
            self.blockMenu.setDisabled(False)

            self.blockMenu.clear()

            for block in self.currentSpecialBlocks:
                self.blockMenu.addItems([block.ID])

            self.currentSwitchBlocksNums = self.redCrossingTriplesIDS

            if self.FileParser.inputPLC is None: self.FileParser = Parser(None,self.redCrossingTriplesIDS,self.allRedBlocks)
            self.sendAllBlocks.emit(self.allRedBlocks)

        if selectedIndex == 1 and self.selectRedLine.isChecked():
            self.currentBlocks = self.allRedBlocks
            self.currentSpecialBlocks = self.specialRedBlocksW2
            self.blockMenu.setDisabled(False)

            self.blockMenu.clear()

            for block in self.currentSpecialBlocks:
                self.blockMenu.addItems([block.ID])

            self.currentSwitchBlocksNums = self.redCrossingTriplesIDS

            if self.FileParser.inputPLC is None: self.FileParser = Parser(None,self.redCrossingTriplesIDS,self.allRedBlocks)
            self.sendAllBlocks.emit(self.allRedBlocks)

    def blockActions(self):
        selectedIndex = self.blockMenu.currentIndex()
        if self.currentBlocks is None or self.currentSpecialBlocks is None : return
        selectedBlock = self.currentSpecialBlocks[selectedIndex]

        if selectedBlock.LIGHT and self.label_7.text() and not selectedBlock.SWITCH:
            self.greenButton.setEnabled(not selectedBlock.lightState and self.label_7.text() == "MANUAL")
            self.redButton.setEnabled(selectedBlock.lightState and self.label_7.text() == "MANUAL")
            self.upCrossingButton.setEnabled(False)
            self.downCrossingButton.setEnabled(False)
            self.switchButton.setEnabled(False)

            self.upCrossingButton.setStyleSheet("")
            self.downCrossingButton.setStyleSheet("")
            self.label_11.setText("")
            
            if selectedBlock.lightState:
                self.greenButton.setStyleSheet('QPushButton {background-color: green; color: yellow;}')
                self.redButton.setStyleSheet("")
            elif not selectedBlock.lightState:
                self.greenButton.setStyleSheet("")
                self.redButton.setStyleSheet('QPushButton {background-color: red; color: yellow;}')

        elif selectedBlock.CROSSING and (self.selectGreenLine.isChecked() or self.selectRedLine.isChecked()):
            self.greenButton.setEnabled(False)
            self.redButton.setEnabled(False)
            self.upCrossingButton.setEnabled(not selectedBlock.crossingState and self.label_7.text() == "MANUAL")
            self.downCrossingButton.setEnabled(selectedBlock.crossingState and self.label_7.text() == "MANUAL")
            self.switchButton.setEnabled(False)

            self.greenButton.setStyleSheet("")
            self.redButton.setStyleSheet("")
            self.label_11.setText("")

            if selectedBlock.crossingState:
                self.upCrossingButton.setStyleSheet("background-color: yellow")
                self.downCrossingButton.setStyleSheet("")
            elif not selectedBlock.crossingState:
                self.upCrossingButton.setStyleSheet("")
                self.downCrossingButton.setStyleSheet("background-color: yellow")

        elif selectedBlock.SWITCH:
            self.greenButton.setEnabled(False or selectedBlock.LIGHT and selectedBlock.lightState)
            self.redButton.setEnabled(False or selectedBlock.LIGHT and not selectedBlock.lightState)
            self.upCrossingButton.setEnabled(False)
            self.downCrossingButton.setEnabled(False)
            self.switchButton.setEnabled(True and self.label_7.text() == "MANUAL")

            self.currentTriple = None

            for triple in self.currentSwitchBlocksNums:
                if triple[0] == selectedBlock.blockNum: 
                    self.currentTriple = triple
                    break

            if selectedBlock.switchState:

                for block in self.currentBlocks:
                    if block.blockNum == triple[1]:
                        letter = block.blockSection
                        break

                self.label_11.setText(letter + self.currentTriple[1])

            else:

                for block in self.currentBlocks:
                    if block.blockNum == triple[2]:
                        letter = block.blockSection
                        break

                self.label_11.setText(letter + self.currentTriple[2])

            if not selectedBlock.LIGHT:
                self.greenButton.setStyleSheet("")
                self.redButton.setStyleSheet("")
            else:
                self.greenButton.setEnabled(not selectedBlock.lightState and self.label_7.text() == "MANUAL")
                self.redButton.setEnabled(selectedBlock.lightState and self.label_7.text() == "MANUAL")

                if selectedBlock.lightState:
                    self.greenButton.setStyleSheet('QPushButton {background-color: green; color: yellow;}')
                    self.redButton.setStyleSheet("")
                elif not selectedBlock.lightState:
                    self.greenButton.setStyleSheet("")
                    self.redButton.setStyleSheet('QPushButton {background-color: red; color: yellow;}')
            self.upCrossingButton.setStyleSheet("")

            self.downCrossingButton.setStyleSheet("")

    def greenButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.currentSpecialBlocks[selectedIndex].lightState = True
        self.greenButton.setEnabled(False)
        self.redButton.setEnabled(True)
        self.greenButton.setStyleSheet('QPushButton {background-color: green; color: yellow;}')
        self.redButton.setStyleSheet("")
        self.sendSpecialBlocks.emit(self.currentBlocks)
        self.sendAllBlocks.emit(self.currentBlocks)
        

    def redButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.currentSpecialBlocks[selectedIndex].lightState = False
        self.greenButton.setEnabled(True)
        self.redButton.setEnabled(False)
        self.greenButton.setStyleSheet("")
        self.redButton.setStyleSheet('QPushButton {background-color: red; color: yellow;}')
        self.sendSpecialBlocks.emit(self.currentBlocks)
        self.sendAllBlocks.emit(self.currentBlocks)

    def upButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.currentSpecialBlocks[selectedIndex].crossingState = True
        self.upCrossingButton.setEnabled(False)
        self.downCrossingButton.setEnabled(True)
        self.upCrossingButton.setStyleSheet("background-color: yellow")
        self.downCrossingButton.setStyleSheet("")
        self.sendSpecialBlocks.emit(self.currentBlocks)
        self.sendAllBlocks.emit(self.currentBlocks)

    def downButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.currentSpecialBlocks[selectedIndex].crossingState = False
        self.upCrossingButton.setEnabled(True)
        self.downCrossingButton.setEnabled(False)
        self.upCrossingButton.setStyleSheet("")
        self.downCrossingButton.setStyleSheet("background-color: yellow")
        self.sendSpecialBlocks.emit(self.currentBlocks)
        self.sendAllBlocks.emit(self.currentBlocks)

    def switchButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.currentSpecialBlocks[selectedIndex].switchState = not self.currentSpecialBlocks[selectedIndex].switchState

        for block in self.currentBlocks:
            if block.blockNum == self.currentTriple[1]:
                letter1 = block.blockSection
            if block.blockNum == self.currentTriple[2]:
                letter2 = block.blockSection        

        current_text = self.label_11.text()
        if current_text[1:] == self.currentTriple[1]:
            self.label_11.setText(letter2 + self.currentTriple[2])
        elif current_text[1:] == self.currentTriple[2]:
            self.label_11.setText(letter1 + self.currentTriple[1])
        self.sendSpecialBlocks.emit(self.currentBlocks)
        self.sendAllBlocks.emit(self.currentBlocks)

        self.sendGreenSwitchPos.emit(self.greenWayside2Blocks)
        self.sendRedSwitchPos.emit(self.allRedBlocks)

    def updateBlocks(self,new_data):

        self.previousOccupiedBlock = self.occupiedBlocks

        sentBlocks = new_data
        for block in self.occupiedBlocks:
            if not block.maintenance:
                self.occupiedBlocks.remove(block)

        for block in self.currentBlocks: 
            if not block.maintenance:
                block.occupied = False

        for block_id in sentBlocks:
            for block in self.currentBlocks:
                if block_id == block.ID:
                    block.occupied = True
                    self.occupiedBlocks.append(block)

        names = []
        
        flag = False

        for block in self.occupiedBlocks:
            if block.maintenance:
                flag = True
                break

        names = [x.ID for x in self.occupiedBlocks]
        if flag: self.BlockOcc.setText(" ".join(names))
        else: self.BlockOcc.setText(" ".join(sentBlocks))


        #ADD CODE HERE FOR MAITANCE
        if self.label_7.text() == "AUTOMATIC" :

            #Validate user has uploaded a PLC file
            if self.FileParser.inputPLC is None:
                error_msg = QMessageBox()
                error_msg.setWindowTitle("Upload Error")
                error_msg.setText("Please Upload a PLC file in Wayside SW")
                error_msg.setIcon(QMessageBox.Critical)

                error_msg.exec_() 
                return

            self.FileParser.parsePLC()  #Update special blocks when automatic mode is set
            check1 = self.currentBlocks.copy #blocks after parsed
            self.FileParser.parsePLC()
            check2 = self.currentBlocks.copy

            if check1 != check2:
                for block in self.currentBlocks: block.authority = False
                print("Redundancy Check Failed")
                return
            
        
        #FIX HERE FIX HERE
            
        self.handleCollisions()
            
        for block in self.currentBlocks:
            self.handleLights(block)
  
        self.blockActions()
        self.sendSpecialBlocks.emit(self.currentBlocks)
        self.sendOccupiedBlocks.emit(self.occupiedBlocks)
        self.sendAllBlocks.emit(self.currentBlocks)

    def receiveSpeedAuth(self,initialTrainSpeedAuthority):
        self.sendTrainSpeedAuth.emit(initialTrainSpeedAuthority)

    def blockClosures(self,closedBlocks):

        #self.previousOccupiedBlock = self.occupiedBlocks

        for block in closedBlocks:
            if block.lineColor == "Green" and block.Wayside == "W2":
                if block.maintenance:
                    block.occupied = True
                    block.maintenance = True
                    self.allGreenBlocks[int(block.blockNum) - 1].occupied = True
                    self.occupiedBlocks.append(block)

                    index = 0

                    for i in range(len(self.currentBlocks)):
                        if block.ID == self.currentBlocks[i].ID:
                            index = i
                            break

                    self.currentBlocks[i] = block


                elif not block.maintenance:
                    block.occupied = False
                    block.maintenance = False
                    self.allGreenBlocks[int(block.blockNum) - 1].occupied = False
                    self.occupiedBlocks.remove(block)

                    index = 0

                    for i in range(len(self.currentBlocks)):
                        if block.ID == self.currentBlocks[i].ID:
                            index = i
                            break

                    self.currentBlocks[i] = block


            elif block.lineColor == "Red":
                if block.maintenance:
                    block.occupied = True
                    block.maintenance = True
                    self.allRedBlocks[int(block.blockNum) - 1].occupied = True
                    self.occupiedBlocks.append(block)

                    index = 0

                    for i in range(len(self.currentBlocks)):
                        if block.ID == self.currentBlocks[i].ID:
                            index = i
                            break

                    self.currentBlocks[i] = block
                elif not block.maintenance:
                    block.occupied = False
                    block.maintenance = False
                    self.allRedBlocks[int(block.blockNum) - 1].occupied = False
                    self.occupiedBlocks.remove(block)

                    index = 0

                    for i in range(len(self.currentBlocks)):
                        if block.ID == self.currentBlocks[i].ID:
                            index = i
                            break

                    self.currentBlocks[i] = block


        flag = False

        for block in self.occupiedBlocks:
            if block.maintenance:
                flag = True
                break

        names = [x.ID for x in self.occupiedBlocks]
        if flag: self.BlockOcc.setText(" ".join(names))
      
        self.handleCollisions()
        self.sendOccupiedBlocks.emit(self.occupiedBlocks)
        self.sendAllBlocks.emit(self.currentBlocks)

    def handleLights(self, block):
        if block.ID == "M76" and block.lineColor == "Green":
            if block.lightState:
                self.allGreenBlocks[75].authority = True
                self.allGreenBlocks[74].authority = True
                self.allGreenBlocks[73].authority = True

            else:
                self.allGreenBlocks[75].authority = False
                self.allGreenBlocks[74].authority = False
                self.allGreenBlocks[73].authority = False

        if block.ID == "E15" and block.lineColor == "Red":
            if block.lightState:
                self.allRedBlocks[14].authority = True
                self.allRedBlocks[13].authority = True

            else:
                self.allRedBlocks[14].authority = False 
                self.allRedBlocks[13].authority = False 

    def handleCollisions(self):
        if self.currentBlocks[0].lineColor == "Green":
            oneDirectionOne = ['K', 'L', 'M','O','P','Q','R','S','I'] #Block sections where collisions could occur
            oneDirectionTwo = [] 
            biDirection = ['N']

            lights = [x.ID for x in self.currentBlocks if x.LIGHT]
          
            tempSkip = []
            for index, block in enumerate(self.currentBlocks):
                if block.blockSection in oneDirectionOne:
                    if block.occupied == True:
                        self.currentBlocks[index-1].authority = False
                        self.currentBlocks[index-2].authority = False
                        tempSkip.append(self.currentBlocks[index-1])
                        tempSkip.append(self.currentBlocks[index-2])
                    elif block.occupied == False and block.ID not in lights:
                        if block not in tempSkip:
                            block.authority = True
                        if self.currentBlocks[index-1] not in tempSkip:
                            self.currentBlocks[index-1].authority = True
                        if self.currentBlocks[index-2] not in tempSkip:
                            self.currentBlocks[index-2].authority = True
                if block.blockSection in oneDirectionTwo:
                    if block.occupied == True:
                        self.currentBlocks[index+1].authority = False
                        self.currentBlocks[index+2].authority = False
                        tempSkip.append(self.currentBlocks[index+1])
                        tempSkip.append(self.currentBlocks[index+2])
                    elif block.occupied == False and block.ID not in lights:
                        if block not in tempSkip:
                            block.authority = True
                        if self.currentBlocks[index+1] not in tempSkip:
                            self.currentBlocks[index+1].authority = True
                        if self.currentBlocks[index+2] not in tempSkip:
                            self.currentBlocks[index+2].authority = True
                if block.blockSection in biDirection:
                    if block.ID == 'D13' or block.ID == 'F22':
                        continue
                    if self.currentBlocks[index-1] in self.previousOccupiedBlock:
                        if block.occupied == True:
                            self.currentBlocks[index-1].authority = False
                            self.currentBlocks[index-2].authority = False
                            tempSkip.append(self.currentBlocks[index-1])
                            tempSkip.append(self.currentBlocks[index-2])
                        elif block.occupied == False and block.ID not in lights:
                            if block not in tempSkip:
                                block.authority = True
                            if self.currentBlocks[index-1] not in tempSkip:
                                self.currentBlocks[index-1].authority = True
                            if self.currentBlocks[index-2] not in tempSkip:
                                self.currentBlocks[index-2].authority = True
                    elif self.currentBlocks[index+1] in self.previousOccupiedBlock:
                        if block.occupied == True:
                            self.currentBlocks[index+1].authority = False
                            self.currentBlocks[index+2].authority = False
                            tempSkip.append(self.currentBlocks[index+1])
                            tempSkip.append(self.currentBlocks[index+2])
                        elif block.occupied == False and block.ID not in lights:
                            if block not in tempSkip:
                                block.authority = True
                            if self.currentBlocks[index+1] not in tempSkip:
                                self.currentBlocks[index+1].authority = True
                            if self.currentBlocks[index+2] not in tempSkip:
                                self.currentBlocks[index+2].authority = True
                    #The following condition indicates a track failure, since an occupancy is randomly generated...
                    #Close blocks on either side as response:
                    elif self.currentBlocks[index-1] not in self.previousOccupiedBlock and self.currentBlocks[index+1] not in self.previousOccupiedBlock:
                        if block.occupied == True:
                            self.currentBlocks[index+1].authority = False
                            self.currentBlocks[index+2].authority = False
                            tempSkip.append(self.currentBlocks[index+1])
                            tempSkip.append(self.currentBlocks[index+2])
                            self.currentBlocks[index-1].authority = False
                            self.currentBlocks[index-2].authority = False
                            tempSkip.append(self.currentBlocks[index-1])
                            tempSkip.append(self.currentBlocks[index-2])
                        elif block.occupied == False and block.ID not in lights:
                            if block not in tempSkip:
                                block.authority = True
                            if self.currentBlocks[index+1] not in tempSkip:
                                self.currentBlocks[index+1].authority = True
                            if self.currentBlocks[index+2] not in tempSkip:
                                self.currentBlocks[index+2].authority = True
                            if self.currentBlocks[index-1] not in tempSkip:
                                self.currentBlocks[index-1].authority = True
                            if self.currentBlocks[index-2] not in tempSkip:
                                self.currentBlocks[index-2].authority = True
                        
            
        elif self.currentBlocks[0].lineColor == "Red":
            oneDirectionOne = ['A','B','C','D','E','J','K','L','M','N'] #Block sections where collisions could occur
            oneDirectionTwo = [] 
            biDirection = ['G','F','H','I']

            lights = [x.ID for x in self.currentBlocks if x.LIGHT]
          
            tempSkip = []
            for index, block in enumerate(self.currentBlocks):
                if block.blockSection in oneDirectionOne:
                    if block.occupied == True:
                        self.currentBlocks[index-1].authority = False
                        self.currentBlocks[index-2].authority = False
                        tempSkip.append(self.currentBlocks[index-1])
                        tempSkip.append(self.currentBlocks[index-2])
                    elif block.occupied == False and block.ID not in lights:
                        if block not in tempSkip:
                            block.authority = True
                        if self.currentBlocks[index-1] not in tempSkip:
                            self.currentBlocks[index-1].authority = True
                        if self.currentBlocks[index-2] not in tempSkip:
                            self.currentBlocks[index-2].authority = True
                if block.blockSection in oneDirectionTwo:
                    if block.occupied == True:
                        self.currentBlocks[index+1].authority = False
                        self.currentBlocks[index+2].authority = False
                        tempSkip.append(self.currentBlocks[index+1])
                        tempSkip.append(self.currentBlocks[index+2])
                    elif block.occupied == False and block.ID not in lights:
                        if block not in tempSkip:
                            block.authority = True
                        if self.currentBlocks[index+1] not in tempSkip:
                            self.currentBlocks[index+1].authority = True
                        if self.currentBlocks[index+2] not in tempSkip:
                            self.currentBlocks[index+2].authority = True
                if block.blockSection in biDirection:
                    if block.ID == 'D13' or block.ID == 'F22':
                        continue
                    if self.currentBlocks[index-1] in self.previousOccupiedBlock:
                        if block.occupied == True:
                            self.currentBlocks[index-1].authority = False
                            self.currentBlocks[index-2].authority = False
                            tempSkip.append(self.currentBlocks[index-1])
                            tempSkip.append(self.currentBlocks[index-2])
                        elif block.occupied == False and block.ID not in lights:
                            if block not in tempSkip:
                                block.authority = True
                            if self.currentBlocks[index-1] not in tempSkip:
                                self.currentBlocks[index-1].authority = True
                            if self.currentBlocks[index-2] not in tempSkip:
                                self.currentBlocks[index-2].authority = True
                    elif self.currentBlocks[index+1] in self.previousOccupiedBlock:
                        if block.occupied == True:
                            self.currentBlocks[index+1].authority = False
                            self.currentBlocks[index+2].authority = False
                            tempSkip.append(self.currentBlocks[index+1])
                            tempSkip.append(self.currentBlocks[index+2])
                        elif block.occupied == False and block.ID not in lights:
                            if block not in tempSkip:
                                block.authority = True
                            if self.currentBlocks[index+1] not in tempSkip:
                                self.currentBlocks[index+1].authority = True
                            if self.currentBlocks[index+2] not in tempSkip:
                                self.currentBlocks[index+2].authority = True
                    #The following condition indicates a track failure, since an occupancy is randomly generated...
                    #Close blocks on either side as response:
                    elif self.currentBlocks[index-1] not in self.previousOccupiedBlock and self.currentBlocks[index+1] not in self.previousOccupiedBlock:
                        if block.occupied == True:
                            self.currentBlocks[index+1].authority = False
                            self.currentBlocks[index+2].authority = False
                            tempSkip.append(self.currentBlocks[index+1])
                            tempSkip.append(self.currentBlocks[index+2])
                            self.currentBlocks[index-1].authority = False
                            self.currentBlocks[index-2].authority = False
                            tempSkip.append(self.currentBlocks[index-1])
                            tempSkip.append(self.currentBlocks[index-2])
                        elif block.occupied == False and block.ID not in lights:
                            if block not in tempSkip:
                                block.authority = True
                            if self.currentBlocks[index+1] not in tempSkip:
                                self.currentBlocks[index+1].authority = True
                            if self.currentBlocks[index+2] not in tempSkip:
                                self.currentBlocks[index+2].authority = True
                            if self.currentBlocks[index-1] not in tempSkip:
                                self.currentBlocks[index-1].authority = True
                            if self.currentBlocks[index-2] not in tempSkip:
                                self.currentBlocks[index-2].authority = True


class TestBench(QMainWindow):

    #signals
    OccBlocksChanged = pyqtSignal(list) #Sending block occupancies to UI
    tbChangeMode = pyqtSignal() #Fliping mode
    ctcSpeed = pyqtSignal(Block) #sending updated block with speed
    ctcAuthority = pyqtSignal(Block) #sending updated block with authority
    ctcIDSpeedAuthority = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        uic.loadUi("Wayside_SW/Wayside_Testbench.ui", self)

        # Buttons
        #self.speedInput.returnPressed.connect(self.sendSpeed)
        #self.authorityInput.returnPressed.connect(self.sendAuthority)
        self.modeInput.clicked.connect(self.sendMode)
        self.addBlock.returnPressed.connect(self.addBlockOcc)
        self.removeBlock.returnPressed.connect(self.remBlockOcc)
        self.tbBlockMenu.currentIndexChanged.connect(self.updateBlockStates)
        self.lineEdit.returnPressed.connect(self.receiveInitialIDSpeedAuth)

        #Backend vars
        self.OccupiedBlocks = []    #Is sent to the UI
        self.specialBlocks = []     #Is sent from the UI

        #blocks per wayside
        self.greenW2Blocks = []
        self.redW1Blocks = []
        self.redW2Blocks = []

        #train id, speed, authority to send
        self.idSpeedAuthority = []
 
    def sendSpeed(self):
        speed = self.speedInput.text()
        self.comSpeed.setText(speed)
        index = self.tbBlockMenu.currentIndex()
        selectedBlock = self.specialBlocks[index]
        selectedBlock.speedLimit = speed
        self.ctcSpeed.emit(selectedBlock)

    def sendAuthority(self):
        authority = self.authorityInput.text()
        self.authOut.setText(authority)
        index = self.tbBlockMenu.currentIndex()
        selectedBlock = self.specialBlocks[index]
        selectedBlock.authority = authority
        self.ctcAuthority.emit(selectedBlock)

    def sendMode(self):
        current_text = self.label_16.text()
        if current_text == "MANUAL":
            self.label_16.setText("AUTOMATIC")
        elif current_text == "AUTOMATIC":
            self.label_16.setText("MANUAL")

        self.tbChangeMode.emit()

    def addBlockOcc(self):
        current_text = self.addBlock.text()
        self.OccupiedBlocks.append(current_text)
        self.OccupiedBlocks = sorted(self.OccupiedBlocks, key=sort_by_number)
        self.label_18.setText(" ".join(self.OccupiedBlocks))
        self.OccBlocksChanged.emit(self.OccupiedBlocks)

    
    def remBlockOcc(self):
        current_text = self.removeBlock.text()
        self.OccupiedBlocks.remove(current_text)
        self.OccupiedBlocks = sorted(self.OccupiedBlocks, key=sort_by_number)
        self.label_18.setText(" ".join(self.OccupiedBlocks))
        self.OccBlocksChanged.emit(self.OccupiedBlocks)

    def updateBlockStates(self, arr):

        if not hasattr(self, 'specialBlocks'): return   #specialBlock check for initialization

        if isinstance(arr, list):
            self.greenW2Blocks = arr
            index = self.tbBlockMenu.currentIndex()
            selectedBlock = self.greenW2Blocks[index]
            

        else:  
            if arr > len(self.greenW2Blocks) - 1 or arr == -1: return 
            selectedBlock = self.greenW2Blocks[arr]
            
        #self.comSpeed.setText(str(selectedBlock.speedLimit))
        #self.authOut.setText(str(selectedBlock.authority))
        self.label_4.setText(str(selectedBlock.authority))

        if selectedBlock.LIGHT:

            self.label_24.setText("")

            if selectedBlock.lightState:
                self.label_19.setText("Green")
                self.label_22.setText("")
            else:
                self.label_19.setText("Red")
                self.label_22.setText("")
        elif selectedBlock.CROSSING:
            
            self.label_24.setText("")

            if selectedBlock.crossingState:
                self.label_19.setText("")
                self.label_22.setText("Up")
            else:
                self.label_19.setText("")
                self.label_22.setText("Down")
        elif selectedBlock.SWITCH:
            if selectedBlock.switchState:
                self.label_19.setText("")
                self.label_22.setText("")
                self.label_24.setText("LEFT")
            else:
                self.label_19.setText("")
                self.label_22.setText("")
                self.label_24.setText("RIGHT")

    def receiveMode(self,mode):
        if mode == True:
            self.label_16.setText("MANUAL")
        else:
            self.label_16.setText("AUTOMATIC")

    def receiveBlocks(self,blocks):
        self.tbBlockMenu.clear()
        if blocks[0].Wayside == "W2" and blocks[0].lineColor == "Green":
            self.greenW2Blocks = blocks
            for block in self.greenW2Blocks: self.tbBlockMenu.addItems([block.ID])
        elif blocks[0].Wayside == "W1" and blocks[0].lineColor == "Red":
            self.redW1Blocks = blocks
            for block in self.redW1Blocks: self.tbBlockMenu.addItems([block.ID])
        elif blocks[0].Wayside == "W2" and blocks[0].lineColor == "Red":
            self.redW2Blocks = blocks
            for block in self.redW2Blocks: self.tbBlockMenu.addItems([block.ID])

    def receiveInitialIDSpeedAuth(self):
        text = self.lineEdit.text()
        splits = text.split(", ")
        self.comSpeed.setText(splits[1])
        self.authOut.setText(splits[2])
        self.ctcIDSpeedAuthority.emit(splits)

    def displaySpeedAuth(self, data):
        self.comSpeed.setText(str(data[1]))
        self.authOut.setText(str(data[2]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WaysideSW()
    window2 = TestBench()

    #Signal: Window
    window.sendSpecialBlocks.connect(window2.updateBlockStates)
    window.changeModeSend.connect(window2.receiveMode)
    window.sendAllBlocks.connect(window2.receiveBlocks)
    window.sendTrainSpeedAuth.connect(window2.displaySpeedAuth)

    #Signal: Window 2
    window2.OccBlocksChanged.connect(window.updateBlocks)
    window2.tbChangeMode.connect(window.changeMode)
    window2.ctcIDSpeedAuthority.connect(window.receiveSpeedAuth)

    window.show()
    window2.show()
    sys.exit(app.exec_())
