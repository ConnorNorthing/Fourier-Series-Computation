# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 13:29:02 2019

@author: Connor Northing
"""
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

#Symbol declarations for iterating through the specified amount of components
n = sp.symbols({'n'});

#Question 1
t = np.arange(0.0, 1.1, 0.1)
func1 = np.sin(2*np.pi*t)

plt.figure(1);
plt.plot(t, func1, 'r')
plt.title('Question 1 Trigonometic Fourier Series [Compact Form]')
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

#Question 2

func2 = (4/n*sp.pi)*sp.sin((sp.pi*n)/2)*sp.cos(2*sp.pi*n*t)

plt.figure(2);
ans = 0
for i in [1,2,5,10]:
    ans += func2.subs({'n':i})
    sp.plot(func2, 'r', label = 'n = {}'.format(i))
plt.title('Question 2 Trigonometic Fourier Series [Compact Form]')
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

#Question 3

func3 = (4/(sp.pi*n))*sp.sin(0.1*sp.pi*n)*sp.cos(2*sp.pi*t)
Co = -0.8

plt.figure(3);
plt.plot(t, func3, 'r')
plt.title('Question 3 Trigonometic Fourier Series [Compact Form]')
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

#Question 4

func4 = ("imaginary j"/(2*sp.pi*n))*np.exp("imaginary j"*2*sp.pi*n*t)
Do = 0.5

plt.figure(4);
plt.plot(t, func4, 'r')
plt.title('Question 4 Exponential Fourier Series [Exponential Form]')
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

  

