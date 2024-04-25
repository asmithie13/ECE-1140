from Train_Controller_SW.mainControl import Ui_MainWindow
import serial
import struct
import time

class Vital_Power():
    def __init__(self,ui, curr_power_sig):
        self.ui = ui

        self.local_clock = 0

        self.Ki = 0
        self.Kp = 0
        self.power = 0
        self.power0 = 0
        self.power1 = 0
        self.power2 = 0
        self.time = 0
        self.dt = 0
        self.error = 0
        self.uk = 0
        self.prevError = 0
        self.prevUk = 0
        self.prevTime = 0

        self.curr_power_sig = curr_power_sig
        #self.ser = serial.Serial('COM5', 57600)  # Replace 'COM6' with your actual port name

    def Control_Ki(self):
            self.ui.lcdKi.display(self.ui.inputKi.value())
            self.Ki = self.ui.inputKi.value()

    def Control_Kp(self):
            self.ui.lcdKp.display(self.ui.inputKp.value())
            self.Kp = self.ui.inputKp.value()

    def Set_Clock(self, time):
         self.local_clock = time
    
    """
    def calculate_power(self):
        self.time = self.local_clock
        self.dt = (self.time - self.prevTime)/1000
        self.prevTime = self.time
        
        
        if self.ui.Ebrake.isChecked():
           self.power = 0
        
        elif self.ui.vertSliderBrk.value() == 1:
            self.power = 0
        
        elif self.ui.vertSliderPow.value() == 0:
            self.power = 0

        else:
            self.error = float(self.ui.lcdCmdSpd.value()) * 0.00044704 - float(self.ui.lcdCurSpd.value()) * 0.00044704
            #has dt
            self.uk = self.prevUk + (self.error + self.prevError) * (self.dt / 2)
            self.prevError = self.error
            self.prevUk = self.uk

            self.power0 = (float(self.ui.lcdKp.value()) * self.error + float(self.ui.lcdKi.value()) * self.uk) * (float(self.ui.vertSliderPow.value()) / 100.0)
            self.power1 = (float(self.ui.lcdKp.value()) * self.error + float(self.ui.lcdKi.value()) * self.uk) * (float(self.ui.vertSliderPow.value()) / 100.0)  
            self.power2 = (float(self.ui.lcdKp.value()) * self.error + float(self.ui.lcdKi.value()) * self.uk) * (float(self.ui.vertSliderPow.value()) / 100.0)

            if(self.power0 == self.power1 or self.power1 == self.power2 or self.power0 == self.power2):
                if(self.power0 == self.power1):
                    self.power = self.power0
                elif(self.power1 == self.power2):
                    self.power = self.power1
                elif(self.power0 == self.power2):
                    self.power = self.power0
            else: 
                self.power = 0
            
            if self.power > 120000: 
                self.power = 120000
            elif self.power < 0:
                self.power = 0
        
        self.ui.lcdPowOut.display(self.ui.vertSliderPow.value())
        self.ui.lcdBrk.display(self.ui.vertSliderBrk.value())
        self.ui.lcdAcel.display(self.power)
        self.curr_power_sig.emit(int(self.power))

    """

    def calculate_power(self):
        self.ser = serial.Serial('COM6', 115200)  # Replace 'COM6' with your actual port name
        if self.ui.Ebrake.isChecked():
           self.power = 0

        elif self.ui.vertSliderBrk.value() == 1:
            self.power = 0

        elif self.ui.vertSliderPow.value() == 0:
            self.power = 0

        else:
            self.time = self.local_clock
            self.dt = self.time - self.prevTime
            self.prevTime = self.time

            cmd_spd = self.ui.lcdCmdSpd.value()  # commanded speed
            cur_spd = self.ui.lcdCurSpd.value()  # current speed
            ki = self.ui.lcdKi.value()  # integral gain
            kp = self.ui.lcdKp.value()
            accel_pct = self.ui.lcdPowOut.value()

            # Pack the values into a byte string. The format string '6i' means six integers.
            data = struct.pack('6i', self.dt, cmd_spd, cur_spd, ki, kp, accel_pct)

            try:
                # Send the packed data
                self.ser.write(data)
                #print("Sent data to Raspberry Pi")

                # Wait for the response
                while self.ser.in_waiting < 4:
                    self.wait = True

                # Assuming the response is also an integer
                response_data = self.ser.read(4)  # Read 4 bytes (size of an integer)
                self.power = struct.unpack('i', response_data)[0]
                #print(f"Received power from Raspberry Pi: {power}")
            finally:
                self.ser.close()  # Make sure to close the serial port

            self.ui.lcdPowOut.display(self.ui.vertSliderPow.value())
            self.ui.lcdBrk.display(self.ui.vertSliderBrk.value())
            self.ui.lcdAcel.display(self.power)
            self.curr_power_sig.emit(int(self.power))
    

    def Control_Accelleration(self):
        self.ui.lcdPowOut.display(self.ui.vertSliderPow.value())
        if(self.ui.vertSliderPow.value() > 0):
            self.ui.vertSliderBrk.setValue(0)
            self.ui.lcdBrk.display(self.ui.vertSliderBrk.value())   