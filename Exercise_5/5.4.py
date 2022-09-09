cities = []

for n in range(0, 5):
    name = input(f"Enter the city {n+1}: ")
    cities.append(name)

print(f"\nThe order of cities are: \n ")
for m in cities:
    print(f"City {cities.index(m)+1} is: {m.capitalize()}")