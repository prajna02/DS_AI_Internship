# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 19:26:19 2026

@author: DELL
"""

import csv

with open("Students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for name, grade, status in reader:
        if status == "Pass":
            print(name)