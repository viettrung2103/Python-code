# class Pet():
#     counter = 0
#     def __init__(self, fName, color):
#         self.fName = fName
#         self.color = color
#         Pet.counter += 1
#
#     def setName(self,name):
#         self.fName = name
#         print("Name is changed")
#
#     def getColor(self):
#         return self.color
#
#     def bark(self,times):
#         for i in range(times):
#             print("bark bark")
#
# dog = Pet("Snowy","Blue")
# print(dog)
# cat = Pet("Che Che","White")
# cat.bark(5)

# class Person():
#     def __init__(self,name,height):
#         self.name = name
#         self.height = height
#
#     def __str__(self):
#         return self.name
#
# class Room():
#     def __init__(self):
#         self.persons = []
#
#     def add(self,person:Person):
#         self.persons.append(person)
#
#     def is_empty(self):
#         return (len(self.persons)) == 0

"""
class Visitor():
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Attraction():
    eligibleVisitor = 0

    def __init__(self):
        self.visitors = []

    def checkHeight(self,visitor:Visitor):
        requiredHeight = 180
        return visitor.height >= requiredHeight

    def add_visitor(self,visitor:Visitor):
        if self.checkHeight(visitor):
            self.visitors.append(visitor)


    def print_info(self):
        for visitor in self.visitors:
            print(visitor)
        print(f"There are {len(self.visitors)} visitors")
"""

class Car:
    def __init__(self,regis_no, color):
        self.regis_no = regis_no
        self.color = color


class PaintStudio:
    def paint(self,car,color):
        car.color = color

car1 = Car("BBC-455","red")
print("This car is",car1.color)

paintShop = PaintStudio()
paintShop.paint(car1,"blue")
print("This car is",car1.color)
