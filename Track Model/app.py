import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import uic

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Track Model/Track_Model.ui", self)
        self.pushButton.clicked.connect(self.upload_track_layout)  # Connect the button's clicked signal to upload_file method

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

