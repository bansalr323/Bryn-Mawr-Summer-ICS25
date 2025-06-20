check = True 


while check == True: 
    print(" ")
    print("Welcome to our calculator:") 
    print("1. addition") 
    print("2. subtraction") 
    print("3. multipliction") 
    print("4. division") 
    print("5. modular division") 
    print("6. quit")
    option = input("Enter your option: ").lower().strip()

    if option == "addition":
        num1 = int(input("Type in num1: "))
        num2 = int(input("Type in num2: ")) 
        sum = num1 + num2
        print(f"The sum of {num1} and {num2} is {sum}.")

    elif option == "subtraction": 
        num3 = int(input("Type in num3: "))
        num4 = int(input("Type in num4: "))
        difference = num3 - num4
        print(f"The difference of {num3} and {num4} is {difference}.")

    elif option == "multiplication": 
        num5 = int(input("Type in num5: "))
        num6 = int(input("Type in num6: "))
        product = num5 * num6 
        print(f"The product of {num5} and {num6} is {product}.")

    elif option == "division": 
        num7 = int(input("Type in num7: "))
        num8 = int(input("Type in num8: "))
        quotient = num7/num8 
        print(f"The quotient of {num7} and {num8} is {quotient}.")

    elif option == "modular division": 
        num9 = int(input("Type in num9: "))
        num10 = int(input("Type in num10: "))
        remainder = num9 % num10
        print(f"The remainder of {num9} and {num10} is {remainder}.")
    
    elif option == "quit": 
        check = False 
        
    else: 
        print("This is not a valid operation.") 