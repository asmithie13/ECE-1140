from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys
from TrackController_HW import *
from TrackController_HW_TB import *
from readTrackFile import *

app = QApplication(sys.argv)
windowOne = TrackController_HW()
windowTwo = TrackController_HW_TB()

#Signal to send a list of occupied blocks from the track model to wayside:
windowTwo.occupiedBlocksSignal.connect(windowOne.modeHandler)

#Signal to send a list of closed blocks from the CTC office to wayside:
windowTwo.closedBlocksSignal.connect(windowOne.getClosedBlocks)

#Signal to send speed and authority (distance-wise) from the CTC office to wayside:
windowTwo.speedAuthoritySignal.connect(windowOne.handleSpeedAuthority)

#Signal to send speed and authority (distance-wise) from wayside to the track model:
windowOne.sendSpeedAuthority.connect(windowTwo.receiveSpeedAuthority)

#Signal to send an updated block list (w/ changed attributes) from wayside to the track model:
windowOne.sendUpdatedBlocks.connect(windowTwo.receiveUpdatedBlocks)

#Signal to send a list of occupied blocks to the CTC office:
windowOne.sendOccupiedBlocks.connect(windowTwo.receiveOccupiedBlocks)

windowOne.show()
windowTwo.show()
sys.exit(app.exec_())