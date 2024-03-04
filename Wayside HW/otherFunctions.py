from Block import Block
import csv

#Function that reads all blocks from a *.csv file and assigns block attributes:
def readTrackFile(fileName):
    totalBlocks = []
    fileName = "Wayside HW/" + fileName
    with open(fileName, "r") as fileObject:
        readObj = csv.reader(fileObject, delimiter=",")
        for i, line in enumerate(readObj):
            hasCrossingTemp = False
            hasSwitchTemp = False
            if(i == 0):
                continue
            else:
                if(line[6] == "RAILWAY CROSSING"):
                    hasCrossingTemp = True
                elif(line[6][0:6] == "Switch" or line[6][0:6] == "SWITCH" ):
                    hasSwitchTemp = True
            tempBlock = Block(line[0], line[1], line[2], hasSwitchTemp, hasCrossingTemp)
            totalBlocks.append(tempBlock)
    
    return totalBlocks #Return a list of all blocks within the file

#Function that divides blocks on the red line depending on wayside:
def splitRedBlocks(allRedBlocks):
    secWaysideThree = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    bothWayside = []
    waysideThree = []
    waysideFour = []

    for block in allRedBlocks:
        if(block.blockSection in secWaysideThree):
            waysideThree.append(block)
        else:
            waysideFour.append(block)
    
    bothWayside.append(waysideThree)
    bothWayside.append(waysideFour)
    return bothWayside

#Function that divides blocks on the red line depending on wayside:
def splitGreenBlocks(allGreenBlocks):
    secWaysideOne = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    bothWayside = []
    waysideOne = []
    waysideTwo = []

    for block in allGreenBlocks:
        if(block.blockSection in secWaysideOne):
            waysideOne.append(block)
        else:
            waysideTwo.append(block)
    
    bothWayside.append(waysideOne)
    bothWayside.append(waysideTwo)
    return bothWayside