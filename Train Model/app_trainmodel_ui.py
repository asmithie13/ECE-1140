import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5 import QtGui as qtg


class MyMainWindow(QMainWindow):
    
    #in mph
    commanded_speed_def=50
    #in lbs
    mass_def=125002.1
    #in seconds
    time_def=10

    def __init__(self):
        super().__init__()
        uic.loadUi("Train Model/TrainModel_UI.ui", self)
        self.Calculate_acceleration()
        self.calculate_force()
        self.get_acceleration()
        self.calculate_acc_velocity()

        self.estop_locked=False

        #changing state when bf_enable/disable are clicked
        self.bf_enable.clicked.connect(self.bf_enable_clicked)
        self.bf_disable.clicked.connect(self.bf_disable_clicked)
        #self.brake_fail_input_tb.stateChanged.connect(self.brake_fail_tb)

        #Initially setting the default colors
        self.bf_enable.setStyleSheet('background-color: rgb(233, 247, 255);')
        self.bf_disable.setStyleSheet('background-color: rgb(38, 207, 4);')

        self.brake_fail_state = False

    def estop_button_clicked(self):
        if not self.estop_locked:
            self.ebrake.setEnabled(False)
            self.ebrake.setStyleSheet('background-color: gray; color: white;')
            self.estop_locked = True

    def change_ebrake_color(self,ebrake_state):
        if ebrake_state:
            self.ebrake.setStyleSheet('background-color:  rgb(99, 99, 99);')
        
        else: 
            self.ebrake.setStyleSheet('background-color: rgb(195, 16, 40);')

    def set_length(self, input_txt):
        self.length_of_vehicle_display.setText(input_txt)

    def set_pcount(self, input_txt):
        self.pcount_display.setText(input_txt)

    def set_ccount(self, input_txt):
        self.ccount_display.setText(input_txt)

    def set_height(self, height):
        self.height_display.setText(height)

    def set_width(self, width):
        self.width_display.setText(width)

    def set_grade(self, grade):
        self.grade_display.setText(grade)


    def get_train_selection(self,seltext):
        self.Train_dropdown.setCurrentText(seltext)

    #function to set Power LCD
    def get_power(self, power_input):
        self.Power_value_lcd.display(power_input)
        self.Calculate_acceleration()
        self.calculate_force()
        #return power_input

    

    #function to calculate the acceleration in ft/s^2 using the power command
    def Calculate_acceleration(self):
       force=self.calculate_force() #newtons
       mass=self.mass_def
       #1m=3.28084ft
       acceleration = (force/mass)*((1/3.28084)*(1/3.28084))
       self.Acceleration_value_lcd.display(acceleration)
       return acceleration
    
    def get_acceleration(self):
        acceleration=self.Calculate_acceleration()
        self.Acceleration_value_lcd.display(acceleration)

    def get_commanded_speed(self,commanded_speed):
        self.commanded_speed_def=commanded_speed
        self.cspeed_display.setText(str(commanded_speed))
        self.calculate_force()
        self.Calculate_acceleration()
        self.calculate_acc_velocity()
       # return self.commanded_speed_def
        
    def calculate_force(self):
        power=1000*(self.Power_value_lcd.value())
        commanded_speed=self.commanded_speed_def
        #input commanded speed was in mph
        speed_fts=commanded_speed*(5280/3600) 
        #Using P=F*v so F= P/v
        force=power/speed_fts #in newtons
        return force
       
    
    def get_mass(self, mass):
        self.mass_display.setText(str(mass))
        #self.mass_display.setAlignment(Qt.AlignRight)
        mass=mass/2.205 #lbs to kgs
        self.mass_def=mass
        self.calculate_force()
        self.Calculate_acceleration()
        self.calculate_acc_velocity()
        
    def calculate_acc_velocity(self):
        #in ft/sec^2
        acceleration = (3600*3600/5280)*self.Calculate_acceleration()
        #in seconds
        time = self.time_def  
        initial_velocity = 0  
        velocity = initial_velocity + (acceleration * time)
        self.Acc_Velo_value_lcd.display(velocity)

    def set_announcements(self, ann_text):
        self.ann_out_label.setText(ann_text)

    def set_cabin_temp(self,cabin_temp):
       self.cabin_temp_value.setFixedSize(279, 98)
       self.cabin_temp_value.setText(cabin_temp+' F')

    #bf_enable_clicked
    def bf_enable_clicked(self):
        if not self.brake_fail_state:
            self.bf_enable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.bf_disable.setStyleSheet('background-color: rgb(233, 247, 255);')
            self.brake_fail_state = True

    #bf_disable_clicked
    def bf_disable_clicked(self):
        if self.brake_fail_state:
            self.bf_enable.setStyleSheet('background-color: rgb(233, 247, 255);')
            self.bf_disable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.brake_fail_state = False
       
    #brake_fail_tb
    def brake_fail_tb(self,state):
       
        self.brake_fail_state = state
        if state:
            self.bf_enable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.bf_disable.setStyleSheet('')
        else:
            self.bf_enable.setStyleSheet('')
            self.bf_disable.setStyleSheet('background-color: rgb(38, 207, 4);')

    #signal_fail_tb
    def signal_fail_tb(self,state):
       
        self.brake_fail_state = state
        if state:
            self.bf_enable.setStyleSheet('background-color: rgb(38, 207, 4);')
            self.bf_disable.setStyleSheet('')
        else:
            self.bf_enable.setStyleSheet('')
            self.bf_disable.setStyleSheet('background-color: rgb(38, 207, 4);')

    
        

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
    cabin_temp_input_signal=qtc.pyqtSignal(str)


    def __init__(self):
        super().__init__()
        uic.loadUi("Train Model/TrainModel_testbench.ui", self)
        self.train_sel_combo_tb.activated[str].connect(self.get_train_selection)

        self.power_input_tb.returnPressed.connect(self.receive_power)
        self.power_input_tb.returnPressed.connect(self.display_power)

        self.mass_input_tb.returnPressed.connect(self.get_mass)
        self.mass_input_tb.returnPressed.connect(self.display_mass)

        self.commanded_speed_input_tb.returnPressed.connect(self.get_commanded_speed)

        self.announcement_input_tb.returnPressed.connect(self.get_announcement)
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

        self.cabin_temp_input_tb.returnPressed.connect(self.get_cabin_temp)
        self.cabin_temp_input_tb.returnPressed.connect(self.display_cabin_temp)

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
    
    window = MyMainWindow()
    window_tb = trainmodel_testbench()

    # Connect the signal from MyMainWindow to trainmodel_testbench
    #sending power input signal from tb to main
    window_tb.power_input_signal.connect(window.get_power)
    #sending commanded speed from tb to main
    window_tb.commanded_speed_input_signal.connect(window.get_commanded_speed)
    #mass signal
    window_tb.mass_input_signal.connect(window.get_mass)
    #announcement signal
    window_tb.announcement_input_signal.connect(window.set_announcements)
    #train selection
    window_tb.train_sel_signal.connect(window.get_train_selection)
    #set length
    window_tb.length_input_signal.connect(window.set_length)
    #set height
    window_tb.height_input_signal.connect(window.set_height)
    #set width
    window_tb.width_input_signal.connect(window.set_width)
    #set grade
    window_tb.grade_input_signal.connect(window.set_grade)
    #set pcount
    window_tb.pcount_input_signal.connect(window.set_pcount)
    #set ccount
    window_tb.ccount_input_signal.connect(window.set_ccount)
    #set ebrake
    window_tb.ebrake_input_signal.connect(window.change_ebrake_color)
    #estop manual
    window.ebrake.clicked.connect(window.estop_button_clicked)
    #brake_fail
    window_tb.brake_fail_input_signal.connect(window.brake_fail_tb)
    #signal_fail
    window_tb.signal_fail_input_signal.connect(window.signal_fail_tb)
    #cabin_temp 
    window_tb.cabin_temp_input_signal.connect(window.set_cabin_temp)


    window.show()
    window_tb.show()
    sys.exit(app.exec_())
