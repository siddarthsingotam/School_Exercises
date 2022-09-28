import mysql.connector

def airport_type(iso_country_code):
    sql = 'SELECT name, type FROM airport WHERE iso_country = ' f'"{iso_country_code}"' + ' ORDER BY type;'
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for rows in result:
        print(f" Airport Name: {rows[0]}, Airport Type: {rows[1]}")
    return

# Connection Part
connection = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    database="flight_game",
    user="root",
    password="yoyo@123",
    autocommit=True

)
# User Input
iso_country_code = input("Please enter Country code: ")

airport_type(iso_country_code)