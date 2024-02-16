class Block:
    def __init__(self, lineColor, blockSection, blockNumber, crossingState, switchState, lightState):
        self.lineColor = lineColor
        self.blockSection = blockSection
        self.blockNumber = blockNumber
        #Need to add more attributes here

        #Intialize all of the states:
        self.crossingState = crossingState #First index = "True" if the block has the attribute, "False" if it does not
        self.crossingState[1] = False #Second index = State of the attribute (Set to False for default)

        self.switchState = switchState
        self.switchState[1] = False

        self.lightState = lightState
        self.lightState[1] = False

    #Function to return the ID of a specific block:
    def returnBlockID(self):
        lineID = self.blockSection + str(self.blockNumber)
        return lineID
    
    #Function to check the state of a crossing:
    def checkCrossingState(self):
        if(self.crossingState[0] == False):
            print("No crossing at this block")
        else:
            if(self.crossingState[1] == False):
                print("The crossing is UP")
            else:
                print("The crossing is DOWN")
            
    #Function to change the state of a crossing:
    def changeCrossingState(self):
        if(self.crossingState[0] == False):
            print("No crossing at this block")
        else:
            if(self.crossingState[1] == False): #"False" means the crossing is UP (Since UP is the default position)
                self.crossingState[1] = True
                print("Crossing has been switched to DOWN")
            else: #"True" means that the crossing is DOWN
                self.crossingState[1] = False
                print("Crossing has been switched to UP")
            

blockOne = Block("Blue", "A", 1, [True, True])
blockOne.checkCrossingState()
blockOne.changeCrossingState()
blockOne.checkCrossingState()