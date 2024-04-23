import math
power= 20000 #in watts kgm^2/s^3
#power_ms=power*(1000000000)
theta=0.0
mass_lbs=90169.07
mass_kgs=mass_lbs/2.205
grav_force=mass_kgs*9.81*math.sin(theta) #in kgm/ms^2
prev_vel=0
a_n_prev=0
velocity=0
dt= .0160
i = 0

while(1):
    try:
        
        force = (power/velocity) - grav_force #in kgm/ms^2
        print("Force", force)
    except ZeroDivisionError:
        force = 10000
        print("Force", force)

    a_n = force/mass_kgs #in m/ms^2
    if a_n > 0.5:
        a_n = 0.5
    print("Acceleration", a_n)

    velocity = prev_vel + ((dt)/2)*(a_n + a_n_prev)

    print("Current Speed in m/s", velocity)
    print("Current Speed in ml/hr", velocity*2.237)
    a_n_prev=a_n 
    prev_vel = velocity
    i+= 1

