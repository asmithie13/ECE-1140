#File to aquire and hold schedule data
#Includes Schedule class
#Also includes a table model class for diplaying schedule on the CTC UI

import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import csv
from CTC.TempData import *

#Schedule class, holds schedule data and defines methods for editing the schedule
class Schedule():
    def __init__(self):
        self.Scheduledata = []
        self.AuthorityInfo = []
        self.TrackData = TempData()
        self.TrainNames = ["*T1"]

    #Function to add a single train to the schedule
    def addTrain(self, line, TrainID, Destination, ArrivalTime, Departure, DepartureTime):
        newTrain = [line, TrainID, Destination, ArrivalTime, Departure, DepartureTime]
        self.Scheduledata.append(newTrain)

    #function to parse a schedule file for automatic mode
    def parseScheduleFile(self, filepath):
        #Parse file using csv library
        if filepath:
            csv_file = open(filepath,"r")
            reader = csv.reader(csv_file)
            headers = next(reader)      #Skip header row
            csv_file.close

        if len(headers) != 4:
            col_error = QMessageBox()
            col_error.setWindowTitle("Input Error")
            col_error.setText("Incorrect Number of Columns in Schedule File")
            col_error.setIcon(QMessageBox.Critical)

            col_error.exec_() 

            return 0

        #For each row besides the header row, calculate departure data and add to schedule
        for row in reader:
            #Check Color and departure station are valid
            if (row[0] == 'Green') or (row[0] == 'green'):
                line = 'Green'
                stationExists = False

                for station in self.TrackData.GreenStations:
                    if station == row[2]:
                        stationExists = True
                        break

            elif (row[0] == 'Red') or (row[0] == 'red'):
                line = 'Red'
                stationExists = False

                for station in self.TrackData.RedStations:
                    if station == row[2]:
                        stationExists = True
                        break
            else:
                #Line is not a valid color
                line_error = QMessageBox()
                line_error.setWindowTitle("Input Error")
                message = row[0] + " is not a valid line color. Please fix the schedule."
                line_error.setText(message)
                line_error.setIcon(QMessageBox.Critical)

                line_error.exec_() 

                return 0
            
            #Destintion is not valid
            if stationExists == False:
                station_error = QMessageBox()
                station_error.setWindowTitle("Input Error")
                message = row[2] + " is not a valid destination on " + line + " line. Please fix the schedule."
                station_error.setText(message)
                station_error.setIcon(QMessageBox.Critical)

                station_error.exec_()
                return 0

            DepartureData = []
            tempArrivalTime = QTime()   #Converting ArrivalTime to QTime for easier math
            self.calculateDeparture(row[2], tempArrivalTime.fromString(row[3]), DepartureData, line)
            #Adding departure Data to the row data
            row.append(DepartureData[0])
            row.append(DepartureData[1])
            #Adding to Schedule
            #Line, TrainID, Destination, Arrival Time, Departure Station, Departure Time
            self.Scheduledata.append(row)
                 
        return 1

    def calculateDeparture(self, Destination, ArrivalTime, Departure, line):
        #Setting Departure Station
        DepartureStation = "Yard"
        Departure.append(DepartureStation)

        #Calculating Departure Time
        TravelTime = 0
        Authority = 0

        if line == 'Green':
            for i in range(len(self.TrackData.GreenRouteInfo)):
                if self.TrackData.GreenRouteInfo[i][0] == DepartureStation:
                    for j in range(i + 1, len(self.TrackData.GreenRouteInfo)):
                        TravelTime += float(self.TrackData.GreenRouteInfo[j][1])
                        Authority += float(self.TrackData.GreenRouteInfo[j][2])

                        if self.TrackData.GreenRouteInfo[j][0] == Destination:
                            break
                    break
        elif line == 'Red':
            for i in range(len(self.TrackData.RedRouteInfo)):
                if self.TrackData.RedRouteInfo[i][0] == DepartureStation:
                    for j in range(i + 1, len(self.TrackData.RedRouteInfo)):
                        TravelTime += float(self.TrackData.RedRouteInfo[j][1])
                        Authority += float(self.TrackData.GreenRouteInfo[j][2])

                        if self.TrackData.RedRouteInfo[j][0] == Destination:
                            break

                    break

        DepartureTime = ArrivalTime.addSecs(int(-1 * 60 * TravelTime))
        DepartureTime = DepartureTime.toString("hh:mm")

        Departure.append(DepartureTime)

        self.AuthorityInfo.append(Authority)




        
#Table class to initialize a Pyqt5 table object that will display the schedule
class ScheduleTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(ScheduleTableModel, self).__init__()
        self._data = data

    #Displays the data to the table
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        
        if role == Qt.BackgroundRole and index.column() == 0 and self._data[index.row()][index.column()] == 'Green':
            # See below for the data structure.
            return QtGui.QColor('#26cf04')
        elif role == Qt.BackgroundRole and index.column() == 0 and self._data[index.row()][index.column()] == 'Red':
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
        headers = ['Line', 'Train ID', 'Destination', 'Arrival Time', 'Departure Station', 'Departure Time']

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(headers[section])
