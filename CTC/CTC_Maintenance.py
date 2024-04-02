#File to aquire and hold maintenance data
#Includes Class to manage that data
#Also includes a table model class for diplaying info on the CTC UI

import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

#Class to manage maintenece mode for CTC
class CTC_Maintenance():
    def __init__(self):
        self.BlocksClosed = []          #Block class object
        self.BlocksClosedIDs = []       #List of lists: Line, BlockID
        self.SwitchText = []            #Block class objects
        self.SwitchesSet = []           #List of lists: Line, Switch, Position

    def addBlockClosure(self, BlockID):
        newBlockClosure = [BlockID]
        self.BlockData.append(newBlockClosure)



#Table class to initialize a Pyqt5 table object that will display the Blocks that are shut down for maintenance
class ClosedBlocksTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(ClosedBlocksTableModel, self).__init__()
        self._data = data

    #Displays the data to the table
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        
        if role == Qt.BackgroundRole and index.column() == 1 and self._data[index.row()][index.column()] == 'Green':
            # See below for the data structure.
            return QtGui.QColor('#26cf04')
        elif role == Qt.BackgroundRole and index.column() == 1 and self._data[index.row()][index.column()] == 'Red':
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
        headers = ['Closed Blocks', 'Line']

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(headers[section])
            

#Table class to initialize a Pyqt5 table object that will display the switch positions set for maintenance
class SwitchPositionTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(SwitchPositionTableModel, self).__init__()
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
        headers = ['Switch', 'Position', 'line']

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(headers[section])