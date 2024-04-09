from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject, QDateTime, QThread
import time

class SimulationTime(QObject):
    timeChanged = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.sim_speed_factor = 1.0
        self.simulation_elapsed = 0
        self.last_update_time = QtCore.QDateTime.currentDateTime()
        self.running = False
        self.start_time = QtCore.QDateTime(QtCore.QDate(1970, 1, 1), QtCore.QTime(0, 0, 0, 0))
        

    def set_sim_speed(self, speed):
        self.sim_speed_factor = speed

    def pause(self,pause):
        self.running = not pause

    def start(self):
        self.running = True
        self.updatetime()
        
    def updatetime(self):
    # Set starting point to a QDateTime object representing midnight with no date (time only)
        while self.running:
            current_time = QtCore.QDateTime.currentDateTime()
        
            elapsed = self.last_update_time.msecsTo(current_time)
            
            self.last_update_time = current_time
            
            self.simulation_elapsed += elapsed * self.sim_speed_factor / 10.0
            
            # Add the elapsed simulation time to the start time
            simulated_time = self.start_time.addMSecs(int(self.simulation_elapsed * 10))
            
            self.timeChanged.emit(simulated_time.toString("hh:mm:ss.zzz"))
            
            #print(simulated_time.toString("hh:mm:ss.zzz"))
            QtCore.QThread.msleep(100)  # Sleep for 1 millisecond
