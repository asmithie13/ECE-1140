import sys
import os

# Using Block Class as a seperate file
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from Track_Resources.Block import Block

class Parser():
    def __init__(self, inputPLC, outPuttedBlocks):
        self.inputPLC = inputPLC
        self.outPuttedBlocks = outPuttedBlocks

    def parsePLC(self):
        lines = self.inputPLC.split('\n')

        for line in lines:
            tokens = line.strip().split()
            command = tokens[0]
            parameters = tokens[1:]
            match = [block for block in self.outPuttedBlocks if block.ID == parameters[0]]

            if command == "LIGHT" or command == "CROSSING":
                if parameters[0][0] != '!':
                    match[0].state = True
                else:
                    match[0].state = False

            elif command == "SWITCH":
                if int(parameters[1][1:]) - 1 == int(parameters[0][1:]): match[0].state = True
                else : match[0].state = False

            elif command == "OCCUPIED":
                match[0].occupied = True



