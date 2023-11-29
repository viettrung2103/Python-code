# Write a program that asks the user to enter the ICAO codes of two airports.
# The program prints out the distance between the two airports in kilometers.
# The calculation is based on the airport coordinates fetched from the database.
# Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.
# Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE,
# write geopy into the search field and finish the installation.

from config import connection
from geopy.distance import geodesic as GD


def getICAO():
    ICAO = input("Type ICAO code: ").upper()
    return ICAO
def getAirportByICAO(ICAO):
    sql = "SELECT ident, name, latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident ='" +ICAO+ "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # print(result)
    if cursor.rowcount > 0:
        for index, row in enumerate(result, start=1) :
            print (f"{index}.  {row[0]} -- {row[1]} -- {row[2]} -- {row[3]}")
    else:
        print(f"There is no airport with ICAO: {ICAO}")
    return result

def getDistant():
    ICAO1 = input("type first ICAO:")
    ICAO2 = input("type second ICAO:")
    airport1 = getAirportByICAO(ICAO1.capitalize())
    airport2 = getAirportByICAO(ICAO2.capitalize())
    # print(air)
    if airport1 != [] and airport2 != []:
        cordinator1 = (airport1[0][2],airport1[0][3])
        print(f"cordinator1: {cordinator1}")
        cordinator2 = (airport2[0][2],airport2[0][3])
        print(f"cordinator2: {cordinator2}")
        totalDistance = GD(cordinator1,cordinator2).km
        print(f" {ICAO1}: {airport1[0][1]} ---- {ICAO2}: {airport1[0][1]}:")
        print(f"total distance between: {totalDistance:,.2f} km")
    else:
        print("Missing information, cannot calculate the distant")
    # print(f"cordinator1 :{cordinator1}")
    # print(f"cordinator2 :{cordinator2}")

def main():
    while True:
        # getDistant()
        ICAO = getICAO()
        # print(ICAO)
        getAirportByICAO(ICAO)


# total = (40.07080078125,-74.93360137939453)
# Aero = (38.704022,-101.473911)
# length = distance.distance(total,Aero).km
# # the "," will add >> 1,000 instead of 1000, .2f >> float, round to 3 decimal
# print(f"{length:,.3f} km")

# ICAO = "00AK"
# print(getAirportByICAO(ICAO)[0][2])
# print(getAirportByICAO(ICAO)[0][3])
# getDistant()
main()
# getAirportByICAO("00AC")
