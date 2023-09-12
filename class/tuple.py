#tuple is immutable list, which mean it cannot be changed throughtout the program
#syntax: ()

# single value tuple
#   tuple1 = (1,)
# print(tuple1)
#

# tuple1 = (1,35,5)
# for i in tuple1:
#     print(i)

# point = (2,4)
# x,y = point
# print(point)
# print(f"x: {x},y: {y}")

# student = ("Timo",22,"Computer Science")
# print(f"Name: {student[0]},Age: {student[1]}, Major: {student[2]}")
#
# grades = (6,8,9,10)
# total = 0
# for grade in grades:
#     total += grade
# print(f"total: {total}")
#
# mean = total / len(grades)
# print(f"mean: {mean}")


students = []

students.append(("Amir",(20,50,80)))
students.append(("Trung",(50,60,70)))
students.append(("Trinh",(90,40,30)))
found = False

for student in students:
    if student[0] == "Tr":
        name = student[0]
        grade = student[1]
        ave = sum(student[1])/len(student[1])
        print(f"{name}:{grade}, ave:  {ave}")
        found = True
        break
    else:
        print("No student with such name in database")
        break
# print(students)

