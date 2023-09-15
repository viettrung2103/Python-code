# Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport,
# fetch the information of an existing airport or quit. If the user chooses to enter a new airport,
# the program asks the user to enter the ICAO code and name of the airport. If the user chooses to fetch airport information instead,
# the program asks for the ICAO code of the airport and prints out the corresponding name.
# If the user chooses to quit, the program execution ends. The user can choose a new option as many times they want until they choose to quit.
# (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK.
# You can easily find the ICAO codes of different airports online.)
#
## airportList = {"Code1":"Airport1","Code2":"Airport2",...}
import sys

airportList = {"EFHY":"Meilahti Hospital Helipad","EFHE":"Hernesaari",}

#add code and airport
def addCode():
    code = input("Type ICAO code: ")
    if checkCode(code):
        print("ICAO code exist:")
        print(f"{code}: {airportList[code]}")

    else:
        airportName = input("Type aiport name: ")
        print("Adding to the system")
        airportList[code] = airportName
        return airportList

#get airport id >> input code >> print out code: airport

def checkCode (code):

    if code in airportList:
        print(f"{code} is existed")
        return True
    else:
        print("Does not exist airport with your code")

def getAirport():
    print("------")
    code =input("Please type hte ICAO code: ")
    #check if airport exist
    if checkCode(code):
        print("aiport code:",code," airport name:", airportList[code])
    print("------")

    # for code in airportList[""]
#quit
def quit():
    sys.exit()

#display all airport
def displayAll():
    print("------")
    print("--DISPLAY ALL DATA--")
    for key, value in airportList.items():
        print(f"{key}: {value}")
    print("------")

def removeAirport():
    code = input("Type ICAO code: ")
    if checkCode(code):
        removeAirport = airportList.pop(code)
        # method pop return the removed item, not the removed list
        print(f"Airport {removeAirport} with ICAO code: {code} is removed")

#main
def main():
    try:
        while True:

            print("------WELCOME TO AIRPORT DATABASE---------")
            print("COMMANDS:")
            print("1. Enter new airport data")
            print("2. Fetch data from existing airport")
            print("3. Display all airports' data")
            print("4. Remove airport")
            print("5. Quit")
            command = int(input("What do you want to do: "))

            if command == 1:
                addCode()
            elif command == 2:
                getAirport()
            elif command == 3:
                displayAll()
            elif command == 4:
                removeAirport()
            elif command == 5:
                print("Thanks for using our system")
                quit()
            else:
                print("Thanks for using our system")
                quit()
    except ValueError:
        print("Thank you for using our system")

main()