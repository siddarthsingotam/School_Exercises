# Dictionary data
airports = {"EFHK": "Helsinki-Vanta",
            "VIDP": "Delhi-International",
            "VOHS": "Hyderabad-International",
            "VABB": "Mumbai-International",
            "VECC": "Kolkata-International",
            "VOBL": "Bengaluru-International"}

# Introduction
print(f"Welcome to Airport Finder application!\n")


# Asking user to enter new airport
new_airport = input("Add new airport to registry? (Y/N): ").upper()

if new_airport == "Y":
    print(f"\nEnter new information.\nIf completed press 'Enter' key to quit the loop.\n")
    code = input("Enter ICAO code: ").upper()
    while code != "":
        airport = input("Enter airport name: ".capitalize())
        airports[code] = airport.capitalize()
        code = input("Enter ICAO code: ").upper()
    print(f"\nYou have pressed the 'Enter' key. Heading to Airport information section......\n")

else:
    print(f"\nYou have pressed the 'Enter' key. Heading to Airport information section......\n")


# Finding airport information
print(f"\nAirport Information ")
find_icao = input("Find airport information? (Y/N): ").upper()

if find_icao == "Y":
    print(f"\nEnter Information.\nIf completed press 'Enter' key to quit the loop.\n")
    icao_airport = input("Enter valid ICAO code: ").upper()
    while icao_airport != "":
        print(airports[icao_airport])
        icao_airport = input("Enter valid ICAO code: ").upper()
    print(f"\nYou have pressed the 'Enter' key, code executed successfully.")

else:
    print(f"\nYou have pressed the 'Enter' key, code executed successfully.")
















