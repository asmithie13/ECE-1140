import csv
from Wayside_SW.WaysideSWandTB import readTrackFile

class TempData:
    def __init__(self):
        #Initializing Stations
        self.RedStations = []
        self.GreenStations = []
        #self.RedStations = ["Shadyside", "Herron Ave", "Swissville",
        #                    "Penn Station", "Steel Plaza", "First Ave",
        #                    "Station Square", "South Hills Junction"]
        #self.GreenStations = ["Pioneer", "Edgebrook", "Station", "Whited",
        #                      "South Bank", "Central", "Inglewood", "Overbrook",
        #                      "Glenbury", "Dormont", "Mt Lebonon", "Popular",
        #                      "Castle Shannon"]
        

        #Dispatch Info has Station, Time to Station, Distance to station from the station before it

        #Getting Green Block Info
        self.GreenBlocks = []
        self.GreenSwitches = []
        self.GreenBlockIDs = []

        self.GreenBlocks = readTrackFile("Wayside_SW/Green_Line.csv", self.GreenSwitches)

        
        for i in self.GreenBlocks:
            self.GreenBlockIDs.append(str(i.ID))

        
        #Repeating to get Red Block Info
        self.RedBlocks = []
        self.RedSwitches = []
        self.RedBlockIDs = []

        self.RedBlocks = readTrackFile("Wayside_SW/Red_Line.csv", self.RedSwitches)
        
        for i in self.RedBlocks:
            self.RedBlockIDs.append(str(i.ID))      


        #Get Green Line Route Info
        self.GreenRouteInfo = []
        csv_file = open("CTC/RouteGreenLine.csv","r")
        GreenRouteReader = csv.reader(csv_file)
        headers = next(GreenRouteReader)    #Skip Header Row
        csv_file.close

        for row in GreenRouteReader:
            self.GreenStations.append(row[0])
            self.GreenRouteInfo.append(row)

        #Repeat to get Red Line Route Info
        self.RedRouteInfo = []
        csv_file = open("CTC/RouteRedLine.csv","r")
        RedRouteReader = csv.reader(csv_file)
        headers = next(RedRouteReader)    #Skip Header Row
        csv_file.close

        for row in RedRouteReader:
            self.RedStations.append(row[0])
            self.RedRouteInfo.append(row)
        