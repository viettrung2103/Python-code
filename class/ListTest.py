# myList = [5,6,7]
#
# print(myList)
# print(myList[0])
# myList[2] = "Software 1"
# print(myList)
# myList.remove(myList[2])
# print(myList)

#ex: create a application, if grade is more than 90, get A
#between 80 and 90, get B
#get 70 and 79, get C
#between 60 and 69, get D
#below 60, fail
#-----
# grades =[]
# rank = ["A","B","C","D","fail"]
# print("Welcome to the Ranking Application")
# run = input("Do you want to run(y/n): ")
# while run == "y":
#     number_str = input("Please input your score: ")
#     while number_str != "-1":
#         nummber = int(number_str)
#         # if nummber >= 90:
#         #     print(f" your score is: {nummber}, you get {rank[0]}")
#         # elif 80 <= nummber < 90:
#         #     print(f" your score is: {nummber}, you get {rank[1]}")
#         # elif 70 <= nummber < 80:
#         #     print(f" your score is: {nummber}, you get {rank[2]}")
#         # elif 60 <= nummber < 70:
#         #     print(f" your score is: {nummber}, you get {rank[3]}")
#         # else:
#         #     print(f" your score is: {nummber}, you get {rank[4]}")
#         grades.append(nummber)
#         number_str = input("Please input your score: ")
#     #enumerate(list): the term when want to go through each item of the list, with index and index value
#     # for index, number in enumerate(list,start= , start is option, if not mention, start from 0)
#     for index, grade in enumerate(grades):
#         print(f"{index} . {grade}")
#         # print(f'list is: {grades}')
#     break
# print(" Thank you for using the application")

# list = [1,2,4,0,3,5,6]
# print(list)
# list_sorted = list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# print(list[0],list[1],list[2],list[3])

# create a shoping list
# when done, print a shopping list in order
#--- appy enumerate
list = []
task = input("What do you need to buy?(type Done when finish) ").lower()
while task != ""  and task != "done" :
    print(f"you have add: {task}")
    list.append(task)
    task = input("What do you need to buy?(type Done when finish) ")
print("task list: ")


for index, task in enumerate(list,start=1):
    print(f"{index}. {task}")
print("Thanks")
#---
# // apply while True, do not need to write input at the end of while loop
# list = []
# while True:
#     item  = input("task:")
#     list.append(item)
#     if item.lower() == "done":
#         break
# print(list)