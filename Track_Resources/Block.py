# Define the Block class
class Block:
    def __init__(self, lineColor, blockSection, blockNum, hasLight, hasCrossing, hasSwitch, lightState, crossingState, switchState,id):
        self.lineColor = lineColor
        self.blockSection = blockSection
        self.blockNum = blockNum
        self.LIGHT = hasLight
        self.CROSSING = hasCrossing
        self.SWITCH = hasSwitch
        self.lightState = lightState
        self.crossingState = crossingState
        self.switchState = switchState
        self.occupied = False
        self.ID = id
        self.speedLimit = None
        self.authority = None
        self.blockLength = None
        self.Wayside = None

