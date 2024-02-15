import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from Block import Block

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Wayside SW/Wayside_UI_Rough.ui",self)

        # Global constants for LIGHT, CROSSING, and SWITCH
        LIGHT_CONST = [True, False, False, True]
        CROSSING_CONST = [False, True, False, True]
        SWITCH_CONST = [False, False, True, True]

        #Defining important blocks
        B3 = Block(*CROSSING_CONST) 
        B5 = Block(*SWITCH_CONST) 
        B6 = Block(*LIGHT_CONST)
        B11 = Block(*LIGHT_CONST)

        #Defines an array of these blocks

        self.BlockArray = [B3,B5,B6,B11]

        # Buttons
        self.fileButton.clicked.connect(self.on_file_button_clicked)
        self.modeButton.clicked.connect(self.changeMode)
        self.selectLine.stateChanged.connect(self.checkLine)
        self.blockMenu.currentIndexChanged.connect(self.blockActions)
        self.greenButton.clicked.connect(self.greenButtonPushed)
        self.redButton.clicked.connect(self.redButtonPushed)
        self.upCrossingButton.clicked.connect(self.upButtonPushed)
        self.downCrossingButton.clicked.connect(self.downButtonPushed)

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
        elif selectedBlock.CROSSING:
            self.greenButton.setEnabled(False)
            self.redButton.setEnabled(False)
            self.upCrossingButton.setEnabled(not selectedBlock.state)
            self.downCrossingButton.setEnabled(selectedBlock.state)
            self.switchButton.setEnabled(False)
        elif selectedBlock.SWITCH:
            self.greenButton.setEnabled(False)
            self.redButton.setEnabled(False)
            self.upCrossingButton.setEnabled(False)
            self.downCrossingButton.setEnabled(False)
            self.switchButton.setEnabled(True)

    def greenButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.BlockArray[selectedIndex].state = True
        self.greenButton.setEnabled(False)
        self.redButton.setEnabled(True)

    def redButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.BlockArray[selectedIndex].state = False
        self.greenButton.setEnabled(True)
        self.redButton.setEnabled(False)

    def upButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.BlockArray[selectedIndex].state = True
        self.upCrossingButton.setEnabled(False)
        self.downCrossingButton.setEnabled(True)

    def downButtonPushed(self):
        selectedIndex = self.blockMenu.currentIndex()
        self.BlockArray[selectedIndex].state = False
        self.upCrossingButton.setEnabled(True)
        self.downCrossingButton.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
