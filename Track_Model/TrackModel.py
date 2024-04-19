import sys
import json
import tkinter as tk
import os #read other .py file
import pandas as pd #read excel files
import random # Generate random num of ticket sales for CTC
import time

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
from PyQt5.QtWidgets import *
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

    grade_signal_tm = pyqtSignal(float)

    send_beacon = pyqtSignal(int)

    send_polarity = pyqtSignal(bool)

    send_bool_auth = pyqtSignal(bool)

    AcutalSpeed = 0
    

    station_lookup = {
    "A2": "PIONEER",
    "C9": "EDGEBROOKE",
    "D16": "STATION",
    "DF22": "WHITED",
    "G31": "SOUTH BANK",
    "I39": "CENTRAL",
    "W141": "CENTRAL",
    "I48": "INGLEWOOD",
    "W132": "INGLEWOOD",
    "I57": "OVERBROOK",
    "W123": "OVERBROOK",
    "K65": "GLENBURY",
    "U114": "GLENBURY",
    "L73": "DORMONT",
    "T105": "DORMONT",
    "N77": "MT LEBANON",
    "O88": "POPLAR",
    "P96": "CASTLE SHANNON"
    }

    # Define the specific blocks that have features
    LIGHT_BLOCKS_SW = ['J59', 'J63', 'M76', 'O86', 'Q100', 'R101']
    LIGHT_BLOCKS_HW = ['A1', 'C12', 'G29', 'Z150']
    CROSSING_BLOCKS = ['E19', 'T108']
    SWITCH_BLOCKS_SW = ['N77', 'N85'] 
    SWITCH_BLOCKS_HW = ['D13', 'F28']
    
    def __init__(self):
        super().__init__()
        self.blockStates = {}
        station_lookup = {}
        self.blockID = None
        self.station = ""
        self.occupied_blocks = []
        self.occupied_block_failures = []
        self.lastGeneratedTickets = {}
        self.blockID = ""
        self.total_block_length = 0
        self.prevblockID = ""
        self.data = None  # Assuming this will be initialized with your data source
        # Add train id, line, distance from starting block, direction, and block occupancy
        self.currentTrains = []
        self.blockIDs_SW = []
        self.blockIDs_HW = []
        self.dt = 0
        self.prev_time = 0
        self.polarity = 0

        # Load the track model straight from the UI file using uic
        uic.loadUi("Track_Model/Track_Model.ui", self)

        self.set_broken_rail.clicked.connect(self.set_broken_rail_failure)
        self.set_track_failure.clicked.connect(self.set_track_circuit_failure)
        self.set_power_failure.clicked.connect(self.set_power_failure_func)
        self.reset_button.clicked.connect(self.reset_block_colors)

        self.temp_in.setValue(70)  # Set the default value for temp_in spinbox
        self.temp_in.valueChanged.connect(self.update_heaters_out)  # Connect the signal to the slot

        # Connect Upload Track Layout button to make upload file
        self.pushButton.clicked.connect(self.upload_track_layout) 

        #Connect failure screen to block selection to make it easier for user/disable dropdown for failure
        self.block_in_1.activated.connect(self.update_block_in_2_based_on_block_in_1)
        self.block_in_2.setEnabled(False)

        self.setup_block_buttons()
        self.block_in_1.activated[str].connect(self.block_clicked)
        #self.generateTickets()
        self.default_track_path = None
        # Instantiate the Data class
        self.data = Data()

        #self.line_select.currentIndexChanged.connect(self.load_track_layout_based_on_selection)

        # Connect the comboBox to the function
        self.green_line.hide()
        self.red_line.hide()
        self.line_select.currentIndexChanged.connect(self.on_line_select_changed)

        # self.default_track_path = "Track_Resources/green_line_block_info.xlsx"
        self.load_default_track_layout()
        
        # After setting up UI elements, load the default track layout
        # if self.line_select.currentText() == "Green Line":
        #     # self.default_track_path = "Track_Resources/green_line_block_info.xlsx"
        #     # self.load_default_track_layout()
        #     print("Green!")
        # elif self.line_select.currentText() == "Red Line":
        #     # self.default_track_path = "Track_Resources/red_line_block_info.xlsx"
        #     # self.load_default_track_layout()
        #     print("Red!")
        
        self.current_line = "Green Line"  # Default line
        self.line_select.currentIndexChanged.connect(self.on_line_select_changed)

    def get_train_id(self, trainID, line):
        if line == "Green":
            self.currentTrains.append([trainID, line, 0, 'increasing', 'K63'])
            self.occupied_blocks.append('K63')
            self.send_beacon.emit(0)
            self.update_occupied_blocks()
        elif line == "Red":
            self.currentTrains.append([trainID, line, 0, 'increasing', 'D10'])
            self.send_beacon.emit(1)

    def update_heaters_out(self):
        # Get the current temperature from the spinbox
        temp_value = self.temp_in.value()

        # Update the temp_out label to match the spinbox value
        self.temp_out.setText(f"{temp_value}°")

        # Update the heaters_out label based on the temperature
        if temp_value <= 32:
            self.heaters_out.setText("ON")
        else:
            self.heaters_out.setText("OFF")

    def load_track_layout_based_on_selection(self):
        selected_option = self.line_select.currentText()
        if selected_option == "Green Line":
            self.default_track_path = "Track_Resources/green_line_block_info.xlsx"

        elif selected_option == "Red Line":
            self.default_track_path = "Track_Resources/red_line_block_info.xlsx"
            #print(self.default_track_path)

        else:
            print("")
        self.load_default_track_layout()
       
    
    def load_default_track_layout(self):
        self.default_track_path = "Track_Resources/green_line_block_info.xlsx"
        if self.default_track_path and os.path.exists(self.default_track_path):
            self.data.read_excel(self.default_track_path)
        else:
            print("")
        
    def process_block(self, block_num, trainId, speed_of_train):
        # Get the length of the current block
            total_dis_from_beg_of_block = self.currentTrains[int(trainId[1:]) - 1][2]
            block_length = self.data.get_length_for_block(block_num)
            #self.total_block_length += block_length  # Cumulative sum of block lengths

            self.dt = self.local_time - self.prev_time
            self.prev_time = self.local_time
            self.speed_limit_km = self.data.get_speed_for_block(block_num)

            speed_of_train_m = speed_of_train * 0.00044704 * self.dt

            total_dis_from_beg_of_block += speed_of_train_m
            self.currentTrains[int(trainId[1:]) - 1][2] = total_dis_from_beg_of_block

            #Compare total block length with some other calculated distance
            # distance_covered = (speed_of_train_m * (1 / (self.speed_limit_km * 1000 / (60 * 60))))

            # if train moves to the next block
            if total_dis_from_beg_of_block >= block_length:
                #Setting train direction after switches
                if block_num == 76:
                    self.currentTrains[int(trainId[1:]) - 1][3] = 'increasing'
                elif block_num == 100:
                    self.currentTrains[int(trainId[1:]) - 1][3] = 'decreasing'
                elif block_num == 150:
                    self.currentTrains[int(trainId[1:]) - 1][3] = 'decreasing'
                elif block_num == 1:
                    self.currentTrains[int(trainId[1:]) - 1][3] = 'increasing'

            # #red line (might use beacon instead)
            #     if block_num == 16:
            #         self.currentTrains[int(trainId[1:]) - 1][3] = 'increasing'
            #     elif block_num == 1:
            #         self.currentTrains[int(trainId[1:]) - 1][3] = 'decreasing'
            #     elif block_num == 14:
            #         self.currentTrains[int(trainId[1:]) - 1][3] = 'decreasing'
            #     elif block_num == 28:
            #         self.currentTrains[int(trainId[1:]) - 1][3] = 'increasing'
            #     elif block_num == 26:
            #         self.currentTrains[int(trainId[1:]) - 1][3] = 'decreasing'
            #     elif block_num == 33:
            #         self.currentTrains[int(trainId[1:]) - 1][3] = 'increasing'
            #     elif block_num == 31:
            #         self.currentTrains[int(trainId[1:]) - 1][3] = 'decreasing'
            #     elif block_num == 39:
            #         self.currentTrains[int(trainId[1:]) - 1][3] = 'increasing'
            #     elif block_num == 37:
            #         self.currentTrains[int(trainId[1:]) - 1][3] = 'decreasing'
            #     elif block_num == 44:
            #         self.currentTrains[int(trainId[1:]) - 1][3] = 'increasing'
            #     elif block_num == 42:
            #         self.currentTrains[int(trainId[1:]) - 1][3] = 'decreasing'
            #     elif block_num == 53:
            #         self.currentTrains[int(trainId[1:]) - 1][3] = 'increasing'
            #     elif block_num == 52:
            #         self.currentTrains[int(trainId[1:]) - 1][3] = 'decreasing'
                
            # Calculate next block for TRAIN MODEL
            # next_block_num = self.get_next_id(block_num, self.currentTrains[int(trainId[1:]) - 1][3], "Green")
            # if next_block_num is not None:
            #     next_block_grade = self.data.get_grade_for_block(next_block_num)  # Fetch grade for the next block
            #     if next_block_grade is not None:
            #         self.grade_signal.emit(next_block_grade)  # Emit the grade of the next block
                    
            #         if self.polarity == 0:
            #             self.polarity = 1
            #         else:
            #             self.polarity = 0
                #self.send_polarity.emit(self.polarity)
                self.grade_signal_tm.emit(self.data.get_grade_for_block(block_num))
                #print(self.data.get_grade_for_block(block_num))

                
                # Getting block section from excel 
                self.section_occ = self.data.get_section_for_block(block_num)
                self.blockID = self.section_occ + str(block_num)
                
                #calculate next block
                next_block_num = self.get_next_id(block_num, self.currentTrains[int(trainId[1:]) - 1][3], "Green")
                self.next_block_id = self.data.get_section_for_block(next_block_num)

                self.occupied_blocks.clear()
                self.occupied_blocks.append(self.next_block_id + str(next_block_num))
                self.update_occupied_blocks()
                #self.update_block_info(self.blockID)

                self.currentTrains[int(trainId[1:]) - 1].pop()
                self.currentTrains[int(trainId[1:]) - 1].append(self.next_block_id + str(next_block_num))
                
                self.currentTrains[int(trainId[1:]) - 1][2] = speed_of_train_m - (block_length - total_dis_from_beg_of_block)

    def get_switch_state(self, block_num):
        # Retrieve the switch state from your blockStates dictionary or similar data structure
        block_info = self.blockStates.get(str(block_num))
        if block_info is not None:
            return block_info['switchState']
        return None 

    def get_next_id(self, BlockNum, direction, line):
        if line == 'Green':
            #print("Switch:",self.get_switch_state(BlockNum))
            
            #A1 to D13 switch block
            if BlockNum == 1:
                if self.get_switch_state(13) == False:
                    return 13
                else:
                    #Error Message
                    error_msg = QMessageBox()
                    error_msg.setWindowTitle("Train Crashed!")
                    error_msg.setText("Switch was not in the correct position")
                    error_msg.setIcon(QMessageBox.Critical)

                    error_msg.exec_() 

                    return 1

            #A-C blocks, train can only come from its previous blocks, but they are in reverse number order
            elif (BlockNum > 1) and (BlockNum <= 12):
                return BlockNum - 1
                
            #D switch block
            elif BlockNum == 13:
                if direction == 'decreasing':
                    return 12
                elif direction == 'increasing':
                    return 14

            #D,E,F blocks (without the switches), bidirectional
            elif (BlockNum > 13) and (BlockNum <= 27):
                if direction == 'increasing':
                    return BlockNum + 1
                else:
                    return BlockNum - 1
                
            #F28 switch block
            elif BlockNum == 28:
                if direction == 'decreasing':
                    return 27
                else:
                    return 29
                            
            #G-I blocks, train can only come from its previous blocks
            elif (BlockNum >= 29) and (BlockNum < 57):
                return BlockNum + 1
            elif BlockNum == 57:
                return 63
                        
            #J Blocks are the ones we skip near the yard
                        
            #K-M blocks, train can only come from its previous blocks
            elif (BlockNum >= 63) and (BlockNum <= 76):
                return BlockNum + 1
                        
            elif BlockNum == 77:
                if direction == 'increasing':
                    return 78
                elif direction == 'decreasing':
                    return 101
                
            #Full n block, bidirectional
            elif (BlockNum > 77) and (BlockNum <= 84):
                if direction == 'increasing':
                    return BlockNum + 1
                else:
                    return BlockNum - 1
                    

            #n switch on block 85, can come from N84 or Q100
            elif BlockNum == 85:
                if direction == 'increasing':
                    return 86
                elif direction == 'decreasing':
                    return 84
                
            #O-Q blocks, train can only come from its previous blocks        
            elif (BlockNum >= 86) and (BlockNum < 100):
                return BlockNum + 1
            
            #Q100
            elif BlockNum == 100:
                return 85

            #R-Z blocks, train can only come from its previous blocks
            elif ((BlockNum >= 101) and (BlockNum < 150)):
                return BlockNum + 1

            elif BlockNum == 150:
                return 28
        
                        
        #Red Line                                  
        if line == "Red":
            #Red line train dispatch case        
            if (BlockNum == 10):
               return 11
        

    def get_and_set_crossing_state(self, block_num):
        block_info = self.blockStates.get(str(block_num))
        if block_info is not None:
            crossing_state = block_info['crossingState']
            return crossing_state
        return None


    # Recieve from Wayside
    def receiveSpecialBlocks_SW(self, specialBlock):
        for block in specialBlock:
            block_id = f"{block.blockSection}{block.blockNum}"
            self.blockStates[block_id] = {
                'lineColor': block.lineColor,
                'lightState': block.lightState,
                'crossingState': block.crossingState,
                'switchState': block.switchState
            }


    def receiveSpecialBlocks_HW(self, specialBlock):
        for block in specialBlock:
            block_id = f"{block.blockSection}{block.blockNum}"
            self.blockStates[block_id] = {
                'lineColor': block.lineColor,
                'lightState': block.lightState,
                'crossingState': block.crossingState,
                'switchState': block.switchState
            }

    def update_ui_for_block(self, block_id):
        # Get the block state if it exists
        block_state = self.blockStates.get(block_id, {})

        # Update for SW
        if block_id in self.LIGHT_BLOCKS_SW or block_id in self.SWITCH_BLOCKS_SW:
            # Update light status for HW
            if block_id in self.LIGHT_BLOCKS_SW:
                light_state = block_state.get('lightState', 'N/A')
                self.light_out.setText(str(light_state))
                self.light_out.setStyleSheet("background-color: green;" if light_state == "GREEN" else "background-color: red;" if light_state == "RED" else "background-color: white;")
            else:
                self.light_out.setText('N/A')
                self.light_out.setStyleSheet("background-color: white;")

            # Update switch status for HW
            if block_id in self.SWITCH_BLOCKS_SW:
                switch_state = block_state.get('switchState', 'N/A')
                self.switch_out.setText(str(switch_state))
            else:
                self.switch_out.setText('N/A')

        # Update for HW
        elif block_id in self.LIGHT_BLOCKS_HW or block_id in self.SWITCH_BLOCKS_HW:
            # Update light status for HW
            if block_id in self.LIGHT_BLOCKS_HW:
                light_state = block_state.get('lightState', 'N/A')
                self.light_out.setText(str(light_state))
                self.light_out.setStyleSheet("background-color: green;" if light_state == "GREEN" else "background-color: red;" if light_state == "RED" else "background-color: white;")
            else:
                self.light_out.setText('N/A')
                self.light_out.setStyleSheet("background-color: white;")

            # Update switch status for HW
            if block_id in self.SWITCH_BLOCKS_HW:
                switch_state = block_state.get('switchState', 'N/A')
                self.switch_out.setText(str(switch_state))
            else:
                self.switch_out.setText('N/A')

        # Update crossing status, which is common for both HW and SW
        if block_id in self.CROSSING_BLOCKS:
            crossing_state = block_state.get('crossingState', 'N/A')
            self.cross_out.setText(str(crossing_state))
        else:
            self.cross_out.setText('N/A')

    def set_clock(self, time):
        self.clock_in.display(time[0:5])
        parts = time.split(':')
        hours, minutes = int(parts[0]), int(parts[1])
        seconds, ms = map(int, parts[2].split('.'))
        self.local_time = hours*3600000 + minutes*60000 + seconds*1000 + ms

    def get_clock(self,clock):
        self.current_time = clock

    def receiveSpeedAuth_tm(self,speedAuth):
        self.trainID=speedAuth[0]
        self.Comm_Speed=speedAuth[1]
        self.Authority=speedAuth[2]
        self.sendSpeedAuth.emit(speedAuth)
        self.send_com_speed_tb.emit(str(self.Comm_Speed))
        self.send_authority_tb.emit(str(self.Authority))

    def update_occupied_blocks(self):
        occupancies = self.occupied_blocks + self.occupied_block_failures  # Combine the lists of occupied and failed blocks
        sections_HW = ["A", "B", "C", "D", "E", "F", "G", "H", "T", "U", "V", "W", "X", "Y", "Z"]
        temp_HW = []
        temp_SW = []

        # Separate the blocks into HW and SW based on the first letter of the block ID
        for block_id in occupancies:
            if block_id[0] in sections_HW:  # Check if the first letter of the block ID is in sections_HW
                temp_HW.append(block_id)
            else:
                temp_SW.append(block_id)

        # Emit the separated lists to HW and SW respectively
        self.sendBlockOcc_SW.emit(temp_SW)
        self.sendBlockOcc_HW.emit(temp_HW)
        





    #FROM TRAIN MODEL for block occupancy
    def receiveSendVelocity(self, train_id, velocity):
        self.train_id = train_id
        trainNum = int(train_id[1:])
        thisTrain = self.currentTrains[trainNum - 1]

        self.process_block(int(thisTrain[-1][1:]), train_id, velocity)

        
    
    def on_line_select_changed(self):
        # Check the selected option and show the corresponding group box
        self.selected_option = self.line_select.currentText()
        if self.selected_option == "Green Line":
            self.green_line.show()
            self.red_line.show()
        elif self.selected_option == "Select Line":
            self.green_line.hide()
            self.red_line.hide()    
        elif self.selected_option == "Red Line":
           self.red_line.show()
           self.green_line.hide()
            # Now call the function to load the track layout based on the new selection
        #self.load_track_layout_based_on_selection()

        return self.line_select.currentText()
            
    def set_broken_rail_failure(self):
        self.selected_block = self.block_in_1.currentText()
        if self.selected_block:
            button = self.findChild(QPushButton, self.selected_block)
            #print(self.selected_block)
            if button:
                self.occupied_block_failures.append(self.selected_block)
                self.update_occupied_blocks()
                button.setStyleSheet("background-color: grey")
                

    def set_track_circuit_failure(self):
        self.selected_block = self.block_in_1.currentText()
        if self.selected_block:
            button = self.findChild(QPushButton, self.selected_block)
            #print(self.selected_block)
            if button:
                self.occupied_block_failures.append(self.selected_block)
                self.update_occupied_blocks()
                button.setStyleSheet("background-color: yellow")
    
    def set_power_failure_func(self):
        self.selected_block = self.block_in_1.currentText()
        if self.selected_block:
            button = self.findChild(QPushButton, self.selected_block)
            #print(self.selected_block)
            if button:
                self.occupied_block_failures.append(self.selected_block)
                self.update_occupied_blocks()
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
        # List of block IDs for both Green and Red Lines
        block_ids_green = [
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
            'Y148', 'Y149', 'Z150'
        ]

        block_ids_red = [
            'A1_r', 'A2_r', 'A3_r', 'B4_r', 'B5_r', 'B6_r', 'C7_r', 'C8_r', 'C9_r', 'D10_r', 'D11_r', 'D12_r',
            'E13_r', 'E14_r', 'E15_r', 'F16_r', 'F17_r', 'F18_r', 'F19_r', 'F20_r', 'G21_r', 'G22_r', 'G23_r',
            'H24_r', 'H25_r', 'H26_r', 'H27_r', 'H28_r', 'H29_r', 'H30_r', 'H31_r', 'H32_r', 'H33_r', 'H34_r',
            'H35_r', 'H36_r', 'H37_r', 'H38_r', 'H39_r', 'H40_r', 'H41_r', 'H42_r', 'H43_r', 'H44_r', 'H45_r',
            'I46_r', 'I47_r', 'I48_r', 'J49_r', 'J50_r', 'J51_r', 'J52_r', 'J53_r', 'J54_r', 'K55_r', 'K56_r',
            'K57_r', 'L58_r', 'L59_r', 'L60_r', 'M61_r', 'M62_r', 'M63_r', 'N64_r', 'N65_r', 'N66_r', 'O67_r',
            'P68_r', 'P69_r', 'P70_r', 'Q71_r', 'R72_r', 'S73_r', 'S74_r', 'S75_r', 'T76_r'
        ]

        all_block_ids = block_ids_green + block_ids_red

        self.block_buttons = {}

        for block_id in all_block_ids:
            button = self.findChild(QPushButton, block_id)
            if button:
                self.block_buttons[block_id] = button
                button.clicked.connect(lambda checked, b_id=block_id: self.block_clicked(b_id))
                # print(f"Connected {block_id}")
            else:
                print("")



    def update_block_info_ui(self, block_data):
        self.elevation_in.setText(str(block_data['elevation_m']))
        self.grade_in.setText(str(block_data['grade']))
        self.length_in.setText(str(block_data['length1_m']))
        self.speed_in.setText(str(block_data['speed_limit_km']))
        self.station_in.setText(self.station_lookup.get(block_data['block_num'], "N/A"))
        self.block_num_in.setText(str(block_data['block_num']))
        self.section_in.setText(block_data['section'])
        self.cumm_elevation_in.setText(str(block_data['cumm_elevation_m']))


    def block_clicked(self, block_id):
        # Update heaters and other UI elements initially
        self.update_heaters_out()

        # Determine if we need to adjust block ID for Red Line blocks
        if self.current_line == "Red Line" and block_id.endswith('_r'):
            # Remove the '_r' suffix for data fetching
            adjusted_block_id = block_id[:-2]
        else:
            adjusted_block_id = block_id

        # Fetch data for the adjusted block ID
        block_data = self.data.get_data_for_block(adjusted_block_id)
        if block_data:
            # If data is found, update the UI with this data
            self.update_ui_for_block(block_data)
            self.update_block_info_ui(block_data)  # Assuming this updates UI elements
            self.block_selected_signal.emit(adjusted_block_id)  # Emit signal with original block ID
        else:
            # Print debug info if no data is found
            # print(f"No data found for block {adjusted_block_id}")
            print("")

        # print(f"Adjusted Block ID for fetching data: {adjusted_block_id} (Original: {block_id}, Line: {self.line_select})")

        # Update UI components to reflect the selected block
        self.block_in_1.setCurrentText(adjusted_block_id)
        self.block_in_2.setCurrentText(adjusted_block_id)

        # Reset the light_out label color to white
        self.light_out.setStyleSheet("background-color: white;")

        # Proceed with updating the UI for the clicked block
        self.update_ui_for_block(adjusted_block_id)

        # Check if the block has special features and update the UI accordingly
        if adjusted_block_id in self.LIGHT_BLOCKS_SW:
            # Fetch the light state for this block and update the UI
            light_state = self.blockStates.get(adjusted_block_id, {}).get('lightState', 'N/A')
            self.light_out.setText("GREEN" if light_state else "RED")
            self.light_out.setStyleSheet("background-color: green;" if light_state else "background-color: red;")
        else:
            self.light_out.setText('N/A')

        if adjusted_block_id in self.CROSSING_BLOCKS:
            # Fetch the crossing state for this block and update the UI
            crossing_state = self.blockStates.get(adjusted_block_id, {}).get('crossingState', 'N/A')
            self.cross_out.setText("UP" if crossing_state else "DOWN")
        else:
            self.cross_out.setText('N/A')

        if adjusted_block_id in self.LIGHT_BLOCKS_HW:
            # Fetch the light state for this block and update the UI
            light_state = self.blockStates.get(adjusted_block_id, {}).get('lightState', 'N/A')
            self.light_out.setText("GREEN" if light_state else "RED")
            self.light_out.setStyleSheet("background-color: green;" if light_state else "background-color: red;")

        if adjusted_block_id in self.SWITCH_BLOCKS_SW:
            # Fetch the switch state for this block and update the UI
            switch_state = self.blockStates.get(adjusted_block_id, {}).get('switchState', 'N/A')
            self.switch_out.setText("LEFT" if switch_state else "RIGHT")
        else:
            self.switch_out.setText('N/A')

        if adjusted_block_id in self.SWITCH_BLOCKS_HW:
            # Fetch the switch state for this block and update the UI
            switch_state = self.blockStates.get(adjusted_block_id, {}).get('switchState', 'N/A')
            self.switch_out.setText("LEFT" if switch_state else "RIGHT")
        else:
            self.switch_out.setText('N/A')


        # Continue with the rest of the block_clicked functionality
        if adjusted_block_id == 'Y0':
            # Manually set the information for the yard block
            self.block_num_in.setText('N/A')  # Block number is 0 for the yard
            self.section_in.setText('N/A')
            self.speed_in.setText('0')  # Assuming speed is 0 in the yard
            self.grade_in.setText('0')
            self.length_in.setText('N/A')
            self.elevation_in.setText('0')
            self.cumm_elevation_in.setText('0')
            self.station_in.setText('Yard')
            self.temp_out.setText('N/A')
            self.heaters_out.setText('N/A')
            self.cross_out.setText('N/A')
            self.under_out.setText('N/A')

        else:
            # Update block info for non-yard blocks
            self.update_block_info(adjusted_block_id)
            self.block_selected_signal.emit(adjusted_block_id)

            if self.is_station(adjusted_block_id):
                self.currentStation = adjusted_block_id
                self.generateTickets(adjusted_block_id, updateUI=True)
            else:
                self.currentStation = None
                self.ticket_out.clear()

  
    def is_station(self, block_id):
        # Check if the block ID is in the station lookup table
        return block_id in self.station_lookup

    # def checkGenerateTickets(self):
    #     for block_id in self.station_lookup:
    #         if self.is_station(block_id):
    #             self.generateTickets(block_id)

    def updateHourlyTickets(self):
        if self.currentStation and self.is_station(self.currentStation):
            self.generateTickets(self.currentStation, updateUI=True, forceNewNumber=True)

    def generateTickets(self, block_id, updateUI=False, forceNewNumber=False):
        if forceNewNumber or block_id not in self.lastGeneratedTickets:
            random_number = random.randint(1, 74)
            self.lastGeneratedTickets[block_id] = random_number

        if updateUI:
            self.ticket_out.setText(str(self.lastGeneratedTickets[block_id]))

        # Emit signal only if a new number is generated
        if forceNewNumber:
            self.SendTicketsales.emit([block_id, self.lastGeneratedTickets[block_id]])

    def get_infra_for_block(self, block_num):
        self.station = None  # Set to None initially to clearly see if it gets changed
        self.block_num = str(block_num)

        if self.block_num == "A2":
            self.station = "PIONEER"
        elif self.block_num == "C9":
            self.station = "EDGEBROOKE"
        elif self.block_num == "D16":
            self.station = "STATION"
        elif self.block_num == "DF22":
            self.station = "WHITED"
        elif self.block_num == "G31":
            self.station = "SOUTH BANK"
        elif self.block_num == "I39" or self.block_num == "W141":
            self.station = "CENTRAL"
        elif self.block_num == "I48" or self.block_num == "W132":
            self.station = "INGLEWOOD"
        elif self.block_num == "I57" or self.block_num == "W123":
            self.station = "OVERBROOK"
        elif self.block_num == "K65" or self.block_num == "U114":
            self.station = "GLENBURY"
        elif self.block_num == "L73" or self.block_num == "T105":
            self.station = "DORMONT"
        elif self.block_num == "N77":
            self.station = "MT LEBANON"
        elif self.block_num == "O88":
            self.station = "POPLAR"
        elif self.block_num == "P96":
            self.station = "CASTLE SHANNON"
        else:
            self.station = ""  

    
    #set temperature
    def set_temp(self, temp):
        pass


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
        # Check if block_text ends with '_r' and remove it
        adjusted_block_text = block_text[:-2] if block_text.endswith('_r') else block_text

        #Now extract the block number assuming the format is something like "B23" or "B23_r"
        block_num = int(adjusted_block_text[1:])  # Skip the letter and convert the rest to int

        # Check if block is currently occupied
        isOccupied = "True" if adjusted_block_text in self.occupied_blocks else "False"
        self.occupancy_in.setText(isOccupied)

        # Retrieve block data using the adjusted block number
        self.elevation_m = self.data.get_elevation_for_block(block_num)
        self.grade = self.data.get_grade_for_block(block_num)
        self.length1_m = self.data.get_length_for_block(block_num)
        self.block_num = self.data.get_block_for_block(block_num)
        self.section = self.data.get_section_for_block(block_num)
        self.speed_limit_km = self.data.get_speed_for_block(block_num)
        self.cumm_elevation_m = self.data.get_cumm_ele_for_block(block_num)

        # Convert metric to imperial for track length, speed limit, and elevation
        elevation_ft = self.elevation_m * 3.28084
        elevation_str = "{:.4f}".format(elevation_ft).rstrip('0').rstrip('.')

        cumm_elevation_ft = self.cumm_elevation_m * 3.28084
        cumm_elevation_str = "{:.4f}".format(cumm_elevation_ft).rstrip('0').rstrip('.')

        length_ft = self.length1_m * 3.28084
        length_str = "{:.4f}".format(length_ft).rstrip('0').rstrip('.')

        speed_limit_ft = self.speed_limit_km / 1.609344 
        speed_limit_str = "{:.4f}".format(speed_limit_ft).rstrip('0').rstrip('.')

        # Update UI with block data
        self.elevation_in.setText(elevation_str)
        self.cumm_elevation_in.setText(cumm_elevation_str)
        self.grade_in.setText(str(self.grade))
        self.length_in.setText(length_str)
        self.block_num_in.setText(str(self.block_num))
        self.section_in.setText(str(self.section))
        self.speed_in.setText(speed_limit_str)
        self.station_in.setText(self.station)

        # Emit signals as needed
        self.grade_signal.emit(self.grade)
        self.block_selected_signal.emit(block_text)


    #Updates block in failure based on block selection
    def update_block_in_2_based_on_block_in_1(self):
    #Get the currently selected text in block_in_1
        selected_text = self.block_in_1.currentText()

        self.block_in_2.setCurrentText(selected_text)

    # def blockClicked(self, block_id):
    #     #Fetch block data and update UI elements
    #     block_data = self.data.get_data_for_block(block_id)
    #     if block_data:
    #         self.block_num_in.setText(str(block_data['block_num']))
    #         self.section_in.setText(block_data['section'])
    #         self.speed_in.setText(str(block_data['speed_limit_km']))
    #         self.grade_in.setText(str(block_data['grade']))
    #         self.length_in.setText(str(block_data['length1_m']))
    #         self.elevation_in.setText(str(block_data['elevation_m']))
    #         self.cumm_elevation_in.setText(str(block_data['cumm_elevation_m']))



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
        self.df = None


    # read Excel files from DataFrame
    def read_excel(self, filename):

        # if filename.endswith('.xlsx'):
        #     self.df = pd.read_excel(filename)
        # elif filename.endswith('.csv'):
        #     try:
        #         self.df = pd.read_csv(filename, error_bad_lines=False)
        #     except Exception as e:
        #         print(f"Failed to read CSV: {e}")
        # else:
        #     print("Unsupported file format")
        self.df = pd.read_excel("Track_Resources/green_line_block_info.xlsx")
        #self.df = pd.read_csv("Track_Resources/green_line_block_info.csv")

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
    
    #function to update light status from wayside
    def updateSpecialBlocks(data):
        pass

    #send beacon information ot train model
    def send_beacon(self):
        #underground
        #station
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

    window.show()
    window_2.show()

    sys.exit(app.exec_())