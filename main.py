#calculator.py

#Import functions
import inputData
from time import sleep

def main():
    print("|| Welcome to the Calculator App ||\n")
    
    #Retry until value is correct
    while True:
        try:    #Check if the number is an int
            firstNum = (int(input("Enter the first number you want to use: ")))
        except ValueError:
            print("\nPlease enter a valid number.\n")
            continue
        break

    #Program loops until it is prompted to exit
    while True:
        #Store result in a variable and print it
        resNum = inputData.MathOption(firstNum)

        print("Answer:", resNum)
        sleep(1)
        print("\n\n[1]\tReset the number\n[2]\tKeep the number\n\n[0]\tExit program")

        #Retry until value is correct
        while True:
            try: #User inputs a choice 
                option = int(input("\nPlease input your choice: "))
            except ValueError or (option < 0 and option > 2):
                print("\nPlease enter a valid input.")
                continue
            break

        #Switch case for option
        match option:
            case 0:
                exit()
            case 1:
                #Retry until value is correct
                while True:
                    try:    #Check if the number is an int
                        firstNum = (int(input("Enter the first number you want to use: ")))
                    except ValueError:
                        print("\nPlease enter a valid number.\n")
                        continue
                    break
            case 2:
                firstNum = resNum
                


#Code initialiser
if __name__ == "__main__":
    main()
