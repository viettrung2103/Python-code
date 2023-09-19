# Write a program that asks the user to enter the area code (for example FI)
# and prints out the airports located in that country ordered by airport type.
# For example, Finland has 65 small airports, 15 helicopter airports and so on.
#

from config import connection

def getCountryCode():
    countryCode = input("Type country code:")
    return countryCode
def getAirportByCountryCode(country):
    sql = "SELECT ident, name, type from airport"
    sql += " WHERE iso_country ='" +country+ "'"
    sql += " ORDER BY type "
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for index, row in enumerate(result,start=1):
            print(f"{index}. {row[0]} -- {row[1]} -- {row[2]} ")
    else:
        print(f"There is no airport with country code: {country}")




# getAirportByCountryCode("FI")

#
def main():
    countryCode = getCountryCode()
    while True:
        while countryCode != "":
            getAirportByCountryCode(countryCode)
            countryCode = getCountryCode()
        else:
            print("Thank you for using our program")
main()