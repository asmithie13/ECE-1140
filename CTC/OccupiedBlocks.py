#File to aquire and hold block occupancy data
#Includes Class to manage that data
#Also includes a table model class for diplaying info on the CTC UI

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

class OccupiedBlocks():
    def __init__(self, Blocks = []):
        #Dummy data for testing
        #Blocks = [['T1', 'B2'], ['T1', 'B1']]

        self.BlockData = Blocks

    def addBlockOccupancy(self, TrainName, BlockNum):
        newBlockOccupancy = [TrainName, BlockNum]
        self.BlockData.append(newBlockOccupancy)




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
        headers = ['Train', 'Block #']

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(headers[section])