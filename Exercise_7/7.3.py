# Dictionary data
airports = {"EFHK": "Helsinki-Vanta",
            "VIDP": "Delhi-International",
            "VOHS": "Hyderabad-International",
            "VABB": "Mumbai-International",
            "VECC": "Kolkata-International",
            "VOBL": "Bengaluru-International"}

# Introduction
print(f"Welcome to Airport Finder application!\nType 'A' to add new airport\nType 'B' to Find airport")
choose = input("Choose A or B option to proceed: ").upper()

# Asking user to enter new airport

if choose == "A":
    new_airport = input("Add new airport to registry? (Y/N): ").upper()
    if new_airport == "Y":
        print(f"\nEnter new information.\nIf completed press 'Enter' key to quit the loop.\n")
        code = input("Enter ICAO code: ").upper()
        while code != "":
            airport = input("Enter airport name: ".capitalize())
            airports[code] = airport.capitalize()
            code = input("Enter ICAO code: ").upper()
    print(f"\nHeading to Airport information section......\n")


# I have put an immediate prompt to verify the new-entered dictionary data.
# The code automatically takes you to find airport info to immediately verify data.
# the advantage of this is that you don't have to re-run the code to find and verify the airport information.

# Finding airport information

print(f"\nAirport Information ")
find_icao = input("Find airport information? (Y/N): ").upper()
if choose == "B" or find_icao == "Y":
    if find_icao == "Y":
        print(f"\nEnter Information.\nIf completed press 'Enter' key to quit the loop.\n")
        icao_airport = input("Enter valid ICAO code: ").upper()
        while icao_airport != "":
            print(airports[icao_airport])
            icao_airport = input("Enter valid ICAO code: ").upper()


print("\nThank you for using this application, code executed successfully.")# Exit















