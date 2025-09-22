Projects = {}
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
        n = int(input("Enter total number of managers:"))
        for i in range(0, n):
            pManagers.append("Enter Manager's name:")
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

        Projects.update(pID, {
            "Project_Title": pTitle,
            "Managers": pManagers,
            "Start Date": sDate,
            "End Date": eDate,
            "Sponsor": pSponsor,
            "Budget": pBudget,
            "Technologies": pTech,
            "Team Members": pTeam
        })


