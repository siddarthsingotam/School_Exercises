# Making an empty set
name_set = set()
print(f"\nThis is a new data structure, enter names to fill. \nPress enter to quit the loop.")
name_add = input(f"\nEnter the first new name: ")

# While loop helps to read each name and tell us if the name exists or not.
while name_add != "":
    name_set.add(name_add)
    name_add = input("Enter name again: ")
    if name_add not in name_set:
        print("new name")
    if name_add in name_set:
        print("Existing name")


# Printing the final created set
print(f"\nThe names in the set are: \n")
for names in name_set:
    print(names.capitalize())