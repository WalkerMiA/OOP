myEmployees = {}
#gross pay is net pay - (deductions + taxes)
#net pay is basic pay + allowance
while 1:
    print("1. Add an Employee")
    print("2. Delete an Employee")
    print("3. Modify an Employee")
    print("4. Display all Employees")
    print("5. Exit the Program")

    option = input("Select an Option: ")

    if option == "1":
        eID = input("Enter employee ID: ")
        employeeName = input("Enter employee name: ")
        basicPay = int(input("Enter basic pay: "))
        allowance = int(input("Enter allowance: "))
        deductions = int(input("Enter deductions: "))
        taxRate = int(input("Enter tax rate: "))

        tax = (taxRate / 100) * basicPay
        netPay = basicPay + allowance
        grossPay = netPay - (deductions + tax)

        myEmployees.update({eID: {
            "Name": employeeName,
            "Basic Pay": basicPay,
            "Allowance": allowance,
            "Deductions": deductions,
            "Tax": tax,
            "Net Pay": netPay,
            "Gross Pay": grossPay
        }

        })

    elif option == "2":
        del myEmployees[input("Enter an employee ID to delete: ")]

    elif option == "3":
        eID = input("Enter employee ID: ")
        employeeName = input("Enter employee name: ")
        basicPay = int(input("Enter basic pay: "))
        allowance = int(input("Enter allowance: "))
        deductions = int(input("Enter deductions: "))
        taxRate = int(input("Enter tax rate: "))

        tax = (taxRate/100) * basicPay
        netPay = basicPay + allowance
        grossPay = netPay - (deductions + tax)

        myEmployees.update({eID: {
            "Name": employeeName,
            "Basic Pay": basicPay,
            "Allowance": allowance,
            "Deductions": deductions,
            "Tax": tax,
            "Net Pay": netPay,
            "Gross Pay": grossPay
        }

        })

    elif option == "4":
        for employeeRecord in myEmployees.items():
            print(employeeRecord)
            print("-----------------------------")

    elif option == "5":
        break

print("Thank you for using the program!")
