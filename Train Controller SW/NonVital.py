from mainControl import Ui_MainWindow
class NonVital():
    def __init__(self,ui):
        self.ui=ui


        self.blocksTraveledCounter = 0
        self.blocksToUnderground = 0
        self.undergroundBlocks = 0
    
    def Control_Headlights(self):

        if(self.ui.buttonHDon.isChecked()):
            self.ui.buttonHDoff.setChecked(False)
            #emit(1)
        if(TrainController.ui.buttonHDoff.isChecked()):
            TrainController.ui.buttonHDon.setChecked(False)
            #emit(0)
    
    
    #i want to change the int lights to a toggle button like the others
    def Control_interiorLights(self):

        if(TrainController.ui.IntLightSld.value() == 1):
            #emit(1)
            print("interior lights on")
        if(TrainController.ui.IntLightSld.value() == 0):
            #emit(0)
            print("interior lights off")

        # after converstion to toggle button
        # if(TrainController.ui.buttonILon.isChecked()):
        #     TrainController.ui.buttonILoff.setChecked(False)
        #     #emit(1)
        # if(TrainController.ui.buttonILoff.isChecked()):
        #     TrainController.ui.buttonILon.setChecked(False)
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

        TrainController.ui.buttonDoorL.toggle()
        TrainController.ui.announcement_sig.emit("Welcome to " + self.ui.lineEditAnn.text())
        TrainController.ui.IntLightSld.setValue(1)
        TrainController.stationTimer.start()
        TrainController.stationTimer.timeout.connect(lambda: self.ui.buttonDoorL.toggle(), self.ui.IntLightSld.setValue(0), self.ui.announcement_sig.emit("Next stop is " + self.ui.lineEditAnn.text()))

    def RightStation(self):
        #open Right doors
        #send announcement
        #turn on int lights
        #wait 60 seconds
        #close right doors
        #turn off int lights
        #send announcement to next station

        TrainController.ui.buttonDoorR.toggle()
        TrainController.ui.announcement_sig.emit("Welcome to " + self.ui.lineEditAnn.text())
        TrainController.ui.IntLightSld.setValue(1)
        TrainController.stationTimer.start()
        TrainController.stationTimer.timeout.connect(lambda: self.ui.buttonDoorR.toggle(), self.ui.IntLightSld.setValue(0), self.ui.announcement_sig.emit("Next stop is " + self.ui.lineEditAnn.text()))

    def BothStation(self):
        #open both doors
        #send announcement
        #turn on int lights
        #wait 60 seconds
        #close both doors
        #turn off int lights
        #send announcement to next station

        TrainController.ui.buttonDoorL.toggle()
        TrainController.ui.buttonDoorR.toggle()
        TrainController.ui.announcement_sig.emit("Welcome to " + self.ui.lineEditAnn.text())
        TrainController.ui.IntLightSld.setValue(1)
        TrainController.stationTimer.start()
        TrainController.stationTimer.timeout.connect(lambda: self.ui.buttonDoorL.toggle(), self.ui.buttonDoorR.toggle(), self.ui.IntLightSld.setValue(0), self.ui.announcement_sig.emit("Next stop is " + self.ui.lineEditAnn.text()))

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
            TrainController.ui.underground.setChecked(True)
            TrainController.ui.buttonHDon.setChecked(True)
            TrainController.ui.buttonHDoff.setChecked(False)
            self.blocksTraveledCounter = 0
        
        #when underground
        if TrainController.ui.underground.isChecked():
            if self.blocksTraveledCounter == self.undergroudBlocks+1:
                TrainController.ui.underground.setChecked(False)
                TrainController.ui.buttonHDon.setChecked(False)
                TrainController.ui.buttonHDoff.setChecked(True)
                self.blocksTraveledCounter = 0
    
    
    def BlockCounter(self):
        self.blocksTraveledCounter += 1
        self.Control_Underground()

            

            
            
