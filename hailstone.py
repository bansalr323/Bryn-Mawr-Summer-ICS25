option = int(input("Enter your number: "))

while option >= 2: 
        if option % 2 == 0: 
            option = option//2
            print(f"The current hailstone's height is: {option}")  
        elif option % 2 == 1: 
            option = option*3 + 1
            print(f"The current hailstone's height is: {option}")  

        