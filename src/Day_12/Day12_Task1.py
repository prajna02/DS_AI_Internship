# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 17:02:26 2026

@author: DELL
"""

import matplotlib.pyplot as plt
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]
plt.scatter(study_hours, scores)
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.show()