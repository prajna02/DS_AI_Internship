
#Task-3

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

np.random.seed(42)

X = np.arange(1, 51).reshape(-1, 1)
y = 3*(X[:, 0]**2) + 5*X[:, 0] + 10 + np.random.normal(0, 200, size=50)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
y_pred_linear = linear_model.predict(X_test)
r2_linear = r2_score(y_test, y_pred_linear)

poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(X_poly, y, test_size=0.2, random_state=42)

poly_model = LinearRegression()
poly_model.fit(X_train_p, y_train_p)
y_pred_poly = poly_model.predict(X_test_p)
r2_poly = r2_score(y_test_p, y_pred_poly)

print("R² Score (Original Features):", r2_linear)
print("R² Score (Polynomial Features degree=2):", r2_poly)