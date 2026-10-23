decision1 = input("Please choose between door 1 or door 2: ")
if decision1 == "door 1":
    decision2 = input("Please choose between door a or door b: ")
    if decision2 == "door a":
        print(f"You have choosen {decision1} and {decision2}.\nCongrats! You have won nothing!")
    elif decision2 == "door b":
        print(f"You have choosen {decision1} and {decision2}.\nYou have won a phone!")
    else:
        print("Invalid input. Please choose either door a or door b.")
elif decision1 == "door 2":
    decision2 = input("Please choose between door c or door d: ")
    if decision2 == "door c":
        print(f"You have choosen {decision1} and {decision2}.\nYou have won a car!")
    elif decision2 == "door d":
        print(f"You have choosen {decision1} and {decision2}.\nCongrats! You have won nothing!!")
    else:
        print("Invalid input. Please choose either door a or door b.")
else:
    print("Invalid input. Please choose either door 1 or door 2")