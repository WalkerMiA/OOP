myList = []

while True:
    print("1. Add an element to the list")
    print("2. Remove a specific element")
    print("3. Replace an element")
    print("4. Sort the elements")
    print("5. Reverse the list of elements")
    print("6. Display the list")
    print("7. Quit")

    option = input("Select an option: ")

    if option == "1":
        myList.append(input("Enter an element to add: "))

    elif option == "2":
        myList.remove(input("Enter an element to remove: "))

    elif option == "3":
        x = int(input("Enter index of element to replace: "))
        new_element = input("Enter new value: ")
        myList[x] = new_element

    elif option == "4":
        myList.sort()

    elif option == "5":
        myList.reverse()

    elif option == "6":
        print(myList)

    elif option == "7":
        break

print("You have exited the list.")