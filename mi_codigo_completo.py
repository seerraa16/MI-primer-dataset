import random
from faker import Faker

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

print(dataset)
