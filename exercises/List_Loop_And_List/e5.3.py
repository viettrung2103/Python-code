# Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.
#
# For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
# On the other hand, 21 is not a prime number as it is divisible by 3 and 7.
import sys

count_list = [] # list so ma number chia dc, count list = 2 thi number la prime number
count = 1

# ask for the number
# if is divisible, add the count list
# if count list is more than two, is not prime number
try:
    number = int(input("type number: "))
    if number == 1:
        print(f"{number} is not a prime number")
        sys.exit()
    while count <= number:
        if number % count == 0:
            count_list.append(count)
            count = count +1
        else:
            count = count + 1
    if len(count_list) != 0:
        # print(count_list) : test the count list
        if len(count_list) > 2: #
            print(f"{number} is not a prime number")
        else:
            print(f"{number} is a prime number ")
except ValueError:
    print("This is not interger")
    # number = int(input("type number: "))
