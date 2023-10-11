#Configure
import mysql.connector
from config import connection
# Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name
# and location (town) from the airport database used on this course.
# The ICAO codes are stored in the ident column of the airport table.

# connection = mysql.connector.connect(
#     host = "127.0.0.1",
#     port = 3300,
#     database = "flight_game",
#     user = "root",
#     password = "",
#     autocommit = True
# )

def runSQL(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def getTables():
    sql = "SHOW tables"
    result =runSQL(sql)
    for table in result:
        print(table)
def getAirportByICAO(ICAO):
    # select ident, name as airport_name from airport where ident = "00AA"
    sql = "SELECT ident, airport.name as airport_name, country.name as country_name  from airport, country"
    sql += " WHERE airport.iso_country = country.iso_country and  ident = '" + ICAO + "'"
    # cursor = connection.cursor()
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # result = runSQL(sql)
    print(result)
    if cursor.rowcount > 0:
        for index, row in enumerate(result, start=1) :
            print (f"{index}. {row[0]} {row[1]}-- Location: {row[2]}")
    else:
        print(f"There is no airport with ICAO: {ICAO}")

# ICAO = "00A"
# sql = "Select ident as ICAO, name as airport_name from airport"
# sql += " WHERE ident = '" + ICAO + "'"
# print(sql)
def main():
    while True:
        countryCode = input("input ICAO code:")
        while countryCode != "":
            getAirportByICAO(countryCode.capitalize())
            countryCode = input("input ICAO code:")

        else:
            print("Thank you for using our program")
            break

# getAirportByICAO("MRPA")
# getTables()
main()
