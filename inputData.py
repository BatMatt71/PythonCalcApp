# Author:
# Date: 
# Program Name: 
# Purpose:
# Assignment No2 Programming principles

import calculator

def MathOption(firstNum):

    #Holds both numbers in a single list
    nums = [firstNum]
    
    

    #Program loops until the program is prompted to quit
    while True:
        #Store all functions in a single list to call
        optionList = [calculator.Exit, calculator.Add, calculator.Sub, calculator.Mult, calculator.Divid, calculator.Modul, calculator.Power, calculator.SqrRoot]

        #Display all possible options
        print("\nMath Operations:\n")
        print("[1]\tAdd (+)\n[2]\tSubtract (-)\n[3]\tMultiply (x)\n[4]\tDivide (/)\n[5]\tModulus (%)\n[6]\tExponent (^)\n[7]\tSquare Root (√)\n")
        print("[0]\tExit")

        while True:
            try: #Chekc if the number is an integer and in range
                option = int(input("\nEnter the option you want to execute: "))
            except ValueError or (option < 0 and option > 7):
                print("Please enter a valid input.")
                continue
            break

        if option != 7 and option != 0: #Since square root and exit dont require a second number, we wont ask user to input one
            
            #Retry until value is correct
            while True:
                try:
                    nums.append(int(input("\nEnter the second number you want to use: ")))
                except ValueError:
                    print("\nPlease enter a valid number")
                    continue
                break
    
        #return value from operation
        return optionList[option](nums)
