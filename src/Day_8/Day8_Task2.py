# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 12:12:14 2026

@author: DELL
"""

import numpy as np

data = np.arange(24)

reshaped = data.reshape(4, 3, 2)

print("Shape after reshape:", reshaped.shape)

final_array = reshaped.transpose(0, 2, 1)

print("Final shape:", final_array.shape)

# Output array
print("\nFinal Array:\n", final_array)


