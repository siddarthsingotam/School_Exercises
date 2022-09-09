num = int(input("Enter the number : "))
#prime numbers are always greater than 1

if num > 1:
    for f in range(2, num):
        if num % f == 0:
            print("The given value is not a prime number.")
            print("This is because", num ,"divided by", f ,"is", num//f)
            print("Therefore it is a divisible composite number")
            break
    else:
        print("The given value is a prime number.")

elif num == 1:
    print("It is not a prime nor composite number")
else:
    print("Enter a positive integer")



