import mysql.connector
from geopy import distance


def getAirportCoordinates(icao_code):
    sql = 'SELECT latitude_deg, longitude_deg FROM airport WHERE gps_code = ' + f'"{icao_code}"' + ";"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


connection = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    database="flight_game",
    user="root",
    password="yoyo@123",
    autocommit=True

)

# Asking input
icao_code_1 = input("Enter Nation Code of Airport 1: ")


icao_code_2 = input("Enter Nation Code of Airport 2: ")

coordinates_1 = []

coordinates_2 = []

# For-loop

for i in getAirportCoordinates(icao_code_1)[0]:
    coordinates_1.append(float(i))

for i in getAirportCoordinates(icao_code_2)[0]:
    coordinates_2.append(float(i))

# Converting list to tuple

coordinates_1 = tuple(coordinates_1)
coordinates_2 = tuple(coordinates_2)

print(f"The distance between {icao_code_1} and {icao_code_2} is {distance.distance(coordinates_1, coordinates_2)}.")