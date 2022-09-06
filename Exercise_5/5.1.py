import random
dice = int(input("Enter the number of dice : "))
outputs = []

for n in range(dice):
    n = random.randint(1,6)
    outputs.append(n)

print(f" The outputs of rolls are : {outputs} \n The sum of the outputs are : {sum(outputs)} ")