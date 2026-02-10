# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 11:50:43 2026

@author: DELL
"""

billamt = float(input("Total bill amount:"));
totalpeople = int(input("Number of people:"));
share_per_person = billamt/totalpeople;
print(f"Total Bill: {billamt}. Each person pays:{share_per_person}.")
print(type(billamt))
print(type(share_per_person))