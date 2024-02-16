import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from Block import Block
from PyQt5.QtCore import QTimer,pyqtSignal

def sort_by_number(block):
    return int(block[1:])  # Convert the string to an integer, excluding the 'B' prefix

class MyApp(QMainWindow):

    #Signals
    sendSpecialBlocks = pyqtSignal(list)    #Send special blocks to testbench

    def __init__(self):
        super().__init__()
        uic.loadUi("Wayside SW/Wayside_UI_Rough.ui",self)

        # Global constants for LIGHT, CROSSING, and SWITCH
        LIGHT_CONST = [True, False, False, False,False]
        CROSSING_CONST = [False, True, False, True,False]
        SWITCH_CONST = [False, False, True, True,False]
        NORMAL_CONST = [False, False, False, False, False]

        #Index [0] of each Block => True if Light
        #Index [1] of each Block => True if Crossing
        #Index [2] of each Block => True if Switch
        #Index [3] of each Block => Default
        #Index [4] of each Block => True if Occupied

        #Switch Directions
        self.B5_Switch_Positions = ["B6","B11"]

        #Defining important blocks
        B1 = Block(*NORMAL_CONST,"B1")
        B2 = Block(*NORMAL_CONST,"B2")
        B3 = Block(*CROSSING_CONST,"B3")
        B4 = Block(*NORMAL_CONST,"B4") 
        B5 = Block(*SWITCH_CONST,"B5") 
        B6 = Block(*LIGHT_CONST,"B6")
        B7 = Block(*NORMAL_CONST,"B7")
        B8 = Block(*NORMAL_CONST,"B8")
        B9 = Block(*NORMAL_CONST,"B9")
        B10 = Block(*NORMAL_CONST,"B10")
        B11 = Block(*LIGHT_CONST,"B11")
        B12 = Block(*LIGHT_CONST,"B12")
        B13 = Block(*LIGHT_CONST,"B13")
        B14 = Block(*LIGHT_CONST,"B14")
        B15 = Block(*LIGHT_CONST,"B15")

        #Defines an array of these blocks

        self.BlockArray = [B3,B5,B6,B11]    #Special Blocks
        self.AllBlocks = [B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,B14,B15] #All Blocks

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

        #initial signals
        self.sendSpecialBlocks.emit(self.BlockArray)

        #Original Map Image
        pixmap = QPixmap('Blue Line Images\BlueLine.png')
        self.label_17.setPixmap(pixmap)

        #Dropdown menu
        self.blockMenu.addItems(['B3','B5','B6','B11'])
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

        # Timer for updating block occupancy every 5 seconds
        #self.timer = QTimer(self)
        #self.timer.timeout.connect(self.updateBlockOccupancy)
        #self.timer.start(5000)  # 5000 milliseconds (5 seconds)
        
    
    def on_file_button_clicked(self):
        # Open a file dialog to select a PLC file
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select PLC File", "", "PLC Files (*.plc);;All Files (*)")

        if file_path:
            # Implement your logic with the selected file path
            print(f"Selected PLC File: {file_path}")

    def changeMode(self):
        current_text = self.label_7.text()
        if current_text == "MANUAL":
            self.label_7.setText("AUTOMATIC")
        elif current_text == "AUTOMATIC":
            self.label_7.setText("MANUAL")

    def checkLine(self):
        checkStatus = self.selectLine.isChecked()
        if checkStatus:
            self.waysideMenu.setEnabled(True)
            self.blockMenu.setEnabled(True)
            self.modeButton.setEnabled(True)
        else:
            self.waysideMenu.setEnabled(False)
            self.blockMenu.setEnabled(False)
            self.modeButton.setEnabled(False)

        self.sendSpecialBlocks.emit(self.BlockArray)

    def blockActions(self):
        selectedIndex = self.blockMenu.currentIndex()
        selectedBlock = self.BlockArray[selectedIndex]

        if selectedBlock.LIGHT:
            self.greenButton.setEnabled(not selectedBlock.state)
            self.redButton.setEnabled(selectedBlock.state)
            self.upCrossingButton.setEnabled(False)
            self.downCrossingButton.setEnabled(False)
            self.switchButton.setEnabled(False)

            self.upCrossingButton.setStyleSheet("")
            self.downCrossingButton.setStyleSheet("")
            
            if selectedBlock.state:
                self.greenButton.setStyleSheet("background-color: green")
                self.redButton.setStyleSheet("")
            elif not selectedBlock.state:
                self.greenButton.setStyleSheet("")
                self.redButton.setStyleSheet("background-color: red")

        elif selectedBlock.CROSSING and self.selectLine.isChecked():
            self.greenButton.setEnabled(False)
            self.redButton.setEnabled(False)
            self.upCrossingButton.setEnabled(not selectedBlock.state)
            self.downCrossingButton.setEnabled(selectedBlock.state)
            self.switchButton.setEnabled(False)

            self.greenButton.setStyleSheet("")
            self.redButton.setStyleSheet("")

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
            self.switchButton.setEnabled(True)

            self.greenButton.setStyleSheet("")
            self.redButton.setStyleSheet("")
            self.upCrossingButton.setStyleSheet("")
            self.downCrossingButton.setStyleSheet("")

    def greenButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.BlockArray[selectedIndex].state = True
        self.greenButton.setEnabled(False)
        self.redButton.setEnabled(True)
        self.greenButton.setStyleSheet("background-color: green")
        self.redButton.setStyleSheet("")
        self.sendSpecialBlocks.emit(self.BlockArray)

    def redButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.BlockArray[selectedIndex].state = False
        self.greenButton.setEnabled(True)
        self.redButton.setEnabled(False)
        self.greenButton.setStyleSheet("")
        self.redButton.setStyleSheet("background-color: red")
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
        for block_id in sentBlocks:
            for block in self.AllBlocks:
                if block_id == block.ID:
                    block.occupied = True

        self.BlockOcc.setText(" ".join(sentBlocks))
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
        self.tbBlockMenu.addItems(['B3','B5','B6','B11'])

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
            if selectedBlock.state:
                self.label_19.setText("Green")
                self.label_22.setText("")
            else:
                self.label_19.setText("Red")
                self.label_22.setText("")
        elif selectedBlock.CROSSING:
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
                self.label_24.setText("B11")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window2 = TestBench()

    #Signal: Window
    window.sendSpecialBlocks.connect(window2.updateBlockStates)

    #Signal: Window 2
    window2.OccBlocksChanged.connect(window.updateBlocks)
    window2.tbChangeMode.connect(window.changeMode)

    window.show()
    window2.show()
    sys.exit(app.exec_())
