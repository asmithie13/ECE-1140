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
        self.switchState = False
        self.lightState = False
        self.crossingState = False
    
    #Function to return the block ID of the block:
    def returnBlockID(self):
       tempStr = self.blockSection + str(self.blockNum)
       return tempStr
      
    #Function to get the state of a switch:
    def getSwitchState(self):
       if(self.hasSwitch == False):
          return "No switch at this block."
       else:
          if(self.switchState == False):
             return "Left"
          else:
             return "Right"
       return self.switchState
      
    #Function to get the state of a light:
    def getLightState(self):
       if(self.hasSwitch == False):
          return "No light at this block."
       else:
          if(self.lightState == False):
             return "Red"
          else:
             return "Green"
      
    #Function to get the state of a crossing:
    def getCrossingState(self):
       if(self.hasCrossing == False):
          return "No crossing at this block."
       else:
          if(self.crossingState == False):
             return "Up"
          else:
             return "Down"