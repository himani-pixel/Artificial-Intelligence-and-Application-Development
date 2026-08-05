#Practical_7b
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
print("Libraries Loaded.")
#Load dataset
data = pd.read_csv("student_marks.csv")
print("Dataset Loaded.")
#Input and output
X = data[['Hours']]
Y = data[['Marks']]

#Split dataset
X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size = 0.3 , random_state=1)
print("Dataset splitted successfully.")
#Train model
model = LinearRegression()
model.fit(X_train , Y_train)
print("Model Trainned Successfully.")
#Display accuracy
print("Training Accuracy:",
     round(model.score(X_train , Y_train) * 100 , 2))
print("Testing Accuracy: ",
     round(model.score(X_test , Y_test) * 100 , 2))
new_data = pd.DataFrame({'Hours': [11]})

pred = model.predict(new_data)

print("Predicted Marks for 11 Hours:", round(pred.item(), 2))
