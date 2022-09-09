cities = []

for n in range(0, 5):
    name = input(f"Enter the city number {n+1}: ")
    cities.append(name)

for m in cities:
    print(f"The {cities.index(m)+1} city is: {m.capitalize()}")