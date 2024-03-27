import sys
from PyQt5 import QtCore

# Fixing file hierarchy issues
import os
import re

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)



class Clock(QtCore.QObject):
    # Define a signal to emit the current time
    current_time_changed = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_time)
        self.time = QtCore.QTime(0, 0, 0)
        self.timer.start(1000)  # Update time every second

    def update_time(self):
        self.time = self.time.addSecs(1)
        current_time = self.time.toString("hh:mm:ss")
        #self.current_time_changed.emit(current_time)

if __name__ == "__main__":
    clock = Clock()
    app = QtWidgets.QApplication(sys.argv)

    # Start the main event loop
    sys.exit(app.exec_())
