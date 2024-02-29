import sys
import os
import re

# Using Block Class as a seperate file
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from Track_Resources.Block import Block
from PLC_Files.Parser import Parser
from PyQt5.QtCore import QTimer,pyqtSignal
import csv

def sort_by_number(block):
    return int(block[1:])  # Convert the string to an integer, excluding the 'B' prefix

#Function that reads all blocks from a *.csv file and assigns block attributes:
def readTrackFile(fileName):
    totalBlocks = []
    lightBlocks = {}
    fileName = "Wayside SW/" + fileName
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

                elif(line[6][0:6] == "SWITCH"):
                    hasSwitchTemp = True
                    switchState = True

                    #numbers = [part for part in line[6].split('-') if part.isdigit()]
                    numbers = re.findall(r'\b(\d+)-(\d+)\b', line[6])
                    lightBlocks.update({num: False for pair in numbers for num in pair})

            tempBlock = Block(hasLightTemp,hasCrossingTemp,hasSwitchTemp,lightState,crossingState,switchState,False,blockId, line[5],None)
            totalBlocks.append(tempBlock)

            #Assign light values now

        for block in totalBlocks:
            if block.ID[1:] in lightBlocks:
                block.LIGHT = True
                block.lightState = False

    
    return totalBlocks #Return a list of all blocks within the file

class MyApp(QMainWindow):

    #Signals
    sendSpecialBlocks = pyqtSignal(list)    #Send special blocks to testbench
    changeModeSend = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        uic.loadUi("Wayside SW/Wayside_UI_Rough.ui",self)

        # Global constants for LIGHT, CROSSING, and SWITCH
        LIGHT_CONST = [True, False, False, False,None,None,False]
        CROSSING_CONST = [False, True, False, None,True,None,False]
        SWITCH_LIGHT_CONST = [True, False, True, False,None,True,False]
        NORMAL_CONST = [False, False, False, None,None,None,False]

        #Switch Directions
        self.B5_Switch_Positions = ["B6","C11"]

        #Defining blue line blocks
        A1 = Block(*NORMAL_CONST,"A1",50,None)
        A2 = Block(*NORMAL_CONST,"A2",50,None)
        A3 = Block(*CROSSING_CONST,"A3",50,None)
        A4 = Block(*NORMAL_CONST,"A4",50,None) 
        A5 = Block(*SWITCH_LIGHT_CONST,"A5",50,None) 
        B6 = Block(*LIGHT_CONST,"B6",50,None)
        B7 = Block(*NORMAL_CONST,"B7",50,None)
        B8 = Block(*NORMAL_CONST,"B8",50,None)
        B9 = Block(*NORMAL_CONST,"B9",50,None)
        B10 = Block(*NORMAL_CONST,"B10",50,None)
        C11 = Block(*LIGHT_CONST,"C11",50,None)
        C12 = Block(*NORMAL_CONST,"C12",50,None)
        C13 = Block(*NORMAL_CONST,"C13",50,None)
        C14 = Block(*NORMAL_CONST,"C14",50,None)
        C15 = Block(*NORMAL_CONST,"C15",50,None)

        #Defines an array of these blocks

        self.BlockArray = [A3,A5,B6,C11]    #Special Blocks
        self.AllBlocks = [A1,A2,A3,A4,A5,B6,B7,B8,B9,B10,C11,C12,C13,C14,C15] #All Blocks
        self.SwitchBlocks = ["B5","B6","C11"]

        #Defines Red line blocks
        self.allRedBlocks = readTrackFile("Red_Line.csv")
        self.specialRedBlocks = []

        for block in self.allRedBlocks:
            if block.state == True: self.specialRedBlocks.append(block)

        #Create Parser Object
        self.FileParser = Parser(None,self.AllBlocks)  #Currently empty onject

        # Buttons
        self.fileButton.clicked.connect(self.on_file_button_clicked)
        self.modeButton.clicked.connect(self.changeMode)
        self.selectLine.stateChanged.connect(self.checkLine)
        self.blockMenu.currentIndexChanged.connect(self.blockActions)
        self.greenButton.clicked.connect(self.greenButtonPushed)
        self.redButton.clicked.connect(self.redButtonPushed)
        self.upCrossingButton.clicked.connect(self.upButtonPushed)
        self.downCrossingButton.clicked.connect(self.downButtonPushed)
        self.switchButton.clicked.connect(self.switchButtonPushed)
        self.saveButton.clicked.connect(self.onSavePLCFile)

        #initial signals
        self.sendSpecialBlocks.emit(self.BlockArray)
        self.changeModeSend.emit(True)

        #Original Map Image
        pixmap = QPixmap('Blue Line Images\BlueLine.png')
        self.label_17.setPixmap(pixmap)

        #Dropdown menu
        self.blockMenu.addItems(['A3','A5','B6','C11'])
        self.waysideMenu.addItems(['W1'])

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

        # Timer for updating block occupancy every 5 seconds
        #self.timer = QTimer(self)
        #self.timer.timeout.connect(self.updateBlockOccupancy)
        #self.timer.start(5000)  # 5000 milliseconds (5 seconds)
        
    
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
            self.blockActions()
            self.sendSpecialBlocks.emit(self.BlockArray)
            self.changeModeSend.emit(False)

        elif current_text == "AUTOMATIC":
            self.label_7.setText("MANUAL")
            self.blockActions()
            self.sendSpecialBlocks.emit(self.BlockArray)
            self.changeModeSend.emit(True)
            

    def checkLine(self):
        checkStatus = self.selectLine.isChecked()
        if checkStatus:
            self.waysideMenu.setEnabled(True)
            self.blockMenu.setEnabled(True)
            self.modeButton.setEnabled(self.FileParser.inputPLC != None) #Can't Change to automatic until PLC is inserted
            self.blockActions()
        else:
            self.waysideMenu.setEnabled(False)
            self.blockMenu.setEnabled(False)
            self.modeButton.setEnabled(False)

        self.sendSpecialBlocks.emit(self.BlockArray)

    def blockActions(self):
        selectedIndex = self.blockMenu.currentIndex()
        selectedBlock = self.BlockArray[selectedIndex]

        if selectedBlock.LIGHT and self.label_7.text():
            self.greenButton.setEnabled(not selectedBlock.state and self.label_7.text() == "MANUAL")
            self.redButton.setEnabled(selectedBlock.state and self.label_7.text() == "MANUAL")
            self.upCrossingButton.setEnabled(False)
            self.downCrossingButton.setEnabled(False)
            self.switchButton.setEnabled(False)

            self.upCrossingButton.setStyleSheet("")
            self.downCrossingButton.setStyleSheet("")
            self.label_11.setText("")
            
            if selectedBlock.state:
                self.greenButton.setStyleSheet('QPushButton {background-color: green; color: yellow;}')
                self.redButton.setStyleSheet("")
            elif not selectedBlock.state:
                self.greenButton.setStyleSheet("")
                self.redButton.setStyleSheet('QPushButton {background-color: red; color: yellow;}')

        elif selectedBlock.CROSSING and self.selectLine.isChecked():
            self.greenButton.setEnabled(False)
            self.redButton.setEnabled(False)
            self.upCrossingButton.setEnabled(not selectedBlock.state and self.label_7.text() == "MANUAL")
            self.downCrossingButton.setEnabled(selectedBlock.state and self.label_7.text() == "MANUAL")
            self.switchButton.setEnabled(False)

            self.greenButton.setStyleSheet("")
            self.redButton.setStyleSheet("")
            self.label_11.setText("")

            if selectedBlock.state:
                self.upCrossingButton.setStyleSheet("background-color: yellow")
                self.downCrossingButton.setStyleSheet("")
            elif not selectedBlock.state:
                self.upCrossingButton.setStyleSheet("")
                self.downCrossingButton.setStyleSheet("background-color: yellow")

        elif selectedBlock.SWITCH:
            self.greenButton.setEnabled(False)
            self.redButton.setEnabled(False)
            self.upCrossingButton.setEnabled(False)
            self.downCrossingButton.setEnabled(False)
            self.switchButton.setEnabled(True and self.label_7.text() == "MANUAL")

            if selectedBlock.state == True:
                self.label_11.setText(self.SwitchBlocks[1])

            else:
                self.label_11.setText(self.SwitchBlocks[2])

            self.greenButton.setStyleSheet("")
            self.redButton.setStyleSheet("")
            self.upCrossingButton.setStyleSheet("")
            self.downCrossingButton.setStyleSheet("")

    def greenButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.BlockArray[selectedIndex].state = True
        self.greenButton.setEnabled(False)
        self.redButton.setEnabled(True)
        self.greenButton.setStyleSheet('QPushButton {background-color: green; color: yellow;}')
        self.redButton.setStyleSheet("")
        self.sendSpecialBlocks.emit(self.BlockArray)

    def redButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.BlockArray[selectedIndex].state = False
        self.greenButton.setEnabled(True)
        self.redButton.setEnabled(False)
        self.greenButton.setStyleSheet("")
        self.redButton.setStyleSheet('QPushButton {background-color: red; color: yellow;}')
        self.sendSpecialBlocks.emit(self.BlockArray)

    def upButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.BlockArray[selectedIndex].state = True
        self.upCrossingButton.setEnabled(False)
        self.downCrossingButton.setEnabled(True)
        self.upCrossingButton.setStyleSheet("background-color: yellow")
        self.downCrossingButton.setStyleSheet("")
        self.sendSpecialBlocks.emit(self.BlockArray)

    def downButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.BlockArray[selectedIndex].state = False
        self.upCrossingButton.setEnabled(True)
        self.downCrossingButton.setEnabled(False)
        self.upCrossingButton.setStyleSheet("")
        self.downCrossingButton.setStyleSheet("background-color: yellow")
        self.sendSpecialBlocks.emit(self.BlockArray)

    def switchButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.BlockArray[selectedIndex].state = not self.BlockArray[selectedIndex].state

        current_text = self.label_11.text()
        if current_text == self.B5_Switch_Positions[0]:
            self.label_11.setText(self.B5_Switch_Positions[1])
        elif current_text == self.B5_Switch_Positions[1]:
            self.label_11.setText(self.B5_Switch_Positions[0])
        self.sendSpecialBlocks.emit(self.BlockArray)

    def updateBlocks(self,new_data):
        sentBlocks = new_data

        for block in self.AllBlocks: block.occupied = False

        for block_id in sentBlocks:
            for block in self.AllBlocks:
                if block_id == block.ID:
                    block.occupied = True

        self.BlockOcc.setText(" ".join(sentBlocks))
        if self.label_7.text() == "AUTOMATIC" : self.FileParser.parsePLC()
        self.blockActions()
        self.sendSpecialBlocks.emit(self.BlockArray)
        

class TestBench(QMainWindow):

    #signals
    OccBlocksChanged = pyqtSignal(list) #Sending block occupancies to UI
    tbChangeMode = pyqtSignal() #Fliping mode

    def __init__(self):
        super().__init__()
        uic.loadUi("Wayside SW/Wayside_Testbench.ui", self)

        # Buttons
        self.speedInput.returnPressed.connect(self.sendSpeed)
        self.authorityInput.returnPressed.connect(self.sendAuthority)
        self.modeInput.clicked.connect(self.sendMode)
        self.addBlock.returnPressed.connect(self.addBlockOcc)
        self.removeBlock.returnPressed.connect(self.remBlockOcc)
        self.tbBlockMenu.currentIndexChanged.connect(self.updateBlockStates)

        #Menu
        self.tbBlockMenu.addItems(['A3','A5','B6','C11'])

        #Backend vars
        self.OccupiedBlocks = []    #Is sent to the UI
        self.specialBlocks = []     #Is sent from the UI

    def sendSpeed(self):
        speed = self.speedInput.text()
        self.comSpeed.setText(speed)

    def sendAuthority(self):
        authority = self.authorityInput.text()
        self.authOut.setText(authority)

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
            self.specialBlocks = arr
            index = self.tbBlockMenu.currentIndex()
            selectedBlock = self.specialBlocks[index]

        else:  
            if arr > len(self.specialBlocks) - 1: return 
            selectedBlock = self.specialBlocks[arr]
            
        if selectedBlock.LIGHT:

            self.label_24.setText("")

            if selectedBlock.state:
                self.label_19.setText("Green")
                self.label_22.setText("")
            else:
                self.label_19.setText("Red")
                self.label_22.setText("")
        elif selectedBlock.CROSSING:
            
            self.label_24.setText("")

            if selectedBlock.state:
                self.label_19.setText("")
                self.label_22.setText("Up")
            else:
                self.label_19.setText("")
                self.label_22.setText("Down")
        elif selectedBlock.SWITCH:
            if selectedBlock.state:
                self.label_19.setText("")
                self.label_22.setText("")
                self.label_24.setText("B6")
            else:
                self.label_19.setText("")
                self.label_22.setText("")
                self.label_24.setText("C11")

    def receiveMode(self,mode):
        if mode == True:
            self.label_16.setText("MANUAL")
        else:
            self.label_16.setText("AUTOMATIC")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window2 = TestBench()

    #Signal: Window
    window.sendSpecialBlocks.connect(window2.updateBlockStates)
    window.changeModeSend.connect(window2.receiveMode)

    #Signal: Window 2
    window2.OccBlocksChanged.connect(window.updateBlocks)
    window2.tbChangeMode.connect(window.changeMode)

    window.show()
    window2.show()
    sys.exit(app.exec_())
