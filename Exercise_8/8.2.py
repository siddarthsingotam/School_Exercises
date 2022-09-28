import mysql.connector


def getAirportType(iso_nation_co):
    sql = 'SELECT name, type FROM airport WHERE iso_country = ' f'"{iso_nation_co}"' + ' ORDER BY type;'
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for rows in result:
        print(f"Airport Name: {rows[0]}, Airport Type: {rows[1]}")
    return


connection = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    database="flight_game",
    user="root",
    password="yoyo@123",
    autocommit=True

)

iso_nation_co = input("Enter nation code: ")
getAirportType(iso_nation_co)

print("Bon voyage!")
#commit 2