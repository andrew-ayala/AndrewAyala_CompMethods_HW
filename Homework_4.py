#Title: Homework 4
#Author: Andrew Ayala

### IMPORT PACKAGES ###
import numpy as np
import scipy.constants as sp
import matplotlib.pyplot as plt


### DEFINE FUNCTIONS ###
def f(r): 
   return G*M*(R**2) - 2*G*M*R*r + G*M*(r**2) - G*m*(r**2) - (omega**2)*(R**2)*(r**3) + 2*(omega**2)*R*(r**4) - (omega**2)*(r**5)
def fprime(r): 
   return -2*G*M*R + 2*G*M*r - 2*G*m*r - 3*(omega**2)*(R**2)*(r**2) + 8*(omega**2)*R*(r**3) - 5*(omega**2)*(r**4)

### MAIN ###
#Define constants
G = 6.674e-11 
M = 5.974e24
m = 7.348e22 
R = 3.844e8 
omega = 2.662e-6

#Create array of r-values
r=np.linspace(0,R,1000)

#Create figure for plots
fig = plt.figure()

#Create plots showing function results for various r-values
ax1 = fig.add_subplot(121)
plt.plot(r,f(r))
plt.xlabel("r (meters)")
plt.ylabel("f(r)")
plt.title("Lagrange Point Function")

ax2 = fig.add_subplot(122)
plt.plot(r,fprime(r))
plt.xlabel("r (meters)")
plt.ylabel("f'(r)")
plt.title("Derivitive of Lagrange Point Function")

plt.tight_layout()
plt.show()

#Implement Newton's Method to retrieve L1 Lagrange point
errorLimit = 1e-4
error = 1
x1 = 1000
print('\nRoot | Error | Function Value') 

while error > errorLimit: 
   x2 = x1 - (f(x1)/fprime(x1)) 
   error = np.abs(x2-x1) 
   x1 = x2 
   print('{:.4e} | {:.4e} | {:.4e}'.format(x2, error, f(x2)))

print('\nL1 Lagrange point is at {:.4e} meters\n'.format(x1))

## END ###