import math
power=120000 #in watts kgm^2/s^3
#power_ms=power*(1000000000)
theta=0.0
mass_lbs=90169.07
mass_kgs=mass_lbs/2.205
grav_force=mass_kgs*9.81*math.sin(theta) #in kgm/ms^2
prev_vel=0
a_n_prev=0
velocity=0
dt= 160

while(1):
    try:
        force = (power / velocity) - grav_force #in kgm/ms^2
        print("Force", force)
    except ZeroDivisionError:
        velocity=0.1
        force = (power / velocity) - grav_force 
        print("Force", force)

    a_n = force/mass_kgs*3.281 #in ft/ms^2
    print("Acceleration", a_n)

    velocity = prev_vel + ((dt)/2)*(a_n + a_n_prev)

    print("Current Speed", velocity)
    a_n_prev=a_n 
    prev_vel = velocity

