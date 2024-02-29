# Define the Block class
class Block:
    def __init__(self, light, crossing, switch, lightState, crossingState, switchState, occupied,id,speedLimit,authority):
        self.LIGHT = light
        self.CROSSING = crossing
        self.SWITCH = switch
        self.lightState = lightState
        self.crossingState = crossingState
        self.switchState = switchState
        self.occupied = occupied
        self.ID = id
        self.speedLimit = speedLimit
        self.authority = authority

