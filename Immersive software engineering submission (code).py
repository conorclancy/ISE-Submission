# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 14:08:21 2024

@author: conor
"""

#This is a simple code to track the motion of a small RING rolling from the bottom of
#of a circular wire, with an initial speed, and calculating the tangential speed, reaction forces, G-forces, evolution of
#the friction/drag forces. Also total mechanical energy and with friction, how much energy is
#lost to heat via friction and/or drag. We can then calculate as a rollercoaster designer, the required
#height for the initial position of the roller coaster to be launched

import numpy as np
import matplotlib.pyplot as plt



#Function to calculate derivatives including froction and drag
def derivatives(theta, v):
    a_tangential=-g*np.sin(theta)
    F_Friction=-mu*(mass*g*np.cos(theta)*np.sign(v)+mass*v**2/R)
    F_drag=-C*rho*(v**2)*A*np.sign(v)
    #print(F_Friction)
    #print(np.sign(v))
    F_net=-mass*g*np.sin(theta)+F_Friction+F_drag
    dtheta_dt=v/R
    dv_dt=F_net/mass
    return dtheta_dt, dv_dt


#Euler Method to update the position (in radians) and velocity

def euler_step(theta,v,dt):
    dtheta_dt, dv_dt=derivatives(theta,v)
    theta=theta+dtheta_dt*dt
    v=v+dv_dt*dt
    return theta,v

#Lists to store theta, reaction forces, g-force values and mechanical energy

theta_values=[]
normal_forces=[]
g_forces=[]
velocity=[]
Kinetic_En=[]
Potential_En=[]
Total_Energy=[]

# We assume particle come into a circular loop at the bottom. It ias attached to
# the track. We calvulate the initial speed required to traverse the track. As we turn on friction
# and track. We modify h, to get the initial required speed

h=100
R=50.0 #radius of the sphere
g=9.8
mass=1070
dt=0.0001 #time step for the Euler iteration
v=np.sqrt(2*g*h)


mu= 0.0
C=0.0
rho=1.25
A=np.pi*(1)**2 #Cross sectional area of a ring, of diameter 1m   

v=np.sqrt(2*g*h)

theta = 0
print(np.degrees(theta))
Kinetic=0.5*mass*v**2
potential=0.0
#v=.0.0000001
print('hi')

while theta <= 2*np.pi:
    #for theta in range(np.pi,0):
    theta,v = euler_step(theta,v,dt)
    normal_force=mass*g*np.cos(theta)+mass*v**2/R
    g_force=normal_force/(mass*g)
    Potential=mass*g*(R-R*np.cos(theta))
    Kinetic=0.5*mass*(v**2)
    Total=Potential+Kinetic
    
    if normal_force >= 0.1:
        print(np.degrees(theta))
        
    theta_values.append(np.degrees(theta))
    velocity.append(v)
    normal_forces.append(normal_force)
    g_forces.append(g_force)  
    Kinetic_En.append(Kinetic)
    Potential_En.append(Potential)
    Total_Energy.append(Total)

#Plotting degrees vs normal forces
print(len(velocity))
print(len(theta_values))
plt.figure(figsize=(10,6))
plt.plot(theta_values, normal_forces, label="Normal Force(N)")
plt.xlabel('Angle(degrees)')
plt.ylabel('Normal Force (Newtons)')
plt.title('Normal Force vs Angle without Friction and Drag')
plt.legend()
plt.show()

print(len(velocity))
print(len(theta_values))
plt.figure(figsize=(10,6))
plt.plot(theta_values, Total_Energy, label="Total joules for one rotation")
plt.xlabel('Angle(degrees)')
plt.ylabel('Total; Mechanical Energy(J)')
plt.title('Total Mechanical Energy vs Angle Without Friction and Drag')
plt.legend()
plt.show()

print(len(velocity))
print(len(theta_values))
plt.figure(figsize=(10,6))
plt.plot(theta_values, velocity, label="Velocity (m/s)")
plt.xlabel('Angle(degrees)')
plt.ylabel('Tangential Speed (m/s)')
plt.title('Speed vs Angle With Friction')
plt.legend()
plt.show()

print(len(velocity))
print(len(theta_values))
plt.figure(figsize=(10,6))
plt.plot(theta_values, Kinetic_En, label="Velocity (m/s)")
plt.xlabel('Angle(degrees')
plt.ylabel('Kinetic Energy (Joules)')
plt.title('Kinetic Energy vs Angle with Friction')
plt.legend()
plt.show()





