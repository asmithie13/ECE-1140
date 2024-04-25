import csv
#Wayside has a file parser to pull out special blocks for maintenance mode
from Wayside_SW.WaysideSWandTB import readTrackFile

class TempData:
    def __init__(self):
        #Getting Green Block Info
        self.GreenBlocks = []
        self.GreenSwitches = []
        self.GreenBlockIDs = []
        self.GreenBlocks = readTrackFile("Wayside_SW/Green_Line.csv", self.GreenSwitches)
        
        for i in self.GreenBlocks:
            self.GreenBlockIDs.append(str(i.ID))

        self.GreenSwitches[0] = ['D13', 'C12', 'A1']
        self.GreenSwitches[1] = ['F28', 'G29', 'Z150']
        self.GreenSwitches[2] = ['N77', 'M76', 'R101']
        self.GreenSwitches[3] = ['N85', 'O86', 'Q100']


        
        #Repeating to get Red Block Info
        self.RedBlocks = []
        self.RedSwitches = []
        self.RedBlockIDs = []
        self.RedBlocks = readTrackFile("Wayside_SW/Red_Line.csv", self.RedSwitches)
        
        for i in self.RedBlocks:
            self.RedBlockIDs.append(str(i.ID))     

        self.RedSwitches[0] = ['E15', 'F16', 'A1']
        self.RedSwitches[1] = ['H27', 'H28', 'T76']
        self.RedSwitches[2] = ['H32', 'H33', 'R72']
        self.RedSwitches[3] = ['H38', 'H39', 'Q71']
        self.RedSwitches[4] = ['H43', 'H44', 'O67']
        self.RedSwitches[5] = ['J52', 'J53', 'N66']


        #Get Green Line Route Info
        self.GreenStations = []
        self.GreenRouteInfo = []
        csv_file = open("CTC/RouteGreenLine.csv","r")
        GreenRouteReader = csv.reader(csv_file)
        headers = next(GreenRouteReader)    #Skip Header Row
        csv_file.close

        for row in GreenRouteReader:
            self.GreenStations.append(row[0])
            self.GreenRouteInfo.append(row)

        #Repeat to get Red Line Route Info
        self.RedStations = []
        self.RedRouteInfo = []
        csv_file = open("CTC/RouteRedLine.csv","r")
        RedRouteReader = csv.reader(csv_file)
        headers = next(RedRouteReader)    #Skip Header Row
        csv_file.close

        for row in RedRouteReader:
            self.RedStations.append(row[0])
            self.RedRouteInfo.append(row)
        