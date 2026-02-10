# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 12:35:11 2026

@author: DELL
"""

def calc_rectangle(length, width):
    area = length*width
    perimeter = 2*(length+width)
    return(area, perimeter)
length = int(input("Enter the length of the rectangle:"))
width = int(input("Enter the width of the rectangle:"))
area, perimeter = calc_rectangle(length, width)
print("Area:", area)
print("Perimeter:", perimeter)

