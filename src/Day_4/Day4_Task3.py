# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 11:00:45 2026

@author: DELL
"""

friend_a = {"Python", "Cooking", "Hiking", "Movies"}
print(friend_a)
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
print(friend_b)
print()

shared_interests = friend_a & friend_b


all_interests = friend_a | friend_b

unique_to_a = friend_a - friend_b

print("Shared Interests:", shared_interests)
print("All Interests:", all_interests)
print("Unique interests:", unique_to_a)

