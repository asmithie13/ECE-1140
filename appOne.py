from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, uic, QtGui
import sys

#Function to confirm whether or not the selected PLC file is a valid file
def PLCvalid(fileName):
        fileOpen = open(fileName, 'r')
        headLine = fileOpen.readline()
        if(headLine != "PLC File"):
            return False
        return True

#Initialization of UI
class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi("TrackControllerHW_UI.ui",self)

        #Signals for PLC upload menu:
        self.buttonBrowse.clicked.connect(self.uploadPLCFile)
        #self.buttonSave.clicked.connect(self.savePLCFile)

        #Signals for line selection:
        self.radioButtonBlue.clicked.connect(self.blueLineButton)
        self.radioButtonRed.clicked.connect(self.redLineButton)
        self.radioButtonGreen.clicked.connect(self.greenLineButton)

        #Signals for mode selection:
        self.checkAuto.clicked.connect(self.automaticMode)
        self.checkManual.clicked.connect(self.manualMode)
    
    #Function to upload the PLC file and display the file location:
    def uploadPLCFile(self):
        fileName = QFileDialog.getOpenFileName(self, "Select PLC File", "C:")
        fileName = fileName[0]

        if(PLCvalid(fileName) == True):
            self.lineEditBrowse.setText(fileName)
            self.labelUploadValid.setText("File Uploaded Successfully")
        else:
            self.lineEditBrowse.setText("")
            self.labelUploadValid.setText("Invalid File")

    #def savePLCFile(self):
        #Implement later (If implementing the "Download PLC" feature)
    
    #Occurs if the blue line is selected:
    def blueLineButton(self):
        print("Selected: Blue Line") #Remove later after adding actual functionality

    #Occurs if the red line is selected:
    def redLineButton(self):
        print("Selected: Red Line")

    #Occurs if the green line is selected:
    def greenLineButton(self):
        print("Selected: Green Line")

    #Occurs if the system is in automatic operation:
    def automaticMode(self):
        print("Mode: Automatic")
    
    #Occcurs if the user selects manual operation:
    def manualMode(self):
        print("Mode: Manual")
        self.checkAuto.setChecked(False)
        self.checkAuto.setEnabled(False) #Unable to move back to automatic operation if currently in manual
        
#Create instance of window:
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())