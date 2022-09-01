import random
number = random.randint(1,10)
guess_taken = 0

print("Welcome to the guessing game!\nGuess a number between 1 and 10")
while guess_taken != number :
    guess = int(input("Take a guess :"))
    guess_taken = guess_taken + 1

    if guess < number:
        print("Your guess is low")

    if guess > number:
        print("Your guess is high")

    if guess == number:
        print("your guess is correct")
        print("yay the number is", number, "you took", guess_taken,"guesse(s)")
        #change formatted


