#Problem 3 08/27/2025

employee_name = input("Enter employee name: ")
wages = int(input("Enter wages: "))
hours = int(input("Enter hours: "))
days = int(input("Enter days: "))
total_wages = wages*hours*days
print(employee_name, "has earned a total of $", total_wages)