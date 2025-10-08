class Student:
    def __init__(self):
        self.sid = ""
        self.stuName = ""
        self.dob = ""
        self.major = ""
        self.gpa = 0.0
        self.courses = []

    def add_student(self):
        self.sid = input("Enter the student ID:")
        self.stuName = input("Enter student name:")
        self.dob = input("Enter date of birth:")
        self.major = input("Enter major:")
        self.gpa = float(input("Enter GPA:"))

    def edit_student(self):
        self.sid = input("Enter the student ID:")
        self.stuName = input("Enter student name:")
        self.dob = input("Enter date of birth:")
        self.major = input("Enter major:")
        self.gpa = float(input("Enter GPA:"))

    def register_course(self, cc1):
        self.courses.append(cc1)

    def display_student(self):
        print("Stu ID:", self.sid)
        print("Name:", self.stuName)
        print("DOB:", self.dob)
        print("Major:", self.major)
        print("GPA:", self.gpa)
        for x in self.courses:
            print("Courses:", x.cname)

class Course:
    def __init__(self):
            self.cid = ""
            self.cname = ""
    def add_course(self):
            self.cid = input("Enter Course ID:")
            self.cname = input("Enter Course Name:")

s1 = Student()
s1.add_student()
s1.display_student()

s2 = Student()
s2.add_student()
s2.display_student()

c1 = Course()
c1.add_course()

c2 = Course()
c1.add_course()

s1.register_course()
s1.display_student()



