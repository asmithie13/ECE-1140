import serial
import struct

# Open serial port
ser = serial.Serial('/dev/ttyS0', 115200)  # Adjust the serial port as needed
prevError = 0
prevUk=0
while True:
    # Read data if available
    if ser.in_waiting >= 24:  # 6 integers * 4 bytes each
        data = ser.read(24)
        dt, cmd_spd, cur_spd, ki, kp, accel_pct = struct.unpack('6i', data)

        # Calculate error, uk, and power based on the received values
        error = cmd_spd*.00044704 - cur_spd*.00044704
        uk = prevUk + (error+prevError) * dt / 2  # Simplified for demonstration; integrate properly in production
        power0 = int((kp * error + ki * uk) * (accel_pct / 100.0))
        power1 = int((kp * error + ki * uk) * (accel_pct / 100.0))
        power2 = int((kp * error + ki * uk) * (accel_pct / 100.0))
        
        if(power0 == power1 and power1 == power2 and power2==power0):
            power=power1
        else:
            power = 0
        
        prevError = error
        prevUk = uk

        # Ensure power is within bounds
        power = max(0, min(power, 120000))

        # Send back the calculated power
        ser.write(struct.pack('i', power))
        #print(f"Sent power back: {power}")