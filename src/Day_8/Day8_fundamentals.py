# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 10:05:33 2026

@author: DELL
"""

#Addition
import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10,20,30])
result = a+b
print(result)
print()
#Vectorized vs loop
arr = np.random.randint(100000)
print(arr)
#Vectorized
squared = arr**2
print(squared)
print()


#array creation
import numpy as np
a = np.array([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])
print(a)
print()
b = np.array([[10, 11],
              [13, 14]])
print(b)
print()
c = np.array([16, 17, 18])
print(c)
print()
d = np.array([])
print(d)
print()

#Reshape
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print(reshaped)
print()

#vstack
a = np.array([1, 2])
b = np.array([3, 4])
vstacked = np.vstack((a, b))
print(vstacked)
print()
hstacked = np.hstack((a, b))
print(hstacked)
print()

#mean, median, mode
data = np.array([[10, 20, 30],
                 [40, 50, 60]])
print(np.mean(data))
print(np.mean(data, axis = 0))
print(np.mean(data, axis = 1))
print()

arr = np.linspace(0, 3, 5)
print(arr)
print()

arr = np.random.rand(2, 3)
print(arr)
print()


arr = np.array([1.2, 2.8, -3.7])
print(np.floor(arr))