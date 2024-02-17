import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QComboBox, QHBoxLayout, QWidget, QPushButton, QSizePolicy
from PyQt5 import uic
from PyQt5.QtCore import Qt  # Import Qt

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
        line_selection.addItems(['Blue', 'Green', 'Red']) 
        line_selection.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Set size policy to fixed
        line_selection.setFixedWidth(189)  # Set fixed width
        layout.addWidget(line_selection)

        # Set spacing between widgets
        layout.setSpacing(10)
        
        # Set the layout for the central widget
        central_widget.setLayout(layout)
        
    def upload_track_layout(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Upload Track Layout', '', 'Excel Files (*.xlsx);;CSV (*.csv)')
        if file_path:
            self.label.setText("File uploaded successfully")

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
    window.show()
    sys.exit(app.exec_())

