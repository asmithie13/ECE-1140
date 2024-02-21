import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui as qtg


class MyMainWindow(QMainWindow):
    
    

    def __init__(self):
        super().__init__()
        uic.loadUi("Train Model/TrainModel_UI.ui", self)
       

    #function to set Power LCD
    def get_power(self, power_input):
        self.Power_value_lcd.display(power_input)

    #function to calculate the acceleration in ft/s^2 using the power command
    def Calculate_acceleration(self):
       power_input=Power_value_lcd.value()
       acceleration = power_input
   # def get_current_velocity(self):

   # def Calculate_Force(self):
       # velocity_input = power_input/

class trainmodel_testbench(QMainWindow):
    power_input_signal = qtc.pyqtSignal(float)
    def __init__(self):
        super().__init__()
        uic.loadUi("Train Model/TrainModel_testbench.ui", self)
        self.train_sel_combo_tb.activated[str].connect(self.get_train_selection)
        self.power_input_tb.returnPressed.connect(self.receive_power)
        self.power_input_tb.returnPressed.connect(self.display_power)

    def get_train_selection(self, text):
        selected_text = text
        self.train_sel_output_tb.setText(selected_text)

    
    def receive_power(self):
        power_input=float(self.power_input_tb.text())
        self.power_input_signal.emit(power_input)

    def display_power(self):
        power_display=self.power_input_tb.text()
        self.power_output_tb.setText(power_display+" W")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("windows")
    
    window = MyMainWindow()
    window_tb = trainmodel_testbench()

    # Connect the signal from MyMainWindow to trainmodel_testbench
    window_tb.power_input_signal.connect(window.get_power)

    window.show()
    window_tb.show()
    sys.exit(app.exec_())
