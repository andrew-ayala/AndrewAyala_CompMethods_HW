#Title: Homework 8
#Author: Andrew Ayala

### IMPORT PACKAGES ###
import numpy as np
import matplotlib.pyplot as plt
import random as r


### DEFINE FUNCTIONS ###

#Define function for calculating valocity and accelration for sphere with air resitance
def f(r, t, R, rho, m):
    g = 9.8
    C = 0.47
    x, y, vx, vy = r
    v = np.sqrt(vx**2 + vy**2)
    d = (np.pi * (R**2) * rho * C) * 0.5
    dvx = -d * vx * v / m
    dvy = (-d * vy * v / m) - g
    return(np.array([vx, vy, dvx, dvy]))

#Define function for calculating using 4th Order Runge Kuta
def RungeKuta4Order(f, r, R, rho, m, a, b, N=1000):
    h = (b - a) / N
    timeArray = np.linspace(a, b, N)
    ans = np.empty((len(timeArray), 4))
    for i, t in enumerate(timeArray):
        ans[i, :] = r
        k1 = h * f(r, t, R, rho, m)
        k2 = h * f(r + (0.5 * k1), t + (0.5 * h), R, rho, m)
        k3 = h * f(r + (0.5 * k2), t + (0.5 * h), R, rho, m)
        k4 = h * f(r + k3, t + h, R, rho, m)
        r += (k1 + (2 * k2) + (2 * k3) + k4) / 6
    return ans


### MAIN ###

#Set constant values
rho = 1.22
R = 0.08
massArray = np.arange(1, 101, 10)

#Loop through mass array and calculate trajectories
for i in massArray:
    r = np.array([0, 0, (100 * np.cos(30 * np.pi / 180)),
                  (100 * np.sin(30 * np.pi / 180))])
    z = RungeKuta4Order(f, r, R, rho, i, 0, 10)
    x = z[:, 0]
    y = [j for j in z[:, 1] if j > 0]
    plt.plot(x[:len(y)], y, label="Mass = {}kg".format(i))

#Set constant values
g = -9.8
v = 100
theta = 30 * np.pi / 180
t = np.linspace(0, 15, 100)

#Calculate velocity and acceleration components
x_0 = (v * np.cos(theta)) * t
y_0 = (v * np.sin(theta) * t) + (0.5 * g * t * t)
z_0 = [i for i in y_0 if i > 0]

#Plot results for various masses and trajectories
plt.plot(x_0[:len(z_0)], z_0, color="k", label="Ignores Air Resistance")
plt.xlabel("X(m)")
plt.ylabel("Y(m)")
plt.title("Displacement of a Cannonball with Different Masses")
plt.legend(fontsize="small")
plt.show()