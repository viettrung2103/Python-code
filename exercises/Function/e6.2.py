# Modify the function above so that it gets the number of sides on the dice as a parameter.
# With the modified function you can for example roll a 21-sided role-playing dice.
# The difference to the last exercise is that
# the dice rolling in the main program continues until the program gets the maximum number on the dice,
# which is asked from the user at the beginning.
import random


#how many side your dice have
def how_many_side():
    side = int(input("How many side your dice have: "))
    return side
#roll value for the dice
def roll(side):
    number = random.randint(1,side)
    return number

def main():
    while True:
        count = 1
        side =how_many_side() # get side
        value = roll(side) # get value
        while value != side:
            print(value) # if value != side, print it
            count += 1
            value = roll(side) # roll again
        if count == 1:
            print(f"It takes {count} time to roll {value}") # if value == 6, print it
        else:

            print(f"It takes {count} times to roll {value}") # if value == 6, print it
        break

main()