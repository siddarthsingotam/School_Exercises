print('''Welcome aboard!
You can choose your travel experience via choosing our classes available on our ship. The classes include :''')
print("1.LUX \n" "2.A \n""3.B \n""3.C \n")
print("For more details enter cabin class below.")
cabin_class = input("Enter cabin class : ").upper()

if cabin_class == "LUX":
    print("upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("windowless cabin above the car deck.")
elif cabin_class == "C":
    print("windowless cabin below the car deck.")
else:
    print(f"INVALID CABIN CLASS!")