#1kg = 2.205 lbs
#1 talent = 20 pounds

tal = float(input("Enter talents:"))
pou = float(input("Enter Pounds:"))
lot = float(input("Enter Lots :"))

grams = (tal*20*32*13.3) + (pou*32*13.3) + (lot*13.3)
kilr = (grams / 1000)
kilo = (grams // 1000)
gramz = ( kilr - kilo)
print("the weight is:")
print( kilo,"kilo grams and", (round(gramz, 3)), "grams" )