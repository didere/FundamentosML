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

n1 = [[4.5]]

p1= modelo.predict(n1)
pb1= modelo.predict_proba(n1)

print("Prediccion", p1)
print("Probabilidad", pb1)

n2 = [[5]]

p2= modelo.predict(n2)
pb2= modelo.predict_proba(n2)

print("Prediccion", p2)
print("Probabilidad", pb2)

n3 = [[6]]

p3= modelo.predict(n3)
pb3= modelo.predict_proba(n3)

print("Prediccion", p3)
print("Probabilidad", pb3)

n4 = [[7]]

p4= modelo.predict(n4)
pb4= modelo.predict_proba(n4)

print("Prediccion", p4)
print("Probabilidad", pb4)