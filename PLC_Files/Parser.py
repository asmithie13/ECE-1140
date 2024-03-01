import sys
import os

# Using Block Class as a seperate file
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from Track_Resources.Block import Block

class Parser():
    def __init__(self, inputPLC,CrossingTriplesIDS,outPuttedBlocks):
        self.inputPLC = inputPLC
        self.CrossingTriplesIDS = CrossingTriplesIDS
        self.outPuttedBlocks = outPuttedBlocks
        
    def parsePLC(self):
        lines = self.inputPLC.split('\n')
        switchLogic, curLightLogic, leftLightLogic, rightLightLogic = lines[0], lines[3], lines[6], lines[9]

        CrossingTripleBlocks = [
            [block for row in self.CrossingTriplesIDS for element in row
             for block in self.outPuttedBlocks if element == block.ID[1:]][i:i+3]
            for i in range(0, len(self.CrossingTriplesIDS)*3, 3)
        ]

        

            
            


