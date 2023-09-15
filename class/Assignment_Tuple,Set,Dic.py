#create a dictionary for a shopping list:
# MilK: 4
#Juice: 3
# Apple: 3
# Oat: 2
import sys

# shoppingList = {"MilK":4,"Juice":3,"Apple":3,"Oat":2}

#create a function to add items to the dictionary
# create function to display the dictionary
# calculate the sum and display to the screen
#


#use dict.value() to go and fetch value from each item


shoppingList = {}

# check if the key, value is in dict, if yes, add new amount, if no, ad the key, value item to the dic
def addItem():
    name = input("What do you want to buy? ")
    quality = int(input("How many:" ))
    if name in shoppingList:
        shoppingList[name] += quality
        return shoppingList
    else:
        shoppingList[name] = quality
        return shoppingList

def display():
    for key, value in shoppingList.items():
        print(f"{key}: {value}")

def totalAmount ():
    # sum = 0
    # for key, value in shoppingList.items():
    #     sum += value
    # print(f"Total: {sum}")

    # get a list of value:
    value_list = shoppingList.values()
    print(f"Total quality is : {sum(value_list)}")



def quit():
    sys.exit()

def main():
    while True:
        print("Shopping List")
        print("1. Add to shopping list")
        print("2. Display the list")
        print("3. Total quality")
        print("4. Quit")

        command = int(input("Which command? "))

        if command == 1:
            addItem()
        elif command == 2:
            display()
        elif command == 3:
            totalAmount()
        elif command == 4:
            quit()

main()

