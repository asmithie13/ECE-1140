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

    def addBlockOccupancy(self, TrainName, BlockNum):
        newBlockOccupancy = [TrainName, BlockNum]
        self.BlockDataNew.append(newBlockOccupancy)

    def matchOccupanciesToTrains(self, BlockID, line):
        BlockNum = int(BlockID[1:])

        if (BlockNum == 63) and (line == 'green'):
            for i in self.currentTrains:
                if i[1] == 'K63':
                    return i[0]
        elif (BlockNum == 10) and (line == 'red'):
            for i in self.currentTrains:
                if i[1] == 'K63':
                    return i[0]
        elif (line == 'green') and (BlockNum > 63) and (BlockNum < 100):
            for i in self.currentTrains:
                if int(i[1][1:]) == (BlockNum - 1):
                    #Update Train Movement
                    return i[0]

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