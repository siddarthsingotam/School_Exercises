print('''Welcome aboard!
You can choose your travel experience via choosing our classes available on our ship. The classes include :''')
print("1.LUX \n" "2.A \n""3.B \n""3.C \n")
print("For more details enter cabin class below.")
cabin_class = str(input("Enter cabin class : "))

if cabin_class == str("LUX") or str("lux") :
    print("upper-deck cabin with a balcony.")
elif cabin_class == str("A") or str("a") :
    print("above the car deck, equipped with a window.")
elif cabin_class == str("B") or str("b"):
    print("windowless cabin above the car deck.")
elif cabin_class == str("C") or str("c") :
    print("windowless cabin below the car deck.")
else:
    print("INVALID CABIN CLASS!")