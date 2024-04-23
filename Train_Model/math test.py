import math
power=12000 #in watts kgm^2/s^3
power_ms=power*(1000000000)
theta=0.0
mass_lbs=90169.07
mass_kgs=mass_lbs/2.205
grav_force=mass_kgs*9.81*math.sin(theta) #in kgm/ms^2
prev_vel=0
a_n_prev=0
velocity=0
dt=160

try:
            force = (power_ms / velocity) - grav_force #in kgm/ms^2
except ZeroDivisionError:
            velocity=0.1
            force = (power_ms / velocity) - grav_force 

a_n = float(force/mass_kgs)*3.281 #in ft/ms^2

current_speed= prev_vel + ((dt)/2)*(a_n + a_n_prev)

a_n_prev=0
