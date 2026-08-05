#Practical 2(code b)
# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
print("Libraries Loaded Successfully.")

# Step 1: Load Dataset
data = pd.read_csv("housing.csv")
print("Dataset Loaded Successfully.\n")

# Step 2: Display First Five Records
print("First Five Records")
print(data.head())

# Step 3: Check Missing Values
print("\nMissing Values")
print(data.isnull().sum())

# Remove Missing Values
data = data.dropna()

# Step 4: Select Independent and Dependent Variables
X = data[['median_income']]
Y = data['median_house_value']

# Step 5: Split Dataset
X_train, X_test, Y_train, Y_test = train_test_split(
   X, Y,
   test_size=0.3,
   random_state=42
)

print("\nDataset Split Successfully.")

# Step 6: Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, Y_train)

# Step 7: Predict House Prices
Y_pred = model.predict(X_test)

# Step 8: Display Results
print("\nCoefficient :", model.coef_[0])
print("Intercept  :", model.intercept_)
print("R2 Score   :", r2_score(Y_test, Y_pred))

# Step 9: Plot Regression Line
plt.figure(figsize=(8,6))

plt.scatter(X_test, Y_test, color='blue', label='Actual Data')

plt.plot(X_test, Y_pred, color='red', linewidth=2, label='Regression Line')

plt.title("Median Income vs Median House Value")
plt.xlabel("Median Income")
plt.ylabel("Median House Value")
plt.legend()

plt.show()
