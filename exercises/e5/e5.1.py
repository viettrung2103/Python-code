# Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and prints out the sum of the numbers.
# Use a for loop.
import random

n_str = input ("How many dices you want to roll? ")
sum = 0
dices = []
n = int(n_str)
x = 1
while x <= n:
    dices.append(x)
    # print(f'dices list: {dices}')
    x = x + 1
print(f'{dices}')
for dice in dices:
    number = random.randint(1,6)
    sum = sum + number
    print(f"dice {dice} roll: {number}")
    print(f"sum: {sum}")
# while n_str != "":

    # n_str = input("Do you want to roll again")
    # when there is at least one dice, add to the list of dice [1,2,3]
    # for dice in range(1,dices,1):
    #     number = random.randint(1,6)
    #     sum = sum + number
    #     print(f' sum is: {sum}')
