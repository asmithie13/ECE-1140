import csv

#Implementation of a block class:
class Block:
    def __init__(self, lineColor, blockSection, blockNum, hasSwitch, hasCrossing):
        #Assign arguments:
        self.lineColor = lineColor
        self.blockSection = blockSection
        self.blockNum = blockNum
        self.hasSwitch = hasSwitch
        self.hasLight = hasSwitch #If there is a switch, there is a light
        self.hasCrossing = hasCrossing

        #All blocks are initialized as unoccupied and operational:
        self.isOccupied = False
        self.isFailed = False

        #All block ttributes begin in the default position:
        self.switchState = False #Switch is left
        self.lightState = False #Light is red
        self.crossingState = False #Crossing is up
