import sys
import tkinter as tk
import os #read other .py file
import pandas as pd #read excel files
import random # Generate random num of ticket sales for CTC

# Using Block Class as a seperate file
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

# import libraries
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QComboBox, QHBoxLayout, QWidget, QLabel, QPushButton, QSizePolicy
from PyQt5 import uic
from PyQt5.QtCore import Qt  
from Track_Resources.Block import Block
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtGui as qtg

#My main window
class MyMainWindow(QMainWindow):
    # Define a signal to emit the grade to testBench UI
    grade_signal = pyqtSignal(float)

    def __init__(self):
        super().__init__()

        # Load the track model straight from the UI file using uic
        uic.loadUi("Track Model/Track_Model.ui", self)

        # Connect Upload Track Layout button to make upload file
        self.pushButton.clicked.connect(self.upload_track_layout) 

        # Generate a random number between 1 and 74 for ticket sales
        random_number = random.randint(1, 74)
        #Output the random numberto ticket sales block info
        self.ticket_out.setText(str(random_number))

        # Connect button to method
        # If clicked, then connect to UI
        self.offButton_1.clicked.connect(self.toggle_button_state)
        self.offButton_2.clicked.connect(self.toggle_button_state_2)
        self.offButton_3.clicked.connect(self.toggle_button_state_3)

        # Set default state for toggle button (default color should be red and "OFF") on all 3 buttons
        self.offButton_1.setText("OFF")
        self.offButton_1.setStyleSheet("background-color: red;")

        self.offButton_2.setText("OFF")
        self.offButton_2.setStyleSheet("background-color: red;")

        self.offButton_3.setText("OFF")
        self.offButton_3.setStyleSheet("background-color: red;")

        # Instantiate the Data class
        self.data = Data()

    #This function is a starter connector to UI from tb for ticket sales
    def update_ticket_sales(self, sales):
        # set new ticket sales
        self.ticket_sales =sales
        # update ticket sales display
        self.ticket_out.setText(str(self.ticket_sales))

    #This function is a starter connector to UI from tb for  block dropdown
    def update_main_dropdown(self, selected_text):
        # update the dropdown in your main UI 
        self.block_in_1.setCurrentText(selected_text)

    #This toggles the button of the failures
    def toggle_button_state(self):
        # Toggle button state and color button for broken rail
        if self.offButton_1.text() == "OFF":
            self.offButton_1.setText("ON")
            self.offButton_1.setStyleSheet("background-color: green;")
        else:
            self.offButton_1.setText("OFF")
            self.offButton_1.setStyleSheet("background-color: red;")
            
    def toggle_button_state_tb(self, bool1):
        # Toggle button state and color button for block broken rail but used from tb to main
        if bool1.lower() in ["yes", "true", "on", "1"]:
            self.offButton_1.setText("ON")
            self.offButton_1.setStyleSheet("background-color: green;")
        elif bool1.lower() in ["no", "false", "off", "0"]:
            self.offButton_1.setText("OFF")
            self.offButton_1.setStyleSheet("background-color: red;")

    def toggle_button_state_2(self):
        # Toggle button state and color button for track circuit failure
        if self.offButton_2.text() == "OFF":
            self.offButton_2.setText("ON")
            self.offButton_2.setStyleSheet("background-color: green;")
        else:
            self.offButton_2.setText("OFF")
            self.offButton_2.setStyleSheet("background-color: red;")

    def toggle_button_state_2_tb(self, bool1):
        # Toggle button state and color button for block track circuit failure but used from tb to main
        if bool1.lower() in ["yes", "true", "on", "1"]:
            self.offButton_2.setText("ON")
            self.offButton_2.setStyleSheet("background-color: green;")
        elif bool1.lower() in ["no", "false", "off", "0"]:
            self.offButton_2.setText("OFF")
            self.offButton_2.setStyleSheet("background-color: red;")

    def toggle_button_state_3(self):
        # toggle button state and color button for power failure
        if self.offButton_3.text() == "OFF":
            self.offButton_3.setText("ON")
            self.offButton_3.setStyleSheet("background-color: green;")
        else:
            self.offButton_3.setText("OFF")
            self.offButton_3.setStyleSheet("background-color: red;")

    def toggle_button_state_3_tb(self, bool1):
        # Toggle button state and color button for power_failure but used from tb to main
        if bool1.lower() in ["yes", "true", "on", "1"]:
            self.offButton_3.setText("ON")
            self.offButton_3.setStyleSheet("background-color: green;")
        elif bool1.lower() in ["no", "false", "off", "0"]:
            self.offButton_3.setText("OFF")
            self.offButton_3.setStyleSheet("background-color: red;")

    def toggle_light_state_tb(self, bool1):
            # Toggle the state and color of the light button
            if bool1.lower() == "green":
                self.light_out.setText("GREEN")
                self.light_out.setStyleSheet("background-color: green;")
            elif bool1.lower() == "red":
                self.light_out.setText("RED")
                self.light_out.setStyleSheet("background-color: red;")

    def toggle_cross_state_tb(self, bool1):
        # Toggle the state of the railway crossing
        if bool1.lower() == "up":
            self.cross_out.setText("UP")
        elif bool1.lower() == "down":
            self.cross_out.setText("DOWN")

    def toggle_switch_tb(self, status):
        # Toggle the switch status
        if status.lower() == "b6":
            self.switch_out.setText("B6")
        elif status.lower() == "b11":
            self.switch_out.setText("B11")

    # This function will upload track layout to main by either excel or csv form
    def upload_track_layout(self):
        file_dialog = QFileDialog()
        uploaded_track, _ = file_dialog.getOpenFileName(self, 'Upload Track Layout', '', 'Excel Files (*.xlsx);;CSV (*.csv)')
        if uploaded_track:
            # Instantiate the Data class and pull
            self.data = Data()
            
            # read data from the uploaded file using the Data class (pandas)
            self.data.read_excel(uploaded_track)

        # Connect the block selection dropdown to update_block_info function!
        self.block_in_1.activated[str].connect(lambda text: self.update_block_info(text))

    # This function uses the data from the data class to update block data and output it to main UI
    def update_block_info(self, block_text):

        # From dropdown of "B#" take out the letter B
        block_num = int(block_text.split()[-1][1:])  

        #Get certain data from specific block
        elevation_m = self.data.get_elevation_for_block(block_num)
        grade = self.data.get_grade_for_block(block_num)
        length1_m = self.data.get_length_for_block(block_num)
        block_num = self.data.get_block_for_block(block_num)
        section = self.data.get_section_for_block(block_num)
        speed_limit_km = self.data.get_speed_for_block(block_num)

        #Math conversion from metric to imperical for track length, speed limit, and elevation.
        elevation_ft = elevation_m *3.28084
        elevation_str = "{:.4f}".format(elevation_ft).rstrip('0').rstrip('.')

        length_ft = length1_m * 3.28084
        length_str = "{:.4f}".format(length_ft).rstrip('0').rstrip('.')

        speed_limit_ft = speed_limit_km / 1.609344 
        speed_limit_str = "{:.4f}".format(speed_limit_ft).rstrip('0').rstrip('.')

        # Update the labels with the block data and output it.
        self.elevation_in.setText(elevation_str)
        self.grade_in.setText(str(grade))
        self.length_in.setText(length_str)
        self.block_num_in.setText(str(block_num))
        self.section_in.setText(str(section))
        self.speed_in.setText(speed_limit_str)

        #Emit the grade signal with the grade value (sig)
        self.grade_signal.emit(grade)

#this is my testbench window
class TestBench(QMainWindow):
    #Change the signal to emit a string for buttons
    broken_rail_input_signal = pyqtSignal(str)
    track_input_signal = pyqtSignal(str)
    power_input_signal = pyqtSignal(str)
    power_input_signal = pyqtSignal(str) 
    light_input_signal = pyqtSignal(str)   
    switch_input_signal = pyqtSignal(str)
    cross_input_signal = pyqtSignal(str)

    # Change the signal to emit a string for dropdowns
    dropdown_broken_signal = pyqtSignal(str)  
    dropdown_track_signal = pyqtSignal(str) 

    # Change signal to emit an int for ticket sales
    ticket_sales_signal = pyqtSignal(int)
    
    def __init__(self):
        super().__init__()

        # Load the track model testbench straight from the UI file using uic
        uic.loadUi("Track Model/testbench_trackmodel.ui", self)

        # Calling test input functions
        self.test_input()
        self.test_input_2()
        self.test_input_3()

        # Press enter should show output for test outputs when inputting values
        self.com_speed_in_1.returnPressed.connect(self.test_input)
        self.authority_in.returnPressed.connect(self.test_input)
        self.broken_in.returnPressed.connect(self.test_input)
        self.track_in.returnPressed.connect(self.test_input_2)
        self.power_in.returnPressed.connect(self.test_input_3)
        self.light_in.returnPressed.connect(self.test_input)
        self.ticket_in.returnPressed.connect(self.test_input)
        self.rail_in.returnPressed.connect(self.test_input)
        self.switch_in.returnPressed.connect(self.test_input)

        #Enter text through QTCombo from dropdown and output that to testbench
        self.line_in.activated[str].connect(self.test_combo_line)
        self.broken_block.activated[str].connect(self.test_combo_broken)

        #Connect the activated signal for te dropdown to emit the selected block text
        self.broken_block.activated[str].connect(self.test_combo_broken_tb)

    # Define a slot to update the grade label, this is for emitting signals from main to tb
    def update_grade_label(self, grade):
        # Update the grade_out label with the received grade
        self.grade_out.setText(str(grade))

    #Function for inputs/outputs for textboxes
    def test_input(self):
        # Get text from the test inputs for broken rail
        broken = self.broken_in.text()
        # Set the output text for broken rail
        self.broken_out.setText(broken)

        # Emit the signal with the input text for broken rail
        self.broken_rail_input_signal.emit(broken)

        # Get text from the test inputs for ticket sales
        ticket_text = self.ticket_in.text().strip()

        # this check if the input is not empty
        if ticket_text:  
            try:
                ticket_sales = int(ticket_text)  # Convert text to integer
                self.ticket_sales_signal.emit(ticket_sales)  # Emit the signal with the ticket sales value
                self.ticket_out.setText(str(ticket_sales))  # Set the output text for ticket sales
            except ValueError:
                print("")
        else:
            pass

        # Get text from the test inputs for light status and emit that info to main UI
        light = self.light_in.text()
        self.light_input_signal.emit(light)

        # Get text from the test inputs for switch status and emit that info to main UI
        switch = self.switch_in.text()
        self.switch_input_signal.emit(switch)

        # Get text from the test inputs for railway crossing status and emit that info to main UI
        cross = self.rail_in.text()
        self.cross_input_signal.emit(cross)        

        # Get text from the test inputs for commanded speed
        com_speed = self.com_speed_in_1.text()
        #set the output text for commanded speed
        self.com_speed_out_1.setText(com_speed)

        # Get text from the test inputs for authority
        authority = self.authority_in.text()
        #set the output text for authority
        self.authority_out.setText(authority)

    #Function for inputs/outputs for textboxes for only track circuit failure
    def test_input_2(self):
        # Get text from the test inputs for track circuit
        broken = self.track_in.text()
        # Set the output text for broken rail
        self.track_out.setText(broken)

        # Emit the signal with the input text for broken rail
        self.track_input_signal.emit(broken)

    #Function for inputs/outputs for only power failure
    def test_input_3(self):
        # Get text from the test inputs for track circuit
        broken = self.power_in.text()
        # Set the output text for broken rail
        self.power_out.setText(broken)

        # Emit the signal with the input text for broken rail
        self.power_input_signal.emit(broken)

    #Function for inputs/outputs for dropdown menus
    def test_combo_line(self, text):
        # Get text from the test inputs
        line_in1 = text
        # Set the text to the output text
        self.line_out.setText(line_in1)

    def test_combo_broken(self, text):
        # Get text from the test inputs for broken rail block
        broken1 = text
        # Set the text to the output text
        self.broken_block_out.setText(broken1)

    def test_combo_broken_tb(self, text):
        # Emit the signal with the selected text from the broken_block dropdown
        self.dropdown_broken_signal.emit(text)

        # Set the text to the output text
        self.broken_block_out.setText(text)

    def test_combo_track(self, text):
        # Get text from the test inputs for track circuit failure block
        track1 = text
        # Set the text to the output text
        self.track_block_out.setText(track1)

    def test_combo_power(self, text):
        # Get text from the test inputs for power faulure block
        power1 = text
        # Set the text to the output text
        self.power_block_out.setText(power1)

#My data class containing data from excel 
class Data:
    def __init__(self):

        # Initializing variables
        self.section = None
        self.line = None
        self.elevation = None
        self.grade = None
        self.length1 = None
        self.temp = None
        self.speed_limit = None
        self.heaters = None
        self.occupancy = None
        self.broken_rail = None
        self.circuit_failure = None
        self.power_failure = None
        self.block_num = None
        self.direction = None
        self.cross = None
        self.infra = None
        self.cumm_elevation = None

    # read Excel files from DataFrame
    def read_excel(self, filename):
        self.df = pd.read_excel("Track_Resources/Blue_Line_Block_Info.xlsx")

        #extract data from DataFrame of the Excel and assign to variables
        self.elevation_data = self.df.set_index('Block Number')['ELEVATION (M)'].to_dict()
        self.elevation = self.df.loc[0, 'ELEVATION (M)']
        self.grade = self.df.loc[0, 'Block Grade (%)']
        self.length1 = self.df.loc[0, 'Block Length (m)']
        self.infra = self.df.loc[0, 'Infrastructure']
        self.block_num = self.df.loc[0, 'Block Number']
        self.cumm_elevation = self.df.loc[0, 'CUMALTIVE ELEVATION (M)']
        self.speed_limit = self.df.loc[0,'Speed Limit (Km/Hr)']
        self.section = self.df.loc[0, 'Section']
        
    def get_elevation_for_block(self, block_num):
        # check if DataFrame is not None
        if self.df is not None:
            # iterate through the DataFrame of the Ecel file
            for index, row in self.df.iterrows():
                #check if the block number matches and if so...
                if row['Block Number'] == block_num:
                    # Return the corresponding elevation value of that row
                    return row['ELEVATION (M)']
        return None  # Return None if block number is not found or there is nothing in the Dataframe
    
    def get_grade_for_block(self, block_num):
        # iterate through the DataFrame of the Ecel file
        if self.df is not None:
            # iterate through the DataFrame
            for index, row in self.df.iterrows():
                #check if the block number matches and if so...
                if row['Block Number'] == block_num:
                    # Return the corresponding grade value of that row
                    return row['Block Grade (%)']
        return None  # Return None if block number is not found or there is nothing in the Dataframe
    
    def get_length_for_block(self, block_num):
        # iterate through the DataFrame of the Ecel file
        if self.df is not None:
            #   iterate through the DataFrame
            for index, row in self.df.iterrows():
                #check if the block number matches and if so...
                if row['Block Number'] == block_num:
                    # Return the corresponding block length value of that row
                    return row['Block Length (m)']
        return None  # Return None if block number is not found or there is nothing in the Dataframe
    
    def get_block_for_block(self, block_num):
        # iterate through the DataFrame of the Ecel file
        if self.df is not None:
            #  iterate through the DataFrame
            for index, row in self.df.iterrows():
                # check if the block number matches and if so...
                if row['Block Number'] == block_num:
                    # Return the corresponding block num value of that row
                    return row['Block Number']
        return None  # Return None if block number is not found or there is nothing in the Dataframe
    
    def get_section_for_block(self, block_num):
        # iterate through the DataFrame of the Ecel file
        if self.df is not None:
            #  iterate through the DataFrame
            for index, row in self.df.iterrows():
                # check if the block number matches and if so...
                if row['Block Number'] == block_num:
                    # Return the corresponding section value of that row
                    return row['Section']
        return None  # Return None if block number is not found or there is nothing in the Dataframe
    
    def get_speed_for_block(self, block_num):
        # iterate through the DataFrame of the Ecel file
        if self.df is not None:
            #  iterate through the DataFrame
            for index, row in self.df.iterrows():
                #check if the block number matches and if so...
                if row['Block Number'] == block_num:
                    # Return the corresponding section value of that row
                    return row['Speed Limit (Km/Hr)']
        return None  # Return None if block number is not found or there is nothing in the Dataframe
    
class Communicate(QObject):
    #object signals (mainly for failures inputs button)
    broken_rail_input_signal = pyqtSignal(str)
    track_input_signal = pyqtSignal(str)
    power_input_signal = pyqtSignal(str)
    ticket_sales_signal = pyqtSignal(int)
    light_input_signal = pyqtSignal(str)
    switch_input_signal = pyqtSignal(str)
    cross_input_signal = pyqtSignal(str)
    dropdown_broken_signal = pyqtSignal(str)

# Call Main window
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window_2 = TestBench()

    #Create an instance of Communicate
    communicator = Communicate()

    # connect the signal from window_2 to the slot in window
    window_2.broken_rail_input_signal.connect(window.toggle_button_state_tb)
    window_2.track_input_signal.connect(window.toggle_button_state_2_tb)
    window_2.power_input_signal.connect(window.toggle_button_state_3_tb)

    window_2.dropdown_broken_signal.connect(window.update_main_dropdown)

    window_2.ticket_sales_signal.connect(window.update_ticket_sales)

    window_2.light_input_signal.connect(window.toggle_light_state_tb)
    window_2.cross_input_signal.connect(window.toggle_cross_state_tb)
    window_2.switch_input_signal.connect(window.toggle_switch_tb)

    # Connect MyMainWindow's method to emit the grade to TestBench's slot to update the grade label
    window.grade_signal.connect(window_2.update_grade_label)

    window.show()
    window_2.show()

    sys.exit(app.exec_())
