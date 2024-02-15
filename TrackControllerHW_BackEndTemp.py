from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import csv

class Block:
    def __init__(self, lineColor, blockSection, blockNumber, hasCrossing): #Function to create block and initialize values
        self.lineColor = lineColor #Initialize the line that the block is on
        self.blockSection = blockSection #Initialize the section (Letter) of the block
        self.blockNumber = blockNumber #Intialize the block number

        self.isOccupied = False #Initialize all blocks as unoccupied
        self.isFailed = False #Intialize all blocks as operable - Change to "false" if rail in this block experiences a failure
        #Initialize crossing information:
        self.crossingInfo = [hasCrossing, False] #First index: Whether or not the block has a crossing; 
                                                #Second index: True = Crossing is UP (No train), False = Crossing is DOWN (Train coming)
    
    #Function will likely later be removed:
    def printBlockInformation(self): #Function to print all block information and as well as occupancy status
        print("Block Information:")
        print("Line: ", self.lineColor, "   Block Section: ", self.blockSection, "  Block #: ", 
              self.blockNumber, "    Occupied?: ", self.isOccupied )
    
    def returnBlockLine(self): #Function to return the line (color) that the block is on
        return self.lineColor #Will be useful for sorting blocks by line (display according to check box on UI)

    def returnBlockID(self): #Function to return the block ID (Section and number)
        strID = self.blockSection + str(self.blockNumber) #Will be useful for displaying occupied blocks in a certain line
        return strID
    
    def setBlockOccupancy(self, occupancyStatus): #Create a function to set block occupancy
        self.isOccupied = occupancyStatus #"True" if the block is occupied, "False" if the block is empty

class WaysideHW():
    def __init__(self, waysideNum):
        self.waysideNum = waysideNum

    #This function separates the occupied blocks depending on the line the block is in.
        #Then, the function concatenates the block IDs of all occupied blocks into a string (separated by commas)
        #to be displayed in the "Occupied Blocks" section of the UI (lineEditOccupiedBlocks)
    def displayOccupiedBlocks(self, occupiedBlockList):
        blueLine = "" #Create an empty string to hold the block IDs of all occupied blocks in the blue line
        redLine = "" #Create an empty string to hold the block IDs of all occupied blocks in the red line
        greenLine = "" #Create an empty string to hold the block IDs of all occupied blocks in the green line

        for block in occupiedBlockList: #Iterate through each of the block objects in the list of occupied blocks sent from the track model:
            if block.returnBlockLine() == "Blue": #If the block is on the blue line:
                blueLine += (block.returnBlockID() + " ") #Concatenate to the blue line list to be displayed when the blue line is selected
            elif block.returnBlockLine() == "Red": #Repeat the above for all other colors
                redLine += (block.returnBlockID() + " ")
            elif block.returnBlockLine() == "Green":
                greenLine += (block.returnBlockID() + " ")
        
        #To be removed later:
        print("Occupied Blocks: ", blueLine)
        #Change "print" method to: Depending on which line is checked in the QCheckBoxes for line selection (checkBlue, etc.),
        #Display those occupied blocks in the lineEditOccupiedBlocks

#Creating sample blocks to test methods:
occBlockList = []
blockOne = Block("Blue", "B", 1, False)
blockTwo = Block("Blue", "A", 2, False)
blockThree = Block("Red", "S", 6, False)

occBlockList.append(blockOne)
occBlockList.append(blockTwo)
occBlockList.append(blockThree)

waysideOne = WaysideHW(1)
waysideOne.displayOccupiedBlocks(occBlockList)

#Next:
#-Create similar function as displayOccupiedBlock to display failed/unavailable blocks
    #This may require the implementation of a second function, or there may be a way to incorporate both
    #Functionalities into one
