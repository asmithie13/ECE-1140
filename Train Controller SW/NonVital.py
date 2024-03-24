from mainControl import Ui_MainWindow
class NonVital():
    def __init__(self,ui):
        self.ui=ui


        self.blocksTraveledCounter = 0
        self.blocksToUnderground = 0
        self.undergroundBlocks = 0
        self.dist_next_station= 0;
    
    def Control_Headlights(self):

        if(self.ui.buttonHDon.isChecked()):
            self.ui.buttonHDoff.setChecked(False)
            #emit(1)
        if(self.ui.buttonHDoff.isChecked()):
            self.ui.buttonHDon.setChecked(False)
            #emit(0)

    def Control_Name_Next_Station(self,string):
        self.ui.CurStatOut.setText(string)

    def Control_Dist_Next_Station(self,dist):
        self.dist_next_station = dist

    def Cabin_Temperature(self,cabinTemp):
        self.ui.temp.setValue(cabinTemp)
    
    #i want to change the int lights to a toggle button like the others
    def Control_interiorLights(self):

        if(self.ui.IntLightSld.value() == 1):
            #emit(1)
            print("interior lights on")
        if(self.ui.IntLightSld.value() == 0):
            #emit(0)
            print("interior lights off")

        # after converstion to toggle button
        # if(self.ui.buttonILon.isChecked()):
        #     self.ui.buttonILoff.setChecked(False)
        #     #emit(1)
        # if(self.ui.buttonILoff.isChecked()):
        #     self.ui.buttonILon.setChecked(False)
        #     #emit(0)

    def Control_Temperature(self, desiredTemp):
        #emit(desiredTemp)
        print("Temperature set to " + str(desiredTemp) + " degrees")

    
    def LeftStation(self):
        #open Left doors
        #send announcement
        #turn on int lights
        #wait 60 seconds
        #close left doors
        #turn off int lights
        #send announcement to next station

        self.ui.buttonDoorL.toggle()
        self.ui.announcement_sig.emit("Welcome to " + self.ui.lineEditAnn.text())
        self.ui.IntLightSld.setValue(1)
        self.stationTimer.start()
        self.stationTimer.timeout.connect(lambda: self.ui.buttonDoorL.toggle(), self.ui.IntLightSld.setValue(0), self.ui.announcement_sig.emit("Next stop is " + self.ui.lineEditAnn.text()))

    def RightStation(self):
        #open Right doors
        #send announcement
        #turn on int lights
        #wait 60 seconds
        #close right doors
        #turn off int lights
        #send announcement to next station

        self.ui.buttonDoorR.toggle()
        self.ui.announcement_sig.emit("Welcome to " + self.ui.lineEditAnn.text())
        self.ui.IntLightSld.setValue(1)
        self.stationTimer.start()
        self.stationTimer.timeout.connect(lambda: self.ui.buttonDoorR.toggle(), self.ui.IntLightSld.setValue(0), self.ui.announcement_sig.emit("Next stop is " + self.ui.lineEditAnn.text()))

    def BothStation(self):
        #open both doors
        #send announcement
        #turn on int lights
        #wait 60 seconds
        #close both doors
        #turn off int lights
        #send announcement to next station

        self.ui.buttonDoorL.toggle()
        self.ui.buttonDoorR.toggle()
        self.ui.announcement_sig.emit("Welcome to " + self.ui.lineEditAnn.text())
        self.ui.IntLightSld.setValue(1)
        self.stationTimer.start()
        self.stationTimer.timeout.connect(lambda: self.ui.buttonDoorL.toggle(), self.ui.buttonDoorR.toggle(), self.ui.IntLightSld.setValue(0), self.ui.announcement_sig.emit("Next stop is " + self.ui.lineEditAnn.text()))

    def Read_Beacon(self):
        #take in beacon info from tanvi
        #call station function depending on beacon info
        print("beacon info")
        
    
    def Control_Underground(self):
        #calc distance from beacon to underground block using d=rt
        #when distance traveled is equal to distance to underground block, turn on beacan indicator
        #this logic should work but if we go in and out of underground multiple times without passing a beacon, it will not work
        
        #enter underground -  we turn on the lights before going under because of safety :)
        if self.blocksTraveledCounter == self.blocksToUnderground-1:
            self.ui.underground.setChecked(True)
            self.ui.buttonHDon.setChecked(True)
            self.ui.buttonHDoff.setChecked(False)
            self.blocksTraveledCounter = 0
        
        #when underground
        """
        if self.ui.underground.isChecked():
            if self.blocksTraveledCounter == self.undergroudBlocks+1:
                self.ui.underground.setChecked(False)
                self.ui.buttonHDon.setChecked(False)
                self.ui.buttonHDoff.setChecked(True)
                self.blocksTraveledCounter = 0
        """
    
    
    def BlockCounter(self):
        self.blocksTraveledCounter += 1
        self.Control_Underground()


            

            
            
