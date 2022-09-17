days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
day_number = int(input("Enter the day number (1-7): "))
day = days_of_the_week[day_number-1]
print (f"Day number {day_number} is {day}.")


















sys.exit(0)

#counting even numbers between the integers
import sys

count = 0
first_number = int(input("enter first no. : "))
last_number = int(input("enter last no. : "))
for x in range (first_number,last_number+1):
    if x % 2 == 0:
     print(x)
     count = count + 1

print("we have :", count, "even no.s")

sys.exit(0)

#infinite loop test

# Faulty program, infinite loop

number = 1
while number<5:
    print (number)

# This part is never reached:
print("All ready.")
