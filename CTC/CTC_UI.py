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


    #Define functionality for Upload File Button
    def open_files(self):
        # Open a file dialog to select a Excel File
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Schedule File", "", "Excel Workbook (*.xlsx);;All Files (*)")

        if file_path:
            # Implement your logic with the selected file path
            print(f"Selected PLC File: {file_path}")
        


test = QtWidgets.QApplication(sys.argv)
window = UI()
window.show()
test.exec_()