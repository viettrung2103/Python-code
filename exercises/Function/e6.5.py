# Write a function that gets a list of integers as a parameter.
# The function returns a second list that is otherwise the same as the original
# list except that all uneven numbers have been removed.
# For testing, write a main program where you create a list, call the function,
# and then print out both the original as well as the cut-down list.
#

# using list.filter( filter_function, list) >> each value inside will go through the filter, any value return false will be remove
def filter_odd(value):
    if value % 2 == 0: # true if even, false if odd
        return True
    else:
        return False

def ask_number():
    number = int(input("Input number:"))
    return number


def main():
    numList = []
    # filter_list = []
    try:
        while True:
            play = input("Would you like to add number(yes/no):").lower()
            if numList == [] and play == "no":
                print("The list is empty:")
                break
            else:
                while play != "no":
                    number = ask_number() # get number from user
                    numList.append(number) # add number to list
                    # print(list)

    except ValueError:
        filter_list = list(filter(filter_odd,numList))
        print(f"Number you have typed: {numList}")
        print(f"List of even of numbers that you have entered:{filter_list}")

main()
# #list
# numb_list = [1,2,3,4,5,6,7,8]
# ## using list class to create a new list with all the filtered number >> create new list
# filtered =list(filter(filter_odd,numb_list))
# print(filtered)