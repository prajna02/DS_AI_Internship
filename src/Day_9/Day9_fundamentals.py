#Topic 1
import pandas as pd
s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([10, 20, 30], index = ['a', 'b', 'c'])
print(s1)
print()
print(s2)
print()

#Topic 3
scores = pd.Series([45, 67, 89, 34, 90])
passed = scores[scores>60]
print(passed)
print()


#missing values
data = pd.Series([10, None, 30, None])
print(data.isnull())
print()
print(data.fillna(0))
print()

#
names = pd.Series(['Aioon','loft','PURE'])
print(names.str.lower())
print()
print(names.str.contains('A'))
print()
print(names.str.upper())
print()