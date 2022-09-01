num = int(input("Enter number :"))
lowest = num
highest = num

while num != "":
    if num < lowest:
        lowest = num
    if num > highest:
        highest = num

    num = (input("Enter number :"))
    if num != "":
        num = int(num)



print("Lowest", lowest, "Highest", highest)