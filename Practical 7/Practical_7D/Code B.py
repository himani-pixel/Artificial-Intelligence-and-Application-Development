#7.4.B
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsRegressor

print("Libraries Loaded.")

# Load Dataset
df = pd.read_csv("housing.csv")
print("Dataset Loaded.")

# Remove rows with missing values
df = df.dropna()

# Convert categorical column into numeric values
df = pd.get_dummies(df, columns=["ocean_proximity"], drop_first=True)

# Features and Target
X = df.drop("median_house_value", axis=1)
y = df["median_house_value"]

# Create KNN Regression Model
model = KNeighborsRegressor()

# Apply 5-Fold Cross Validation
scores = cross_val_score(model, X, y, cv=5, scoring="r2")

# Print Results
print("\nR² Score for each fold:")
print(scores)

print("\nAverage R² Score:", round(scores.mean(), 4))
