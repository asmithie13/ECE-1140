import sys
import os 

# Using Block Class as a seperate file
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)


from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QComboBox, QHBoxLayout, QWidget, QLabel, QPushButton, QSizePolicy
from PyQt5 import uic
from PyQt5.QtCore import Qt  
from Track_Resources.Block import Block

# Define the Block class
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Track Model/Track_Model.ui", self)
        self.pushButton.clicked.connect(self.upload_track_layout)  # Connect the button's clicked signal to upload_file method

        # Connect button to method
        self.offButton_1.clicked.connect(self.toggle_button_state)
        self.offButton_2.clicked.connect(self.toggle_button_state_2)
        self.offButton_3.clicked.connect(self.toggle_button_state_3)

        # Set default state for toggle button
        self.offButton_1.setText("OFF")
        self.offButton_1.setStyleSheet("background-color: red;")

        self.offButton_2.setText("OFF")
        self.offButton_2.setStyleSheet("background-color: red;")

        self.offButton_3.setText("OFF")
        self.offButton_3.setStyleSheet("background-color: red;")

    def toggle_button_state(self):
        # Toggle button state and color button 1
        if self.offButton_1.text() == "OFF":
            self.offButton_1.setText("ON")
            self.offButton_1.setStyleSheet("background-color: green;")
        else:
            self.offButton_1.setText("OFF")
            self.offButton_1.setStyleSheet("background-color: red;")

    def toggle_button_state_2(self):
        # Toggle button state and color button 2
        if self.offButton_2.text() == "OFF":
            self.offButton_2.setText("ON")
            self.offButton_2.setStyleSheet("background-color: green;")
        else:
            self.offButton_2.setText("OFF")
            self.offButton_2.setStyleSheet("background-color: red;")

    def toggle_button_state_3(self):
        # Toggle button state and color button 3
        if self.offButton_3.text() == "OFF":
            self.offButton_3.setText("ON")
            self.offButton_3.setStyleSheet("background-color: green;")
        else:
            self.offButton_3.setText("OFF")
            self.offButton_3.setStyleSheet("background-color: red;")
        
    def upload_track_layout(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Upload Track Layout', '', 'Excel Files (*.xlsx);;CSV (*.csv)')
        if file_path:
            self.label.setText("File uploaded successfully")


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
        self.elevation = None
        self.grade = None
        self.length1 = None
        self.temp = None
        self.heaters = None
        self.occupancy = None
        self.broken_rail = None
        self.circuit_failure = None
        self.power_failure = None
        self.block_num = None
        self.direction = None
        self.cross = None

    def get_elevation(self):
        #start it bro
        pass
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window_2 = TestBench()

    window.show()
    window_2.show()

    sys.exit(app.exec_())

