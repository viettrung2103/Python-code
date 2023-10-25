# class Book():
#
#     def __init__(self,name):
#         self.name = name
#
#     # def getAuthor(self,author):
#     #     print(f"The author of {self.name} is {author.name}")
#
class Author():

    def __init__(self,fName,lName):
        self.fName = fName
        self.lName = lName
        self.bookList = []

    def __str__(self):
        return f"{self.fName} {self.lName}"

    def add(self,book):
        self.bookList.append(book)

    def showInfo(self):
        print(f"Author: {self}")
        print("Books writen by the author:")
        for book in self.bookList:
            print(f"- {book.name}")

    def getAuthorByBook(self,book):
        print(f"The author of '{book.name}' is {self}")
#
# class BookStore():
#     def __init__(self):
#         self.authorList =[]
#
#     def addAuthor(self,author):
#         self.authorList.append(author)
#
#     def getAuthorByBook(self,book):
#         for author in self.authorList:
#             if book in author.bookList:
#                 print(f"The author of '{book.name}' is {author}")
#
#     def showAllAuthor(self):
#         for author in self.authorList:
#             author.showInfo()
#             print("")
#
#
# author1 = Author("J.K","Rowling")
# author2 = Author("George","Orwell")
#
# book1 = Book("Harry Potter and the Socerer's Stone")
# book2 = Book("I donot know")
# book3 = Book("the year 1984")
#
# bookStore1 = BookStore()
#
# author1.add(book1)
# author1.add(book2)
# author2.add(book3)
#
# bookStore1.addAuthor(author1)
# bookStore1.addAuthor(author2)
#
# bookStore1.showAllAuthor()
# bookStore1.getAuthorByBook(book3)
#
#
# # author1.showInfo()
# print("")
# # author2.showInfo()
# print("")
# # author2.getAuthorByBook(book3)

class Course():
    def __init__(self,name):
        self.name = name
        self.studentList = []

    def __str__(self):
        return self.name

    def add(self,student):
        self.studentList.append(student)
        # student.add(self)

    def getStudentList(self):
        return [student.name for student in self.studentList]

    def showCourseInfo(self):
        print(f"{self.name} has the following student: {self.getStudentList()}")


class Student():
    def __init__(self,name):
        self.name = name
        self.courseList = []

    def __str__(self):
        return self.name


    def add(self,course: Course):
        self.courseList.append(course)
        # course.add(self)

    def getCourseList(self):
        newCourseList = []
        for course in self.courseList:
            print("This is course",course)
            newCourseList.append(course)
        return newCourseList


    def showStudentInfo(self):
        print(f"{self.name} is enrolled to courses: {self.getCourseList()}")


student1 = Student("Trung")
student2 = Student("Amir")
student3 =Student("Timo")

course1 = Course("Mathematics")
course2 = Course("Physics")
course3 = Course("History")

student1.add(course1)
student1.add(course2)

student2.add(course2)

student3.add(course1)
student3.add(course3)

course1.add(student1)
course1.add(student3)

course2.add(student1)
course2.add(student2)

course3.add(student3)

for student in [student1,student2,student3]:
    student.showStudentInfo()

for course in [course1,course2,course3]:
    course.showCourseInfo()

# course1.showStudentInfo()
# course2.showStudentInfo()
# course3.showStudentInfo(