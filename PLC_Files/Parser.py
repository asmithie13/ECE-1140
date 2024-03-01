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
        self.commandsToRun = []
        self.blockOccsByID = [False] * 26 #initially no blocks are occupied

    def blockState(self):   #will break up inputPLC into what commands to run based off of conditions of occupancies
        lines = self.inputPLC.split('\n')
        index = 0
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        for char in alphabet:
            occupied_blocks = [block for block in self.outPuttedBlocks if char in block.ID and block.occupied]
            self.blockOccsByID[index] = True if occupied_blocks else False
            index = index + 1

        index = 0
        indexOcc = 0
        indexNotOcc = 0
        indexNextOcc = 0
        indexEnd = len(lines) - 1
        
        for length in range(2,25):  #start with 2 for C
            if (length + 1) >= 25 or not ("OCCUPIED " + alphabet[length]) in lines: break

            isOcc = False
        
            if (length + 1) < 25 and "OCCUPIED " + alphabet[length + 1] in lines  : indexNextOcc = lines.index("OCCUPIED " + alphabet[length + 1])
            else: indexNextOcc = indexEnd

            indexOcc = lines.index("OCCUPIED " + alphabet[length])
            indexNotOcc = lines.index("OCCUPIED !" + alphabet[length])

            if self.blockOccsByID[length]:
                isOcc = True
           
            if isOcc: 
                indexLoopStart = indexOcc + 1
                indexLoopEnd = indexNotOcc - 1
            else:
                indexLoopStart = indexNotOcc + 1
                if indexNextOcc != indexEnd : indexLoopEnd = indexNextOcc - 1
                else: indexLoopEnd = indexNextOcc + 1
        
            for pos in range(indexLoopStart, indexLoopEnd):
                self.commandsToRun.append(lines[pos])


    def parsePLC(self):
        self.blockState()

        for line in self.commandsToRun:
            if line == '' : break
            tokens = line.strip().split()
            command = tokens[0]
            parameters = tokens[1:]
            block_id = parameters[0][1:] if parameters[0][0] == '!' else parameters[0]
            match = [block for block in self.outPuttedBlocks if block.ID == block_id]

            if command == "LIGHT" or command == "CROSSING":
                if parameters[0][0] != '!':
                    match[0].state = True
                else:
                    match[0].state = False

            #CHANGE TO BE LIKE ABOVE JUST WITH DEFAULT STATES

            elif command == "SWITCH":
                if int(parameters[1][1:]) - 1 == int(parameters[0][1:]): match[0].state = True
                else : match[0].state = False

        self.commandsToRun = []


