while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    option = input("Select your option: ")

    if option == "1":
        a1 = int(input("Enter the first number: "))
        a2 = int(input("Enter the second number: "))
        print("The sum is:", a1+a2)

    elif option == "2":
        s1 = int(input("Enter the first number: "))
        s2 = int(input("Enter the second number: "))
        print("The difference is:", s1-s2)

    elif option == "3":
        m1 = int(input("Enter the first number: "))
        m2 = int(input("Enter the second number: "))
        print("The product is:", m1*m2)

    elif option == "4":
        d1 = int(input("Enter the first number: "))
        d2 = int(input("Enter the second number: "))
        print("The dividend is:", d1/d2)

    elif option == "5":
        break

print("Thank you for using this app!")
