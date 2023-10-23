# import math
#
# Names = 123
# name = Name = Names
# name1 = name2 ="S\ntring"
#
# print(name1)
# print(0.3)
import math

print(f"{'Pi':12s}:{math.pi:10.5f}")
# print(f"{'e':12s}:{math.e:10.5f}")
#
# a = 100000.30002
# print(f"{a:20,.2f}")
# b = "Happy Birthday"
# print(f"{b:^20s}")
#string align: < left, ^ center, > right + number os character + s
# print(f"{variable:number of character,.number of decimal type of data}")

# i1 = range(10)
# print(i1)
# # i = 1
# for i in range(10):
#     print(i)
    # i +=1

# first = 1
# while first <= 5:
#     second = 1
#     while second <= 5:
#         print(f"{first} time {second}  is {first * second}")
#         second += 1
#     first += 1
#slice list[startingIndex:endingIndex(exclusive):step]
listEg = [1,4,4,3,5,6,"Apple"]
# list1 = list[::2]
# list2 = listEg.pop(0)
# print(listEg)
# print(list1)
#common methods:
#append: add to the end of list
#insert(index,value) insert value to list[index]
#pop: remove value at index . pop(index) # return the removed item
# list2 = listEg.pop(0)
#remove: remove value from list.  remove(value) eg: remove("Apple")
# list2 = listEg.remove(4)
# print(type(listEg[1]))

#extend: join to lists list1.extend(list2)
#index: find index of specific item list.index("Apple")
# print(listEg)
# print(list2)
#list.sort: return the sorted list
#sort(list) return a new sorted list
# in: check item in list. if item in list:

# numberList = list(range(1,5))
# print(numberList)
#
# sentence = "this is a string"
# sentence = " " +sentence
# print(sentence[-1])
#
# for index_num in range(1,len(sentence)):
#     if sentence[index_num-1] == " " and sentence[index_num] != " ":
#         print(sentence[index_num].upper())
    # index_num +=1
#
# courses =['History','Math','Physics','ComSci']
# # list to string
# course_str =' - '.join(courses)
# print("course_str ",course_str)
# #string to list
# new_list = course_str.split(' - ')
# print("new_list ",new_list)

#SET
#intersection: set1.intersection(set2) return set of same item from both set
#difference set1.difference(set2) return set of items only belong to set1
#union set1.union(set2) return set of item belongs to both lists

# #empty list
# empty_list1 = []
# empty_list2 = list()
#
# #empty tuple
# empty_tuple1 = ()
# empty_tuple2 = tuple()
#
# #empty set
# empty_set1 = set()

#dictionary: key-value pair list {key:value}
student = {'name':'John','age':25,'courses':['Math','Comsci']}
#retrieve value: dict.get[key] >> return value of key, or not, return None
#dict.get[key,"Return String if NOT FOUND"] >> return string if not found
#add or update key
# student['phone']= "555-5555" # add to the end of dict if such key-value is not found
# student['name'] = "Trung" #edit value of key
# print(student)
#
# #update several key-value pairs dict.update({updated-dict})
# student.update({'name':'Jane','age':'26','phone':'555-5555'})
# print(student)

#delete
# del student['age']
# print(student)
#pop
# age = student.pop('age')
# print(student)
# print(age)
#Method of dic
#dict.len()
#dict.keys()
#dict.values()
#dict.item()

for key in student:
    print(key)