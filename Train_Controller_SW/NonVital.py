from Train_Controller_SW.mainControl import Ui_MainWindow
class NonVital():
    def __init__(self,ui, door_control_sig,announcement_sig,
    temp_control_sig,int_light_sig,ext_light_sig,internal_speed_lim_sig):
        
        self.block_index = 0
        self.ui=ui
        self.line
        self.door_control_sig=door_control_sig
        self.announcement_sig=announcement_sig
        self.temp_control_sig=temp_control_sig
        self.int_light_sig=int_light_sig
        self.ext_light_sig=ext_light_sig
        self.speed_lim = internal_speed_lim_sig
        #inherited signalsd

        self.blocksTraveledCounter = 0
        self.blocksToUnderground = 0
        self.undergroundBlocks = 0
        self.dist_next_station= 0
    
    def Control_Headlights_On(self):
            self.ui.buttonHDoff.toggle()
            self.ext_light_sig.emit(1)

    def Control_Headlights_Off(self):
            self.ui.buttonHDon.toggle()
            self.ext_light_sig.emit(0)

    def Control_Name_Next_Station(self,string):
        self.ui.CurStatOut.setText(string)

    def Control_Dist_Next_Station(self,dist):
        self.dist_next_station = dist

    def Cabin_Temperature(self,cabinTemp):
        self.ui.temp.setValue(cabinTemp)
    
    def Control_interiorLights(self):

        if(self.ui.IntLightSld.value() == 1):
            self.int_light_sig.emit(1)
            print("interior lights on")
        elif(self.ui.IntLightSld.value() == 0):
            self.int_light_sig.emit(0)
            print("interior lights off")
        elif(self.ui.IntLightSld.value() == 2):
            self.int_light_sig.emit(2)
            print("interior lights dimmed")


    #might not need this function, may be able to connect directly
   # def Control_Temperature(self):
    
    def LeftStation(self):
        #open Left doors
        #send announcement
        #turn on int lights
        #wait 60 seconds
        #close left doors
        #turn off int lights
        #send announcement to next station

        self.ui.buttonDoorL.toggle()
        self.door_control_sig.emit(2)
        self.announcement_sig.emit("Welcome to " + self.ui.lineEditAnn.text())

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
        self.door_control_sig.emit(1)
        self.ui.SpkrOut.setText("Welcome to " + self.ui.lineEditAnn.text())
        self.announcement_sig.emit("Welcome to " + self.ui.lineEditAnn.text())
        self.ui.IntLightSld.setValue(1)
        self.int_light_sig.emit(1)
        self.stationTimer.start()

        #need to fix this  --- needs to include emit signals
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
        self.door_control_sig.emit(2)
        self.ui.announcement_sig.emit("Welcome to " + self.ui.lineEditAnn.text())
        self.ui.IntLightSld.setValue(1)
        self.stationTimer.start()
        self.stationTimer.timeout.connect(lambda: self.ui.buttonDoorL.toggle(), self.ui.buttonDoorR.toggle(), self.ui.IntLightSld.setValue(0), self.ui.announcement_sig.emit("Next stop is " + self.ui.lineEditAnn.text()))

    def Read_Beacon(self,beacon):
        self.line = beacon     

    def Set_Underground(self,underground):
        if underground == True:
            self.ui.undergrnd_ind.setStyleSheet("color: red;\n"
                                            "background-color: rgb(255, 255, 255);")
            self.ext_light_sig.emit(1)
        else:
            self.ui.undergrnd_ind.setStyleSheet("color: rgb(225, 225, 225);\n"
                                        "background-color: rgb(255, 255, 255);")
            self.int_light_sig.emit(0)
                


    def Door(self):
        if(self.ui.buttonDoorR.isChecked() and self.ui.buttonDoorL.isChecked()):
            self.door_control_sig.emit(3) #check these
        elif(self.ui.buttonDoorR.isChecked() and not(self.ui.buttonDoorL.isChecked())):
            self.door_control_sig.emit(1) #check these
        elif(not(self.ui.buttonDoorR.isChecked()) and self.ui.buttonDoorL.isChecked()):
            self.door_control_sig.emit(2)  #check these
        else:
            self.door_control_sig.emit(0)



    def Block_Changed(self,bool):
        #change index 
        self.block_index += 1
        #green line parse
        if self.line == "green" :
            self.speed_lim.emit(self.LineDictionary.green_get_speed_lim(self.block_index))
            self.Set_Underground(self.self.Line_Dictionary.green_get_underground(self.block_index))
            
        #red line parse
        elif self.line == "red" :
            self.ext_light_sig.emit(self.Line_Dictionary.green_get_underground(self.block_index))
            self.speed_lim.emit(self.LineDictionary.green_get_speed_lim(self.block_index))

            


            

            
            
