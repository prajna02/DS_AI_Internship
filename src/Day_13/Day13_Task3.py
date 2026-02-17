
#Task-3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "SquareFootage": [600, 750, 900, 1100, 1300, 1500, 1700, 2000, 2300, 2600],
    "Bedrooms":      [1, 2, 2, 3, 3, 3, 4, 4, 4, 5],
    "Bathrooms":     [1, 1, 2, 2, 2, 3, 3, 3, 4, 4],
    "Price":         [35, 45, 55, 70, 85, 95, 110, 140, 160, 300]  # outlier at 300
}
df = pd.DataFrame(data)
corr_matrix = df.corr(numeric_only=True)
print("Correlation Matrix:\n")
print(corr_matrix)
plt.figure(figsize=(7, 5))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()
high_corr_pairs = []
for i in range(len(corr_matrix.columns)):
    for j in range(i + 1, len(corr_matrix.columns)):
        value = corr_matrix.iloc[i, j]
        if value > 0.8:
            high_corr_pairs.append((corr_matrix.columns[i], corr_matrix.columns[j], value))

print("\nHighly correlated pairs (> 0.8):")
for pair in high_corr_pairs:
    print(pair)
plt.figure(figsize=(6, 4))
sns.boxplot(y=df["Price"])
plt.title("Boxplot for Outliers in Price")
plt.ylabel("Price")
plt.show()