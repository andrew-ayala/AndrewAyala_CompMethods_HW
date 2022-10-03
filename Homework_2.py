#Title: Homework 2
#Author: Andrew Ayala

### IMPORT PACKAGES ###
import numpy as np
import matplotlib.pyplot as plt


### DEFINE FUNCTIONS ###
#Define exponential-e function
def f(x):
    return np.e**(-x**2)

#Define a function that numerically integrates using Simpson's rule
def SimpsonIntegral(f, a, b):
    N = 10
    h = (b-a)/N
    S1 = 0.0
    S2 = 0.0
    kRange = np.arange(1,N//2,1)

    for k in kRange:
        S1 += f(a + (2*k-1)*h)
    
    for k in kRange:
        S2 += f(a + 2*k*h)

    y = (1/3) * h * (f(a) + f(b) + 4*S1 + 2*S2)

    return y


### MAIN ###
#Initialiaze constants and arrays
a = 0
b = 3
h = 0.1
x = np.arange(a,b,h)
Ex = []

#Solve E(x) for various x values in range given by exercise
for i in x:
    y = SimpsonIntegral(f, a, i)
    Ex.append(y)

#Plot E(x) vs. x figure
plt.figure(figsize=(8,5))
plt.title("E(x) vs. x")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,Ex)
plt.xlim(x[0],x[-1])
plt.show()

### END ###