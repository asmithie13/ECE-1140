#File to run the UI for the CTC Module
#Abby Magistro

import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
#from UI_temp import MainWindow

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("CTC/CTC_UI.ui", self)

        #Connect Buttons
        self.UploadButton.clicked.connect(self.open_files)
        self.ManualModeButton.clicked.connect(self.selectManualMode_button)
        self.AddTrainButton.clicked.connect(self.addTrain_button)

        #Change Button Colors
        self.AddTrainButton.setStyleSheet("background-color : #26cf04")
        self.UploadButton.setStyleSheet("background-color : #26cf04")

        


    #Define functionality for Upload File Button
    def open_files(self):
        # Open a file dialog to select a Excel File
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Schedule File", "", "Excel Workbook (*.xlsx);;All Files (*)")

        """
        #TO DO LATER
        if file_path:
            # Implement your logic with the selected file path
            print(f"Selected PLC File: {file_path}")
        """
    

    #Define mutually exclisive auto/manual mode
    def selectManualMode_button(self):
        #When Manual Mode button is pressed

        #Disable AutoMode Button
        self.AutoModeButton.setEnabled(False)
        #And File Upload Button
        self.UploadButton.setEnabled(False)
        self.UploadButton.setStyleSheet("background-color : #ebfae8")

        #Disable Manual Mode button (because it's one use)
        self.ManualModeButton.setEnabled(False)
        self.ManualModeButton.setStyleSheet("background-color : blue; color: black;")
    
    #defing manual mode add train button functionality
    def addTrain_button(self):
        #Time edit tutorial
        #https://www.pythontutorial.net/pyqt/pyqt-qtimeedit/
        ArrivalTime = self.ArrivalTimeEdit.time()
        print(ArrivalTime.toString())



test = QtWidgets.QApplication(sys.argv)
window = UI()
window.show()
test.exec_()