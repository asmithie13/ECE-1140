#File to aquire and hold block occupancy data
#Includes Class to manage that data
#Also includes a table model class for diplaying info on the CTC UI

import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
#From other folders
from Track_Resources import *

#Class to hold the data and manage the occupied blocks
class OccupiedBlocks():
    def __init__(self):
        #Green 1, Green 2, Red 1, Red 2
        self.recievedFromWayside = []

        for i in range(4):
            self.recievedFromWayside.append([])

        #Holds train name and block num to display
        #Based on current occupied Blocks
        self.BlockDataCurrent = []
        self.BlockDataNew = []

        #Holds train and block num
        #Based on current Trains
        self.currentTrains = []
        self.newTrains = []

    def addBlockOccupancy(self, TrainName, BlockNum):
        newBlockOccupancy = [TrainName, BlockNum]
        self.BlockDataNew.append(newBlockOccupancy)

    def matchOccupanciesToTrains(self, BlockID, line):
        #Get block number from ID
        BlockNum = int(BlockID[1:])

        #Check to see if the block was occupied already
        for i in self.BlockDataCurrent:
            if i[1] == BlockID:
                return i[0]

        #Begin logic to see if the block is occupied by a train
        #Green Line
        if line == 'Green':
            #A-C blocks, train can only come from its previous blocks, but they are in reverse number order
            if (BlockNum >= 1) and (BlockNum <= 12):
                ID = self.searchPreviousBlockR(BlockNum)
                if ID != -1:
                    return ("T" + str(ID+1))

            #D13 switch block
            elif BlockNum == 13:
                for i in range(len(self.currentTrains)):
                    for j in self.currentTrains[i]:
                        if int(j[1:]) == 1:
                            return ("T" + str(i+1))
                        if int(j[1:]) == 12:
                            return ("T" + str(i+1))
                        if int(j[1:]) == 14:
                            return ("T" + str(i+1))
                            
            #D,E,F blocks (without the switches), bidirectional
            elif (BlockNum >= 14) and (BlockNum <= 27):
                ID = self.searchBothDirections(BlockNum)
                if ID != -1:
                    return ("T" + str(ID+1))

            #F28 switch block
            elif BlockNum == 28:
                for i in range(len(self.currentTrains)):
                    for j in self.currentTrains[i]:
                        if int(j[1:]) == 27:
                            return ("T" + str(i+1))
                        if int(j[1:]) == 150:
                            return ("T" + str(i+1))
                        
            #G-I blocks, train can only come from its previous blocks
            elif (BlockNum >= 29) and (BlockNum <= 57):
                ID = self.searchPreviousBlock(BlockNum)
                if ID != -1:
                    return ("T" + str(ID+1))
                        
            #J Blocks are the ones we skip near the yard
                        
            #Green line train dipatch case
            elif BlockNum == 63:
                #for each train
                for i in range(len(self.currentTrains)):
                    if len(self.currentTrains[i]) > 0:
                        #for each block the train occupies
                        if self.currentTrains[i][0] == 'K63':
                            #return the current train if conditions are meet
                            return ("T" + str(i+1))
                        
            #K-M blocks, train can only come from its previous blocks
            elif (BlockNum >= 64) and (BlockNum <= 76):
                ID = self.searchPreviousBlock(BlockNum)
                if ID != -1:
                    return ("T" + str(ID+1))
                        
            #Full n block, bidirectional
            elif (BlockNum >= 77) and (BlockNum <= 84):
                ID = self.searchBothDirections(BlockNum)
                if ID != -1:
                    return ("T" + str(ID+1))

            #n switch on block 85, can come from N84 or Q100
            elif BlockNum == 85:
                for i in range(len(self.currentTrains)):
                    for j in self.currentTrains[i]:
                        if int(j[1:]) == 84:
                            return ("T" + str(i+1))
                        elif int(j[1:]) == 100:
                            return ("T" + str(i+1))
                        
            #O-Q blocks, train can only come from its previous blocks        
            elif (BlockNum >= 86) and (BlockNum <= 100):
                ID = self.searchPreviousBlock(BlockNum)
                if ID != -1:
                    return ("T" + str(ID+1))

            #R101 block, comes from n track
            elif BlockNum == 101:
                for i in range(len(self.currentTrains)):
                    for j in self.currentTrains[i]:
                        if int(j[1:]) == 77:
                            return ("T" + str(i+1))            

            #S-Z blocks, train can only come from its previous blocks
            elif ((BlockNum >= 102) and (BlockNum <= 150)):
                ID = self.searchPreviousBlock(BlockNum)
                if ID != -1:
                    return ("T" + str(ID+1))             
            
        #Red Line                                  
        if line == "Red":
            #A1 switch
            if BlockNum == 1:
                for i in range(len(self.currentTrains)):
                    for j in self.currentTrains[i]:
                        if int(j[1:]) == 16:
                            return ("T" + str(i+1))

            #A-C Blocks
            elif (BlockNum > 1) and (BlockNum <= 9):
                ID = self.searchBothDirections(BlockNum)
                if ID != -1:
                    return ("T" + str(ID+1)) 
            
            #Red line train dispatch case  
            elif BlockNum == 10:
                for i in range(len(self.currentTrains)):
                    if len(self.currentTrains[i]) > 0:
                        if self.currentTrains[i][0] == 'D10':
                            return ("T" + str(i+1))
            
            #D-E blocks       
            elif (BlockNum > 10) and (BlockNum <= 15):
                ID = self.searchPreviousBlock(BlockNum)
                if ID != -1:
                    return ("T" + str(ID+1))

            #F-H to first switch blocks
            elif (BlockNum >= 16) and (BlockNum < 27):
                ID = self.searchBothDirections(BlockNum)
                if ID != -1:
                    return ("T" + str(ID+1)) 

            #First H switch on block 27
            elif BlockNum ==  27:
                for i in range(len(self.currentTrains)):
                    for j in self.currentTrains[i]:
                        if int(j[1:]) == 26:
                            return ("T" + str(i+1))
                        elif int(j[1:]) == 28:
                            return ("T" + str(i+1))
                        elif int(j[1:]) == 76:
                            return ("T" + str(i+1))
                        
            #H28-H31 to first switch blocks
            elif (BlockNum >= 28) and (BlockNum <= 31):
                ID = self.searchBothDirections(BlockNum)
                if ID != -1:
                    return ("T" + str(ID+1))       

            #Second H switch on block 32
            elif BlockNum ==  32:
                for i in range(len(self.currentTrains)):
                    for j in self.currentTrains[i]:
                        if int(j[1:]) == 31:
                            return ("T" + str(i+1))
                        elif int(j[1:]) == 33:
                            return ("T" + str(i+1))
                        elif int(j[1:]) == 72:
                            return ("T" + str(i+1))
                        
            #H33-H37 to first switch blocks
            elif (BlockNum >= 33) and (BlockNum <= 37):
                ID = self.searchBothDirections(BlockNum)
                if ID != -1:
                    return ("T" + str(ID+1))  

            #Third H switch on block 38
            elif BlockNum ==  38:
                for i in range(len(self.currentTrains)):
                    for j in self.currentTrains[i]:
                        if int(j[1:]) == 37:
                            return ("T" + str(i+1))
                        elif int(j[1:]) == 39:
                            return ("T" + str(i+1))
                        elif int(j[1:]) == 71:
                            return ("T" + str(i+1))
                            
            #H39-H42 to first switch blocks
            elif (BlockNum >= 39) and (BlockNum <= 42):
                ID = self.searchBothDirections(BlockNum)
                if ID != -1:
                    return ("T" + str(ID+1))  

            #Fourth H switch on block 43
            elif BlockNum ==  43:
                for i in range(len(self.currentTrains)):
                    for j in self.currentTrains[i]:
                        if int(j[1:]) == 42:
                            return ("T" + str(i+1))
                        elif int(j[1:]) == 44:
                            return ("T" + str(i+1))
                        elif int(j[1:]) == 67:
                            return ("T" + str(i+1))
                        
            #H44-J51
            elif (BlockNum >= 44) and (BlockNum <= 51):
                ID = self.searchBothDirections(BlockNum)
                if ID != -1:
                    return ("T" + str(ID+1)) 

            #J52 switch
            elif BlockNum ==  52:
                for i in range(len(self.currentTrains)):
                    for j in self.currentTrains[i]:
                        if int(j[1:]) == 51:
                            return ("T" + str(i+1))
                        elif int(j[1:]) == 53:
                            return ("T" + str(i+1))
                        elif int(j[1:]) == 66:
                            return ("T" + str(i+1))
                        
            #J53-N65
            elif (BlockNum >= 53) and (BlockNum <= 65):
                ID = self.searchBothDirections(BlockNum)
                if ID != -1:
                    return ("T" + str(ID+1)) 
                
            #N66
            elif BlockNum ==  66:
                for i in range(len(self.currentTrains)):
                    for j in self.currentTrains[i]:
                        if int(j[1:]) == 52:
                            return ("T" + str(i+1))
                        elif int(j[1:]) == 65:
                            return ("T" + str(i+1))

            #O67
            elif BlockNum ==  67:
                for i in range(len(self.currentTrains)):
                    for j in self.currentTrains[i]:
                        if int(j[1:]) == 43:
                            return ("T" + str(i+1))
                        elif int(j[1:]) == 68:
                            return ("T" + str(i+1))
            
            #P Blocks
            elif (BlockNum >= 68) and (BlockNum <= 70):
                ID = self.searchBothDirections(BlockNum)
                if ID != -1:
                    return ("T" + str(ID+1)) 
            
            #Q71
            elif BlockNum ==  71:
                for i in range(len(self.currentTrains)):
                    for j in self.currentTrains[i]:
                        if int(j[1:]) == 38:
                            return ("T" + str(i+1))
                        elif int(j[1:]) == 70:
                            return ("T" + str(i+1))

            #R72
            elif BlockNum ==  72:
                for i in range(len(self.currentTrains)):
                    for j in self.currentTrains[i]:
                        if int(j[1:]) == 32:
                            return ("T" + str(i+1))
                        elif int(j[1:]) == 73:
                            return ("T" + str(i+1))
            
            #S Blocks
            elif (BlockNum >= 73) and (BlockNum <= 75):
                ID = self.searchBothDirections(BlockNum)
                if ID != -1:
                    return ("T" + str(ID+1)) 
            
            #T76
            elif BlockNum ==  76:
                for i in range(len(self.currentTrains)):
                    for j in self.currentTrains[i]:
                        if int(j[1:]) == 75:
                            return ("T" + str(i+1))
                        elif int(j[1:]) == 27:
                            return ("T" + str(i+1))
        
        return 'X'

    #Internal function that searches if the current occupancy coresponds to train from a previous block
    def searchPreviousBlock(self, BlockNum):
        for i in range(len(self.currentTrains)):
            for j in self.currentTrains[i]:
                if int(j[1:]) == (BlockNum - 1):
                    return i
        
        return -1

    #Internal function that searches if the current occupancy coresponds to train from a previous block, in reverse order
    def searchPreviousBlockR(self, BlockNum):
        for i in range(len(self.currentTrains)):
            for j in self.currentTrains[i]:
                if int(j[1:]) == (BlockNum + 1):
                    return i
        
        return -1

    #Internal function that searches if the current occupancy coresponds to train from a previous block, iin both direction
    def searchBothDirections(self, BlockNum):
        for i in range(len(self.currentTrains)):
            for j in self.currentTrains[i]:
                if int(j[1:]) == (BlockNum - 1):
                    return i
                if int(j[1:]) == (BlockNum + 1):
                    return i
        
        return -1


#Table class to initialize a Pyqt5 table object that will display the list of block occupancies
class BlocksTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(BlocksTableModel, self).__init__()
        self._data = data

    #Displays the data to the table
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        
        if role == Qt.BackgroundRole and index.column() == 2 and self._data[index.row()][index.column()] == 'Green':
            # See below for the data structure.
            return QtGui.QColor('#26cf04')
        elif role == Qt.BackgroundRole and index.column() == 2 and self._data[index.row()][index.column()] == 'Red':
            return QtGui.QColor('#c31028')

    #Returns the row count of the table
    def rowCount(self, index):
        return len(self._data)

    #returns the column count of the table
    def columnCount(self, index):
        if(len(self._data) > 0):
            return len(self._data[0])
        else:
            return 0
    
    #Adds the column header with the correct data
    def headerData(self, section, orientation, role):
        headers = ['Train', 'Block #', 'Line']

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(headers[section])