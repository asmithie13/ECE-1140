from TrainController import *

class NonVital(TrainController):
    def __init__(self):
        self.stationTimer = QTimer()
        self.stationTimer.setInterval(1000)
        self.stationTimer.timeout.connect(self.updateTemperature)
    
    def Control_Temperature(self,temp):
        self.ui.lcdCurTemp.display(temp)
    
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