import sys
#Fixing file hierarchy issues
import os
import re
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
import math
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5 import QtGui as qtg
from PyQt5.QtCore import Qt
from Train_Model.clock_test import Clock
from Train_Controller_SW.TrainController import TrainController
import subprocess


class TrainModel_mainwindow(QMainWindow):
    
    #in mph
    comm_speed= 0
    
    train_base=90169.07 #in lbs

    mass= 0 #in kgs

    prev_vel=0
    a_n=0
    prev_time=0
    prev_acc=0
    cabin_temp=0
    grade=0
    force=0
    velocity=0
    door_state=3
    brake_state=0
    ebrake_state=0
    people_count=0
    crew_count=2
    total_cap=people_count+crew_count
    people_getting_off=10
    stop_bool= False
    #Track Model Signals
    stop_at_station_sig = qtc.pyqtSignal(bool)
    track_model_acc_velo = qtc.pyqtSignal(str, float)
    people_disemb_sig=qtc.pyqtSignal(int)

    def __init__(self,TrainID):
        super().__init__()
        uic.loadUi("Train_Model/TrainModel_UI.ui", self)
        
        #self.main_window = main_window
        #this is added stuff for the TC
        self.TC = TrainController()
        self.TrainID = TrainID
        self.Set_Train_ID(TrainID)

        # Instantiate TrainCalculations and pass self (MyMainWindow instance) as an argument
        self.train_calculations = TrainCalculations(self,TC=self.TC)
        #CLOCK
        self.clock = Clock()
        self.clock.current_time_changed.connect(self.update_time)
        #self.people_disemb(self.people_count)

        #Connecting TC signals to Train Model
        self.TC.int_light_sig.connect(self.interior_lights)    
        self.TC.ext_light_sig.connect(self.exterior_lights)
        self.TC.curr_power_sig.connect(self.get_power_input)
        self.TC.announcement_sig.connect(self.set_announcements)
        self.TC.temp_control_sig.connect(self.set_cabin_temp)
        self.TC.service_brake_sig.connect(self.train_calculations.get_service_brake)
        self.TC.door_control_sig.connect(self.door_status)
        self.TC.ebrake_disable_sig.connect(self.ebrake_disabled)  
        self.TC.stop_at_station_sig.connect(self.stop_at_station)      
        

        
        #changing state when sig_fail_enable/disable are clicked
        self.sig_fail_enable.clicked.connect(self.sig_fail_enable_clicked)
        self.sig_fail_disable.clicked.connect(self.sig_fail_disable_clicked) 

        #changing state when bf_enable/disable are clicked
        self.bf_enable.clicked.connect(self.bf_enable_clicked)
        self.bf_disable.clicked.connect(self.bf_disable_clicked)

        #changing state when en_fail_enable/disable are clicked
        self.en_fail_enable.clicked.connect(self.en_fail_enable_clicked)
        self.en_fail_disable.clicked.connect(self.en_fail_disable_clicked)
        #self.brake_fail_input_tb.stateChanged.connect(self.brake_fail_tb)

        
        #ebrake signals
        self.ebrake.setCheckable(True)
        self.ebrake.clicked.connect(lambda: self.ebrake_disabled(self.ebrake.isChecked()))

       
        
        #Initially setting the default colors
        self.bf_enable.setStyleSheet('background-color: rgb(233, 247, 255);')
        self.bf_disable.setStyleSheet('background-color: rgb(38, 207, 4);')
        self.sig_fail_enable.setStyleSheet('background-color: rgb(233, 247, 255);')
        self.sig_fail_disable.setStyleSheet('background-color: rgb(38, 207, 4);')
        self.en_fail_enable.setStyleSheet('background-color: rgb(233, 247, 255);')
        self.en_fail_disable.setStyleSheet('background-color: rgb(38, 207, 4);')

        #Initialising failure states
        self.brake_fail_state = False
        self.sig_fail_state = False
        self.en_fail_state = False
        self.emergency_stop_state=False

    def Set_Train_ID(self,TrainID):
        self.Train_ID=TrainID
        self.Train_ID_Label.setText(str(TrainID))


    def Return_TrainController(self):
        return self.TC

    #CLOCK
    def update_time(self, current_time):
        self.TC.time_sig.emit(current_time)
        parts = current_time.split(':')
        hours, minutes = int(parts[0]), int(parts[1])
        seconds, ms = map(int, parts[2].split('.'))
        total_ms = hours*3600000 + minutes*60000 + seconds*1000 + ms
        self.train_calculations.set_time(total_ms)
        
        self.mass=self.train_calculations.get_mass(self.comm_speed,self.grade,self.mass)
        self.train_calculations.calculate_force(self.comm_speed,self.grade,self.mass)
        self.train_calculations.Calculate_acceleration(self.comm_speed,self.grade,self.mass)
        self.train_calculations.calculate_acc_velocity(self.comm_speed,self.grade,self.mass)
        
        self.set_ccount(self.crew_count)
        self.set_pcount(self.people_count)
        
        
        
        
    #function to set Power LCD
    def get_power_input(self, power_input):
        self.Power_value_lcd.display(int(power_input)) #watts 
        # self.train_calculations.Calculate_acceleration(self.comm_speed,self.grade, self.mass)
        # self.train_calculations.calculate_force(self.comm_speed,self.grade,self.mass)
        return power_input

    #sending authority to train controller 
    def receiveSpeedAuth_tm(self,speedAuth):
        trainID=speedAuth[0]
        self.comm_speed=speedAuth[1]
        self.comm_speed=self.train_calculations.get_commanded_speed(float(self.comm_speed),self.grade,self.mass)
        Authority=speedAuth[2]
        self.TC.curr_auth_sig.emit(float(Authority))
        if trainID == self.TrainID:
            self.comm_speed=speedAuth[1]
            self.train_calculations.get_commanded_speed(float(self.comm_speed),self.grade,self.mass)
            Authority=speedAuth[2]
            self.TC.curr_auth_sig.emit(float(Authority))
            

    #sending beacon_info_sig to Train Controller
    def receive_beacon_info(self,beacon_info):
        self.TC.beacon_info_sig.emit(beacon_info)

    #sending polarity to Train Controller
    def receive_polarity(self,polarity):
        self.TC.block_passed_sig.emit(polarity)
    
    def stop_at_station(self,stop_bool):
        self.stop_bool=stop_bool
        self.stop_at_station_sig.emit(stop_bool)
        
        

    def ebrake_disabled(self, ebrake_state):
        self.ebrake_state = ebrake_state
    
        # If ebrake is enabled
        if self.ebrake_state:
            if self.ebrake.setChecked(True):
                self.TC.ebrake_sig.emit(1)  # Emit the ebrake signal with value 1
            else:
                self.ebrake.setChecked(True)  # Set the ebrake button to checked (ON)
            self.ebrake.setEnabled(False)  # Disable the ebrake button

        else:

            self.ebrake.setEnabled(True)  # Enable the ebrake button
            self.ebrake.setChecked(False)  # Set the ebrake button to unchecked (OFF)
            
  
    def set_length(self, input_txt):
        self.length_of_vehicle_display.setText(input_txt)

    def set_pcount(self, people_count):
        self.people_count=people_count
        self.pcount_display.setText(str(self.people_count))

    def set_ccount(self, crew_count):
        self.ccount_display.setText(str(self.crew_count))

    def set_height(self, height):
        self.height_display.setText(height)

    def set_width(self, width):
        self.width_display.setText(width)

    def set_grade(self, grade):
        self.grade=grade
        self.grade_display.setText(str(grade))



    def get_train_selection(self,seltext):
        self.Train_dropdown.setCurrentText(seltext)
      

    def set_announcements(self, ann_text):
        self.ann_out_label.setText(ann_text)

    def set_cabin_temp(self,cabin_temp):
       self.cabin_temp=cabin_temp
       self.cabin_temp_value.setFixedSize(279, 98)
       self.cabin_temp_value.setText(self.cabin_temp+' F')

       self.TC.curr_temp_sig.emit(cabin_temp)

    #bf_enable_clicked
    def bf_enable_clicked(self):
        if not self.brake_fail_state:
            self.bf_enable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.bf_disable.setStyleSheet('background-color: rgb(233, 247, 255);')
            self.brake_fail_tb(True)
            self.brake_fail_state = True

    #bf_disable_clicked
    def bf_disable_clicked(self):
        if self.brake_fail_state:
            self.bf_enable.setStyleSheet('background-color: rgb(233, 247, 255);')
            self.bf_disable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.brake_fail_tb(False)
            self.brake_fail_state = False
       
    #brake_fail_tb
    def brake_fail_tb(self,state):
       
        self.brake_fail_state = state
        if state:
            self.bf_enable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.bf_disable.setStyleSheet('')
            self.ebrake_state=True
            self.ebrake_disabled(self.ebrake_state)
        else:
            self.bf_enable.setStyleSheet('')
            self.bf_disable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.ebrake_state=False
            self.ebrake_disabled(self.ebrake_state)

        self.TC.brk_fail_sig.emit(state)

     #sig_fail_enable_clicked
    def sig_fail_enable_clicked(self):
        if not self.sig_fail_state:
            self.sig_fail_enable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.sig_fail_disable.setStyleSheet('background-color: rgb(233, 247, 255);')
            self.signal_fail_tb(True)
            self.sig_fail_state = True

    #sig_fail_disable_clicked
    def sig_fail_disable_clicked(self):
        if self.sig_fail_state:
            self.sig_fail_enable.setStyleSheet('background-color: rgb(233, 247, 255);')
            self.sig_fail_disable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.signal_fail_tb(False)
            self.sig_fail_state = False

    #signal_fail_tb
    def signal_fail_tb(self,state):
       
        self.sig_fail_state = state
        if state:
            self.sig_fail_enable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.sig_fail_disable.setStyleSheet('')
        else:
            self.sig_fail_enable.setStyleSheet('')
            self.sig_fail_disable.setStyleSheet('background-color: rgb(38, 207, 4);')

        self.TC.sig_fail_sig.emit(state)

     #sig_fail_enable_clicked
    def en_fail_enable_clicked(self):
        if not self.en_fail_state:
            self.en_fail_enable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.en_fail_disable.setStyleSheet('background-color: rgb(233, 247, 255);')
            self.engine_fail_tb(True)
            self.en_fail_state = True

    #en_fail_disable_clicked
    def en_fail_disable_clicked(self):
        if self.en_fail_state:
            self.en_fail_enable.setStyleSheet('background-color: rgb(233, 247, 255);')
            self.en_fail_disable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.engine_fail_tb(False)
            self.en_fail_state = False

    #engine_fail_tb
    def engine_fail_tb(self,state):
       
        self.en_fail_state = state
        if state:
            self.en_fail_enable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.en_fail_disable.setStyleSheet('')
        else:
            self.en_fail_enable.setStyleSheet('')
            self.en_fail_disable.setStyleSheet('background-color: rgb(38, 207, 4);')

        self.TC.pwr_fail_sig.emit(state)
    #SETTING INTERIOR LIGHTS TO ON/DIM/OFF STATUS
    def interior_lights(self,state):
        if state==0:
            self.int_lights_value.setFixedSize(109, 98)
            self.int_lights_value.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.int_lights_value.setText('OFF')

        elif state==1:
            self.int_lights_value.setFixedSize(109, 98)
            self.int_lights_value.setText('ON')
        elif state==2:
            self.int_lights_value.setFixedSize(109, 98)
            self.int_lights_value.setText('DIM')

    #SETTING EXTERIOR LIGHTS TO ON/DIM/OFF STATUS
    def exterior_lights(self,state):
        if state==0:
            self.ext_lights_value.setFixedSize(109, 97)
            self.ext_lights_value.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.ext_lights_value.setText('OFF')

        elif state==1:
            self.ext_lights_value.setFixedSize(109, 97)
            self.ext_lights_value.setText('ON')



    #sending acc/velocity to track model
    def acc_vel_to_track_model(self,velocity):
        velocity=self.train_calculations.calculate_acc_velocity
        self.track_model_acc_velo.emit(int(velocity))

    #random generation for people disembarking
    def people_disemb(self, people_count):
        self.people_getting_off=random.randint(1,people_count)
        self.people_count=self.total_cap-self.people_getting_off
        self.total_cap= self.people_count + self.crew_count
        self.people_disemb_sig.emit(self.people_getting_off)
        
    
    def get_ticket_sales(self, tick_sales):
        self.people_count= tick_sales
        self.total_cap= self.people_count + self.crew_count

    def door_status(self, door_state):
        self.door_state=door_state
        if door_state==3:
            self.right_doors_value.setFixedSize(109, 98)
            self.left_doors_value.setFixedSize(109, 98)
            self.right_doors_value.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.left_doors_value.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.right_doors_value.setText('OPEN')
            self.left_doors_value.setText('OPEN')
        elif door_state==2:
            self.right_doors_value.setFixedSize(109, 98)
            self.left_doors_value.setFixedSize(109, 98)
            self.right_doors_value.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.left_doors_value.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.right_doors_value.setText('CLOSED')
            self.left_doors_value.setText('OPEN')
        elif door_state==1:
            self.right_doors_value.setFixedSize(109, 98)
            self.left_doors_value.setFixedSize(109, 98)
            self.right_doors_value.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.left_doors_value.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.right_doors_value.setText('OPEN')
            self.left_doors_value.setText('CLOSED')
        elif door_state==0:
            self.right_doors_value.setFixedSize(109, 98)
            self.left_doors_value.setFixedSize(109, 98)
            self.right_doors_value.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.left_doors_value.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.right_doors_value.setText('CLOSED')
            self.left_doors_value.setText('CLOSED')


        
    
    




#CLASS CONTAINING ALL TRAIN CALCULATIONS
class TrainCalculations:

    def __init__(self, main_window,TC):

        self.train_model_time =0
        self.main_window = main_window
        self.TC = TC
        commanded_speed=main_window.comm_speed
        mass=main_window.mass #in lbs
        grade=main_window.grade
        #print("mass1", mass)

    def get_service_brake(self,brake):
            self.main_window.brake_state=brake
        

    def set_time(self,time_calc):
        self.train_model_time=time_calc

    def get_time(self):
        return self.train_model_time
    
    def get_power(self, power_input):
        self.main_window.get_power_input(power_input)

    def get_commanded_speed(self, commanded_speed, grade, mass):
        self.mass=mass
        self.commanded_speed=commanded_speed/1.609  #converting kph to mph
        self.TC.curr_cmd_spd_sig.emit(int(self.commanded_speed))
        self.grade=grade
        self.main_window.cspeed_display.setText("{:.2f}".format(self.commanded_speed))
        self.commanded_speed=self.commanded_speed/2.237 #mph to meter/sec
        return(self.commanded_speed) #in m/sec
        # self.get_mass(self.commanded_speed,grade,mass)
        # self.calculate_force(self.commanded_speed,grade,mass)
        # self.Calculate_acceleration(self.commanded_speed,grade, mass)
        # self.calculate_acc_velocity(self.commanded_speed,grade,mass)
        

    def get_mass(self, commanded_speed, grade, mass):
        #avg mass of a person = 80 kgs
        self.mass=mass
        self.mass=(self.main_window.total_cap*80*2.205+self.main_window.train_base) #in pounds
        round(self.mass,2)
        self.commanded_speed=commanded_speed
        self.grade=grade
        self.main_window.mass_display.setText("{:.2f}".format(self.mass))
        self.mass=self.mass/2.205 #lbs to kgs
        return self.mass
        # self.calculate_force(self.commanded_speed,self.grade, self.mass)
        # self.Calculate_acceleration(self.commanded_speed,self.grade, self.mass)
        # self.calculate_acc_velocity(self.commanded_speed,self.grade, self.mass)

    def calculate_force(self,commanded_speed,grade,mass):
        #FORMULA: FORCE= MASS*g*SIN(THETA)
        #GRADE=SIN(THETA)
        self.mass=mass #in kgs
        self.commanded_speed=commanded_speed #in meters/sec
        self.grade=grade
        self.g=9.81 #m/sec^2
        #self.force=self.main_window.force
       
       
    
        theta=math.atan(grade/100)
        self.grav_force=mass*9.81*math.sin(theta)
        power = self.main_window.Power_value_lcd.value()#in watts
        try:
            self.main_window.force = (power / self.main_window.velocity) - self.grav_force 
        except ZeroDivisionError:
            self.main_window.velocity=0.1
            self.main_window.force = (power / self.main_window.velocity) - self.grav_force 

    
    
        return self.main_window.force

    def Calculate_acceleration(self,commanded_speed,grade,mass):
        self.mass=mass #in kg
        self.commanded_speed=commanded_speed #in m/s
        self.grade=grade
        #force = self.calculate_force(self.commanded_speed,self.grade,mass) #in kgm/s^2
        
        acceleration = float((self.main_window.force/self.mass)*3.281) #in ft/s^2
            #acceleration=round(acceleration,3)

        # if self.main_window.brake_state==1:
        #     acceleration=-3.9370078740157477 #in ft/s^2
        
        # if self.main_window.ebrake_state==1:
        #     acceleration=-8.956692913385826 #in ft/s^2

        self.main_window.Acceleration_value_lcd.display("{:.3f}".format(acceleration))
        return acceleration

    # def get_acceleration(self,commanded_speed,grade,mass):
    #     self.mass=mass
    #     self.commanded_speed=commanded_speed
    #     self.grade=grade
    #     acceleration = self.Calculate_acceleration(commanded_speed,grade,mass)
    #     self.main_window.Acceleration_value_lcd.display(acceleration)


    def calculate_acc_velocity(self,commanded_speed,grade,mass):
        self.mass=mass
        self.commanded_speed=commanded_speed
        self.grade=grade
        #converting acceleration to mph^2
        self.a_n_prev=self.main_window.a_n
        self.main_window.a_n = self.Calculate_acceleration(self.commanded_speed,self.grade,self.mass) #in ft/s^2

        train_model_time=self.get_time()
        
        #converting sec to hours
        train_model_time_sec=train_model_time/(1000)  #in seconds
        self.main_window.velocity = self.main_window.prev_vel + ((train_model_time_sec-self.main_window.prev_time)/2)*(self.main_window.a_n + self.a_n_prev)
        if self.main_window.velocity>0:
            if self.main_window.ebrake_state==1:
                #('ebrake state entered')
                self.main_window.a_n=-8.956692913385826 #in ft/s^2
                self.main_window.velocity = self.main_window.prev_vel + ((train_model_time_sec-self.main_window.prev_time)/2)*(self.main_window.a_n)
                self.main_window.Acceleration_value_lcd.display("{:.3f}".format(self.main_window.a_n))
                                    

            elif self.main_window.brake_state==1:
                #print('service brakes entered')
                self.main_window.a_n=-3.9370078740157477 #in ft/s^2
                self.main_window.velocity = self.main_window.prev_vel + ((train_model_time_sec-self.main_window.prev_time)/2)*(self.main_window.a_n)
                self.main_window.Acceleration_value_lcd.display("{:.3f}".format(self.main_window.a_n))
                if self.main_window.velocity<0.1:
                    self.main_window.velocity=0
            
        self.main_window.prev_vel=self.main_window.velocity
       

        if self.main_window.velocity <= 0:
            acceleration=0
            self.main_window.velocity=0
            self.main_window.prev_vel=0
            
  
        self.main_window.prev_time=train_model_time_sec

        # if self.main_windowprev_acc==0:
        #     self.main_window.Acc_Velo_value_lcd.display(self.main_window.)
        #     self.TC.curr_spd_sig.emit(int(self.main_window.velocity))
        #     self.main_window.track_model_acc_velo.emit(int(self.main_window.velocity))
        #
        # self.main_window.comm_speed=self.main_window.velocity

        #ft/sec to mph
        self.velocity_mph=(self.main_window.velocity)/1.467



        self.main_window.Acc_Velo_value_lcd.display("{:.2f}".format(self.velocity_mph))
        self.TC.curr_spd_sig.emit(float(self.velocity_mph))
        self.main_window.track_model_acc_velo.emit(str(self.main_window.TrainID), self.velocity_mph)
        
        return (self.main_window.velocity)
        



        

class trainmodel_testbench(QMainWindow):
                          
    #initializing all signals that the testbench is gonna be sending to the main window
    power_input_signal = qtc.pyqtSignal(float)
    commanded_speed_input_signal=qtc.pyqtSignal(float)
    mass_input_signal=qtc.pyqtSignal(float)
    announcement_input_signal=qtc.pyqtSignal(str)
    train_sel_signal=qtc.pyqtSignal(str)
    length_input_signal=qtc.pyqtSignal(str)
    height_input_signal=qtc.pyqtSignal(str)
    width_input_signal=qtc.pyqtSignal(str)
    pcount_input_signal=qtc.pyqtSignal(str)
    ccount_input_signal=qtc.pyqtSignal(str)
    grade_input_signal=qtc.pyqtSignal(str)
    ebrake_input_signal=qtc.pyqtSignal(int)
    brake_fail_input_signal=qtc.pyqtSignal(int)
    signal_fail_input_signal=qtc.pyqtSignal(int)
    engine_fail_input_signal=qtc.pyqtSignal(int)
    right_doors_input_signal=qtc.pyqtSignal(int)
    left_doors_input_signal=qtc.pyqtSignal(int)
    int_lights_input_signal=qtc.pyqtSignal(int)
    ext_lights_input_signal=qtc.pyqtSignal(int)
    cabin_temp_input_signal=qtc.pyqtSignal(str)


    def __init__(self,TC):
        super().__init__()

        #self.TC = TC

        uic.loadUi("Train_Model/TrainModel_testbench.ui", self)

       


        #TC.service_brake_sig.connect(self.)
        # self.TC.curr_power_sig.connect(self.receive_power)
        
        #TC.door_control_sig.connect(self.
        # self.TC.announcement_sig.connect(self.get_announcement)
        # self.TC.temp_control_sig.connect(self.get_cabin_temp)
        # self.TC.int_light_sig.connect(self.interior_lights_tb)    
        # self.TC.ext_light_sig.connect(self.exterior_lights_tb)
        # self.TC.ebrake_disable_sig.connect(self.emit_ebrake_state)
        
        self.train_sel_combo_tb.activated[str].connect(self.get_train_selection)

        self.power_input_tb.returnPressed.connect(self.receive_power)
        self.power_input_tb.returnPressed.connect(self.display_power)

        self.mass_input_tb.returnPressed.connect(self.get_mass)
        self.mass_input_tb.returnPressed.connect(self.display_mass)

        self.commanded_speed_input_tb.returnPressed.connect(self.get_commanded_speed)

        #self.announcement_input_tb.returnPressed.connect(self.get_announcement)
        self.announcement_input_tb.returnPressed.connect(self.display_announcement)

        self.length_of_vehicle_input_tb.returnPressed.connect(self.get_length)
        self.length_of_vehicle_input_tb.returnPressed.connect(self.display_length)

        self.height_input_tb.returnPressed.connect(self.get_height)
        self.height_input_tb.returnPressed.connect(self.display_height)

        self.width_input_tb.returnPressed.connect(self.get_width)
        self.width_input_tb.returnPressed.connect(self.display_width)

        self.grade_input_tb.returnPressed.connect(self.get_grade)
        self.grade_input_tb.returnPressed.connect(self.display_grade)

        self.passenger_count_input_tb.returnPressed.connect(self.get_pcount)
        self.passenger_count_input_tb.returnPressed.connect(self.display_pcount)

        self.crew_count_input_tb.returnPressed.connect(self.get_ccount)
        self.crew_count_input_tb.returnPressed.connect(self.display_ccount)

        self.estop_input_label.stateChanged.connect(self.emit_ebrake_state)

        self.brake_fail_input_tb.stateChanged.connect(self.brake_fail)
        self.sig_pick_input_tb.stateChanged.connect(self.sig_pick_fail)
        self.engine_fail_input_tb.stateChanged.connect(self.en_fail)

       # self.cabin_temp_input_tb.returnPressed.connect(self.get_cabin_temp)
        self.cabin_temp_input_tb.returnPressed.connect(self.display_cabin_temp)

       # self.int_lights_input_tb.returnPressed.connect(self.interior_lights_tb)
      
    #self.ext_lights_input_tb.returnPressed.connect(self.exterior_lights_tb)
       
        self.right_doors_input_tb.returnPressed.connect(self.right_doors_tb)
        
        self.left_doors_input_tb.returnPressed.connect(self.left_doors_tb)

        

    def interior_lights_tb(self):
        state=self.int_lights_input_tb.text()
        self.int_lights_input_signal.emit(state)


    def exterior_lights_tb(self):
        state=self.ext_lights_input_tb.text()
        self.ext_lights_input_signal.emit(state)
        

    def right_doors_tb(self):
        state=int(self.right_doors_input_tb.text())
        self.right_doors_input_signal.emit(state)

    def left_doors_tb(self):
        state=int(self.left_doors_input_tb.text())
        self.left_doors_input_signal.emit(state)

    def en_fail(self,state):
        self.engine_fail_input_signal.emit(state)


    def sig_pick_fail(self,state):
        self.signal_fail_input_signal.emit(state)
      

    def brake_fail(self,state):
       self.brake_fail_input_signal.emit(state)

        
    def get_cabin_temp(self):
        cabin_temp=str(self.cabin_temp_input_tb.text())
        self.cabin_temp_input_signal.emit(str(cabin_temp))

    def display_cabin_temp(self):
        cabin_temp= self.cabin_temp_input_tb.text()
        self.cabin_temp_output_tb.setText(cabin_temp)


    def emit_ebrake_state(self,state):
        self.ebrake_input_signal.emit(state)

    def ebrake_state(self):
        return self.estop_input_label.isChecked()
    

    def get_ccount(self):
        ccount_input=self.crew_count_input_tb.text()
        self.ccount_input_signal.emit(ccount_input)

    def display_ccount(self):
        ccount_display= self.crew_count_input_tb.text()
        self.crew_count_output_tb.setText(ccount_display)


    def get_pcount(self):
        pcount_input=self.passenger_count_input_tb.text()
        self.pcount_input_signal.emit(pcount_input)

    def display_pcount(self):
        pcount_display= self.passenger_count_input_tb.text()
        self.passenger_count_output_tb.setText(pcount_display)

    def get_grade(self):
        grade_input=self.grade_input_tb.text()
        self.grade_input_signal.emit(grade_input)

    
    def display_grade(self):
        grade_display= self.grade_input_tb.text()
        self.grade_output_tb.setText(grade_display+" %")


    def get_train_selection(self, text):
        selected_text = text
        self.train_sel_output_tb.setText(selected_text)
        self.train_sel_signal.emit(selected_text)

    def get_length(self):
        length_input=self.length_of_vehicle_input_tb.text()
        self.length_input_signal.emit(length_input)

    def display_length(self):
        length_display= self.length_of_vehicle_input_tb.text()
        self.length_of_vehicle_output_tb.setText(length_display+" ft")

    def get_height(self):
        height_input=self.height_input_tb.text()
        self.height_input_signal.emit(height_input)
    
    def display_height(self):
        height_display= self.height_input_tb.text()
        self.height_output_tb.setText(height_display+" ft")

    def get_width(self):
        width_input=self.width_input_tb.text()
        self.width_input_signal.emit(width_input)

    def display_width(self):
        width_display= self.width_input_tb.text()
        self.width_output_tb.setText(width_display+" ft")

    
    def receive_power(self):
        power_input=float(self.power_input_tb.text())
        self.power_input_signal.emit(power_input)

    def display_power(self):
        power_display=self.power_input_tb.text()
        self.power_output_tb.setText(power_display+" W")

    def get_commanded_speed(self):
        commanded_speed=float(self.commanded_speed_input_tb.text())
        self.commanded_speed_input_signal.emit(commanded_speed)

    def display_mass(self):
        mass_display= self.mass_input_tb.text()
        self.mass_vehicle_output_tb.setText(mass_display+" Lbs")

    def get_mass(self):
        mass=float(self.mass_input_tb.text())
        self.mass_input_signal.emit(mass)

    def get_announcement(self):
        ann_text=self.announcement_input_tb.text()
        self.announcement_input_signal.emit(ann_text)
    
    def display_announcement(self):
        ann_text= self.announcement_input_tb.text()
        self.announcements_output_tb.setText(ann_text)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    app.setStyle("windows")
    
    #add functionality to take in Train Controller Varible
    window = TrainModel_mainwindow(1)
    TC = window.Return_TrainController()
  
    window.show()
    sys.exit(app.exec_())

