myList = []

while True:
    print("1. Add an element to the list")
    print("2. Remove a specific element")
    print("3. Pop the last element")
    print("4. Display the list")
    print("5. Quit")

    option = input("Select an option: ")

    if option == "1":
        myList.append(input("Enter an element to add: "))

    elif option == "2":
        myList.remove(input("Enter an element to remove: "))

    elif option == "3":
        myList.pop()
        print("Popped last element in list")

    elif option == "4":
        print(myList)

    elif option == "5":
        break

print("You have exited the list.")