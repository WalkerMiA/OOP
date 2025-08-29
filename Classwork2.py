course1 = int(input("Input score for course 1: "))
course2 = int(input("Input score for course 2: "))
course3 = int(input("Input score for course 3: "))
course4 = int(input("Input score for course 4: "))
course5 = int(input("Input score for course 5: "))

total = course1+course2+course3+course4+course5
total_percentage = ((total/500)*100)

print("Your score is total: ", total)
print("Your average is: ", total_percentage)

if total_percentage <= 100 and total_percentage >=90:
    print("Grade A")
elif total_percentage <= 89 and total_percentage >=80:
    print("Grade B")
elif total_percentage <= 79 and total_percentage >=70:
    print("Grade C")
elif total_percentage <= 69 and total_percentage >=60:
    print("Grade D")
elif total_percentage <= 59 and total_percentage >=0:
    print("Grade F")
