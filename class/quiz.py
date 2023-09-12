# create a TODO app
# user can
#1. add todo
#2. remove todo
#3. display todo list
#4. quit


import sys

list = []

def display():
    for index, item in enumerate(list,start=1):
        print(f"{index}: {item}")

def quit():
    print("Thank you for using the program")
    sys.exit()
def add():
    todo = input("What toDo do you want to add: ")
    list.append(todo)

def remove():
    item = input("What toDo do you want to remove? ")
    if item in list:
        list.remove(item)
    else:
        print(f" The toDo: {item} is not in the list")

def main():
    while True:
        print("TODO APP")
        print('-----COMMAND-----')
        print("1. Add todDo")
        print("2. Remove Todo")
        print("3. Display")
        print("4. Quit")

        command = int(input("What is your command:"))
        if command == 1:
            add()
        elif command ==2:
            # item = input("What todo do you want to remove:")
            remove()
        elif command == 3:
            display()
        elif command == 4:
            quit()
        else:
            break

main()