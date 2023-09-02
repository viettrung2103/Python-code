# Write a program that asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.
number_str = input("Type number: ")
smallest = largest = 0
n = 0
while number_str != "":
    while n <= 1 and number_str != "": #to assign the first two number as smallest and largest
        number = int(number_str)

        if number > largest:
            smallest = largest
            largest = number

        elif number == largest:
            smallest = smallest
            largest = number
        elif largest < number <= smallest:
            smallest = number
        else :
            smallest = number
        n = n +1
        print(f'so nho nhat: {smallest}')
        print(f'so lon nhat: {largest}')

        number_str = input("Type number:")

        # while n == 0: # n = 0
        #     if number >= largest:
        #         largest = number
        #     else:
        #         if number <= smallest:
        #             smallest = number
        #     print(f'so nho nhat: {smallest}')
        #     print(f'so lon nhat: {largest}')
        #     print(f'n : {n}')
        #     n = n+1
        #     number_str = input("Type number:")
        # else: # n = 1
        #     if number >= largest:
        #         smallest = largest
        #         largest = number
        #     elif largest > number >= smallest:
        #
        #         smallest = number
        #     else:
        #         smallest = smallest
        #     print(f'so nho nhat: {smallest}')
        #     print(f'so lon nhat: {largest}')
        #     print(f'n: {n}')
        #     n = n+ 1
        #     number_str = input("Type number:")
    else: #n > 1
        number = int(number_str)
        if number >= largest:
            largest = number
        elif number <= smallest:
            smallest = number


        print(f'n: {n}')
        n = n+1
        print(f'so nho nhat: {smallest}')
        print(f'so lon nhat: {largest}')

        number_str = input("Type number:")
else:
    print(f'smallest {smallest}')
    print(f'largest {largest}')
    print(f'input times: {n}')