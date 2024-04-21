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






#CLASS CONTAINING ALL TRAIN CALCULATIONS
class TrainCalculations:

    def __init__(self, main_window,TC):
        self.main_window = main_window
        self.TC = TC
        
        #commanded_speed=main_window.comm_speed
        mass=main_window.mass #in lbs
        grade=main_window.grade

    # def get_service_brake(self,brake):
    #         self.main_window.brake_state=brake
        
    # def set_time(self,time_calc):
    #     self.train_model_time=time_calc

    # def get_time(self):
    #     return self.train_model_time
    
    # def get_power(self, power_input):
    #     self.main_window.get_power_input(power_input)

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


    def calculate_velcoity(self,grade,mass):
        self.mass=mass #in kgs
        self.grade=grade
        theta=math.atan(grade/100)
        self.grav_force=mass*9.81*math.sin(theta)
        power = self.main_window.Power_value_lcd.value()#in watts
        try:
            self.main_window.force = (power / self.main_window.velocity) - self.grav_force 
        except ZeroDivisionError:
            if(not self.main_window.service_brake): 
                forceCalc = self.FRICTION_COEFFICIENT * (trainMass) * self.GRAVITY * math.cos(slopeAngle) + 1000
                e)
            else:
                self.main_window.force = 0

    
    











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
            
        self.main_window.prev_vel=self.main_window.velocity
        self.main_window.prev_time=train_model_time_sec

        if self.main_window.velocity <= 0:
            acceleration=0
            self.main_window.prev_vel=0   
        

        # if self.main_windowprev_acc==0:
        #     self.main_window.Acc_Velo_value_lcd.display(self.main_window.)
        #     self.TC.curr_spd_sig.emit(int(self.main_window.velocity))
        #     self.main_window.track_model_acc_velo.emit(int(self.main_window.velocity))
        #
        # self.main_window.comm_speed=self.main_window.velocity

        #ft/sec to mph
        self.velocity_mph=(self.main_window.velocity)/1.467



        self.main_window.Acc_Velo_value_lcd.display("{:.3f}".format(self.velocity_mph))
        self.TC.curr_spd_sig.emit(float(self.velocity_mph))
        self.main_window.track_model_acc_velo.emit(str(self.main_window.TrainID),float(self.velocity_mph))
        
        return (self.main_window.velocity)
        
