import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
   'Area': [600, 800, 1000, 1200, 1400, 1600],
   'Price': [32, 40, 49, 58, 68, 79]
})

X = data[['Area']]
y = data['Price']

model = LinearRegression()
model.fit(X, y)

print("Regression Equation :")
print("Price =", round(model.coef_[0], 6), "* Area +", round(model.intercept_, 6))

house1 = pd.DataFrame([[1500]], columns=['Area'])
pred1 = model.predict(house1)

house2 = pd.DataFrame([[2500]], columns=['Area'])
pred2 = model.predict(house2)

print("Predicted Price for 1500 sq.ft. :", round(pred1[0], 2), "Lakhs")
print("Predicted Price for 2500 sq.ft. :", round(pred2[0], 2), "Lakhs")
