#Title: Homework 7
#Author: Andrew Ayala

### IMPORT PACKAGES ###
import numpy as np


### DEFINE FUNCTIONS ###

#Define function to be integrated
def f(x):
    return(1/((np.exp(x)+1)*np.sqrt(x)))

#Define w(x) weight function
def w(x):
    return(1/np.sqrt(x))

#Define transform function, which normalizes weight function to values between 0 and 1
#Transorm is constructed by dividing the weight function by it's integral from 0 to 1
#In the case of w(x) = 1/sqrt(x), the resultant transform is x**2
def transform(x):
    return(x*x)

#Define function to calculate Monte Carlo integral
def mcIntegral(x):
    sum = 0
    for i in x:
        sum += f(i)/w(i)*2
    I = (sum/len(x))
    return(I)


### MAIN ###

#Set total number of random x-values
N = 1000000

#Initialize random number generator and create array of random x-values
rng = np.random.default_rng()
x = rng.random(N)

#Create array of transformed random x-values using new probability distribution
newX = transform(x)

#Calculate Monte Carlo integral with transformed x-values
ans = mcIntegral(newX)
print(ans)
