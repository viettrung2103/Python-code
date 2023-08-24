# Write a program that asks the user to enter
# a mass in medieval units: talents (leiviskä),
# pounds (naula), and lots (luoti).
# The program converts the input to full kilograms
# and grams and outputs the result to the user:
#
# One talent is 20 pounds.
# One pound is 32 lots.
# # One lot is 13,3 grams.

import sys

talent_str = input("Enter talents: ")
try:
    talent = float(talent_str)
except:
    print("This is not a number")
    sys.exit(1)

pound_str = input("Enter pounds: ")
try:
    pound = float(pound_str)
except:
    print("This is not a number")
    sys.exit(1)

lot_str = input("Enter lots: ")
try:
    lot = float(lot_str)
except:
    print("This is not a number")
    sys.exit(1)

total = ((talent*20)*32)*13.3 + (pound*32)*13.3 + lot*13.3
kilo = int(total // 1000)
remain = total - kilo*1000
print(f"total {total:.2f}")
print(f"kilo:{kilo} and gram: {remain:.2f}")