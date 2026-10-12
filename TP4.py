from os import read
import pandas as pd
import random
donnee = pd.read_csv("fichiervitesse.csv")
donnee["Danger"] = donnee["Danger"].str.strip().map({"FAUX": 0, "VRAI": 1})


w = random.randint(-10, 10)
b = random.randint(-10, 10)
X=donnee["Vitesse en km/h"].tolist()
Y=donnee["Danger"].tolist()
print(w, b)
print(X[:5],Y[:5])
def Zpredict(x):
    z = w * x + b
    if z >= 0:
        return 1
    else:
        return 0
for x, y in zip(X, Y):
    y_prediction = Zpredict(x)
    erreur = y - y_prediction
    print("x =",x," y réel =", y," prédiction y =",y_prediction," erreur =",erreur)