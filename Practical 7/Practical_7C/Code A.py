import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load Dataset
digits = load_digits()
print("Dataset Loaded.")

# Features and Target
X = digits.data
Y = digits.target

# Binary Classification (True if digit is 5)
Y = (Y == 5)

# Split Dataset
X_Train, X_Test, Y_Train, Y_Test = train_test_split(
   X, Y, test_size=0.3, random_state=1
)

print("Dataset Split Successfully.")

# Train Model
model = LogisticRegression(max_iter=1000)
model.fit(X_Train, Y_Train)

# Accuracy
print("Training Accuracy:", model.score(X_Train, Y_Train) * 100)
print("Testing Accuracy :", model.score(X_Test, Y_Test) * 100)

# Predict First Test Sample
prediction = model.predict([X_Test[0]])

if prediction[0]:
   print("Digit is 5")
else:
   print("Digit is not 5")
