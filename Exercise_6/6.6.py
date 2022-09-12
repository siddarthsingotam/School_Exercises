
def pizza(cost, d):
    f = cost / (3.14*(d/2)**2)
    return f

cost1 = float(input("Enter the cost of Pizza 1 (EUR): "))
dia1 = float(input("Enter the diameter of Pizza1 (CM): "))
cost2 = float(input("Enter the cost of Pizza 2 (EUR): "))
dia2 = float(input("Enter the diameter of Pizza2 (CM): "))

f1 = round(pizza(cost1, dia1), 2)
f2 = round(pizza(cost2, dia2), 2)

print(f"\nThe cost per area of Pizza 1 is: {f1} \nThe cost per area of Pizza 2 is: {f2}")

if f1 > f2:
    print("You can choose Pizza 2 as it is", round(f1-f2, 2), "(EUR/cm^2) cheaper than Pizza 1 by cost per area.")
elif f1 < f2:
    print("You can choose Pizza 1 as it is", round(f2-f1, 2), "(EUR/cm^2) cheaper than Pizza 2 by cost per area.")
else:
    print(f"\nBoth have the same cost ratio, buy whatever you like from the two :D")