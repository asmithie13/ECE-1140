import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QComboBox, QLabel
#from TrainModel_testbench import Ui_MainWindow  # Import the generated UI class
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, uic, QtGui

class trainmodel_testbench(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("Train_Model/TrainModel_testbench.ui", self)
        
        #self.run_button_tb.clicked.connect(self.get_train_selection)
        self.train_sel_combo_tb.activated[str].connect(self.get_train_selection)
        #self.get_train_selection()

    #function to fix tb checkboxes
    def get_train_selection(self, text):
        # Get the selected option text
        selected_text = text

        # Display the selected option information in the label
        self.train_sel_output_tb.setText(selected_text)

   # def 





if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("windows")
    window = QMainWindow()
    window.show()
    sys.exit(app.exec_())