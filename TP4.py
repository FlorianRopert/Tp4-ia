import pandas as pd
donnee = pd.read_csv("fichiervitesse.csv")
donnee["Danger"] = donnee["Danger"].str.strip().map({"FAUX": 0, "VRAI": 1})
print(donnee)
