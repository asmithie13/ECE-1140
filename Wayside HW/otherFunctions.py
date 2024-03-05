from Block import Block
import csv
import re

#Function that reads all blocks from a *.csv file and assigns block attributes:
def readTrackFile(fileName, crossingTriples):
    totalBlocks = []
    lightBlocks = {}
    fileName = "Wayside HW/" + fileName
    with open(fileName, "r") as fileObject:
        readObj = csv.reader(fileObject, delimiter=",")
        for i, line in enumerate(readObj):
            hasCrossingTemp = False
            hasSwitchTemp = False
            hasLightTemp = False
            lightState = None
            crossingState = None
            switchState = None
            blockId = line[1] + line[2]
            if(i == 0):
                continue
            else:
                if(line[6] == "RAILWAY CROSSING"):
                    hasCrossingTemp = True
                    crossingState = True

                elif(line[6][0:6] == "SWITCH"):
                    hasSwitchTemp = True
                    switchState = True

                    #numbers = [part for part in line[6].split('-') if part.isdigit()]
                    numbers = re.findall(r'\b(\d+)-(\d+)\b', line[6])
                    current = {num: False for pair in numbers for num in pair}
                    crossingTriples.append(list(current.keys()))
                    lightBlocks.update(current)

            tempBlock = Block(line[0],line[1],line[2],hasLightTemp,hasCrossingTemp,hasSwitchTemp,lightState,crossingState,switchState,blockId, line[5])
            totalBlocks.append(tempBlock)
            #Assign light values now

        for block in totalBlocks:
            if block.ID[1:] in lightBlocks:
                block.LIGHT = True
                block.lightState = False
            
            if block.lineColor == "Green" or block.lineColor == "Blue":
                if block.SWITCH == True:
                    block.LIGHT = False
                    block.lightState = None

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