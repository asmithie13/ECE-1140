# Define the Block class
class Block:
    def __init__(self, light, crossing, switch, state,occupied,id):
        self.LIGHT = light
        self.CROSSING = crossing
        self.SWITCH = switch
        self.state = state
        self.occupied = occupied
        self.ID = id
