#Title: Homework 1
#Author: Andrew Ayala

### IMPORT PACKAGES ###
import numpy as np
import math as m
import matplotlib.pyplot as plt



### DEFINE FUNCTIONS ###

#Define function for creating Deltoid Curve
def DeltoidCurve():
    #Initialize arrays to hold theta, x, and y values
    theta = np.linspace(0,2*np.pi,1000)
    x = np.ones(len(theta), dtype=np.float32)
    y = np.ones(len(theta), dtype=np.float32)

    #Loop over each index of x & y arrays to perform maths
    x = 2*np.cos(theta) + np.cos(2*theta)
    y = 2*np.sin(theta) - np.sin(2*theta)
    
    #Plot resulting function
    plt.plot(x, y, color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Deltoid Curve')

#Define function for creating Galilean Spiral
def GalileanSpiral():
    #Initialize arrays to hold theta, r, x, and y values
    theta = np.linspace(0,10*m.pi,5000)
    r = np.ones(len(theta), dtype=np.float32)
    x = np.ones(len(theta), dtype=np.float32)
    y = np.ones(len(theta), dtype=np.float32)

    #Loop over each index of x, y, & r arrays to perform maths
    r = theta**2
    x = r*np.cos(theta)
    y = r*np.sin(theta)

    #Plot resulting function
    plt.plot(x, y, color='green')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Galilean Spiral')

#Define function for creating Fay's Function
def FaysFunction():
    #Initialize arrays to hold theta, r, x, and y values
    theta = np.linspace(0,24*m.pi,24000)
    r = np.ones(len(theta), dtype=np.float32)
    x = np.ones(len(theta), dtype=np.float32)
    y = np.ones(len(theta), dtype=np.float32)

    #Loop over each index of x, y, & r arrays to perform maths
    
    r = np.exp(1)**(np.cos(theta)) - 2*np.cos(4*theta) + np.sin(theta/12.0)**5
    x = r*np.cos(theta)
    y = r*np.sin(theta)

    #Plot resulting function
    plt.plot(x, y, color='blue')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Fay's Function")



### MAIN ###

#Initialize figure to display subplots
fig = plt.figure()

#Create respective sublots using functions defined above
ax1 = fig.add_subplot(131)
ax1.set_aspect('equal')
DeltoidCurve()

ax2 = fig.add_subplot(132)
ax2.set_aspect('equal')
GalileanSpiral()

ax3 = fig.add_subplot(133)
ax3.set_aspect('equal')
FaysFunction()

#Display figure with sublots
plt.tight_layout()
plt.show()

### END ###