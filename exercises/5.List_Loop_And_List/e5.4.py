# Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names)
# and stores them into a list structure.
# Finally, the program prints out the names of the cities one by one, one city per line, in the same order they were read as input.
# Use a for loop for asking the names and a for/in loop to iterate through the list.

city_list = []
# N = 5  # C1
# count = 1 # C1


#
#C1
# while city != "" and count <= N: # input is not empty and count is less than 5
#     print(f"City name: {city}")
#     city_list.append(city)
#     count = count + 1
#     if count == 6:
#         break
#     city = input ("Input city: ")

#C2
for index in range(5):
    city = input("Input city: ")
    print(f"city you have entered: {city}")
    city_list.append(city)
    city = input("Input City")

# print(f"You have typed 5 cities: {city_list}")
for index, item in enumerate(city_list,start=1):
    print(f"{index}.  {item}")