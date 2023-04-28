import random
from faker import Faker
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

faker = Faker()

planets = ['Tierra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Neptuno']
accelerations = [9.8, 3.7, 24.8, 9.0, 8.7, 11.0]

dataset = []

for i in range(1903):
    L = random.uniform(0.5, 2.0)
    t = random.uniform(0.3, 0.8)
    planet = random.choice(planets)
    g = accelerations[planets.index(planet)] + random.uniform(-0.5, 0.5)
    error = random.uniform(0.01, 0.1)
    row = {
        'ID': faker.uuid4(),
        'L (m)': round(L, 2),
        't (s)': round(t, 2),
        'Planet': planet,
        'g (m/s^2)': round(g, 2),
        'Error': round(error, 2)
    }
    dataset.append(row)

df = pd.DataFrame(dataset)


colors = {'Tierra': 'blue', 'Saturno': 'red', 'Urano': 'green', 'Neptuno': 'purple'}

scatter_matrix(df, figsize=(10, 10), diagonal='kde', color=df['Planeta'].apply(lambda x: colors[x]))
plt.show() #Creamos una matriz de dispersion
# creacion de histogramas
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

for ax, col in zip(axes.flatten(), df.columns[:-1]):
    ax.hist(df[col], bins=10, color=colors[df['Planeta']], alpha=0.5)
    ax.set_xlabel(col)
    ax.set_ylabel('Frecuencia')

plt.tight_layout()
plt.show()


