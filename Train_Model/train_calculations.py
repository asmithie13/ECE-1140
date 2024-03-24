class TrainCalculations:
    def __init__(self, main_window):
        self.main_window = main_window

    def get_power(self, power_input):
        self.main_window.get_power(power_input)

    def Calculate_acceleration(self):
        force = self.calculate_force()
        mass = self.main_window.mass_def
        acceleration = (force / mass) * ((1 / 3.28084) * (1 / 3.28084))
        self.main_window.Acceleration_value_lcd.display(acceleration)
        return acceleration

    def get_acceleration(self):
        acceleration = self.Calculate_acceleration()
        self.main_window.Acceleration_value_lcd.display(acceleration)

    def get_commanded_speed(self, commanded_speed):
        self.main_window.commanded_speed_def = commanded_speed
        self.main_window.cspeed_display.setText(str(commanded_speed))
        self.calculate_force()
        self.Calculate_acceleration()
        self.calculate_acc_velocity()

    def calculate_force(self):
        power = 1000 * (self.main_window.Power_value_lcd.value())
        commanded_speed = self.main_window.commanded_speed_def
        speed_fts = commanded_speed * (5280 / 3600)
        force = power / speed_fts
        return force

    def get_mass(self, mass):
        self.main_window.mass_display.setText(str(mass))
        mass = mass / 2.205
        self.main_window.mass_def = mass
        self.calculate_force()
        self.Calculate_acceleration()
        self.calculate_acc_velocity()

    def calculate_acc_velocity(self):
        acceleration = (3600 * 3600 / 5280) * self.Calculate_acceleration()
        time = self.main_window.time_def
        initial_velocity = 0
        velocity = initial_velocity + (acceleration * time)
        self.main_window.Acc_Velo_value_lcd.display(velocity)
