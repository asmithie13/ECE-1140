import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Wayside SW/Wayside_UI_Rough.ui",self)

        #Define special blocks constants
        LIGHT = [True,False,False,True]
        CROSSING = [False,True,False,True]
        SWITCH = [False,False,True,True]

        #Defining important blocks
        B3 = CROSSING    
        B5 = SWITCH
        B6 = LIGHT
        B11 = LIGHT

        #Defines an array of these blocks

        self.BlockArray = [B3,B5,B6,B11]

        # Buttons
        self.fileButton.clicked.connect(self.on_file_button_clicked)
        self.modeButton.clicked.connect(self.changeMode)
        self.selectLine.stateChanged.connect(self.checkLine)
        self.blockMenu.currentIndexChanged.connect(self.blockActions)

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

        if selectedBlock[0]:
            self.greenButton.setEnabled(True)
            self.redButton.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
