#Configure
import mysql.connector
# Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name
# and location (town) from the airport database used on this course.
# The ICAO codes are stored in the ident column of the airport table.

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3300,
    database = "flight_game",
    user = "root",
    password = "",
    autocommit = True
)

def getTables():
    sql = "SHOW tables"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for table in result:
        print(table)
def getAirportByICAO(ICAO):
    sql = "SELECT ident, name  from airport"
    sql += " WHERE ident = '" + ICAO + "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # print(result)
    if cursor.rowcount > 0:
        for index, row in enumerate(result, start=1) :
            print (f"{index}. {row[0]} {row[1]}")
    else:
        print(f"There is no airport with ICAO: {ICAO}")

# ICAO = "00A"
# sql = "Select ident as ICAO, name as airport_name from airport"
# sql += " WHERE ident = '" + ICAO + "'"
# print(sql)

getAirportByICAO("MRPA")
# getTables()

