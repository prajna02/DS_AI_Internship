
#Task-2

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.DataFrame({
    "Age": [22, 25, 28, 30, 35, 40, 45, 50],
    "Salary": [25000, 30000, 45000, 50000, 65000, 80000, 100000, 120000]
})

standard_scaler = StandardScaler()
minmax_scaler = MinMaxScaler()

df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)

df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist(df["Salary"], bins=6)
plt.title("Salary Before Scaling")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
plt.hist(df_standardized["Salary"], bins=6)
plt.title("Salary After StandardScaler")
plt.xlabel("Scaled Salary")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()