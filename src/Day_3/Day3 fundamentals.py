# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 12:15:18 2026

@author: DELL
"""

#list example
numbers = [10, 20, 30 ,40]
#tuple example
coordinators= (5, 10)
print(numbers)
print(coordinators)
print()

print("Slicing")
a = [100, 200, 300, 400, 500, 600, 700, 800]
print(a[-3:-1])

print(a[-1:-3])

print(a[1:6:2])

print(a[-6:-1:2])
print()

#Sorting
print("Sorting")
data = [5, 3, 7, 2, 1]
data.sort()
print(data)
data.sort(reverse=True)
print(data)
print()

#append
print("Appending")
data = [3, 4, 5]
data.append(7)
print(data)
print()

#insert 
print("Insert")
data = [ 2, 4, 6]
data.insert(2,7)
print(data)
print()

#extend(Adding another list to the end)
print("Extend")
data = [2, 4, 6]
data.extend([7, 8, 9])
print(data)

