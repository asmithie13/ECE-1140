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

        #Naming Window
        self.setWindowTitle("CTC")
        self.layout = QVBoxLayout(self)

        #nitialize Tabs
        self.tabs = QTabWidget()
        self.CTC_tab = QWidget()
        self.Testbench_tab = QWidget()
        self.tabs.resize(300,200)

        # Add tabs
        self.tabs.addTab(self.CTC_tab,"CTC")
        self.tabs.addTab(self.Testbench_tab,"Testbench")
    


        columns_layout = QHBoxLayout()
        c1_layout = QVBoxLayout()
        c2_layout = QVBoxLayout()

        #c1_layout.addWidget(Color('red'))
        self.manual_dispatch = ManualDispatch(self)
        c1_layout.addWidget(self.manual_dispatch)

        c1_layout.addWidget(Color('yellow'))

        columns_layout.addLayout(c1_layout)

        c2_layout.addWidget(Color('red'))
        c2_layout.addWidget(Color('orange'))
        c2_layout.addWidget(Color('yellow'))
        c2_layout.addWidget(Color('green'))
        c2_layout.addWidget(Color('blue'))

        columns_layout.addLayout(c2_layout)


        #Set CTC tab
        self.CTC_tab.setLayout(columns_layout)

        
        self.setCentralWidget(self.tabs)


        """
        label = QLabel("Train Name")

        self.setCentralWidget(label)
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        """

    """
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CTC_tab), _translate("MainWindow", "CTC"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Testbench_tab), _translate("MainWindow", "Testbench"))\
    """

#Define Behavior for the Manual Dispatch function
class ManualDispatch(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        layout = QGridLayout()

        #Add Labels
        #Add train name label
        trainname_label = QLabel("Train Name")
        font = trainname_label.font()
        font.setPointSize(20)
        trainname_label.setFont(font)
        trainname_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(trainname_label, 0, 0)

        #Add destination label
        destination_label = QLabel("Destination")
        destination_label.setFont(font)
        destination_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(destination_label, 1, 0)

        #Add departure station label
        departurestation_label = QLabel("Departure Station")
        departurestation_label.setFont(font)
        departurestation_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(departurestation_label, 2, 0)

        #Add Train Name Text Box
        trainname_widget = QLineEdit()
        trainname_widget.setMaxLength(10)
        trainname_widget.setPlaceholderText("Enter your text")
        layout.addWidget(trainname_widget, 0, 1)

        #layout.addWidget(Color('red'), 0, 0)
        #layout.addWidget(Color('orange'), 0, 1)
        layout.addWidget(Color('yellow'), 0, 2)
        #layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(Color('purple'), 1, 2)
        #layout.addWidget(Color('red'), 2, 0)
        layout.addWidget(Color('orange'), 2, 1)
        layout.addWidget(Color('yellow'), 2, 2)

        self.setLayout(layout)


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

#QApplication instance
app = QApplication(sys.argv)

#Creating a window usign a QWidget
window = MainWindow()
window.show()

#Open Window
app.exec()