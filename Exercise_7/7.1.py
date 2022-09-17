# Here, seasons is a set data structure.
seasons = ("spring", "summer", "autumn", "winter")
month = int(input("Enter the month number to find the season. (1-12) :"))

# We can define each season to last three months, December(12)  being the first month of winter.
if month in range(1, 3):
    print(f"\nIt's {seasons[3]} season.")

if month in range(3, 6):
    print(f"\nIt's {seasons[0]} season. ")

if month in range(6, 9):
    print(f"\nIt's {seasons[1]} season. ")

if month in range(9, 12):
    print(f"\nIt's {seasons[2]} season. ")

if month == 12:
    print(f"\nIt's {seasons[3]} season. ")

if month not in range(1,13):
    print(f"\nYou have entered a wrong month number which is, {month}. it should range from (1-12).")





