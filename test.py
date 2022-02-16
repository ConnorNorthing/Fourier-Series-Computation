# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 14:38:53 2019

@author: Connor Northing
"""
import numpy as np
from matplotlib import pyplot as plt

t = np.arange(0,1.01,0.01)
func1 = 0
for n in [1]:
    func1 += (4/n*sp.pi)*sp.sin((sp.pi*n)/2)*sp.cos(2*sp.pi*n*t)


func2 =0
for i in [1,2]:
    func2 += (4/n*sp.pi)*sp.sin((sp.pi*n)/2)*sp.cos(2*sp.pi*n*t)

func5 = 0  
for n in np.arange(0,5.1,1):
    func5 += (4/n*sp.pi)*sp.sin((sp.pi*n)/2)*sp.cos(2*sp.pi*n*t)

func10 = 0  
for n in np.arange(0,5.1,1):
    func10 += (4/n*sp.pi)*sp.sin((sp.pi*n)/2)*sp.cos(2*sp.pi*n*t)

plt.figure(1)
plt.plot(t, func1, 'r', label = 'n=1')
plt.plot(t, func2, 'r', label = 'n=2')
plt.plot(t, func5, 'r', label = 'n=5')
plt.plot(t, func10, 'r', label = 'n=10')
plt.show()