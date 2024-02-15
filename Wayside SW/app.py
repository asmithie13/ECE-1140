import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from Block import Block
from PyQt5.QtCore import QTimer

class MyApp(QMainWindow):
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

        #Defines an array of these blocks

        self.BlockArray = [B3,B5,B6,B11]    #Special Blocks
        self.AllBlocks = [B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11] #All Blocks

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

    def redButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.BlockArray[selectedIndex].state = False
        self.greenButton.setEnabled(True)
        self.redButton.setEnabled(False)
        self.greenButton.setStyleSheet("")
        self.redButton.setStyleSheet("background-color: red")

    def upButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.BlockArray[selectedIndex].state = True
        self.upCrossingButton.setEnabled(False)
        self.downCrossingButton.setEnabled(True)
        self.upCrossingButton.setStyleSheet("background-color: yellow")
        self.downCrossingButton.setStyleSheet("")

    def downButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.BlockArray[selectedIndex].state = False
        self.upCrossingButton.setEnabled(True)
        self.downCrossingButton.setEnabled(False)
        self.upCrossingButton.setStyleSheet("")
        self.downCrossingButton.setStyleSheet("background-color: yellow")

    def switchButtonPushed(self):
        current_text = self.label_11.text()
        if current_text == self.B5_Switch_Positions[0]:
            self.label_11.setText(self.B5_Switch_Positions[1])
        elif current_text == self.B5_Switch_Positions[1]:
            self.label_11.setText(self.B5_Switch_Positions[0])

    #def updateBlockOccupancy(self):
        # Your logic to update the last index (index 4) of each block in self.AllBlocks
        #for block in self.AllBlocks:
         #   block[4] = not block[4]
        #print("Block occupancy updated.")

    
    #def onOccupancyChanged(self):

class TestBench(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Wayside SW/Wayside_Testbench.ui", self)

        # Buttons
        self.speedInput.returnPressed.connect(self.sendSpeed)
        self.authorityInput.returnPressed.connect(self.sendAuthority)
        self.modeInput.clicked.connect(self.sendMode)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    window2 = TestBench()
    window2.show()
    sys.exit(app.exec_())
