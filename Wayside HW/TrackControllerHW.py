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

        #Signal to send a list of changed block objects to the track model module:
        windowOne.blockStates.connect(windowTwo.getUpdatedBlockList)

        #Signals to send block occupancies from test bench to UI (later to be received from track model)
        windowTwo.occBlocksChanged.connect(windowOne.displayOccupancies)
        windowTwo.failedBlocksChanged.connect(windowOne.displayFailures)

        windowOne.show()
        windowTwo.show()
        sys.exit(app.exec_())

waysideOne = TrackControllerHW()