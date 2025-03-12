#calculator.py

#Introduction: completing a program for assignment n2
import choice

def main():
    print("|| Welcome to the Calculator App ||\n")
    
    #List that holds both numbers
    nums = []
    
    try:    #Check if the number is an int
        nums.append(int(input("Enter the first number you want to use: ")))
    except ValueError:
        print("\nPlease enter a valid number.\n")

    #Display all possible options
    print("\nMath Operations:\n")
    print("[1]\tAdd (+)\n[2]\tSubtract (-)\n[3]\tMultiply (x)\n[4]\tDivide (/)\n[5]\tModulus (%)\n[6]\tExponent (^)\n[7]\tSquare Root (√)\n")
    print("[0]\tExit")


    try:
        option = int(input("\nEnter the option you want to execute:"))
    except ValueError or (option < 0 and option > 7):
        print("Please enter a valid input.")

    if option != 7 or option != 0: #Since square root and exit dont require a second number, we wont ask user to input one
        try:
            nums.append(int(input("\nEnter the second number you want to use: ")))
        except ValueError:
            print("\nPlease enter a valid number")
    
    resNum = choice.MathOption(nums, option)
    
    
    print("Answer:", resNum)


#Code initialiser
if __name__ == "__main__":
    main()