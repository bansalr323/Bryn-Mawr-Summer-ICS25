mushrooms = []
check = True 

while check == True: 
    option = int(input("Enter mushroom weight, or STOP to end: "))
    if option == "STOP": 
        check = False 
        for mushroom in mushrooms: 
            if mushroom >100: 
                mushroom = large_mushroom 
            elif mushroom <100: 
                mushroom = small_mushroom 
            else: 
                mushroom = medium_mushroom  
    elif option < 1: 
        print("Weight must be bigger than zero!") 
    else: 
        mushrooms.append(option)



