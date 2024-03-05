from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from TrackControllerHW_UI import *
from TrackControllerHW_TestBench import *
from Block import *
from otherFunctions import *
import sys

#Intialize Wayside object
class TrackControllerHW():
    def __init__(self):
        #Create instance of window:
        app = QApplication(sys.argv)
        windowOne = TrackController_UI()
        windowTwo = TrackController_TestBench()

        windowOne.blockStates.connect(windowTwo.getUpdatedBlockList)

        windowTwo.occBlocksChanged.connect(windowOne.displayOccupancies)
        windowTwo.failedBlocksChanged.connect(windowOne.displayFailures)

        windowOne.show()
        windowTwo.show()
        sys.exit(app.exec_())

waysideOne = TrackControllerHW()