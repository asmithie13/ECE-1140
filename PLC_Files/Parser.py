import sys
import os

# Using Block Class as a seperate file
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from Track_Resources.Block import Block

class Parser():
    def __init__(self, inputPLC, CrossingTriplesIDS, outPuttedBlocks):
        self.inputPLC = inputPLC
        self.CrossingTriplesIDS = CrossingTriplesIDS
        self.outPuttedBlocks = outPuttedBlocks

    def parsePLC(self):
        lines = self.inputPLC.split('\n')
        switchLogic, curLightLogic, leftLightLogic, rightLightLogic = lines[0], lines[3], lines[6], lines[9]

        CrossingTripleBlocks = [
            [block for row in self.CrossingTriplesIDS for element in row
             for block in self.outPuttedBlocks if str(element) == str(block.ID[1:])][i:i + 3]
            for i in range(0, len(self.CrossingTriplesIDS) * 3, 3)
        ]

        for block in self.outPuttedBlocks:
            if block.CROSSING:
                setattr(block, str(lines[13]), not block.occupied)
            

        for data in CrossingTripleBlocks:
            SwitchOcc = data[0].occupied
            SwitchLeftOcc = data[1].occupied
            SwitchRightOcc = data[2].occupied

            if eval(lines[15]): #continue if no blocks are occupied
                continue

            if eval(lines[18]):
                data[0].switchState = True
                data[0].lightState = True
                continue
               
            data[0].switchState = eval(switchLogic)
            data[0].lightState = eval(curLightLogic)
            data[1].lightState = eval(leftLightLogic)
            data[2].lightState = eval(rightLightLogic)
