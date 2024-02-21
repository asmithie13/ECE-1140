#File to aquire and hold schedule data
#Includes Schedule class
#Also includes a table model class for diplaing schedule on the CTC UI

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

#Schedule class, holds schedule data and defines methods for editing the schedule
class Schedule():
    def __init__(self, ScheduleData = []):
        #Dummy schedule data for testing
        self.Scheduledata = ScheduleData

    def addTrain(self, TrainID, Destination, ArrivalTime, Departure, DepartureTime):
        newTrain = [TrainID, Departure, DepartureTime, Destination, ArrivalTime]
        self.Scheduledata.append(newTrain)


        
#Table class to initialize a Pyqt5 table object that will display the schedule
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        if(len(self._data) > 0):
            return len(self._data[0])
        else:
            return 0
    
    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        headers = ['Train ID', 'Departure Station', 'Departure Time', 'Destination', 'Arrival Time']

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(headers[section])
