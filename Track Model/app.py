import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QComboBox, QHBoxLayout, QWidget, QPushButton, QSizePolicy
from PyQt5 import uic
from PyQt5.QtCore import Qt  

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Track Model/Track_Model.ui", self)
        self.pushButton.clicked.connect(self.upload_track_layout)  # Connect the button's clicked signal to upload_file method

        # Get the central widget of the QMainWindow
        central_widget = self.centralWidget()
        
        # Create a QHBoxLayout for the central widget
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignTop)  # Align to the top
        
       # Dropdown menu for block selection
        block_selection = QComboBox()
        block_selection.addItems(['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15']) 
        block_selection.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Set size policy to fixed
        block_selection.setFixedWidth(189)  # Set fixed width
        layout.addWidget(block_selection)

        # Dropdown menu for line selection
        line_selection = QComboBox()
        line_selection.addItems(['Blue']) 
        line_selection.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Set size policy to fixed
        line_selection.setFixedWidth(189)  # Set fixed width
        layout.addWidget(line_selection)

        # Set spacing between widgets
        layout.setSpacing(10)
        
        # Set the layout for the central widget
        central_widget.setLayout(layout)

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

