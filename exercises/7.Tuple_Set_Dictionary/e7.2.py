# Write a program that asks the user to enter names
# until he/she enters an empty string.
# After each name is read the program
# either prints out New name or Existing name
# depending on whether the name was entered for the first time.
# Finally, the program lists out the input names one by one,
# one below another in any order.
# Use the set data structure to store the names.

#set data set = {}
# to initialize a empty set, use method set()
nameList = set()
def ask_name ():
    name = input("Type name: ")
    return name
#check if name exist
def check_name(inputName):
    if inputName in nameList:
        print("Typed name is already exist")
    else:
        print(f"{inputName} is added")
        nameList.add(inputName)

#display all name in set
def display():
    for name in nameList:
        print(name)
def main():
        #ask name from user
        name = ask_name()
        while True:
            while name !="":
                check_name(name) #check name
                name =ask_name() #type again
                print("Names that have been typed:")
                display()
            else:
                break

main()

