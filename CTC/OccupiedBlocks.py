#File to aquire and hold block occupancy data
#Includes Class to manage that data
#Also includes a table model class for diplaying info on the CTC UI

import sys
from PyQt5 import QtCore, QtWidgets
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
        #Green line train dipatch case
        if (BlockNum == 63) and (line == 'Green'):
            for i in range(len(self.currentTrains)):
                if self.currentTrains[i][0] == 'K63':
                    return ("T" + str(i+1))
        #Red line train dispatch case        
        elif (BlockNum == 10) and (line == 'Red'):
            for i in range(len(self.currentTrains)):
                if self.currentTrains[i][0] == 'D10':
                    return ("T" + str(i+1))
        elif (line == 'Green') and (BlockNum > 63) and (BlockNum < 100):
            for i in range(len(self.currentTrains)):
                for j in self.currentTrains[i]:
                    if int(j[1:]) == (BlockNum - 1):
                        #Update Train Movement
                        return ("T" + str(i+1))

        return 'X'
    



#Table class to initialize a Pyqt5 table object that will display the list of block occupancies
class BlocksTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(BlocksTableModel, self).__init__()
        self._data = data

    #Displays the data to the table
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

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