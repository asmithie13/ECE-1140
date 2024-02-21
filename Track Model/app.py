import sys
import os #read other .py file
import pandas as pd #read excel/csv files

# Using Block Class as a seperate file
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QComboBox, QHBoxLayout, QWidget, QLabel, QPushButton, QSizePolicy
from PyQt5 import uic
from PyQt5.QtCore import Qt  
from Track_Resources.Block import Block


#My main UI
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Track Model/Track_Model.ui", self)
        self.pushButton.clicked.connect(self.upload_track_layout)  # Connect the button's clicked signal to upload_file method

        # Connect button to method
        #If clicked, then connect to UI
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

    def toggle_button_state(self):
        # Toggle button state and color button broken rail
        if self.offButton_1.text() == "OFF":
            self.offButton_1.setText("ON")
            self.offButton_1.setStyleSheet("background-color: green;")
        else:
            self.offButton_1.setText("OFF")
            self.offButton_1.setStyleSheet("background-color: red;")

    def toggle_button_state_2(self):
        #Toggle button state and color button track circuit failure
        if self.offButton_2.text() == "OFF":
            self.offButton_2.setText("ON")
            self.offButton_2.setStyleSheet("background-color: green;")
        else:
            self.offButton_2.setText("OFF")
            self.offButton_2.setStyleSheet("background-color: red;")

    def toggle_button_state_3(self):
        # Toggle button state and color button power failure
        if self.offButton_3.text() == "OFF":
            self.offButton_3.setText("ON")
            self.offButton_3.setStyleSheet("background-color: green;")
        else:
            self.offButton_3.setText("OFF")
            self.offButton_3.setStyleSheet("background-color: red;")
    
    def upload_track_layout(self):
        file_dialog = QFileDialog()
        uploaded_track, _ = file_dialog.getOpenFileName(self, 'Upload Track Layout', '', 'Excel Files (*.xlsx);;CSV (*.csv)')
        if uploaded_track:
            #Instantiate the Data class
            self.data = Data()
            
            #Read data from the uploaded file using the Data class
            self.data.read_excel(uploaded_track)

        # Connect block selection dropdown to update_block_info function
        self.block_in_1.activated[str].connect(lambda text: self.update_block_info(text))

    def update_block_info(self, block_text):
        #From dropdown of "B#" take out the letter B
        block_num = int(block_text.split()[-1][1:])  

        #Get elevation from chosen block
        elevation = self.data.get_elevation_for_block(block_num)
        grade = self.data.get_grade_for_block(block_num)
        length1 = self.data.get_length_for_block(block_num)
        block_num = self.data.get_block_for_block(block_num)
        section = self.data.get_section_for_block(block_num)

        #Update the labels with the block data
        self.elevation_in.setText(str(elevation))
        self.grade_in.setText(str(grade))
        self.length_in.setText(str(length1))
        self.block_num_in.setText(str(block_num))
        self.section_in.setText(str(section))




class TestBench(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Track Model/testbench_trackmodel.ui", self)
        self.test_input()

        #Press enter should show output for test outputs
        self.com_speed_in_1.returnPressed.connect(self.test_input)
        self.authority_in.returnPressed.connect(self.test_input)
        self.broken_in.returnPressed.connect(self.test_input)
        self.track_in.returnPressed.connect(self.test_input)
        self.power_in.returnPressed.connect(self.test_input)

        #Enter text through QTCombo from dropdown and output that to testbench
        self.line_in.activated[str].connect(self.test_combo_line)
        self.broken_block.activated[str].connect(self.test_combo_broken)
        self.track_block.activated[str].connect(self.test_combo_track)
        self.power_block.activated[str].connect(self.test_combo_power)

    #Function for inputs/outputs for textboxes
    def test_input(self):
        # Get text from the test inputs for commanded speed
        com_speed = self.com_speed_in_1.text()
        # Set the output text for commanded speed
        self.com_speed_out_1.setText(com_speed)

        # Get text from the test inputs for authority
        authority = self.authority_in.text()
        # Set the output text for authority
        self.authority_out.setText(authority)

        # Get text from the test inputs for broken rail
        broken = self.broken_in.text()
        # Set the output text for broken rail
        self.broken_out.setText(broken)

        # Get text from the test inputs for track circuit failure
        track = self.track_in.text()
        # Set the output text for track circuit failure
        self.track_out.setText(track)

        # Get text from the test inputs for power failure
        power = self.power_in.text()
        # Set the output text for power failure
        self.power_out.setText(power)

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

class Data:
    def __init__(self):
        #Initializing variables
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

    def read_excel(self, filename):
        #read Excel files from DataFrame
        self.df = pd.read_excel("Track_Resources/Blue_Line_Block_Info.xlsx")

        #Extract data from DataFrame of the Excel and assign to variables
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
    # Check if DataFrame is not None
        if self.df is not None:
            # Iterate through the DataFrame of the Ecel file
            for index, row in self.df.iterrows():
                # Check if the block number matches and if so...
                if row['Block Number'] == block_num:
                    # Return the corresponding elevation value of that row
                    return row['ELEVATION (M)']
        return None  # Return None if block number is not found or there is nothing in the Dataframe
    
    def get_grade_for_block(self, block_num):
        #Iterate through the DataFrame of the Ecel file
        if self.df is not None:
            # Iterate through the DataFrame
            for index, row in self.df.iterrows():
                #Check if the block number matches and if so...
                if row['Block Number'] == block_num:
                    # Return the corresponding grade value of that row
                    return row['Block Grade (%)']
        return None  #Return None if block number is not found or there is nothing in the Dataframe
    
    def get_length_for_block(self, block_num):
        #Iterate through the DataFrame of the Ecel file
        if self.df is not None:
            #   Iterate through the DataFrame
            for index, row in self.df.iterrows():
                #Check if the block number matches and if so...
                if row['Block Number'] == block_num:
                    # Return the corresponding block length value of that row
                    return row['Block Length (m)']
        return None  #Return None if block number is not found or there is nothing in the Dataframe
    
    def get_block_for_block(self, block_num):
        #Iterate through the DataFrame of the Ecel file
        if self.df is not None:
            #   Iterate through the DataFrame
            for index, row in self.df.iterrows():
                #Check if the block number matches and if so...
                if row['Block Number'] == block_num:
                    # Return the corresponding block num value of that row
                    return row['Block Number']
        return None  #Return None if block number is not found or there is nothing in the Dataframe
    
    def get_section_for_block(self, block_num):
        #Iterate through the DataFrame of the Ecel file
        if self.df is not None:
            #   Iterate through the DataFrame
            for index, row in self.df.iterrows():
                #Check if the block number matches and if so...
                if row['Block Number'] == block_num:
                    # Return the corresponding section value of that row
                    return row['Section']
        return None  #Return None if block number is not found or there is nothing in the Dataframe
    

    


    ################################
    #Get and set just individual variables. 
    def get_elevation(self):
        return self.elevation
    
    def get_grade(self):
        return self.grade
    
    def get_length(self):
        return self.length1
    
    def get_temp(self):
        return self.temp
    
    def get_heaters(self):
        return self.heaters
    
    def get_occupancy(self):
        return self.occupancy
    
    def get_broken_rail(self):
        return self.broken_rail
    
    def get_circuit_failure(self):
        return self.circuit_failure
    
    def get_power_failure(self):
        return self.power_failure
    
    def get_block_num(self):
        return self.block_num
    
    def get_direction(self): 
        return self.direction
    
    def get_cross(self):
        return self.cross
    
    def set_elevation():
        pass

    def set_grade():
        pass

# Call Main window
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window_2 = TestBench()

    window.show()
    window_2.show()

    sys.exit(app.exec_())

