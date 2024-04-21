import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
#from TrainModel_UI import Ui_MainWindow  # Import the generated UI class
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, uic, QtGui

class MyMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("Train Model/TrainModel_UI.ui", self)
        self.get_power()
        #self.ui = Ui_MainWindow()
        #self.ui.setupUi(self)
    def get_power(self):
        power_value=self.Power_value_lcd
        self.Power_value_lcd.display(799)
        

    
    def Calculate_power(self):
        Power_value = self.Power_value_lcd
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("windows")
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
