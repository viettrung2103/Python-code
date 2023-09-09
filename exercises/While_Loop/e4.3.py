# Write a program that asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.
number_str = input("Type number: ")
smallest = largest = 0
n = 0
while number_str != "":
    while n <= 1 : #to assign the first two number as smallest and largest

        number = int(number_str)
        if number > largest: #
            # when n = 0:number =1 [0,1]
            #when n =  1, number =2 [1,2] !!
            smallest = largest
            largest = number

        elif number == largest:
            # when n = 0:number =1 [0,1]
            #when n =  1, number =1 [0,1]
            smallest = smallest
            largest = number
        elif largest < number <= smallest:
            # when n = 0:number =3 [0,3]
            #when n =  1, number =2 [2,3]
            smallest = number
        else :
            # when n = 0:number =3 [0,3]
            #when n =  1, number =0 [0,3]
            smallest = number
        print(f"n: {n}")
        n = n +1
        print(f'so nho nhat: {smallest}')
        print(f'so lon nhat: {largest}')
        number_str = input("Type number:")
        if number_str == "": # break when next input is ''
            break


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
    print("--Finally--")
    print(f'smallest {smallest}')
    print(f'largest {largest}')
    print(f'input times: {n}')