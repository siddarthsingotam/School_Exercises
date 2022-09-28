import mysql.connector

def airport_name_town(icao_code):
    sql = 'SELECT name, municipality from airport where ident ='+f'"{icao_code}"'+";"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0:
        for row in result:
            print(f"Name: {result[0][0]}, Town: {result[0][1]}")
    return


connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='root',
    password='yoyo@123',
    autocommit=True)


i_code = input("Enter ICAO code: ").upper()
print(airport_name_town(i_code))
# commit 2
