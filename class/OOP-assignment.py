#Student(name,age,major)
class Student():
    def __init__(self,name,age,major):
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"{self.name} is {self.age} age, in major: {self.major}"

    def getName (self):
        return self.name
    def getAge(self):
        return self.age
    def getMajor(self):
        return self.major

    def setName(self,name):
        self.name = name
        print("name is changed")

student1 = Student("John",23,"ICT")
student1.setName("JohnNew")
print(student1)