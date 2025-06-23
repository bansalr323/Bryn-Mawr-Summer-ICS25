option = int(input("Enter your number: "))
check = True 

while check == True: 
        if option >= 2: 
            option % 2 
            if option % 2 == 0: 
                option/2 
                print(f"The current hailstone's height is: {option}")  
            elif option % 2 == 1: 
                option*3 + 1
                print(f"The current hailstone's height is: {option}")  

        elif option < 2: 
            print("Please enter a number that is less than or equal to 2.")