attempts = 0
user = "python"
password = "rules"

while attempts <= 4:
    user = input("Enter username : ")
    password = input("Enter password : ")
    attempts = attempts + 1

    if user != "python" and password != "rules":
        print("invalid credentials")

    if user == "python" and password == "rules":
        print("Welcome to your Domain")
        break

    if attempts == 5:
        print("Access denied failed to unlock 5 times")
        break




