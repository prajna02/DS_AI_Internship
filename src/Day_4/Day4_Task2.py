# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 10:47:09 2026

@author: DELL
"""

row_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
print(row_logs)
unique_users = set(row_logs)
print(unique_users)
print("ID05" in unique_users)
print("Length of row logs: ", len(row_logs))
print("Length of unique users:", len(unique_users))