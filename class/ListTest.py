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
grades =[]
rank = ["A","B","C","D","fail"]
print("Welcome to the Ranking Application")
run = input("Do you want to run(y/n): ")
while run == "y":
    number_str = input("Please input your score: ")
    while number_str != "-1":
        nummber = int(number_str)
        if nummber >= 90:
            print(f" your score is: {nummber}, you get {rank[0]}")
        elif 80 <= nummber < 90:
            print(f" your score is: {nummber}, you get {rank[1]}")
        elif 70 <= nummber < 80:
            print(f" your score is: {nummber}, you get {rank[2]}")
        elif 60 <= nummber < 70:
            print(f" your score is: {nummber}, you get {rank[3]}")
        else:
            print(f" your score is: {nummber}, you get {rank[4]}")
        grades.append(nummber)
        number_str = input("Please input your score: ")
    print(f'list is: {grades}')
    break

    # for grade in grades:

    # run = input("Do you want to run again (y/n):")
print(" Thank you for using the application")

# list = [1,2,4,0,3,5,6]
# print(list)
# list_sorted = list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# print(list[0],list[1],list[2],list[3])