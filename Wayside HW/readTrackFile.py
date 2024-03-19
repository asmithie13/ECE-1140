from Block import Block
import csv
import re

#Function that reads all blocks from a *.csv file and assigns block attributes:
def readTrackFile(fileName, crossingTriples):
    totalBlocks = []
    lightBlocks = {}
    #fileName = fileName
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
            elif(35 < i < 105):
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