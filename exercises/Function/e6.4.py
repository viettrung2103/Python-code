# Write a function that gets a list of integers as a parameter.
# The function returns the sum of all the numbers in the list.
# For testing, write a main program where you create a list,
# call the function, and print out the value it returned.
#

# ask user for input >> add to list
# "do you want to add more number"
#Y: add to list
#N: print out sum of the list

def ask_number():
    number = int(input("Input number:"))
    return number

def main():
    list = []
    sum = 0
    try:
        while True:
            play = input("Would you like to add number(yes/no):").lower()
            if list == [] and play == "no":
                print("sum is 0")
                break
            else:
                while play != "no":
                    number = ask_number() # get number from user
                    list.append(number) # add number to list
                    # print(list)
                    # sum = sum + number # C1: get sum everytime add number to list
                    # print(f"The sum of the numbers you have entered is: {sum}")
    except ValueError:
        # print(list)
        # print(sum)
        #C2: get sum after finish adding all number
        for index, value in enumerate(list):
            sum = sum + value
            print(sum)
        print(f"Sum of the number you have enter:{sum}")

main()