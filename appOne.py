from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, uic, QtGui
import sys
from Block import Block

#Function to confirm whether or not the selected PLC file valid
def PLCvalid(fileName):
        fileOpen = open(fileName, 'r')
        headLine = fileOpen.readline()
        if(headLine != "PLC File"):
            return False
        return True

#Initialization of UI
class TrackController_UI(QMainWindow):
    def __init__(self):
        super(TrackController_UI, self).__init__()
        uic.loadUi("TrackControllerHW_UI.ui", self)

        #Disable red and green line selections - Not yet implemented:
        self.radioButtonRed.setEnabled(False) #TO BE REMOVED LATER
        self.radioButtonGreen.setEnabled(False)

        #Disable automatic mode button until a PLC file is uploaded:
        self.checkAuto.setEnabled(False)

        #Set wayside and block selections are disabled before a line is selected:
        self.comboBoxWayside.setEnabled(False)
        self.comboBoxBlock.setEnabled(False)

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
            #self.labelUploadValid.setText("File Uploaded Successfully")
            self.buttonBrowse.setEnabled(False) #Cannot upload another PLC file if one is already uploaded
            #Only option is to switch to manual operation from this point

            self.checkAuto.setEnabled(True)
            self.checkAuto.setChecked(True)
            self.automaticMode()
        else:
            self.lineEditBrowse.setText("")
            #self.labelUploadValid.setText("Invalid File")
        

    #def savePLCFile(self):
        #Implement later (If implementing the "Download PLC" feature)
    
    #Occurs if the blue line is selected:
    def blueLineButton(self):
        self.comboBoxWayside.setEnabled(True)
        self.comboBoxBlock.setEnabled(True)
        print("Selected: Blue Line") #Remove later after adding actual functionality

    #Occurs if the red line is selected:
    def redLineButton(self):
        self.comboBoxWayside.setEnabled(True)
        self.comboBoxBlock.setEnabled(True)
        print("Selected: Red Line")

    #Occurs if the green line is selected:
    def greenLineButton(self):
        self.comboBoxWayside.setEnabled(True)
        self.comboBoxBlock.setEnabled(True)
        print("Selected: Green Line")

    #Occurs if the system is in automatic operation:
    def automaticMode(self):
        print("Mode: Automatic")
    
    #Occcurs if the user selects manual operation:
    def manualMode(self):
        print("Mode: Manual")
        self.checkAuto.setChecked(False)
        self.checkAuto.setEnabled(False) #Unable to move back to automatic operation if currently in manual
        self.buttonBrowse.setEnabled(False)
        self.lineEditBrowse.setText("")
        self.labelUploadValid.setText("")

#Initialization of test bench:
class TrackController_TestBench(QMainWindow):
    def __init__(self):
        super(TrackController_TestBench, self).__init__()
        uic.loadUi("TrackControllerHW_TestBench.ui", self)

#Intialize Wayside object
class Wayside():
    def __init__(self):
        #Create instance of window:
        if __name__ == "__main__":
            app = QApplication(sys.argv)
            windowOne = TrackController_UI()
            windowOne.show()

            windowTwo = TrackController_TestBench()
            windowTwo.show()

            sys.exit(app.exec_())

waysideOne = Wayside()


