class Student:
    def __init__(self):
        self.sid = ""
        self.stuName = ""
        self.dob = ""
        self.major = ""
        self.gpa = 0.0
    def add_student(self):
        self.sid = input("Enter the student ID:")
        self.stuName = input("Enter student name:")
        self.dob = input("Enter date of birth:")
        self.major = input("Enter major:")
        self.gpa = int(input("Enter GPA:"))
    def edit_student(self):
        self.sid = input("Enter the student ID:")
        self.stuName = input("Enter student name:")
        self.dob = input("Enter date of birth:")
        self.major = input("Enter major:")
        self.gpa = int(input("Enter GPA:"))
    def display_student(self):
        print("Stu ID:", self.sid)
        print("Name:", self.stuName)
        print("DOB:", self.dob)
        print("Major:", self.major)
        print("GPA:", self.gpa)

