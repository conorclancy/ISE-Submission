# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 17:34:22 2024

@author Conor Clancy for submission for Immersive Software Engineering  
"""

import numpy as np
import matplotlib.pyplot as plt 

#Initial conditions and constants
theta =0.00000000000000000001 #Initial angle with respect to the vertical radius of the circle otherwise particle would not move (Radians)
v=0.0 #top of sphere m/s
R=20 #Radius of the sphere (m)
g=9.8 #Gravitational acceleration m/s2
m=1
dt=.0001 #time step for euler iteration

velocity=[]
theta_values=[]
normal_forces=[]

#Function to update the position of the ball and velocity
def posvel(theta,v,dt):
    a_t=g*np.sin(theta)
#Tangential acceleration to the sphere
    v_new=v+a_t*dt
#Velocity of the ball is updated using previous velocity and acceleration
    theta_new=theta+(v*dt/R)
    return theta_new, v_new

# Euler Method
while True:
    print(theta)
    theta, v = posvel(theta, v, dt)
    normal_force = m * g * np.cos(theta) - (m * v ** 2 / R)
    print(normal_force)
    if normal_force <= 0:
        break
    
    # Append values to lists for plotting
    theta_values.append(np.degrees(theta))
    velocity.append(v)
    normal_forces.append(normal_force)

degrees = np.degrees(theta)
print(degrees)

# Plotting degrees vs normal forces
print(len(velocity))
print(len(theta_values))
plt.figure(figsize=(10, 6))
plt.plot(theta_values, normal_forces, label="Normal Force(N)")
plt.xlabel('Angle(degrees)')
plt.ylabel('Normal Force (Newtons)')
plt.title('Normal Force vs Angle without Friction and Drag')
plt.legend()
plt.show()
