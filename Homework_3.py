#Title: Homework 3
#Author: Andrew Ayala

### IMPORT PACKAGES ###
import numpy as np
import scipy.constants as sp
import matplotlib.pyplot as plt


### MAIN ###

#Set constants of grid and charges
##Grid constants
L = 1
N = 100
d = 0.1
h = L/N
##Charge constants and positions
k = 1/(4*sp.pi*sp.epsilon_0)
q1 = 1
q2 = -1
x1 = (N/2 - (d/L)/2)
x2 = (N/2 + (d/L)/2)
y1 = N/2
y2 = N/2

#Initialize arrays for scalar and vector quantities
x = np.arange(0,L,h)
y = np.arange(0,L,h)
V = np.zeros([N,N], dtype=float)
Ex = np.zeros([N,N], dtype=float)
Ey = np.zeros([N,N], dtype=float)

#Loop over scalar/vector arrays and calculate local values
for i in range(N):
    for j in range(N):
        V[j,i] = q1*k/(np.sqrt((x1-i)**2 + (y1-j)**2))
        V[j,i] += q2*k/(np.sqrt((x2-i)**2 + (y2-j)**2))

for i in range(N-1):
    for j in range(N-1):
        Ex[j,i] = (V[j,i+1]-V[j,i])/h
        Ey[j,i] = (V[j+1,i]-V[j,i])/h

#Create figure for plots
fig = plt.figure()

ax1 = fig.add_subplot(121)
ax1.set_aspect('equal')
plt.imshow(V, extent=(0,L,0,L), vmin=-4e6, vmax=4e6)
plt.colorbar()
plt.xlabel("x (meters)")
plt.ylabel("y (meters)")
plt.title("Electric Potential")

ax2 = fig.add_subplot(122)
ax2.set_aspect('equal')
ax2.set_xlim(0,L)
ax2.set_ylim(0,L)
plt.streamplot(x, y, Ex, Ey, density=1.5)
plt.xlabel("x (meters)")
plt.ylabel("y (meters)")
plt.title("Electric Field")

plt.tight_layout()
plt.show()

### END ###