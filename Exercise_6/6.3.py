def conversion(gallon):
    while gallon >= 0:
        gallon = float(input("Enter in Gallon : "))
        litres = gallon * 4.54
        if gallon >= 0:
            print(round(litres, 3), "litres")
    else:
        print("negative value recorded")

    return gallon

print(conversion(1))