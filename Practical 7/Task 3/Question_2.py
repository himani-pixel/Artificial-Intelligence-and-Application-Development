import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.DataFrame({
   'Employee_ID': [101,102,103,104,105,106,107,108,109,110],
   'Employee_Age': [22,24,26,28,30,32,34,36,38,40],
   'Years_of_Experience': [1,2,3,4,5,6,7,8,9,10],
   'Salary': [25000,30000,35000,40000,45000,50000,55000,60000,65000,70000]
})

X = data[['Years_of_Experience']]
y = data['Salary']

X_train, X_test, y_train, y_test = train_test_split(
   X, y, test_size=0.3, random_state=1
)

model = LinearRegression()
model.fit(X_train, y_train)

new_data = pd.DataFrame([[7]], columns=['Years_of_Experience'])
pred = model.predict(new_data)

print("Predicted Salary for 7 Years of Experience :", round(pred[0],2))
print("Slope (Coefficient) :", model.coef_[0])
print("Intercept :", model.intercept_)
print("R2 Score :", round(r2_score(y_test, model.predict(X_test)),2))

plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression")
plt.show()
