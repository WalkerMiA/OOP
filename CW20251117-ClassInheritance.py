class Person:
    def __init__(self,x,y,z):
        self.__pname= x
        self.__dob= y
        self.__gender= z
    def display(self):
        print("Person_Name:", self.__pname)
        print("Person_DOB:", self.__dob)
        print("Person_Gender:", self.__gender)
        return ""

class Student(Person):
    def __init__(self,x,y,z,a,b):
        Person.__init__(self,x,y,z)
        self.dept=a
        self.id=b
    def display(self):
        print(Person.display(self))
        print("Stu_Dept:", self.dept)
        print("Stu_ID", self.id)

class Faculty(Person):
    def __init__(self,x,y,z,a,b):
        Person.__init__(self,x,y,z)
        self.dept=a
        self.design=b
    def display(self, Value="", oneMore=""):
        print(Person.display(self))
        print("Fac_Dept:", self.dept)
        print("Fac_Design:", self.design)
        if Value != "":
            print("Within Polymorphism", Value)

s1=Student("Jim", "2004", "Male", "CS", "123")
s1.display()

f1=Faculty("John", "1995", "Male", "CYB", "Apple")
f1.display()
f1.display("John")
f1.display("Jim", "99")