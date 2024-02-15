import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import uic

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Track Model/Track_Model.ui", self)
        self.pushButton.clicked.connect(self.upload_file)  # Connect the button's clicked signal to upload_file method

    def upload_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Upload Track Layout', '', 'Excel Files (*.xlsx);;CSV (*.csv)')
        if file_path:
            self.label.setText("File uploaded successfully")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())