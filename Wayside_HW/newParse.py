import sys
import os
import re

#Using Block Class as a seperate file
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from Wayside_HW.readTrackFile import *
from Track_Resources.Block import Block

def newParse(occupiedBlockSections, allBlocks):
    fileObject = open("Wayside_HW/testOtherPLC.txt", "r")
    PLCfile = fileObject.read()
    allLines = PLCfile.split('\n')
    
    for line in allLines:
        tempLine = line.split(" ")
        if tempLine[0] == 'IF' and tempLine[1] != 'ANY':
            logicFlag = 0
            for section in tempLine:
                if section in occupiedBlockSections:
                    logicFlag = 1
                    break
        elif tempLine[0] == 'IF' and tempLine[1] == 'ANY':
            logicFlag = 1

        elif tempLine[0] == 'SWITCH' or tempLine[0] == 'LIGHT' or tempLine[0] == 'CROSSING':
            if logicFlag == 1:
                for block in allBlocks:
                    if block.ID == tempLine[1]:
                        if tempLine[0] == 'SWITCH':
                            block.switchState = int(tempLine[2])
                        elif tempLine[0] == 'LIGHT':
                            block.lightState = int(tempLine[2])
                        elif tempLine[0] == 'CROSSING':
                            block.crossingState = int(tempLine[2])
                        break

        elif tempLine[0] == "ELSE":
            logicFlag = not logicFlag

    return allBlocks