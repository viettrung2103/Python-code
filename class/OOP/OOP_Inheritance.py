#Person: fName,lName,occupatioon,doB
#User should be  able to get or set a name of the person
# print detail of a person
#create a class Student, Student inherent from a Person
#Student: seft.name,self.course, self.major


class Person():
    def __init__(self,fName,lName,occupation,DoB):
        self.fname = fName
        self.lName = lName
        self.occupation = occupation
        self.DoB = DoB

    def set_occupation(self,newJob):
        self.occupation = newJob

    def get_occupation(self):
        return self.occupation

    def get_detail(self):
        return f"Fullname: {self.fname} {self.lName}\nOccupatioon: {self.occupation}\nDate Of Birth: {self.doB}"

class Student(Person):
    def __init__(self,fName, lName, DoB, major):
        occupation = "Student"
        super().__init__(fName,lName,occupation,DoB)
        self.major = major
        self.courses = []

    def __str__(self):
        return f"Full Name: {self.fname} {self.lName} -DoB: {self.DoB} - Occupation: {self.occupation}"

    def add_course(self,course):
        self.courses.append(course)

    def get_detail(self):
        print()
class Teacher(Person):
    def __init__(self,fName,lName,major):
        occupation = "Teacher"
        # DoB = ""
        super().__init__(fName,lName,occupation,"")
        # super().__init__(fName,lName,occupation,DoB)
        self.major = major
        self.courses = []
        self.students = []

    def add_course(self,course):
        self.courses.append(course)

    def add_student(self,student):
        self.students.append(student)

    def get_detail(self):
        print(f"Teacher: {self.name}")
        print("Student:")
        for student in self.students:
            print(student.fName)
        print("Course:")
        for course in self.courses:
            print(course)

if __name__ == "__main__":
    student1 = Student("Trung","Doan","21.03.94","ICT")
    student2 = Student("Trinh","Nguyen","01.01.93","ICT")
    course1 = "OOP"
    course2 = "Database"
    course3 = "Embed System"
    teacher1 = Teacher("Armir","lName","ICT")
    teacher2 = Teacher("Chau","Nguyen","ICT")

    student1.add_course(course1)
    student1.add_course(course2)
    student2.add_course(course2)
    student2.add_course(course3)

\