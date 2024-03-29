import sys
import os
import re

#Using Block Class as a seperate file
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from Wayside_HW.readTrackFile import *
from Track_Resources.Block import Block

def newParse(occupiedBlockIDs, allBlocks):
    #CONSIDER HARD-CODING FOR ITERATION #3
    occupiedBlocks = []
    for block in allBlocks:
        if block.ID in occupiedBlockIDs:
            block.occupied = True
            occupiedBlocks.append(block)

    fileObject = open("Wayside_HW/testOtherPLC.txt", "r")
    PLCfile = fileObject.read()
    allLines = PLCfile.split('\n')

    for line in allLines:
        tempLine = line.split(" ")
        if tempLine[0] == 'LOGIC':
            print(tempLine)



