class SimulationTime(QObject):
    timeChanged = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.sim_speed_factor = 1.0
        self.simulation_elapsed = 0
        self.last_update_time = QDateTime.currentDateTime()
        self.current_time = 0
        self.running = True

    def start(self): 
        self.running = True

    def cancel(self):
        self.running = False

    def stop(self):
        self.pause_sim_speed_factor = self.sim_speed_factor
        self.sim_speed_factor = 0

    def restart(self):
        self.sim_speed_factor = self.pause_sim_speed_factor

    def pause(self,clicked):
        if clicked :
            self.stop()
        else :
            self.restart()

    def get_running(self):
        return self.running

    def set_sim_speed(self, factor: int):
        self.sim_speed_factor = factor

    def get_speed_factor(self):
        return self.sim_speed_factor
    
    def updatetime(self):
        while self.running:
            current_time = QDateTime.currentDateTime()
            elapsed = self.last_update_time.msecsTo(current_time)
            self.last_update_time = current_time
            # Increment the simulation time by the elapsed time times the speed factor
            self.simulation_elapsed += elapsed * self.sim_speed_factor / 1000.0  # Convert to seconds
            # Format the simulation time
            simulatedtime = QDateTime.fromMSecsSinceEpoch(int(self.simulation_elapsed * 1000))
            self.current_time = simulatedtime.toString("hh:mm:ss.zzz") #hh:mm:ss.zzz for milliseconds
            self.timeChanged.emit(self.current_time)
            time.sleep(0.001) # update every millise