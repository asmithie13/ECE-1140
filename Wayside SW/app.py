import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, uic, QtGui

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Wayside SW/Wayside_UI_Rough.ui",self)

        # Buttons
        self.fileButton.clicked.connect(self.on_file_button_clicked)
        self.modeButton.clicked.connect(self.changeMode)

        #Original Map Image
        pixmap = QPixmap('Blue Line Images\BlueLine.png')
        self.label_17.setPixmap(pixmap)

        #Dropdown menu
        self.blockMenu.addItems(['B3','B5','B6','B11'])
        self.waysideMenu.addItems(['W1'])
        
    
    def on_file_button_clicked(self):
        # Open a file dialog to select a PLC file
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select PLC File", "", "PLC Files (*.plc);;All Files (*)")

        if file_path:
            # Implement your logic with the selected file path
            print(f"Selected PLC File: {file_path}")

    def on_save_button_clicked(self):
        # Implement your save button logic here
        print("Save Button Clicked")

    def on_file_button_3_clicked(self):
        # Implement your file button 3 logic here
        print("File Button 3 Clicked")

    def changeMode(self):
        current_text = self.label_7.text()
        if current_text == "MANUAL":
            self.label_7.setText("AUTOMATIC")
        elif current_text == "AUTOMATIC":
            self.label_7.setText("MANUAL")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
