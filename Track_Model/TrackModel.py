import sys
import json
import tkinter as tk
import os #read other .py file
import pandas as pd #read excel files
import random # Generate random num of ticket sales for CTC

# Using Block Class as a seperate file
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

# import libraries
from PyQt5.QtWidgets import QApplication,QLCDNumber, QGroupBox,QMainWindow, QFileDialog, QVBoxLayout, QComboBox, QHBoxLayout, QWidget, QLabel, QPushButton, QSizePolicy
from PyQt5 import uic,QtCore
from PyQt5.QtCore import Qt,QAbstractTableModel
from PyQt5.QtCore import QTimer, QTime
from Track_Resources.Block import Block
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtGui as qtg 
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsItem
from PyQt5.QtCore import QRectF, Qt
from PyQt5 import QtGui


#My main window
class TrackModelMain(QMainWindow):
    # Define a signal to emit the grade to testBench UI
    grade_signal = pyqtSignal(float)
    #Adding a signal to update information based on block selection:
    block_selected_signal = pyqtSignal(str)  

    getSpecialBlocks = pyqtSignal(list)
    #sendOccupancies = pyqtSignal(list)

    #send ticket sales to ctc
    SendTicketsales = pyqtSignal(list)

    #send train model train id, speed, and authority
    sendSpeedAuth = pyqtSignal(list)

    # Send Wayside_SW block occupancies as a list
    sendBlockOcc_SW = pyqtSignal(list)

    # Send Wayside_HW block occupancies as a list
    sendBlockOcc_HW = pyqtSignal(list)
    
    #send com speed to testbenchs
    send_com_speed_tb = pyqtSignal(str)

    #send authority to ttestbench
    send_authority_tb = pyqtSignal(str)

    AcutalSpeed = 0

    def __init__(self):
        super().__init__()
        self.blockStates = {}

        # Load the track model straight from the UI file using uic
        uic.loadUi("Track_Model/Track_Model.ui", self)

        self.set_broken_rail.clicked.connect(self.set_broken_rail_failure)
        self.set_track_failure.clicked.connect(self.set_track_circuit_failure)
        self.set_power_failure.clicked.connect(self.set_power_failure_func)
        self.reset_button.clicked.connect(self.reset_block_colors)

        # Connect Upload Track Layout button to make upload file
        self.pushButton.clicked.connect(self.upload_track_layout) 

        #Connect failure screen to block selection to make it easier for user/disable dropdown for failure
        self.block_in_1.activated.connect(self.update_block_in_2_based_on_block_in_1)
        self.block_in_2.setEnabled(False)

        self.setup_block_buttons()
        self.block_in_1.activated[str].connect(self.block_clicked)
        self.generateTickets()

        # Instantiate the Data class
        self.data = Data()

        # Connect the comboBox to the function
        self.green_line.hide()
        #self.red_line.hide()
        self.line_select.currentIndexChanged.connect(self.on_line_select_changed)

        # After setting up UI elements, load the default track layout
        self.default_track_path = "Track_Resources/green_line_block_info.xlsx"
        self.load_default_track_layout()

    def get_block_occupancy(self, authority, speed_of_train):
        #initializing varibales
        self.total_block_length = 0
        self.iteration = 0

        # Convert train speed to m/s from km/h for calculation 
        self.speed_of_train_kms = speed_of_train / 2237

        for block_num in range(63, 66):
            self.total_block_length = self.data.get_length_for_block(block_num)
            self.speed_limit_km = self.data.get_speed_for_block(block_num)
            while self.total_block_length != authority:
                if self.total_block_length <= (speed_of_train*(self.total_block_length*(1/(self.speed_limit_km*1000/(60*60))))):
                    self.block_num_occ = self.data.get_block_for_block(block_num)
                    self.section_occ = self.data.get_section_for_block(block_num)
                    blockID = self.block_num_occ + self.section_occ
                    print("block occ", blockID)
                else:
                    self.total_block_length 

    # Adding str block id that is occupied based on failures and where the train is (might send 1) 
    def add_block_occ(self, blockID):
        self.block_occ_list.append(blockID)

    def remove_block_occ(self, blockID):
    # If exists, remove it
        if blockID in self.block_occ_list:
            self.block_occ_list.remove(blockID)


    def recieveSpecialBlocks(self, specialBlock):
        self.specialBlock_list = specialBlock
        print("i'm getting blocks", specialBlock)

          
    def sendBlockOcc(self):
        self.sendBlockOcc_SW.emit(self.block_occ_list)


    def load_default_track_layout(self):
        # Directly load the default track layout file
        if os.path.exists(self.default_track_path):
            self.data.read_excel(self.default_track_path)
        else:
            print("")

    def set_clock(self, time):
        self.clock_in.display(time)
        self.current_time = time
        
    #use time for calculations
    def get_time(self):
        return self.current_time

    def receiveSpeedAuth_tm(self,speedAuth):
        self.trainID=speedAuth[0]
        self.Comm_Speed=speedAuth[1]
        self.Authority=speedAuth[2]
        self.sendSpeedAuth.emit(speedAuth)
        self.send_com_speed_tb.emit(str(self.Comm_Speed))
        self.send_authority_tb.emit(str(self.Authority))

        self.get_block_occupancy(self.Authority, self.AcutalSpeed)


    #FROM TRAIN MODEL
    def receiveSendVelocity(self, velocity):
        self.AcutalSpeed = velocity
        print("velocity = ", self.AcutalSpeed)
    
    def on_line_select_changed(self):
        # Check the selected option and show the corresponding group box
        selected_option = self.line_select.currentText()
        if selected_option == "Green Line":
            self.green_line.show()
        elif selected_option == "Select Line":
            self.green_line.hide()    
       # elif selected_option == "Red Line":
        #    self.red_line.show()
        #    self.green.hide()
            
    def set_broken_rail_failure(self):
        selected_block = self.block_in_1.currentText()
        if selected_block:
            button = self.findChild(QPushButton, selected_block)
            if button:
                button.setStyleSheet("background-color: grey")

    def set_track_circuit_failure(self):
        selected_block = self.block_in_1.currentText()
        if selected_block:
            button = self.findChild(QPushButton, selected_block)
            if button:
                button.setStyleSheet("background-color: yellow")
    
    def set_power_failure_func(self):
        selected_block = self.block_in_1.currentText()
        if selected_block:
            button = self.findChild(QPushButton, selected_block)
            if button:
                button.setStyleSheet("background-color: tan")

    def reset_block_colors(self):
        # Defaull stylesheet of buttons for the Track Layout
        default_color = '''
            QPushButton {
                border-style: solid;
                border-width: 0.5px;
                border-color: black;
                background-color: rgb(50, 205, 50);
            }
        '''
        #iterate through all buttons to reset them
        for block_id, button in self.block_buttons.items():
            button.setStyleSheet(default_color)

    def setup_block_buttons(self):
        #list of block IDs
        block_ids = [
        'A1', 'A2', 'A3', 'B4', 'B5', 'B6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12',
        'D13', 'D14', 'D15', 'D16', 'E17', 'E18', 'E19', 'E20', 'F21', 'F22', 'F23', 'F24',
        'F25', 'F26', 'F27', 'F28', 'G29', 'G30', 'G31', 'G32', 'H33', 'H34', 'H35', 'I36',
        'I37', 'I38', 'I39', 'I40', 'I41', 'I42', 'I43', 'I44', 'I45', 'I46', 'I47', 'I48',
        'I49', 'I50', 'I51', 'I52', 'I53', 'I54', 'I55', 'I56', 'I57', 'J58', 'J59', 'J60',
        'J61', 'J62', 'K63', 'K64', 'K65', 'K66', 'K67', 'K68', 'L69', 'L70', 'L71', 'L72',
        'L73', 'M74', 'M75', 'M76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84',
        'N85', 'O86', 'O87', 'O88', 'P89', 'P90', 'P91', 'P92', 'P93', 'P94', 'P95', 'P96',
        'P97', 'Q98', 'Q99', 'Q100', 'R101', 'S102', 'S103', 'S104', 'T105', 'T106', 'T107',
        'T108', 'T109', 'U110', 'U111', 'U112', 'U113', 'U114', 'U115', 'U116', 'V117',
        'V118', 'V119', 'V120', 'V121', 'W122', 'W123', 'W124', 'W125', 'W126', 'W127',
        'W128', 'W129', 'W130', 'W131', 'W132', 'W133', 'W134', 'W135', 'W136', 'W137',
        'W138', 'W139', 'W140', 'W141', 'W142', 'W143', 'X144', 'X145', 'X146', 'Y147',
        'Y148', 'Y149', 'Z150', 'Y1', 'Y2', 'Y0'
        ]

        self.block_buttons = {}

        for block_id in block_ids:
                button = self.findChild(QPushButton, block_id)
                if button:
                    self.block_buttons[block_id] = button
                    #pass block_id
                    button.clicked.connect(lambda checked, b_id=block_id: self.block_clicked(b_id))

    def block_clicked(self, block_id):
        self.block_in_1.setCurrentText(block_id)
        self.block_in_2.setCurrentText(block_id) 

        #Call the update_block_info to fetch and update the UI with block data
        self.update_block_info(block_id)

        #Emit a signal or perform actions needed when a block is selected
        self.block_selected_signal.emit(block_id)

    def generateTickets(self):
        # Generate a random number between 1 and 74 for ticket sales
        random_number = random.randint(1, 74)
        #Output the random numberto ticket sales block info
        self.ticket_out.setText(str(random_number))
        self.SendTicketsales.emit([random_number])
        
    
    #set temperature
    def set_temp(self, temp):
        pass

    #use global clock
    def clock(self):
        pass

    #failures:
    def set_broken(broke):
        broken = broke
        #send occupancies

    def set_track_circuit(fail1):
        track_circuit = fail1
        #send occupancies

    def set_power_fail(fail2):
        power_fail = fail2
        #send occupancies

    def get_broken(self):
        return self.broken

    def get_track_circuit(self):
        return self.track_circuit

    def get_power_fail(self):
        return self.power_fail


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

    def toggle_light_state_tb(self, bool1):
            # Toggle the state and color of the light button
            if bool1.lower() == "green":
                self.light_out.setText("GREEN")
                self.light_out.setStyleSheet("background-color: green;")
            elif bool1.lower() == "red":
                self.light_out.setText("RED")
                self.light_out.setStyleSheet("background-color: rgb(195, 16, 40);")

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

        self.data.read_excel(uploaded_track)
 
        # Connect the block selection dropdown to update_block_info function!
        self.block_in_1.activated[str].connect(lambda text: self.update_block_info(text))

    #This function uses the data from the data class to update block data and output it to main UI
    def update_block_info(self, block_text):
        # Reset the states of the buttons whenever a new block is selected
        #self.reset_button_states()

        # From dropdown of "B#" take out the letter B
        block_num = int(block_text.split()[-1][1:])  

        # Get certain data from specific block
        self.elevation_m = self.data.get_elevation_for_block(block_num)
        self.grade = self.data.get_grade_for_block(block_num)
        self.length1_m = self.data.get_length_for_block(block_num)
        self.block_num = self.data.get_block_for_block(block_num)
        self.section = self.data.get_section_for_block(block_num)
        self.speed_limit_km = self.data.get_speed_for_block(block_num)
        self.cumm_elevation_m = self.data.get_cumm_ele_for_block(block_num)

        # Math conversion from metric to imperial for track length, speed limit, and elevation.
        elevation_ft = self.elevation_m * 3.28084
        elevation_str = "{:.4f}".format(elevation_ft).rstrip('0').rstrip('.')

        cumm_elevation_ft = self.cumm_elevation_m * 3.28084
        cumm_elevation_str = "{:.4f}".format(cumm_elevation_ft).rstrip('0').rstrip('.')

        length_ft = self.length1_m * 3.28084
        length_str = "{:.4f}".format(length_ft).rstrip('0').rstrip('.')

        speed_limit_ft = self.speed_limit_km / 1.609344 
        speed_limit_str = "{:.4f}".format(speed_limit_ft).rstrip('0').rstrip('.')

        # Update the labels with the block data and output it.
        self.elevation_in.setText(elevation_str)
        self.cumm_elevation_in.setText(cumm_elevation_str)
        self.grade_in.setText(str(self.grade))
        self.length_in.setText(length_str)
        self.block_num_in.setText(str(block_num))
        self.section_in.setText(str(self.section))
        self.speed_in.setText(speed_limit_str)

        # Emit the grade signal with the grade value (sig)
        self.grade_signal.emit(self.grade)

        # Emit screen change based on block selection
        self.block_selected_signal.emit(block_text)

    #Updates block in failure based on block selection
    def update_block_in_2_based_on_block_in_1(self):
    #Get the currently selected text in block_in_1
        selected_text = self.block_in_1.currentText()

        self.block_in_2.setCurrentText(selected_text)

    def blockClicked(self, block_id):
        #Fetch block data and update UI elements
        block_data = self.data.get_data_for_block(block_id)
        if block_data:
            self.block_num_in.setText(str(block_data['block_num']))
            self.section_in.setText(block_data['section'])
            self.speed_in.setText(str(block_data['speed_limit_km']))
            self.grade_in.setText(str(block_data['grade']))
            self.length_in.setText(str(block_data['length1_m']))
            self.elevation_in.setText(str(block_data['elevation_m']))
            self.cumm_elevation_in.setText(str(block_data['cumm_elevation_m']))



#this is my testbench window
class TrackModel_tb(QMainWindow):
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

    #signal to from get speed
    Wayside_speed = pyqtSignal(Block)
    Wayside_authority = pyqtSignal(Block)
    
    def __init__(self):
        super().__init__()

        # Load the track model testbench straight from the UI file using uic
        uic.loadUi("Track_Model/testbench_trackmodel.ui", self)

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

    def update_commanded_speed(self, commanded_speed):
        self.com_speed_out_1.setText(str(commanded_speed))

    def update_authority(self, authority1):
        self.authority_out.setText(str(authority1))


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

    def update_on_block_selection(self, selected_block):
        pass
    
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

    def set_heater(self): #based on set temp
        pass
    

    # read Excel files from DataFrame
    def read_excel(self, filename):

        self.df = pd.read_excel("Track_Resources/Blue_Line_Block_Info.xlsx")
        self.df = pd.read_csv("Track_Resources/Blue_Line_Block_Info.csv")

        self.df = pd.read_excel("Track_Resources/green_line_block_info.xlsx")
        self.df = pd.read_csv("Track_Resources/green_line_block_info.csv")

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


    def get_data_for_block(self, block_num):
        #Ensure the DataFrame is not empty and contains data
        if self.df is not None and not self.df.empty:
            #find datain row
            block_row = self.df[self.df['Block Number'] == block_num]
            if not block_row.empty:
                #Block  data presented
                return {
                    'block_num': block_row.iloc[0]['Block Number'],
                    'section': block_row.iloc[0]['Section'],
                    'speed_limit_km': block_row.iloc[0]['Speed Limit (Km/Hr)'],
                    'grade': block_row.iloc[0]['Block Grade (%)'],
                    'length1_m': block_row.iloc[0]['Block Length (m)'],
                    'elevation_m': block_row.iloc[0]['ELEVATION (M)'],
                    'cumm_elevation_m': block_row.iloc[0]['CUMALTIVE ELEVATION (M)'],

                }
        return None 
    
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
    
    def get_cumm_ele_for_block(self, block_num):
        # iterate through the DataFrame of the Ecel file
        if self.df is not None:
            #  iterate through the DataFrame
            for index, row in self.df.iterrows():
                #check if the block number matches and if so...
                if row['Block Number'] == block_num:
                    # Return the corresponding section value of that row
                    return row['CUMALTIVE ELEVATION (M)']
        return None  # Return None if block number is not found or there is nothing in the Dataframe
    
    #receive speed
    def recieveSpeedAuthority(data):#block
        pass

    #function to send commanded speed to train model
    def send_commandedSpeed(void):
        pass

    #function to send authority to train model
    def send_Authority(void):
        pass
    
    #function to update light status from wayside
    def updateSpecialBlocks(data):
        pass

    #send beacon information ot train model
    def send_beacon(self):
        #underground
        #station
        pass

    #calculate where train is/occupancies
    def set_occupancies(self):
        pass

    def send_occupancies(self):
        pass

# class for fault table per block
class TrackFaultTable(QAbstractTableModel):
    def __init__(self, data=None):
        super().__init__()
        self._data = []

        

# Call Main window
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = TrackModelMain()
    window_2 = TrackModel_tb()


    window_2.dropdown_broken_signal.connect(window.update_main_dropdown) 

    window_2.ticket_sales_signal.connect(window.update_ticket_sales)

    window_2.light_input_signal.connect(window.toggle_light_state_tb)
    window_2.cross_input_signal.connect(window.toggle_cross_state_tb)
    window_2.switch_input_signal.connect(window.toggle_switch_tb)

    # window.send_com_speed_tb.connect(window_2.update_commanded_speed)
    # window.send_authority_tb.connect(window_2.update_authority)

    # Connect TrackModelMain's method to emit the grade to TestBench's slot to update the grade label
    window.grade_signal.connect(window_2.update_grade_label)

    window.block_selected_signal.connect(window_2.update_on_block_selection)
    window.show()
    window_2.show()

    sys.exit(app.exec_())
