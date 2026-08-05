import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load Dataset
data = pd.read_csv("mnist_test.csv")   # Loaded but not used
digits = load_digits()

# Features and Target
X = digits.data
y = digits.target

# Binary Classification (True if digit is 9)
y = (y == 9)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
   X, y, test_size=0.3, random_state=1
)

# Train Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Accuracy
print("Training Accuracy :", model.score(X_train, y_train) * 100)
print("Testing Accuracy  :", model.score(X_test, y_test) * 100)

# Predict First 20 Test Samples
predictions = model.predict(X_test[:20])

for prediction in predictions:
   if prediction:
       print("Digit is 9")
   else:
       print("Digit is not 9")
