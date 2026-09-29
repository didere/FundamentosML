from sklearn.linear_model import LogisticRegression

X=[
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8]
]

y= [0,0,0,0,1,1,1,1]

modelo = LogisticRegression()
modelo.fit(X,y)

print("Intercepto: ",modelo.intercept_)
print("Coeficiente: ",modelo.coef_)

for horas in range (1,9):
    prob = modelo.predict_proba([[horas]]) [0] [1]
    pred = modelo.predict([[horas]]) [0]

    print (horas, round(prob, 3), pred)