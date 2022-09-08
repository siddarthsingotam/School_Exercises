list = []

number = int(input("Enter the integer : "))

while number != "":
    number = (input("Enter number : "))
    if number != "":
        list.append(number)

list.sort(reverse=True)
print("The five greatest numbers are : ",list[0:5])