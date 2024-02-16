import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from TrainModel_UI import Ui_MainWindow  # Import the generated UI class
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, uic, QtGui

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Train Model/TrainModel_UI.ui", self)

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())