"""
Tutorial I'm using
https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/
"""


from PyQt5 import QtWidgets #Import necessary libraries
#from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QPushButton, QLabel, QFileDialog, QLineEdit, QFontDialog
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys

#from PyQt5.QtWidgets import QApplication, QWidget

# Subclass QMainWindow to customize application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CTC")

        label = QLabel("Train Name")

        self.setCentralWidget(label)
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        #self.button = QPushButton("Press Me!")
        #self.button_is_checked = True

        
        #self.button.clicked.connect(self.the_button_was_clicked)
        #self.button.clicked.connect(self.the_button_was_toggled)

        #self.setFixedSize(QSize(400, 300))

        # Set the central widget of the Window.
        #self.setCentralWidget(self.button)
    """
    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

        # Also change the window title.
        self.setWindowTitle("My Oneshot App")
    
    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        
        print(self.button_is_checked)
    """

#QApplication instance
app = QApplication(sys.argv)

#Creating a window usign a QWidget
window = MainWindow()
window.show()

#Open Window
app.exec()