import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    "Price": [250000, 270000, 300000, 320000, 350000, 400000,
              450000, 500000, 600000, 750000, 900000, 1200000],
    "City": ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Bangalore",
             "Bangalore", "Mumbai", "Delhi", "Delhi", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=6, density=True, alpha=0.6)
mean = df["Price"].mean()
std = df["Price"].std()
x = np.linspace(df["Price"].min(), df["Price"].max(), 100)
y = (1/(std*np.sqrt(2*np.pi))) * np.exp(-0.5*((x-mean)/std)**2)
plt.plot(x, y)
plt.title("Histogram + Smooth Curve of House Prices")
plt.xlabel("Price")
plt.ylabel("Density")
plt.grid(True)
plt.show()
skewness = df["Price"].skew()
kurtosis = df["Price"].kurt()
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)
city_counts = df["City"].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(city_counts.index, city_counts.values)
plt.title("Count Plot of City")
plt.xlabel("City")
plt.ylabel("Count")
plt.grid(axis="y")
plt.show()


