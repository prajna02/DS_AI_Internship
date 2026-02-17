
#Task-2
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "SquareFootage": [600, 750, 900, 1100, 1300, 1500, 1700, 2000, 2300, 2600],
    "Price":         [35, 45, 55, 70, 85, 95, 110, 140, 160, 190],  
    "City": ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi",
             "Bangalore", "Bangalore", "Mumbai", "Delhi", "Mumbai"]
}
df = pd.DataFrame(data)
plt.figure(figsize=(7, 5))
plt.scatter(df["SquareFootage"], df["Price"])
plt.title("Scatter Plot: SquareFootage vs Price")
plt.xlabel("Square Footage")
plt.ylabel("Price (in Lakhs)")
plt.grid(True)
plt.show()
plt.figure(figsize=(7, 5))
df.boxplot(column="Price", by="City")
plt.title("Boxplot: City vs Price")
plt.suptitle("")  
plt.xlabel("City")
plt.ylabel("Price (in Lakhs)")
plt.grid(True)
plt.show()
print("Observation: As SquareFootage increases, Price seems to increase.")