pyProjects = {}
while 1:
    print("1. Project Initiation")
    print("2. Project Closure")
    print("3. Project Progress Update")
    print("4. Print a Specific Project")
    print("5. Print All Projects")
    print("6. Quit Application")

    #projectTitle
    #Managers
    #startDate
    #endDate
    #Sponsor
    #Budget
    #Tech
    #Team



    option = input("Enter an option: ")

    if option == "1":
        pManagers = []
        pTech = []
        pTeam = []
        pID = input("Enter Project ID:")
        pTitle = input("Enter Project Title:")
        m = int(input("Enter total number of managers:"))
        for i in range(0, m):
            pManagers.append(input("Enter Manager's name:"))
        sDate = input("Enter Start Date:")
        eDate = input("Enter End Date:")
        pSponsor = input("Enter Project Sponsor:")
        pBudget = input("Enter Project Budget:")
        tn = int(input("Enter the number of technologies used:"))
        for i in range(0, tn):
            pTech.append(input("Enter the Technology:"))
        tm = int(input("Enter total number of team members:"))
        for i in range(0, tm):
            pTeam.append(input("Enter the Team Member's Name:"))

        pyProjects.update({pID: {
            "Project_Title": pTitle,
            "Managers": pManagers,
            "Start Date": sDate,
            "End Date": eDate,
            "Sponsor": pSponsor,
            "Budget": pBudget,
            "Technologies": pTech,
            "Team Members": pTeam
        }})

    if option == "2":
        pID = input("Enter Project ID to close:")
        del pyProjects[pID]

    if option == "3":
        while 1:
            print("1. Add to Project")
            print("2. Remove from Project")
            print("3. Exit Updates")

            option = input("Enter an option: ")

            if option == "1":
                pID = input("Enter Project ID to update:")
                pyProjects[pID]["Project_Title"] = input("Enter Project Title:")
                m = int(input("Enter total number of managers to add:"))
                for i in range(0, m):
                    pyProjects[pID]["Managers"].append(input("Enter Manager Name to Add:"))
                pyProjects[pID]["Start Date"] = input("Enter Start Date:")
                pyProjects[pID]["End Date"] = input("Enter End Date:")
                pyProjects[pID]["Sponsor"] = input("Enter Project Sponsor:")
                pyProjects[pID]["Budget"] = input("Enter Project Budget:")
                tn = int(input("Enter the number of technologies to add:"))
                for i in range(0, tn):
                    pyProjects[pID]["Technologies"].append(input("Enter Tech Name to Add:"))
                tm = int(input("Enter total number of team members to add:"))
                for i in range(0, tm):
                    pyProjects[pID]["Team Members"].append(input("Enter Team Member's Name to Add:"))

            if option == "2":
                pID = input("Enter Project ID update:")
                m = int(input("Enter total number of managers to remove:"))
                for i in range(0, m):
                    pyProjects[pID]["Managers"].remove(input("Enter Manager Name to Remove:"))
                tn = int(input("Enter the number of technologies to remove:"))
                for i in range(0, tn):
                    pyProjects[pID]["Technologies"].remove(input("Enter Tech Name to Remove:"))
                tm = int(input("Enter total number of team members to remove:"))
                for i in range(0, tm):
                    pyProjects[pID]["Team Members"].remove(input("Enter Tech Member's Name to Remove:"))

            if option == "3":
                break

    if option == "4":
        pID = input("Enter Project ID to print:")
        print(pyProjects[pID])

    if option == "5":
        for key, project in pyProjects.items():
            print({key})
            print(project)
            print("-" * 20)

    if option == "6":
        break

print("Thank you!")

