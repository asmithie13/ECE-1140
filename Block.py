import csv

#Implementation of a block class:
class Block:
    def __init__(self, lineColor, blockSection, blockNum, hasSwitch, hasCrossing):
        self.lineColor = lineColor
        self.blockSection = blockSection
        self.blockNum = blockNum
        self.hasSwitch = hasSwitch
        self.hasCrossing = hasCrossing

        self.isOccupied = False
        self.switchState = False
        self.lightState = False
        self.crossingState = False
    
    #Function to return the line that the block is on:
    def returnLineColor(self):
       return self.lineColor
    
    #Function to return the block ID of the block:
    def returnBlockID(self):
       tempStr = self.blockSection + str(self.blockNum)
       return tempStr

    #Function to set the occupancy of a block:
    def setOccupied(self, occState):
       self.isOccupied = occState
    
    #Function to return the occupancy state of a block
    def getOccupancy(self):
       return self.isOccupied
    
    #Function to set the state of a switch:
    def changeSwitch(self, switchState):
       if(self.hasSwitch == True):
         self.switchState = switchState
      
    #Function to get the state of a switch:
    def getSwitchState(self):
       return self.switchState
    
    #Function to set the state of a light:
    def changeLight(self, lightState):
       if(self.hasSwitch == True):
         self.lightState = lightState
      
    #Function to get the state of a light:
    def getLightState(self):
       return self.lightState
    
    #Function to set the state of a crossing:
    def changeCrossing(self, crossingState):
       if(self.hasCrossing == True):
         self.crossingState = crossingState
      
    #Function to get the state of a crossing:
    def getCrossingState(self):
       return self.crossingState