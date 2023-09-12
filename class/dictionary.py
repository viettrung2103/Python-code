#dictionary
#type of list, have pair: "key":"value"
#syntax: {}
# dic1 = {"key":"value1","key2":"value2"}
#
# # del dic1["key"]
#
# print((dic1))

student = {
    "name": "Amir",
    "grade": "A",
    "courses" : ["Math","Physics","Programming"]
}
# Access to dictionary
# print("name: ",student["name"])
# print("Grade: ",student["grade"])
# print("Courses: ",student["courses"])

student["age"] = 21  # add item(key,value) to a dictionary
student["city"] = "Espoo"
student['age'] = 30 # edit value based on key in dics
# student["Age"].append(20) //
print(student)

for key, value in student.items():
    print(key+ ":",value)

print(student)

#Check if a key exist in dictionary
print("------")

# if 'school' in student:
#     print( student["name"])
# else:
#     print("Not in dictionary")

print("-----")
value = student.values()
print(student.get("name"))

d = {1: "a", 2: "b"}

a = d.values()
print(a)
