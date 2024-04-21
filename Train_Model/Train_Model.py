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
    track_model_acc_velo = qtc.pyqtSignal(str, int)
    stop_at_station_sig=qtc.pyqtSignal(bool)

    def __init__(self,TrainID):
        super().__init__()
        uic.loadUi("Train_Model/TrainModel_UI.ui", self)
        
        #self.main_window = main_window
        #this is added stuff for the TC
        self.TC = TrainController()
        self.TrainID = TrainID
        self.Train_ID_Label.setText(str(TrainID))

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

        #initalizing crew count
        self.ccount_display.setText(str(self.crew_count))

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
        # self.set_ccount(self.crew_count)
        # self.set_pcount(self.people_count)
        

    #function to set Power LCD
    def get_power_input(self, power_input):
        self.Power_value_lcd.display(int(power_input)) #watts 

    #sending authority to train controller 
    def receiveSpeedAuth_tm(self,speedAuth):
        trainID=speedAuth[0]
        self.comm_speed=speedAuth[1]
        #self.comm_speed=self.train_calculations.get_commanded_speed(float(self.comm_speed),self.grade,self.mass)
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
        ##self.stop_bool=stop_bool
        #self.get_ticket_sales()
        self.people_disemb()

        #send to ahn? 
        
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

    def set_height(self, height):
        self.height_display.setText(height)

    def set_width(self, width):
        self.width_display.setText(width)

    def set_grade(self, grade):
        self.grade=grade
        self.grade_display.setText(str(grade))

    def set_announcements(self, ann_text):
        self.ann_out_label.setText(ann_text)

    def set_cabin_temp(self,cabin_temp):
       self.cabin_temp_value.setFixedSize(279, 98)
       self.cabin_temp_value.setText(cabin_temp+' F')
       self.TC.curr_temp_sig.emit(cabin_temp)

    #bf_enable_clicked
    def bf_clicked(self):
        if not self.brake_fail_state: #enable
            self.bf_enable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.bf_disable.setStyleSheet('background-color: rgb(233, 247, 255);')
            self.brake_fail_tb(True)
            self.brake_fail_state = True
        else : #disable
            self.bf_enable.setStyleSheet('background-color: rgb(233, 247, 255);')
            self.bf_disable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.brake_fail_tb(False)
            self.brake_fail_state = False
       

    # #brake_fail_tb
    # def brake_fail_tb(self,state):
       
    #     self.brake_fail_state = state
    #     if state:
    #         self.bf_enable.setStyleSheet('background-color: rgb(38, 207, 4);')
    #         self.bf_disable.setStyleSheet('')
    #         self.ebrake_state=True
    #         self.ebrake_disabled(self.ebrake_state)
    #     else:
    #         self.bf_enable.setStyleSheet('')
    #         self.bf_disable.setStyleSheet('background-color: rgb(38, 207, 4);')
    #         self.ebrake_state=False
    #         self.ebrake_disabled(self.ebrake_state)

    #     self.TC.brk_fail_sig.emit(state)

     #sig_fail_enable_clicked


    def sig_fail_clicked(self):
        if not self.sig_fail_state: #enable 
            self.sig_fail_enable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.sig_fail_disable.setStyleSheet('background-color: rgb(233, 247, 255);')
            self.signal_fail_tb(True)
            self.sig_fail_state = True
        else : #disable
            self.sig_fail_enable.setStyleSheet('background-color: rgb(233, 247, 255);')
            self.sig_fail_disable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.signal_fail_tb(False)
            self.sig_fail_state = False

    # #signal_fail_tb
    # def signal_fail_tb(self,state):
       
    #     self.sig_fail_state = state
    #     if state:
    #         self.sig_fail_enable.setStyleSheet('background-color: rgb(38, 207, 4);')
    #         self.sig_fail_disable.setStyleSheet('')
    #     else:
    #         self.sig_fail_enable.setStyleSheet('')
    #         self.sig_fail_disable.setStyleSheet('background-color: rgb(38, 207, 4);')

    #     self.TC.sig_fail_sig.emit(state)

     #sig_fail_enable_clicked



    def en_fail_enable_clicked(self):
        if not self.en_fail_state: #enabled
            self.en_fail_enable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.en_fail_disable.setStyleSheet('background-color: rgb(233, 247, 255);')
            self.engine_fail_tb(True)
            self.en_fail_state = True
        else : #disabled
            self.en_fail_enable.setStyleSheet('background-color: rgb(233, 247, 255);')
            self.en_fail_disable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.engine_fail_tb(False)
            self.en_fail_state = False


    # #engine_fail_tb
    # def engine_fail_tb(self,state):
       
    #     self.en_fail_state = state
    #     if state:
    #         self.en_fail_enable.setStyleSheet('background-color: rgb(38, 207, 4);')
    #         self.en_fail_disable.setStyleSheet('')
    #     else:
    #         self.en_fail_enable.setStyleSheet('')
    #         self.en_fail_disable.setStyleSheet('background-color: rgb(38, 207, 4);')

    #     self.TC.pwr_fail_sig.emit(state)


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


    # #sending acc/velocity to track model
    # def acc_vel_to_track_model(self,velocity):
    #     #velocity=self.train_calculations.calculate_acc_velocity
    #     self.track_model_acc_velo.emit(int(self.velocity))

    #random generation for people disembarking
    def people_disemb(self):
        self.people_getting_off=random.randint(1,self.people_count)
        self.people_count=self.total_cap-self.people_getting_off
        self.total_cap= self.people_count + self.crew_count
        self.pcount_display.setText(str(self.people_count))
        
        

     ## unused    
    def get_ticket_sales(self,ticket_sales):
        self.people_count= self.people_count + ticket_sales 
        self.total_cap= self.people_count + self.crew_count
        self.pcount_display.setText(str(self.people_count))



    def door_status(self, door_state):
        self.door_state=door_state
        if door_state==3:
            self.right_doors_value.setFixedSize(109, 98)
            self.left_doors_value.setFixedSize(109, 98)
            self.right_doors_value.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.left_doors_value.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.right_doors_value.setText('CLOSED')
            self.left_doors_value.setText('CLOSED')
        elif door_state==2:
            self.right_doors_value.setFixedSize(109, 98)
            self.left_doors_value.setFixedSize(109, 98)
            self.right_doors_value.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.left_doors_value.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.right_doors_value.setText('OPEN')
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
            self.left_doors_value.setText('OPEN')


        
    