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

        self.GreenBlocks = readTrackFile("Wayside_SW/Green_Line.csv", [])

        
        for i in self.GreenBlocks:
            if i.SWITCH:
                self.GreenSwitches.append(i.ID)
            
            self.GreenBlockIDs.append(str(i.ID))
        
        #Repeating to get Red Block Info
        self.RedBlocks = []
        self.RedSwitches = []
        self.RedBlockIDs = []

        self.RedBlocks = readTrackFile("Wayside_SW/Red_Line.csv", [])

        
        for i in self.RedBlocks:
            if i.SWITCH:
                self.RedSwitches.append(i.ID)
            
            self.RedBlockIDs.append(str(i.ID))        

        