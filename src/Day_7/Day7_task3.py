# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 19:28:00 2026

@author: DELL
"""

filename=input("Enter your filename:");
try:
    with open("config.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Oops! That file doesn't exist yet");