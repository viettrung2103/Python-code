# Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument

list = []
N = 5
count = 0
number_str = input("Type number:")
while number_str != "":
    number = int(number_str)
    list.append(number)
    print(f'you type: {number}')
    count = count+1
    print(f"You have type: {count} times")
    # print(f'list:  {list}')
    number_str = input("Type another number:")
print("Thank you!")
# print(f"Here is the list of numbers you have types: {list}")
list.sort(reverse=True)
# print(f"Here is the sorted list of numbers you have types: {list}")
try:
    print(f"the top 5 greatest number in your list is: {list[0]}, {list[1]}, {list[2]}, {list[3]}, {list[4]}")
except IndexError:
    print("You have not type enough number")