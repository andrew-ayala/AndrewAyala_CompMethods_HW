#Title: Homework 5
#Author: Andrew Ayala

### IMPORT PACKAGES ###
import sys
import numpy as np
import scipy.constants as sp
import matplotlib.pyplot as plt
import argparse

### ARGUMENT PARSER ###

parser = argparse.ArgumentParser(prog='FourierAnalysis', description='Calculate Fourier Transform of input function')
parser.add_argument('dowData', metavar='F1', type=str, nargs=1, help='File or path for DFT input')
parser.add_argument('dow2Data', metavar='F2', type=str, nargs=1, help='File or path for DCT input')
parser.add_argument('per', metavar='N', type=int, nargs=1, help='Percentage of coeffients to reduce for smoothing. Greater N equals greater smoothing')

args = parser.parse_args()
### DEFINE FUNCTIONS ###

#Function for Discrete Cosine Transform
def dct(y):
    N = len(y)
    y2 = np.empty(2*N,float)
    y2[:N] = y[:]
    y2[N:] = y[::-1]

    c = np.fft.rfft(y2)
    phi = np.exp(-1j*np.pi*np.arange(N)/(2*N))
    return np.real(phi*c[:N])

#Function for Inverse Cosine Transform
def idct(a):
    N = len(a)
    c = np.empty(N+1,complex)

    phi = np.exp(1j*np.pi*np.arange(N)/(2*N))
    c[:N] = phi*a
    c[N] = 0.0
    return np.fft.irfft(c)[:N]


### MAIN ###

#7.4
#a)
#Download Dow data and create figure plot
<<<<<<< HEAD
file = args.dowData
dowData = np.loadtxt(file[0], dtype=float)
# print(dowData)
=======
dowData = np.loadtxt(args.dowData)
>>>>>>> abc994c2ed5dacf831cc2a4e6bbb65d6923ee305
figure1 = plt.figure()
plt.plot(dowData)
plt.xlabel("Day")
plt.ylabel("Dow Closing Value")
plt.title("Dow 2007-2011")
figure1.show

#Calculate transform coefficients
#b)
dowCoeff = np.fft.rfft(dowData)
print("Dow Data FFT Coefficients:\n", dowCoeff, "\n")

#Set last 90% of coefficients to zero
#c)
N = len(dowCoeff)
dowCoeff[N//10:] = 0.0
print("Dow Data 90% Reduced FFT Coefficients:\n", dowCoeff, "\n")

#Recreate original function by calculating inverse transform
#Resultant function is smoothed out version of original input function
#d)
data2 = np.fft.irfft(dowCoeff)
plt.plot(data2)

#Repeat inverse transform, setting last 98% of coefficients to zero
#e)
<<<<<<< HEAD
perInput = args.per
fraction = 1 - perInput[0]/100
=======
fraction = 1 - args.per/100
>>>>>>> abc994c2ed5dacf831cc2a4e6bbb65d6923ee305
dowCoeff[int(N*fraction):] = 0.0
data3 = np.fft.irfft(dowCoeff)
plt.plot(data3)
plt.show()
<<<<<<< HEAD
#Reducing the last 90% of coefficients to zero restricts the FFTvto the most dominant periodic frequency signals in our input function.
=======
#Reducing the last 90%\ of coefficients to zero restricts the FFTvto the most dominant periodic frequency signals in our input function.
>>>>>>> abc994c2ed5dacf831cc2a4e6bbb65d6923ee305
#Thus, removing all the jitter in our original function and returning a smoothed out signal


#7.6
#a)
#Download Dow2 data and create figure plot
<<<<<<< HEAD
file2 = args.dow2Data
dow2Data = np.loadtxt(file2[0], dtype=float)
=======
dow2Data = np.loadtxt(args.dow2Data, float)
>>>>>>> abc994c2ed5dacf831cc2a4e6bbb65d6923ee305
figure2 = plt.figure()
plt.plot(dow2Data)
plt.xlabel("Day")
plt.ylabel("Dow Closing Value")
plt.title("Dow 2004-2008")
figure2.show()

#Calculate transform coefficients and set last 90% of coefficients to zero
dow2Coeff = np.fft.rfft(dow2Data)
N = len(dow2Coeff)
<<<<<<< HEAD
dow2Coeff[N//10:] = 0.0
=======
dow2Coeff[N//50:] = 0.0
>>>>>>> abc994c2ed5dacf831cc2a4e6bbb65d6923ee305

#Recreate function using inverse transform
newDow2Data = np.fft.irfft(dow2Coeff)
plt.plot(newDow2Data)
plt.show()

#b)
#Create transform coefficients for cosine transform. Use inverse cosine transform to retrieve original function
dow2Coeff = dct(dow2Data)
<<<<<<< HEAD
fraction = 1 - perInput[0]/100
=======
fraction = 1 - args.per/100
>>>>>>> abc994c2ed5dacf831cc2a4e6bbb65d6923ee305
dow2Coeff[int(N*fraction):] = 0.0
newDow2Data = idct(dow2Coeff)
plt.plot(newDow2Data)
plt.show()
