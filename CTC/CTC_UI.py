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

        columns_layout = QHBoxLayout()
        c1_layout = QVBoxLayout()
        c2_layout = QVBoxLayout()

        c1_layout.addWidget(Color('red'))
        c1_layout.addWidget(Color('yellow'))

        columns_layout.addWidget(c1_layout)

        c2_layout.addWidget('red')
        c2_layout.addWidget('orange')
        c2_layout.addWidget('yellow')
        c2_layout.addWidget('green')
        c2_layout.addWidget('blue')

        columns_layout.addWidget(c2_layout)


        """
        label = QLabel("Train Name")

        self.setCentralWidget(label)
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        """

        """
        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setObjectName("tabWidget")
        self.CTC_tab = QtWidgets.QWidget()
        self.CTC_tab.setObjectName("CTC_tab")
        self.tabWidget.addTab(self.CTC_tab, "")
        self.Testbench_tab = QtWidgets.QWidget()
        self.Testbench_tab.setObjectName("Testbench_tab")
        self.tabWidget.addTab(self.Testbench_tab, "")
        """

    """
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CTC_tab), _translate("MainWindow", "CTC"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Testbench_tab), _translate("MainWindow", "Testbench"))\
    """

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