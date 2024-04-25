from Train_Controller_SW.mainControl import Ui_MainWindow
from Train_Controller_SW.Line_Dictionary import Line_Dictionary

class NonVital():
    def __init__(self,ui, door_control_sig,announcement_sig,
    temp_control_sig,int_light_sig,ext_light_sig,internal_speed_lim_sig):
        self.block_index = 0
        self.ui=ui
        self.line = 0
        self.door_control_sig=door_control_sig
        self.announcement_sig=announcement_sig
        self.temp_control_sig=temp_control_sig
        self.int_light_sig=int_light_sig
        self.ext_light_sig=ext_light_sig
        self.speed_lim = internal_speed_lim_sig
        #inherited signalsd
        self.doors = 0
        self.LineDictionary = Line_Dictionary()
        self.station_index = 0


        

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


#         self.stationTimer.start()
#         self.stationTimer.timeout.connect(lambda: self.ui.buttonDoorL.toggle(), self.ui.buttonDoorR.toggle(), self.ui.IntLightSld.setValue(0), self.ui.announcement_sig.emit("Next stop is " + self.ui.lineEditAnn.text()))

    def Read_Beacon(self,beacon):
        print("receieved")
        if beacon == 1:
            self.line = 1
            self.ui.CurStatOut.setText(self.LineDictionary.green_station[0])
        elif beacon == 0:
            self.ui.CurStatOut.setText(self.LineDictionary.red_station[0])
            self.line = 0
        else:
            print("Error: Invalid Beacon")     

    def Set_Underground(self,underground):
        if underground == True:
            self.ui.undergrnd_ind.setStyleSheet("color: red;\n"
                                            "background-color: rgb(255, 255, 255);")
            self.ext_light_sig.emit(1)
        else:
            self.ui.undergrnd_ind.setStyleSheet("color: rgb(225, 225, 225);\n"
                                        "background-color: rgb(255, 255, 255);")
            self.ext_light_sig.emit(0)
                


    def Door(self):
        if(self.ui.buttonDoorR.isChecked() and self.ui.buttonDoorL.isChecked()):
            self.door_control_sig.emit(3) #ALL
        elif(self.ui.buttonDoorR.isChecked() and not(self.ui.buttonDoorL.isChecked())):
            self.door_control_sig.emit(1) # RIGHT
        elif(not(self.ui.buttonDoorR.isChecked()) and self.ui.buttonDoorL.isChecked()):
            self.door_control_sig.emit(2)  #LEFT
        else:
            self.door_control_sig.emit(0) #NONE

    def Emit_Doors(self):
        self.door_control_sig.emit(self.doors)
        if(self.doors == 0):
            self.ui.buttonDoorR.setChecked(False)
            self.ui.buttonDoorL.setChecked(False)
        elif(self.doors == 1):
            self.ui.buttonDoorR.setChecked(True)
            self.ui.buttonDoorL.setChecked(False)
        elif(self.doors == 2):
            self.ui.buttonDoorR.setChecked(False)
            self.ui.buttonDoorL.setChecked(True)
        elif(self.doors == 3):
            self.ui.buttonDoorR.setChecked(True)
            self.ui.buttonDoorL.setChecked(True)


    def Block_Changed(self,bool):
        #change index 
        self.ui.SpkrOut.setText("test")
        self.block_index = self.block_index + 1
        #green line parse
        if self.line ==  0 : #green 
            self.speed_lim.emit(self.LineDictionary.green_get_speed_lim(self.block_index))
            self.Set_Underground(self.LineDictionary.green_get_underground(self.block_index))
            self.announcement = self.LineDictionary.get_green_station(self.block_index)
            self.ui.SpkrOut.setText(self.announcement)
            self.arrived = False
            self.doors = self.LineDictionary.get_green_door_side(self.block_index)
            if len(self.announcement) > 0 and len(self.doors) > 0 :
                self.station_index += 1
                self.announcement_sig.emit(self.announcement)
                self.ui.CurStatOut.setText(self.LineDictionary.green_station[self.station_index])
                self.arrived = True
            elif len(self.announcement) > 0:
                self.announcement_sig.emit(self.announcement)
               
    
            
        #red line parse
        elif self.line == 1 :
            self.speed_lim.emit(self.LineDictionary.red_get_speed_lim(self.block_index))
            self.Set_Underground(self.LineDictionary.red_get_underground(self.block_index))
            self.announcement = self.LineDictionary.get_red_station(self.block_index)
            self.doors = self.LineDictionary.get_red_door_side(self.block_index)
            if len(self.announcement) > 0 and len(self.doors):
                self.announcement_sig.emit(self.announcement)
                self.ui.SpkrOut.setText(self.announcement)
                self.arrived = True
                self.doors = int(self.LineDictionary.get_red_door_side(self.block_index))
                self.int_light_sig.emit(1)
                self.ui.CurrStatOut.setText(self.LineDicitonary.red_station[self.station_index])
            elif len(self.announcement) :
                self.ui.SpkrOut.setText(self.announcement)
                self.announcement_sig.emit(self.announcement)
            else :
                self.int_light_sig.emit(0)
                self.doors = 0
                self.arrived = False
                self.ui.SpkrOut.setText("Heading to Next Station")

            


            

            
            
