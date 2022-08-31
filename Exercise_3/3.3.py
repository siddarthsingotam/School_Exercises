print ("You must be an adult to get youe hemoglobin value right in this calculator")
gender = str(input("Please enter your gender. \n (male/female) : "))

if gender == str("male") :
    h_m = float(input("Enter your hemoglobin Value (g/l) :"))
    if 134 <= h_m <= 167:
        print("hemoglobin is normal")
    elif h_m < 134:
        print("hemoglobin is low")
    else:
        print("hemoglobin is high")

elif gender == str("female") :
    h_m = float(input("Enter your hemoglobin Value (g/l) :"))
    if 117 <= h_m <= 155:
        print("hemoglobin is normal")
    elif h_m < 117:
        print("hemoglobin is low")
    else:
        print("hemoglobin is high")