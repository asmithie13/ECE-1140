import csv
from Wayside_SW.WaysideSWandTB import readTrackFile

class TempData:
    def __init__(self):
        self.RedStations = ["Shadyside", "Herron Ave", "Swissville",
                            "Peen Station", "Steel Plaza", "First Ave",
                            "Station Square", "South Hills Junction"]
        self.GreenStations = ["Pioneer", "Edgebrook", "Station", "Whited",
                              "South Bank", "Central", "Inglewood", "Overbrook",
                              "Glenbury", "Dormont", "Mt Lebonon", "Popular",
                              "Castle Shannon"]
        
        #Getting Green Block Info
        self.GreenBlocks = []
        self.GreenSwitches = []
        self.GreenBlockIDs = []

        self.GreenBlocks = readTrackFile("Wayside_SW/Green_Line.csv", self.GreenSwitches)
        print(self.GreenSwitches)

        
        for i in self.GreenBlocks:
            self.GreenBlockIDs.append(str(i.ID))

        
        #Repeating to get Red Block Info
        self.RedBlocks = []
        self.RedSwitches = []
        self.RedBlockIDs = []

        self.RedBlocks = readTrackFile("Wayside_SW/Red_Line.csv", self.RedSwitches)
        print(self.RedSwitches)

        
        for i in self.RedBlocks:
            self.RedBlockIDs.append(str(i.ID))        

        