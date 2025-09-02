import sklearn as sk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv('data.csv')
df2 = df[['type_local', 'nombre_pieces_principales', 'valeur_fonciere', 'nom_commune', 'surface_terrain', 'surface_reelle_bati']]
df3 = df2[(df2['type_local'] == 'Maison') | (df2['type_local'] == 'Appartement')]
df4 = df3[df3['nom_commune'] == 'Bordeaux']
df4['nombre_pieces_principales'] = df4['nombre_pieces_principales'].astype('Int64')

df5 = df4.dropna(axis=0, how='any', ignore_index=True)
print(df5.value_counts())

def random_forest(df):
    DATA_PATH = "data.csv"   # ton fichier
    TARGET = "valeur_fonciere"          # colonne cible
     
    X = df.drop(columns=['valeur_fonciere'])
    y = df['valeur_fonciere']
    
    X = pd.get_dummies(X)
    print(df.dtypes)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    print("Score:", model.score(X_test, y_test))
    
    joblib.dump(model, "model.joblib")
    joblib.dump(list(X.columns), "features.joblib")
    
random_forest(df5)
