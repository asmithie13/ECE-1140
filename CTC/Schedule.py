#File to aquire and hold schedule data
#Includes Schedule class
#Also includes a table model class for diplaying schedule on the CTC UI

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import csv

#Schedule class, holds schedule data and defines methods for editing the schedule
class Schedule():
    def __init__(self, ScheduleData = []):
        self.Scheduledata = ScheduleData

    #Function to add a single train to the schedule
    def addTrain(self, TrainID, Destination, ArrivalTime, Departure, DepartureTime):
        newTrain = [TrainID, Departure, DepartureTime, Destination, ArrivalTime]
        self.Scheduledata.append(newTrain)

    #function to parse a schedule file for automatic mode
    def parseScheduleFile(self, filepath):
        #print(filepath)
        
        if filepath:
            csv_file = open(filepath,"r")
            reader = csv.reader(csv_file)
            csv_file.close

        for row in reader:
            self.Scheduledata.append(row)



        
#Table class to initialize a Pyqt5 table object that will display the schedule
class ScheduleTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(ScheduleTableModel, self).__init__()
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
        headers = ['Train ID', 'Departure Station', 'Departure Time', 'Destination', 'Arrival Time']

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(headers[section])