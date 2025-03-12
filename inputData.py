import calculator

def MathOption():

    #Holds both numbers in a single list
    nums = []
    
    try:    #Check if the number is an int
        nums.append(int(input("Enter the first number you want to use: ")))
    except ValueError:
        print("\nPlease enter a valid number.\n")

    #Store all functions in a single list to call
    optionList = [calculator.Exit, calculator.Add, calculator.Sub, calculator.Mult, calculator.Divid, calculator.Modul, calculator.Power, calculator.SqrRoot]

    #Display all possible options
    print("\nMath Operations:\n")
    print("[1]\tAdd (+)\n[2]\tSubtract (-)\n[3]\tMultiply (x)\n[4]\tDivide (/)\n[5]\tModulus (%)\n[6]\tExponent (^)\n[7]\tSquare Root (√)\n")
    print("[0]\tExit")


    try: #Chekc if the number is an integer and in range
        option = int(input("\nEnter the option you want to execute:"))
    except ValueError or (option < 0 and option > 7):
        print("Please enter a valid input.")

    if option != 7 or option != 0: #Since square root and exit dont require a second number, we wont ask user to input one
        try:
            nums.append(int(input("\nEnter the second number you want to use: ")))
        except ValueError:
            print("\nPlease enter a valid number")
    
    #return value from operation
    return optionList[option](nums)