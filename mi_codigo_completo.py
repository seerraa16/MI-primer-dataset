import random
from faker import Faker
import pandas as pd
import matplotlib.pyplot as plt

faker = Faker()

planets = ['Tierra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Neptuno']
accelerations = [9.8, 3.7, 24.8, 9.0, 8.7, 11.0]

def generate_sample():
    
    L = random.uniform(0.5, 2.0)
    t = random.uniform(0.3, 0.8)
    planet = random.choice(planets)
    g = accelerations[planets.index(planet)] + random.uniform(-0.5, 0.5)
    error = random.uniform(0.01, 0.1)
    most_probable_planet = planets[accelerations.index(min(accelerations, key=lambda x: abs(x - g)))]
    second_most_probable_planet = planets[accelerations.index(max(accelerations, key=lambda x: abs(x - g)))]
    return {
        'ID': faker.uuid4(),
        'L (m)': round(L, 2),
        't (s)': round(t, 2),
        'Planet': planet,
        'g (m/s^2)': round(g, 2),
        'Error': round(error, 2)
        
    }
dataset = [generate_sample() for _ in range(1903)] #1903 datos por el atleti.   
df = pd.DataFrame(dataset)



print(df.describe())


#codificar etiquetas de planetas
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
df['Planet (code)'] = label_encoder.fit_transform(df['Planet'])
# Gráfico de dispersión
plt.scatter(df["L (m)"], df["t (s)"])
plt.xlabel("Longitud (m)")
plt.ylabel("Tiempo (s)")
plt.show()
# Histogramas
df.hist(column=["L (m)", "t (s)", "g (m/s^2)"])
plt.show() 
# Regresión lineal
from sklearn.linear_model import LinearRegression
#datos que mas han salido tras el analisis
print(df.corr())


