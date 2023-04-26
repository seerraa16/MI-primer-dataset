#creamos un dataset con 1000 filas y 3 columnas
import random 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from faker import Faker
from sklearn.preprocessing import LabelEncoder

fake = Faker()

def generate_sample():
    L = round(random.uniform(0.8, 2.5), 2) 
    t = round(random.uniform(0.4, 0.7), 2)
    g_calculated = round((2 * L) / (t**2), 2)
    most_probable_planet = "Tierra" if abs(g_calculated - 9.8) < abs(g_calculated - 9.0) else "Saturno"
    second_most_probable_planet = "Saturno" if most_probable_planet == "Tierra" else "Tierra"
    
    return {
        "ID": fake.uuid4(),
        "Longitud (m)": L,
        "Tiempo (s)": t,
        "g_calculado (m/s²)": g_calculated,
        "Planeta más probable": most_probable_planet,
        "2do más probable": second_most_probable_planet
    }

dataset = [generate_sample() for _ in range(100)]

# Crear el DataFrame con el dataset
df = pd.DataFrame(dataset)

# Estadísticas descriptivas
print(df.describe())

# Histogramas
df.hist(column=["Longitud (m)", "Tiempo (s)", "g_calculado (m/s²)"])
plt.show()

# Gráfico de dispersión
plt.scatter(df["Longitud (m)"], df["Tiempo (s)"])
plt.xlabel("Longitud (m)")
plt.ylabel("Tiempo (s)")
plt.show()

# Codificar etiquetas de planetas
label_encoder = LabelEncoder()
df["Planeta más probable (código)"] = label_encoder.fit_transform(df["Planeta más probable"])
df["2do más probable (código)"] = label_encoder.fit_transform(df["2do más probable"])

# Correlación entre variables
print(df.corr())

# Regresión lineal
from sklearn.linear_model import LinearRegression

X = df["Longitud (m)"].values.reshape(-1, 1)
y = df["Tiempo (s)"].values.reshape(-1, 1)

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

# Gráfico de regresión lineal
plt.scatter(X, y, color="blue")
plt.plot(X, y_pred, color="red")
plt.xlabel("Longitud (m)")
plt.ylabel("Tiempo (s)")
plt.show()