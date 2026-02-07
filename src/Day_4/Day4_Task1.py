# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 10:02:11 2026

@author: DELL
"""

contacts = {"Aioon":9947362718, 
            "Pruthvi":7338362034, 
            "Loft":8967453627, 
            "Prajna":7645372683
            }
print("Contacts:")
print(contacts)
print()
contacts["Pure"]=98574623832
print("Updated contacts:")
print(contacts)
print()
contacts["Aioon"] = 7685947640
print("Number Updated to the existing contact:")
print(contacts)
print()
print(contacts.get("Aioon"))
print()
print(contacts.get("Air", "Air's contact not found"))
print()
for name, number in contacts.items():
    print(f"contact:{name} | phone:{number}")
    