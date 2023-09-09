# Write a function that returns a random dice roll between 1 and 6.
# The function should not have any parameters.
# Write a main program that rolls the dice until the result is 6.
# The main program should print out the result of each roll.
import random

# Write a function that returns a random dice roll between 1 and 6.
# The function should not have any parameters.
def roll():
    number = random.randint(1,6)
    return number

def main():
    while True:
        count = 1
        value = roll() # get value
        while value != 6:
            print(value) # if value != 6, print it
            count += 1
            value = roll() # roll again
        if count == 1:
            print(f"It takes {count} time to roll {value}") # if value == 6, print it
        else:

            print(f"It takes {count} times to roll {value}") # if value == 6, print it
        break

main()