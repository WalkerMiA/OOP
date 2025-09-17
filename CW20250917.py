'''myStudents.update({"s3":"Melba"})
myStudents.update({"s4":"John", "s5":"Paul"})
print(myStudents)

del myStudents[input("Select Student ID to delete: ")]
print(myStudents)
myStudents = {"s1": {
                "name":"Michael",
                "major":"CS",
                "year":"freshman",
                "credits":13,
                "gpa":0.0
                    },
              "s2": {
                "name":"John",
                "major":"Music",
                "year":"Junior",
                "credits":15,
                "gpa":3.5
                    }
              }

sid = input("Enter student ID:")
nName = input("Enter Student Name:")
mMajor = input("Enter Student's Major:")
yYear = input("Enter Student's year:")
cCredits = input("Enter Student's credits:")
gGpa = input("Enter Student's gpa:")

myStudents.update({sid: {
                    "name":nName,
                    "major":mMajor,
                    "year":yYear,
                    "credits":cCredits,
                    "gpa":gGpa
}

}

)

print(myStudents)

for student_record in myStudents.items():
    print(student_record)
    print("------------")'''
myStudents = {}

while 1:
    print("1. Add a record to the Dictionary")
    print("2: Delete a record from the Dictionary")
    print("3: Replace a record in the Dictionary")
    print("4: Print the Dictionary")
    print("5: Quit")

    option = input("Select an option:")

    if option == "1":
        sid = input("Enter Student ID:")
        nName = input("Enter Student Name:")
        mMajor = input("Enter Student's Major:")
        yYear = input("Enter Student's year:")
        cCredits = input("Enter Student's credits:")
        gGpa = input("Enter Student's gpa:")

        myStudents.update({sid: {
            "name": nName,
            "major": mMajor,
            "year": yYear,
            "credits": cCredits,
            "gpa": gGpa
        }

        })

    elif option == "2":
        for student_record in myStudents.items():
            print(student_record)
            print("------------")
        del myStudents[input("Select Student ID to delete: ")]

    elif option == "3":
        sid = input("Enter Student ID:")
        nName = input("Enter Student Name:")
        mMajor = input("Enter Student's Major:")
        yYear = input("Enter Student's year:")
        cCredits = input("Enter Student's credits:")
        gGpa = input("Enter Student's gpa:")
        
        myStudents.update({sid: {
            "name": nName,
            "major": mMajor,
            "year": yYear,
            "credits": cCredits,
            "gpa": gGpa
        }

        })

    elif option == "4":
        for student_record in myStudents.items():
            print(student_record)
            print("------------")

    elif option == "5":
        break

print("End program")